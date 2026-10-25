# AGENTS.md — 心灵的分岔（mind-forks）文件夹记忆

> 本文件是本仓库的工具链、约定与踩坑记录。改动后新会话生效。
> 系列级约定见 `../AGENTS.md`；本书与系列的差异，在本文件最后列出。

## 1. 这个仓库是什么

《心灵的分岔——从无意识可观察：心理学流派的六次划线》，一本科普专著。

- 6 部分、25 章、17 个附录（A—Q）、309 页（A4 印刷版）、25 幅 SVG、68 个表。
- 六个提问：看见 / 记住 / 跟上 / 选择 / 讲述 / 临界。
- `source/*.html` 是唯一权威正文来源；`output/`、`release/` 是派生产物。
- 证据等级 A／B／C；结论强度不超过证据强度。
- 不提供临床建议，不裁判疗效；“讲述”不做“揭穿”。

## 2. 工具链（本机实测，2026-10）

```bash
PY="/mnt/d/0_Code/Iris Series/.venv/Scripts/python.exe"
GIT="/mnt/d/Git/cmd/git.exe"
CHROME="C:\Program Files\Google\Chrome\Application\chrome.exe"
```

- Python 已装 numpy scipy pandas matplotlib bs4 lxml pypdf requests；无 weasyprint / markdown。
- PDF 由 `build_book.py --pdf` 调无头 Chrome 打印（含分级书签），不是 weasyprint。
- `.env.build` 的 `PYTHON` 指向上述解释器；路径含空格，必须加引号。
- Git 不在 WSL PATH；用绝对路径 `/mnt/d/Git/cmd/git.exe`。

## 3. 常用命令

```bash
"$PY" analysis/make_figures.py      # 25 幅 SVG（确定性生成）
"$PY" analysis/make_cover.py        # 满版封面 SVG
"$PY" analysis/audit.py             # 结构/引用校对 → 校对清单.md + analysis/results/audit.json
"$PY" build_book.py                 # -> output/book.html
"$PY" build_book.py --pdf           # -> output/book.pdf
"$PY" build_book.py --ereader --pdf # -> output/book-ereader.pdf
"$PY" build_epub.py                 # -> output/book.epub
"$PY" build_markdown.py             # -> output/markdown/
bash scripts/build.sh               # 全流程
bash scripts/validate.sh            # audit + EPUB 结构校验
bash scripts/release.sh             # release/ 交付包
```

## 4. 目录契约

```
source/                 唯一正文来源
  book.json             书名/副标题/作者/日期/摘要/关键词
  parts.json            6 部分 → 25 章 → 节（sections 由 h3 标题自动同步）
  front_*.html          总纲、导论、怎么读、六核速查
  ch01.html … ch25.html 章（h2.chapter + h3 编号 + h4 子节）
  back_*.html           尾声、后记、系列页
  appendix_a.html … q   17 个附录
assets/svg/             25 幅插图 + cover.svg
assets/css/             paper / book / ereader
analysis/               make_figures / make_cover / audit
output/                 book.pdf / book-ereader.pdf / book.epub / book.html / markdown/
release/                发布包（不入库）
docs/                   方法、数据缺口、读者、发布说明
versions/CHANGELOG.md   内部版本记录（不进发布包）
```

## 5. 写作与结构约定

- **每章五段**：人物/争议开场 → 一个核心主提问展开 → 它让出了什么 → 被埋没与回归 → 一句话带走。
- **每章只用一个核心当主提问**；其他核心作背景。
- **每章必须有一句“它让出了什么”**，且要落到可查证的历史后果（被谁批评、被什么实验卡住、在哪次分裂中被逐出）。
- **每章“让出了什么”之后有【这笔账的判据｜F1/F2】小框**（box-ledger）：一到两句话，写清这个“让出”是根据哪个历史后果判断的；附录 F.2 是这 25 个判据的索引。
- **“一句话带走”末尾有“更刺的一句”**：每章至少一句反直觉/有画面的短句，防止结尾过于平衡。
- **开题与结算可以不同**：每章只用一个核心开题，结算可以用另一个核心；导论 4—5 节与 front_howto 已写明。
- **h3 编号**：`X.Y　标题`；**h4 编号**：`X.Y.Z　标题`，必须物理位于 `X.Y` 这一节内（在下一个 h3 之前）。
- **图**：`<img class="fig" src="assets/svg/…">` + `<div class="cap"><b>图 X.Y　…</b></div>`。
- **表**：`<table class="nat">` + `<caption class="cap"><b>表 X.Y　…</b></caption>` + `<div class="datasrc">来源/等级/局限</div>`。
- **等级**：A 可查证/可复算；B 稳定但有争议；C 思辨/开放。正文一处标注即可，不反复免责。
- **日期**：只用 `book.json` 的 `date`（真实完成日 2026-10-25），版权页与元数据一致；正文不写版本号。
- **口吻**：张力，不宿命；反例进正文；负面结果照实写；不在每句里表演谦逊。

## 6. 本书与系列的差异（有意为之）

- **行距 1.62、段距 9.5pt**（系列默认 1.5 / 8pt）：为达到 300 页以上的科普专著体量，并提高长文可读性。改 `assets/css/paper.css` 的 `body{line-height}` 与 `p{margin}` 即可回退。
- **17 个附录**：比系列专著多，因为本书要覆盖“分支、精神病理学、被漏掉的传统、中国心理学、疗法、AI、方法手册”；这是内容需要，不是凑页。
- **4 级目录**：部分 → 章 → 节（h3）→ 子节（h4）。h4 大量用于“案例/反例”，是本书的主要论证装置。
- **第 11 章/第 17 章的接口**：第 11 章加“为什么这一章在第二部分”（讲述的预演）；第 17 章加“为什么这一章讲临界”（临界的预演）；第 5/16 章开头加部分导言。
- **第 25 章分两半**：25.1—25.4 回望，25.5“从回望到边界”，25.6 边界，25.7 尺子，25.8 一句话。
- **第 17 章的“临界”副线**：17.4 开头明确“皮亚杰与乔姆斯基都把门槛设得比数据更整齐”，避免“临界”只在 17.6 出现。
- **第 7 章判据**：用 1942—1944“争论讨论”三派分裂这一制度事实；“无法操作化”留在 7.5 正文。

## 7. 已踩过的坑（改稿前先看）

1. **h4 插错位置**：用 `str.replace(head, block+head, 1)` 插入 h4 时，若插在“一句话带走”前，会落到最后一个 h3 下，而不是目标节。必须检查每个 h4 的编号前缀与最近的前一个 h3 一致；不一致时，把整块移到目标 h3 之后、下一个 h3 之前。
2. **`parts.json` 与正文 h3 不同步**：正文合并/删节后，TOC 会列出不存在的节。用脚本从 h3 标题重建 `sections`。
3. **`<div class="box…"><p>…</div>` 缺 `</p>`**：HTML5 能渲染，XML 不合法，EPUB 校验会报错。批量补 `</p>`。
4. **字面 `\n`**：在 bash heredoc 里写 `\n` 会原样进入 HTML；追加内容后必须 `s.replace('\\n','\n')` 并 grep。
5. **繁体残留**：新增段落里容易混入“症狀/治療/科學/歷史/隨時/哪種/問題/篩查”；`analysis/audit.py` 的 A6 会报。
6. **未转义 `&` 与 `<`**：`Smith & Glass`、`p < 0.05` 必须写成 `&amp;`、`&lt;`。
7. **图号与章号**：每章图号用 `图 X.1`，不要跨章共用；`audit.py` 只查缺失文件，不查编号连续性，改图后人工核一遍。
8. **页数**：`pypdf` 量 `output/book.pdf`；本书 309 页。若改稿后掉到 300 以下，优先加“案例/反例”h4，不要靠拉大字号。

## 8. 发布

- `release/` 只放读者面文件：印刷 PDF、电子阅读 PDF、EPUB、HTML、Markdown、封面、README、修订说明、数据缺口、欢迎补充。
- `BASE=mind-forks`；脚本 `scripts/release.sh` 已按本书文件名适配。
- GitHub Release：一个产物一个 tag（若采用 Model B），或一个 release 承载全部资产（Model A）；同一版次不重复建 tag。
- Zenodo：先确认仓库已开启 Enabled Repositories；概念 DOI 与版本 DOI 发布后写回 `CITATION.cff` 与 `README.md`。

## 9. 待办

- [ ] Zenodo 归档，取得概念 DOI / 版本 DOI，写回 `CITATION.cff`、`README.md`、`versions/CHANGELOG.md`。
- [ ] 若有外部审阅，优先核对：附录 J 的精神病理学史年份、附录 L 的中国心理学年份、第 24 章的复现率数字。
- [ ] 英文研究笔记（5—10 页）：六问 + 两个案例（行为主义、DSM）+ 边界，附本书 DOI。
