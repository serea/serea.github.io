This is my personal github page repository. This was forked by [academic websites](https://github.com/academicpages/academicpages.github.io).


### Dependency security

Do not delete lockfiles to resolve security alerts. Update the affected dependency deliberately, commit the lockfile, and rerun the security and browser checks.

## AI 使用说明 / AI Contributor Instructions

AI 修改本项目之前必须阅读 [AGENTS.md](AGENTS.md)。个人主页的中文与英文必须在同一 PR 中同步更新，论文须同步主页列表及详情。提交前运行 `python3 scripts/check_bilingual.py`；构建后运行 `python3 scripts/check_bilingual.py --site _site`。

AI contributors must follow [AGENTS.md](AGENTS.md): update both languages together and verify the source, rendered pages, and deployment.

# Instructions

1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://serea.github.io/

## To run locally (not on GitHub Pages, to serve on your own computer)

1. Clone the repository and made updates as detailed above
1. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle clean` to clean up the directory (no need to run `--force`)
1. Run `bundle install` to install Ruby dependencies. Diagnose dependency errors and update affected versions without deleting lockfiles.

## CI/CD 验证 / Release gates

PR 和 master 更新都会运行 `.github/workflows/pages.yml`。仅当构建、双语检查、真实浏览器交互测试和安全检查全部通过时才部署 master；PR 仅验证，不持有发布权限。

- `npm ci --prefix ci/browser`，然后 `cd ci/browser && npx playwright install chromium && npm test`：在构建后的 `_site` 上用桌面和手机尺寸验证语言按钮、键盘、导航菜单、跨页、刷新、显式语言链接和禁用存储。
- `python3 scripts/check_security.py`：检查第一方代码中的高风险模式及凭据。
- `npm audit --audit-level=high` 与 `ci/security/node_modules/.bin/retire --path assets/js --severity high --exitwith 1`：高危依赖漏洞阻止发布；测试工具依赖也审计。
- 浏览器失败时上传 trace、截图和报告，不能跳过失败检查发布。

Security checks cover configured source patterns and known dependency advisories, not a proof that all vulnerabilities are absent. Browser tests run against the production build before deployment. Do not replace real clicks with mocked DOM tests.
1. Run `bundle exec jekyll liveserve` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change.
