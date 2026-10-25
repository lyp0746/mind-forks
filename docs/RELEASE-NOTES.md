# 发布说明（RELEASE-NOTES）

## 本版内容

- 6 部分、25 章、17 个附录（A—Q）。
- 309 页（A4 印刷版）；415 页（B5 电子阅读版，因字号与行距不同）。
- 25 幅矢量插图；68 个表；约 26 万字。
- 四种格式：`mind-forks-print.pdf`、`mind-forks-ereader.pdf`、`mind-forks.epub`、`mind-forks.html`、`mind-forks.md`。

## 结构

- 前置：封面、扉页、版权页、目录、总纲、导论、怎么读、六核速查。
- 正文：第一部分（1—4）、第二部分（5—11）、第三部分（12—15）、第四部分（16—19）、第五部分（20—22）、第六部分（23—25）。
- 后置：尾声、后记、附录 A—Q、本系列（八本书）。

## 证据与边界

- 所有结论标注 A／B／C；C 级只作方向判断。
- 不提供临床建议，不裁判疗效；“讲述”不做“揭穿”。
- 附录 F 是可证伪登记簿；附录 G 是数据缺口与边界。

## 已知问题

- 个别实验（小艾伯特、斯坦福监狱、米尔格拉姆）的史学解释仍有争议；正文同时给原始报告与批评，不把任何一方写成定论。
- 附录 J、L 的部分年份为常见史学说法，个别事件的时间有不同版本；正文从略。
- 插图是示意图，不是历史照片，不能作为史料使用。

## 复现

```bash
PY="/mnt/d/0_Code/Iris Series/.venv/Scripts/python.exe"
"$PY" analysis/make_figures.py && "$PY" analysis/make_cover.py
"$PY" analysis/audit.py
"$PY" build_book.py --pdf
"$PY" build_book.py --ereader --pdf
"$PY" build_epub.py
"$PY" build_markdown.py
bash scripts/release.sh
```

## 归档

Zenodo DOI 待发布后写回 `CITATION.cff` 与 `README.md`。若仓库未开启 Enabled Repositories，需手动上传发布包（或走 API）。
