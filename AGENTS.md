# AI 使用说明 / Instructions for AI Contributors

适用范围：整个仓库。修改前先阅读本文件和 README.md。

## 必须同步中英文 / Keep Chinese and English in sync

- 每次更新个人主页，必须在同一提交/PR 中同步更新中文与英文；不能只修改其中一种语言。
- `_pages/about.md` 包含 `div.lang-en` 和 `div.lang-zh` 两个区块。最新动态、荣誉奖项、代表论文、工作经历等对应内容的事实、年份、顺序和链接必须一致。
- 新增获奖信息时，同步更新两种语言的“最新动态 / What's New”和“荣誉奖项 / Awards & Honors”。
- 新增或修改论文时，检查两种语言的“代表论文 / Selected Publications”、`_publications/` 详情及 `/publications/` 列表；已有论文不得重复创建。
- 论文正式英文标题、作者姓名及顺序无需翻译，不得改写。中文翻译说明与英文必须表达同一事实。
- 以用户明确提供的元数据和现有可靠记录为依据；不得编造作者、会议、录用状态、DOI、页码、链接或精确日期。只有年份时使用 `publication_year`，如 Jekyll 需要排序日期，必须注释说明占位日期，且页面只展示已确认年份。
- 保留既有论文永久链接。预印本升级会议版本时同步修改 venue、citation、主页描述与显示年份；预印本链接可以保留，但不能继续把会议版本标注为 arXiv 论文。

## 验证 / Verification

- 提交前运行 `git diff --check`、`python3 scripts/check_bilingual.py`。
- 构建后运行 `python3 scripts/check_bilingual.py --site _site`；部署工作流也运行此检查，防止双语条目缺失。
- 检查 `/?lang=en` 与 `/?lang=zh`，确认对应内容属于正确语言区块、语言切换正常，不能只对整个 HTML 搜索关键词就宣布双语验证通过。
- 语言切换使用独立 `assets/js/language.js` 和原生按钮。运行 `node scripts/check_language.js _site/index.html` 检查接线，并运行 `cd ci/browser && npm test` 真实浏览器测试；必须覆盖桌面/手机点击、键盘、跨页、刷新及禁用存储。不得以模拟 DOM 测试替代真实点击。
- 发布必须通过 `.github/workflows/pages.yml` 的浏览器和安全门禁。不得删除/忽略失败检查或漏洞结果来发布；安全扫描是有限规则与已知漏洞检查，不能宣称代码绝对安全。
- 线上内容已存在但用户未看到时，先调查语言偏好、渲染和缓存；没有证据不得宣称根因已确定。

## 发布与改动范围 / Delivery

- 保留无关本地改动，仅提交本次任务涉及文件。
- 用户已授权本项目主页更新完成后创建 GitHub PR、合并并发布；遵守分支保护，不绕过检查。若用户本次另有要求，以本次要求为准。
- 发布前确认内容检查通过；发布后等待 GitHub Pages 构建/部署成功，再验证线上页面和链接。
- 区分已提交、已合并、部署中与已上线；失败或阻塞要如实说明。

English summary: Update both languages in the same change. Keep news, awards, homepage publications, and publication records consistent. Preserve canonical paper titles, author order, and permalinks; never invent metadata. Run bilingual source and rendered-site checks, verify both language views, and confirm deployment before claiming the update is live.
