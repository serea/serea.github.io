#!/usr/bin/env python3
"""Check bilingual homepage parity; optionally validate generated or deployed HTML."""
import argparse
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = [("What's New", "最新动态"), ("Selected Publications", "代表论文"),
            ("Awards & Honors", "荣誉奖项")]


def normalized(text):
    return ' '.join(unescape(text).replace('’', "'").split())


def source_sections():
    source = (ROOT / '_pages/about.md').read_text()
    result = {}
    for lang in ('en', 'zh'):
        match = re.search(r'<div class="lang-' + lang + r'"[^>]*>(.*?)</div>', source, re.S)
        assert match, f'Missing source language block: {lang}'
        for en, zh in SECTIONS:
            heading = en if lang == 'en' else zh
            section = re.search(r'^## ' + re.escape(heading) + r'\n(.*?)(?=^## |\Z)', match[1], re.M | re.S)
            assert section, f'Missing source section: {heading}'
            entries = re.findall(r'^(?:\*|\d+\.) (.+)$', section[1], re.M)
            assert entries, f'Empty source section: {heading}'
            result[lang, en] = entries
    for en, _ in SECTIONS:
        a, b = result['en', en], result['zh', en]
        assert len(a) == len(b), f'Bilingual entry count differs: {en}'
        for left, right in zip(a, b):
            assert set(re.findall(r'(?<!\d)(?:19|20)\d{2}', left)) == set(re.findall(r'(?<!\d)(?:19|20)\d{2}', right)), f'Year mismatch: {en}'
            assert re.findall(r'\]\((.*?)\)', left) == re.findall(r'\]\((.*?)\)', right), f'Link mismatch: {en}'
            if en == 'Selected Publications':
                # Only the link label differs; titles, author order, and venues must agree.
                strip_label = lambda s: re.sub(r'\[(?:paper|论文)\]', '[paper]', s)
                assert strip_label(left) == strip_label(right), 'Publication metadata differs between languages'
    return result


class Homepage(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = None
        self.depth = 0
        self.heading = None
        self.section = None
        self.item = None
        self.sections = {}

    def handle_starttag(self, tag, attrs):
        classes = dict(attrs).get('class', '').split()
        if tag == 'div':
            if self.lang:
                self.depth += 1
            elif 'lang-en' in classes or 'lang-zh' in classes:
                self.lang = 'en' if 'lang-en' in classes else 'zh'
                self.depth = 1
        if not self.lang:
            return
        if tag == 'h2':
            self.heading = []
        elif tag == 'li' and self.section:
            self.item = []

    def handle_endtag(self, tag):
        if not self.lang:
            return
        if tag == 'h2' and self.heading is not None:
            self.section = normalized(''.join(self.heading))
            self.sections[self.lang, self.section] = []
            self.heading = None
        elif tag == 'li' and self.item is not None:
            self.sections[self.lang, self.section].append(normalized(''.join(self.item)))
            self.item = None
        if tag == 'div':
            self.depth -= 1
            if self.depth == 0:
                self.lang = self.section = None

    def handle_data(self, data):
        if self.heading is not None:
            self.heading.append(data)
        if self.item is not None:
            self.item.append(data)


def verify_html(html, expected):
    parser = Homepage()
    parser.feed(html)
    for lang in ('en', 'zh'):
        for en, zh in SECTIONS:
            actual = parser.sections.get((lang, en if lang == 'en' else zh), [])
            entries = expected[lang, en]
            assert len(actual) == len(entries), f'Rendered entry count mismatch: {lang}/{en}'
            for raw, rendered in zip(entries, actual):
                plain = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', raw).replace('**', '')
                assert normalized(plain) == rendered, f'Rendered content mismatch: {lang}/{en}: {rendered}'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--site', type=Path)
    parser.add_argument('--url', help='Deployed homepage URL, optionally including a cache-busting query')
    args = parser.parse_args()
    expected = source_sections()
    if args.site:
        verify_html((args.site / 'index.html').read_text(), expected)
    if args.url:
        with urllib.request.urlopen(args.url, timeout=30) as response:
            verify_html(response.read().decode('utf-8'), expected)
    print('PASS: bilingual news, selected publications, and awards match; supplied rendered pages match source.')


if __name__ == '__main__':
    main()
