# 心灵的分岔 · 

> 从无意识到可观察——心理学流派的六次划线
>
> **DOI**：10.5281/zenodo.23637236　·　概念 DOI：10.5281/zenodo.23637235　·　283 页 / 6 部分 / 25 章

心理学一百五十年的历史，看起来是一连串互相否定的流派：精神分析说人由无意识驱动，行为主义说只该研究可观察的行为，认知革命又把“内部”划了回来，人本主义说你们都在研究残缺的人。本书不判断谁对谁错，只问同一个问题：这个流派把什么划进了“心理”，又把什么划到了外面；它记住了什么、忘了什么；它用哪一个钟；它在紧预算下保了哪两项、让出了哪一项；谁有资格说它“科学”；它的门槛是观察到的还是被规定的。全书以“看见、记住、跟上、选择、讲述、临界”六个核心作暗线，分六部分二十五章，从一个流派的故事开场，以一句“它让出了什么”收束：从柏拉图与笛卡尔的前史，到冯特、詹姆斯、弗洛伊德、荣格、克莱因、鲍尔比、拉康、华生、斯金纳、皮亚杰、乔姆斯基、马斯洛、罗杰斯、弗兰克尔、维果茨基、贝特森，直到 DSM 与循证治疗、复现危机、WEIRD 与本土心理学。附流派×六核心对照表、一百五十年时间线、术语表、一百个人名、被埋没与重新发现的清单、可证伪登记簿与数据缺口。它是一本科普书，也是一次方法演示：六核心不是裁判，是六个提问。

---

## 结构

| 部分 | 标题 | 章数 | 起 → 止 |
|---|---|---:|---|
| 1 | 第一部分　划线的诞生 | 4 | 哲学的遗产：在心理学诞生之前，“心”被划在哪里 → 格式塔：整体不等于部分之和 |
| 2 | 第二部分　深度的代价 | 7 | 弗洛伊德：把无意识划进来 → 心理测量：谁有资格给人打分 |
| 3 | 第三部分　可观察的约束 | 4 | 行为主义革命：华生与巴甫洛夫 → 行为主义的遗产：它没有死 |
| 4 | 第四部分　内部的回归 | 4 | 认知革命：把“内部”划回来 → 社会认知与群体：情境的力量 |
| 5 | 第五部分　意义与时间 | 3 | 人本主义：第三势力 → 发展心理学：一生的钟 |
| 6 | 第六部分　系统与定价 | 3 | 系统与后现代：谁有资格定义问题 → 六核回望：每个流派让出了什么 |

每章八段：主提问 → 场景开篇 → 导论 → 机制 → 表/图 → 反例 → 本章小结 → 一句话带走。
每个部分有满栏插图扉页（`assets/svg/part-NN.svg`）、一段部分导语与一段部分小结。

## 证据与自检

- 结论标注 **A/B/C** 证据等级与甲/乙/丙概念等级；结论强度不超过证据强度。
- 可证伪登记簿：`docs/preregistration/checkups.csv`（append-only）。
- 结构校阅：系列 lint 24 条规则，本书 **error 0 / warn 0**（见 `_series/lint/REPORT.md`）。

## 文件

| 路径 | 是什么 |
|---|---|
| `source/` | **唯一正文来源**（HTML）；`book.json` 元数据、`parts.json` 结构 |
| `analysis/` | 图表、统计、抓取脚本（可重跑） |
| `assets/` | 封面、SVG 图、CSS |
| `scripts/build.sh` | audit → 印刷 PDF → 电子版 → EPUB → Markdown |
| `docs/` | 方法、数据来源、缺口与登记簿 |

产物（`output/`、`release/`）不入库，可由 `source/` 重建。

## 引用

```
心灵的分岔：从无意识到可观察——心理学流派的六次划线。李毅芃，2026。10.5281/zenodo.23637236
```

## 系列（九本书）

| 书 | 仓库 |
|---|---|
| 只能选两样 | [knowledge-tradeoffs](https://github.com/lyp0746/knowledge-tradeoffs) |
| 区分的语法 | [distinction-evolution](https://github.com/lyp0746/distinction-evolution) |
| 遗忘的边界 | [capacity-cascade](https://github.com/lyp0746/capacity-cascade) |
| 错位的时间 | [entropy-spiral](https://github.com/lyp0746/entropy-spiral) |
| 选择的代价 | [impossibility-triangle](https://github.com/lyp0746/impossibility-triangle) |
| 诠释的权衡 | [interpretation-tradeoff](https://github.com/lyp0746/interpretation-tradeoff) |
| 涌现的临界 | [emergence-critical](https://github.com/lyp0746/emergence-critical) |
| 热点的账单 | [hotspot-bills](https://github.com/lyp0746/hotspot-bills) |

十四篇工作论文与全部条目的 DOI 见 [series-workspace](https://github.com/lyp0746/series-workspace)。

## 许可

正文与图件 CC BY 4.0；脚本 MIT。
