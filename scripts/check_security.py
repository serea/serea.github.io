#!/usr/bin/env python3
"""Limited first-party security lint (Python standard library only).

Scope: assets/js except vendor/, plugins/ and generated main.min.js; HTML
includes/layouts; root HTML and YAML configuration. Articles, Markdown examples,
publication data, generated sites and dependencies are deliberately NOT scanned.
Third-party JS and the shipped bundle are covered separately by
`npm ci --prefix ci/security && npm run check --prefix ci/security` (Retire).

This is pattern matching, NOT an AST/taint analysis or a comprehensive secret
scanner. It catches obvious eval/Function/string timers/document.write, dynamic
HTML setters, literal javascript: URLs and selected credential formats. Literal
HTML arguments are allowed (including Liquid interpolations): review escaping
and data provenance manually. Aliases, constructed/encoded JS, dynamic URLs,
other injection sinks, unknown token formats, Git history and article content
are outside its coverage. No finding is proof of exploitability; a clean result
is NOT proof of safety. Diagnostics never print suspected credential values.
Run --self-test to exercise positive/negative fixtures without scanning articles.
"""
from __future__ import annotations

import argparse
import html
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
RULES = {
    "dynamic-code": r"\b(?:eval|Function)\s*\(",
    "string-timer": r"\bset(?:Timeout|Interval)\s*\(\s*['\"`]",
    "document-write": r"\bdocument\s*\.\s*write(?:ln)?\s*\(",
    "html-assignment": r"\.\s*(?:innerHTML|outerHTML)\s*[+]?=\s*(?!\s*['\"`])\S",
    "dynamic-html-call": r"\.\s*html\s*\(\s*(?!\s*['\"`\)])\S",
    "adjacent-html": r"\.\s*insertAdjacentHTML\s*\(\s*['\"][^'\"]*['\"]\s*,\s*(?!\s*['\"`])\S",
    "javascript-url": r"(?i)javascript\s*:",
    "private-key": r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |ENCRYPTED )?PRIVATE KEY-----",
    "aws-access-key": r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    "github-token": r"\b(?:gh[pousr]_[A-Za-z0-9]{36,255}|github_pat_[A-Za-z0-9_]{50,255})\b",
    "slack-token": r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b",
    "credential-literal": r'''(?ix)\b(?:api[_-]?key|access[_-]?token|client[_-]?secret|password|passwd|secret[_-]?key)\b["']?\s*[:=]\s*["'][A-Za-z0-9_+/=.!-]{16,}["']''',
}
PATTERNS = {name: re.compile(pattern) for name, pattern in RULES.items()}


def source_files(root: Path):
    files = set(root.glob('*.html')) | set(root.glob('*.yml')) | set(root.glob('*.yaml'))
    for directory in ('_includes', '_layouts'):
        files.update((root / directory).rglob('*.html'))
    for path in (root / 'assets/js').rglob('*.js'):
        relative = path.relative_to(root / 'assets/js')
        if relative.parts[0] not in ('vendor', 'plugins') and relative.as_posix() != 'main.min.js':
            files.add(path)
    return sorted(path for path in files if path.is_file())


def findings(text: str):
    # Decode HTML entities for URLs (e.g. javascript&#58;), preserving source
    # line numbers. Strip ASCII controls inside that rule to catch tab/newline
    # obfuscation; other JavaScript encodings are intentionally unsupported.
    for name, pattern in PATTERNS.items():
        candidate = html.unescape(text) if name == 'javascript-url' else text
        if name == 'javascript-url':
            # Preserve original offsets via an index map.
            positions = [i for i, c in enumerate(candidate) if ord(c) > 32]
            compact = ''.join(candidate[i] for i in positions)
            for match in pattern.finditer(compact):
                yield candidate.count('\n', 0, positions[match.start()]) + 1, name
        else:
            for match in pattern.finditer(candidate):
                yield candidate.count('\n', 0, match.start()) + 1, name


def self_test():
    positive = [
        ('eval(input)', 'dynamic-code'), ('new Function(code)', 'dynamic-code'),
        ('setTimeout("bad()", 0)', 'string-timer'),
        ('document.write(value)', 'document-write'),
        ('el.innerHTML = payload', 'html-assignment'),
        ('el.outerHTML += payload', 'html-assignment'),
        ('node.html( value)', 'dynamic-html-call'),
        ('node.insertAdjacentHTML("beforeend", payload)', 'adjacent-html'),
        ('<a href="JaVaScRiPt:alert(1)">', 'javascript-url'),
        ('<a href="java&#x73;cript&#58;alert(1)">', 'javascript-url'),
        ('<a href="java\nscript:alert(1)">', 'javascript-url'),
        ('-----BEGIN ' + 'PRIVATE KEY-----', 'private-key'),
        ('AKIA' + 'A' * 16, 'aws-access-key'),
        ('ghp_' + 'a' * 36, 'github-token'),
        ('password = "' + 'a' * 20 + '"', 'credential-literal'),
    ]
    for source, rule in positive:
        assert rule in {name for _, name in findings(source)}, (source, rule)
    for source in ('el.textContent = value', 'setTimeout(callback, 10)',
                   'node.html()', 'node.html("literal")', "el.innerHTML = ''",
                   'const url = "https://example.com"'):
        assert not list(findings(source)), source
    assert all('_posts' not in str(p) and p.suffix != '.md' for p in source_files(ROOT))
    print('Security lint self-tests passed.')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    files = source_files(ROOT)
    if not files:
        print('ERROR: no first-party source files found.', file=sys.stderr)
        return 2
    errors = 0
    try:
        for path in files:
            for line, rule in findings(path.read_text(encoding='utf-8')):
                print(f'{path.relative_to(ROOT)}:{line}: {rule} (review required)')
                errors += 1
    except (OSError, UnicodeError) as error:
        print(f'ERROR: security scan incomplete: {error}', file=sys.stderr)
        return 2
    print(f'Limited first-party security lint: {len(files)} files, {errors} findings. '
          'Excludes articles, vendor/plugins and bundle; run Retire separately. See --help for boundaries.')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
