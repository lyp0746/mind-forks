# -*- coding: utf-8 -*-
"""make_cover.py — 生成《心灵的分岔》满版封面 SVG（A4 比例 1000×1414）。

系列统一版式：暗色渐变、顶部金线、标题/副标题/作者/英文行的位置与字号，
仅中心线描母题因书而异。母题：一条主干向上分岔成六条支线——
六次划线；其中一条用红色虚线，表示“被划到外面的那一条”。
"""
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "assets", "svg", "cover.svg")

W, H = 1000, 1414
INK = "#e8e6df"
DIM = "#9aa0a6"
GOLD = "#b8862f"
RED = "#c94f4f"


def build():
    layers = []

    # 主干：从底部向上
    trunk = "M 500 1040 L 500 860"
    layers.append(f'<path d="{trunk}" fill="none" stroke="#7d8a99" stroke-width="2" opacity="0.7"/>')

    # 三个分叉点
    forks = [(500, 860, 380, 720), (500, 860, 500, 720), (500, 860, 620, 720)]
    for x1, y1, x2, y2 in forks:
        layers.append(f'<path d="M {x1} {y1} Q {(x1+x2)/2} {y1-60} {x2} {y2}" fill="none" stroke="#7d8a99" stroke-width="1.8" opacity="0.7"/>')

    # 六个末端
    ends = [(380, 720, 260, 570), (380, 720, 360, 570),
            (500, 720, 460, 560), (500, 720, 540, 560),
            (620, 720, 640, 570), (620, 720, 740, 570)]
    for i, (x1, y1, x2, y2) in enumerate(ends):
        dash = ' stroke-dasharray="7,6"' if i == 5 else ''
        col = RED if i == 5 else "#7d8a99"
        opacity = "0.85" if i == 5 else "0.7"
        layers.append(f'<path d="M {x1} {y1} Q {(x1+x2)/2+ (18 if i%2 else -18)} {y1-70} {x2} {y2}" '
                      f'fill="none" stroke="{col}" stroke-width="1.8" opacity="{opacity}"{dash}/>')
        fill = "none" if i == 5 else GOLD
        layers.append(f'<circle cx="{x2}" cy="{y2}" r="7" fill="{fill}" stroke="{RED if i==5 else GOLD}" '
                      f'stroke-width="1.6" opacity="0.9"/>')

    # 标签（六核），避开线路
    labels = [("看见", 225, 548), ("记住", 330, 540), ("跟上", 430, 532),
              ("选择", 570, 532), ("讲述", 670, 540), ("临界", 775, 548)]
    for i, (t, x, y) in enumerate(labels):
        col = RED if i == 5 else "#cfd6de"
        layers.append(f'<text x="{x}" y="{y}" text-anchor="middle" class="vl" fill="{col}">{t}</text>')

    # 中间题字
    layers.append(f'<text x="500" y="800" text-anchor="middle" class="mid">六次划线</text>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#0e1117"/><stop offset="0.55" stop-color="#151a23"/>
<stop offset="1" stop-color="#0b0e14"/>
</linearGradient>
</defs>
<rect x="0" y="0" width="{W}" height="{H}" fill="url(#bg)"/>
<rect x="0" y="0" width="{W}" height="8" fill="{GOLD}" opacity="0.85"/>
{chr(10).join(layers)}
<style>
text{{font-family:'Microsoft YaHei','SimHei',Arial,sans-serif;}}
.ttl{{font-size:112px;font-weight:700;letter-spacing:14px;fill:{INK};}}
.sub{{font-size:28px;fill:{DIM};letter-spacing:2px;}}
.eng{{font-size:20px;fill:{DIM};letter-spacing:1px;}}
.au{{font-size:30px;fill:{INK};letter-spacing:2px;}}
.rule{{stroke:{DIM};stroke-width:1;opacity:0.6;}}
.vl{{font-size:22px;letter-spacing:1px;}}
.mid{{font-size:32px;fill:{GOLD};letter-spacing:8px;font-weight:700;}}
</style>
<text x="80" y="176" class="eng">THE FORKING MIND</text>
<text x="80" y="300" class="ttl">心灵的分岔</text>
<line x1="84" y1="344" x2="760" y2="344" class="rule"/>
<text x="84" y="396" class="sub">从无意识到可观察：</text>
<text x="84" y="440" class="sub">心理学流派的六次划线</text>
<text x="84" y="500" class="eng">看见 · 记住 · 跟上 · 选择 · 讲述 · 临界</text>
<text x="80" y="1180" class="au">李毅芃　著</text>
<text x="80" y="1232" class="eng">Six Ways Psychology Drew Its Lines</text>
<text x="80" y="1274" class="eng">科普专著 · 2026</text>
</svg>
'''
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", OUT)


if __name__ == "__main__":
    build()
