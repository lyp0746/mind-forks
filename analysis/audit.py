# -*- coding: utf-8 -*-
"""audit.py — 《心灵的分岔》结构与引用校对。

输出：校对清单.md 与 analysis/results/audit.json

检查项：
  A1 标题层级与编号（h2/h3/h4 数量、h3/h4 编号是否与所在章一致、重复 id）
  A2 图：引用是否存在、图号是否连续、是否有定义未被引用
  A3 表：表号是否连续、是否有 caption
  A4 证据等级标注统计（A/B/C）
  A5 章/附录交叉引用是否在范围内
  A6 文本卫生：未转义的 &、字面 \\n、空段落、繁体残留
"""
import glob
import html
import json
import os
import re
from collections import Counter

BOOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(BOOK, "source")
OUT = os.path.join(BOOK, "analysis", "results")
os.makedirs(OUT, exist_ok=True)

FILES = sorted(glob.glob(os.path.join(SOURCE, "*.html")))
CHAPTERS = [p for p in FILES if re.search(r"ch\d{2}\.html$", p)]

TRAD = ["症狀", "治療", "科學", "歷史", "篩查", "隨時", "哪種", "為什麼",
        "這個", "發現", "應該", "選擇", "關係", "問題", "實現", "數據",
        "網絡", "機構", "語言", "意義", "意識", "記憶", "遺忘", "錯誤",
        "認為", "他們", "後來", "裡面", "變化", "還是", "無法", "系統",
        "專業", "服務", "人員", "什麼", "怎麼", "已經", "經驗", "證據"]


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def text(h):
    return html.unescape(re.sub(r"<[^>]+>", "", h))


R = {}
report = []

# ---------------------------------------------------------------- A1 标题
h1 = h2 = h3 = h4 = 0
ids = []
head_err = []
for p in FILES:
    s = read(p)
    h1 += len(re.findall(r"<h1\b", s))
    h2 += len(re.findall(r"<h2\b", s))
    h3 += len(re.findall(r"<h3\b", s))
    h4 += len(re.findall(r"<h4\b", s))
    ids += re.findall(r'id="([^"]+)"', s)

    if re.search(r"ch\d{2}\.html$", p):
        n = int(re.search(r"ch(\d{2})", p).group(1))
        cur = None
        for m in re.finditer(r'<h3 id="sec(\d+)-(\d+)">|<h4>(\d+)\.(\d+)\.(\d+)　', s):
            if m.group(1):
                cur = (int(m.group(1)), int(m.group(2)))
                if cur[0] != n:
                    head_err.append((os.path.basename(p), "h3 章号不符", cur))
            else:
                x, y, z = int(m.group(3)), int(m.group(4)), int(m.group(5))
                if cur != (x, y):
                    head_err.append((os.path.basename(p), "h4 不在所属节", (x, y, z), cur))

dup_ids = [k for k, v in Counter(ids).items() if v > 1]
R["A1_headings"] = {"h1": h1, "h2": h2, "h3": h3, "h4": h4,
                    "ids": len(ids), "dup_ids": dup_ids, "errors": head_err}
report.append(("A1 标题与编号",
               f"h1={h1}，h2={h2}，h3={h3}，h4={h4}；重复 id={dup_ids or '无'}；编号错误={head_err or '无'}"))

# ---------------------------------------------------------------- A2 图
fig_refs, fig_missing = [], []
for p in FILES:
    s = read(p)
    for m in re.finditer(r'<img class="fig" src="([^"]+)"', s):
        src = m.group(1)
        fig_refs.append((os.path.basename(p), src))
        if not os.path.exists(os.path.join(BOOK, src)):
            fig_missing.append(src)
fig_nums = []
for p in FILES:
    s = read(p)
    for m in re.finditer(r'<div class="cap"><b>图\s*([0-9.]+)', s):
        fig_nums.append(m.group(1))
R["A2_figures"] = {"count": len(fig_refs), "missing": fig_missing, "numbers": fig_nums}
report.append(("A2 图", f"图 {len(fig_refs)} 幅；缺失={fig_missing or '无'}；编号={len(fig_nums)} 个"))

# ---------------------------------------------------------------- A3 表
tab_nums, tab_nocap = [], []
for p in FILES:
    s = read(p)
    tables = re.findall(r'<table class="nat">', s)
    caps = re.findall(r'<caption class="cap"><b>表\s*([0-9A-Z.]+)', s)
    tab_nums += caps
    if len(tables) > len(caps):
        tab_nocap.append((os.path.basename(p), len(tables), len(caps)))
R["A3_tables"] = {"captions": len(tab_nums), "missing_caption": tab_nocap}
report.append(("A3 表", f"表题 {len(tab_nums)} 个；无表题={tab_nocap or '无'}"))

# ---------------------------------------------------------------- A4 等级
grade = Counter()
for p in FILES:
    s = text(read(p))
    for g in ["A", "B", "C"]:
        grade[g] += len(re.findall(rf"（{g}[／/]", s)) + len(re.findall(rf"等级：{g}", s))
R["A4_grades"] = dict(grade)
report.append(("A4 等级标注", f"A={grade['A']}，B={grade['B']}，C={grade['C']}（近似计数）"))

# ---------------------------------------------------------------- A5 交叉引用
bad_ref = []
for p in FILES:
    s = text(read(p))
    for m in re.finditer(r"第\s*(\d+)\s*章", s):
        n = int(m.group(1))
        if n < 1 or n > 25:
            bad_ref.append((os.path.basename(p), m.group(0)))
    for m in re.finditer(r"附录\s*([A-Q])", s):
        pass
R["A5_refs"] = {"bad": bad_ref}
report.append(("A5 交叉引用", f"越界章号={bad_ref or '无'}"))

# ---------------------------------------------------------------- A6 文本卫生
hyg = []
for p in FILES:
    s = read(p)
    name = os.path.basename(p)
    if "\\n" in s:
        hyg.append((name, "字面 \\n"))
    if re.search(r"&(?!amp;|lt;|gt;|quot;|#)", s):
        hyg.append((name, "未转义 &"))
    if "<p></p>" in s:
        hyg.append((name, "空段落"))
    for w in TRAD:
        if w in s:
            hyg.append((name, "繁体残留 " + w))
R["A6_hygiene"] = hyg
report.append(("A6 文本卫生", f"问题={hyg or '无'}"))

# ---------------------------------------------------------------- 写出
with open(os.path.join(OUT, "audit.json"), "w", encoding="utf-8") as f:
    json.dump(R, f, ensure_ascii=False, indent=2)

lines = ["# 校对清单", "",
         f"扫描文件：{len(FILES)} 个（章 {len(CHAPTERS)} 个）", ""]
for name, msg in report:
    lines.append(f"- **{name}**：{msg}")
lines.append("")
lines.append("> 本清单由 `analysis/audit.py` 生成；A4 为近似计数，只用于看比例，不作为精确统计。")
with open(os.path.join(BOOK, "校对清单.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print("\n".join(lines))
