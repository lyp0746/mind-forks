# -*- coding: utf-8 -*-
"""make_figures.py — 《心灵的分岔》全部矢量插图（确定性生成）。

输出：assets/svg/fig-*.svg
风格与系列一致：白底、微软雅黑、标题居中、统一配色。
每图一个主张；标注放在空白区，不压线。
"""
import math
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "assets", "svg")
os.makedirs(OUT, exist_ok=True)

INK = "#1a1a1a"
GRY = "#666666"
BLU = "#2f6db0"
GRN = "#2e7d32"
ORG = "#ef6c00"
RED = "#c62828"
GLD = "#b8862f"
PNK = "#8e5a9c"
FONT = "Microsoft YaHei, PingFang SC, SimHei, sans-serif"


def head(w, h, title, sub=None):
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
         f'font-family="{FONT}">',
         f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
         f'<text x="{w/2:.0f}" y="38" text-anchor="middle" font-size="22" font-weight="bold" fill="{INK}">{title}</text>']
    if sub:
        s.append(f'<text x="{w/2:.0f}" y="62" text-anchor="middle" font-size="14" fill="{GRY}">{sub}</text>')
    return s


def box(x, y, w, h, fill="#f5f7fa", stroke=BLU, rx=8, sw=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def txt(x, y, t, size=14, fill=INK, anchor="middle", weight="normal", italic=False):
    st = ' font-style="italic"' if italic else ''
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}"{st}>{t}</text>')


def line(x1, y1, x2, y2, color=GRY, w=1.6, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"{d}/>'


def arrow(x1, y1, x2, y2, color=GRY, w=1.8, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"{d} '
            f'marker-end="url(#ah)"/>')


DEFS = f'''<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"
markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 z" fill="{GRY}"/></marker></defs>'''


def circle(cx, cy, r, fill="none", stroke=INK, sw=1.6, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def save(name, parts):
    svg = "\n".join(parts + ["</svg>"])
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", name + ".svg")


# ------------------------------------------------------------------ 0 结构
def fig_structure():
    W, H = 1000, 700
    s = head(W, H, "全书结构：六部分、二十五章、一条暗线",
             "每一部分以一个核心为主提问，同时把前一个核心的成果带在身后")
    s.append(DEFS)
    parts = [
        ("一　划线的诞生", "看见 / 记住", "第 1—4 章", BLU, "哲学 · 冯特 · 构造/机能 · 格式塔"),
        ("二　深度的代价", "记住 / 选择", "第 5—11 章", GRN, "精神分析全谱系 · 心理测量"),
        ("三　可观察的约束", "看见 / 讲述", "第 12—15 章", ORG, "行为主义 · 斯金纳 · 行为疗法"),
        ("四　内部的回归", "看见 / 记住", "第 16—19 章", PNK, "认知革命 · 皮亚杰/乔姆斯基 · 神经 · 社会"),
        ("五　意义与时间", "选择 / 跟上", "第 20—22 章", GLD, "人本 · 存在 · 发展"),
        ("六　系统与定价", "讲述 / 临界", "第 23—25 章", RED, "系统/后现代 · 当代 · 回望"),
    ]
    y = 92
    for i, (name, core, rng, col, members) in enumerate(parts):
        s.append(box(80, y, 840, 82, "#fbfcfe", col, 10))
        s.append(txt(112, y + 32, name, 19, col, "start", "bold"))
        s.append(txt(112, y + 58, members, 13, GRY, "start"))
        s.append(txt(700, y + 30, f"主核：{core}", 15, INK, "start"))
        s.append(txt(700, y + 56, rng, 13, GRY, "start"))
        if i < len(parts) - 1:
            s.append(arrow(500, y + 84, 500, y + 100, GRY, 1.6))
        y += 100
    save("fig-structure", s)


# ------------------------------------------------------------------ 1 两条谱系
def fig_lineage():
    W, H = 1000, 620
    s = head(W, H, "心理学诞生前的两条谱系",
             "哲学给出问题，生理学给出方法；两条线在 1879 年汇合")
    s.append(DEFS)
    # 左列哲学
    s.append(box(70, 100, 340, 380, "#f7f9fc", BLU))
    s.append(txt(240, 132, "哲学谱系：问“心是什么”", 17, BLU, weight="bold"))
    ph = ["柏拉图：三分灵魂", "亚里士多德：灵魂是形式", "笛卡尔：心身二元", "洛克：白板与联想",
          "莱布尼茨：微知觉", "康德：先天形式与现象"]
    for i, t in enumerate(ph):
        s.append(txt(240, 172 + i * 50, t, 14, INK))
    # 右列生理学
    s.append(box(590, 100, 340, 380, "#f7fbf8", GRN))
    s.append(txt(760, 132, "生理学谱系：问“心如何工作”", 17, GRN, weight="bold"))
    bi = ["布洛卡：脑区与语言", "亥姆霍兹：神经传导速度", "费希纳：心理物理学", "赫尔巴特：意识阈",
          "达尔文：适应与进化", "反射学：刺激—反应"]
    for i, t in enumerate(bi):
        s.append(txt(760, 172 + i * 50, t, 14, INK))
    # 汇合
    s.append(arrow(410, 290, 480, 350, BLU))
    s.append(arrow(590, 290, 520, 350, GRN))
    s.append(box(330, 360, 340, 110, "#fff8e1", GLD, 10, 1.8))
    s.append(txt(500, 396, "1879　心理学实验室", 19, GLD, weight="bold"))
    s.append(txt(500, 424, "可测量的对象 + 可公共重复的实验", 13, INK))
    s.append(txt(500, 448, "＝ 心理学成为一门建制学科", 13, GRY))
    s.append(txt(500, 540, "注：这是一条主线，不是唯一路径；冯特本人仍把高层思维留给民族心理学。", 12, GRY))
    save("fig-lineage", s)


# ------------------------------------------------------------------ 2 三种钟
def fig_three_clocks():
    W, H = 1000, 620
    s = head(W, H, "三种钟：毫秒、一次行为、一生",
             "同一个心理过程，在三个尺度上是三种不同的对象")
    s.append(DEFS)
    rows = [
        ("冯特：毫秒", "反应时、阈限、注意转移", "0.001 s — 1 s", BLU, 0.08),
        ("布伦塔诺：一次行为", "看见一个对象、判断一个命题", "1 s — 1 min", GRN, 0.34),
        ("詹姆斯：一生", "习惯、适应、选择", "1 年 — 80 年", ORG, 0.70),
    ]
    for i, (name, what, scale, col, frac) in enumerate(rows):
        y = 120 + i * 150
        s.append(txt(80, y, name, 17, col, "start", "bold"))
        s.append(txt(80, y + 26, what, 13, GRY, "start"))
        s.append(line(80, y + 56, 920, y + 56, "#dddddd", 8))
        x = 80 + frac * 840
        s.append(circle(x, y + 56, 8, col, col))
        s.append(txt(x, y + 88, scale, 13, col))
        s.append(txt(920, y + 88, "→ 能看见", 12, GRY, "end"))
    s.append(txt(500, 580, "选哪个钟，决定了你能看见什么、看不见什么；三个钟不能同时对准。", 13, GRY))
    save("fig-three-clocks", s)


# ------------------------------------------------------------------ 3 构造 vs 机能
def fig_cat():
    W, H = 1000, 640
    s = head(W, H, "第一次三选二：构造主义与机能主义",
             "C 完备 / A 可组合 / T 传递 —— 两条路各保两项")
    s.append(DEFS)
    cx, cy, R = 500, 310, 150

    def pt(deg):
        a = math.radians(deg)
        return cx + R * math.cos(a), cy + R * math.sin(a)
    xc, yc = pt(-90)
    xa, ya = pt(150)
    xt, yt = pt(30)
    s.append(f'<polygon points="{xc:.0f},{yc:.0f} {xa:.0f},{ya:.0f} {xt:.0f},{yt:.0f}" fill="#f7f9fc" stroke="#9aa4b2" stroke-width="2"/>')
    s.append(circle(xc, yc, 9, BLU, BLU))
    s.append(circle(xa, ya, 9, GRN, GRN))
    s.append(circle(xt, yt, 9, ORG, ORG))
    s.append(txt(xc, yc - 32, "C 完备（精确分析）", 15, BLU, weight="bold"))
    s.append(txt(xa, ya + 36, "A 可组合（元素/功能）", 15, GRN, weight="bold"))
    s.append(txt(xt, yt + 36, "T 传递（应用）", 15, ORG, weight="bold"))
    # 两条边加粗
    s.append(line(xc, yc, xa, ya, BLU, 5))
    s.append(line(xa, ya, xt, yt, ORG, 5))
    s.append(txt(cx, cy + 4, "构造：C+A", 15, BLU, weight="bold"))
    s.append(txt(cx, cy + 30, "让出 T", 14, RED))
    s.append(txt(500, 540, "机能：A+T　→　让出 C（精确机制）", 15, GRN, weight="bold"))
    s.append(txt(500, 570, "两条边都经过 A；分歧在“要不要为了精确而放弃应用”。", 13, GRY))
    save("fig-cat", s)


# ------------------------------------------------------------------ 4 格式塔
def fig_gestalt():
    W, H = 1000, 560
    s = head(W, H, "三个格式塔现象：你看见的不是纸上画的东西",
             "似动 · 闭合 · 图形—背景")
    s.append(DEFS)
    # phi
    s.append(box(50, 100, 280, 340, "#fbfcfe", BLU))
    s.append(txt(190, 132, "① phi 现象", 16, BLU, weight="bold"))
    s.append(circle(120, 220, 12, BLU, BLU))
    s.append(circle(260, 220, 12, BLU, BLU))
    s.append(arrow(140, 220, 240, 220, GRY, 1.4, "4,4"))
    s.append(txt(190, 270, "两次静止闪光 → 看见运动", 13, INK))
    s.append(txt(190, 300, "运动是第一性的，不是推断", 12, GRY))
    # closure
    s.append(box(360, 100, 280, 340, "#fbfcfe", GRN))
    s.append(txt(500, 132, "② 闭合", 16, GRN, weight="bold"))
    s.append(f'<path d="M 430 210 A 70 70 0 1 1 500 290" fill="none" stroke="{GRN}" stroke-width="5"/>')
    s.append(txt(500, 330, "缺口被自动补成“圆”", 13, INK))
    s.append(txt(500, 360, "看见的是整体，不是弧段", 12, GRY))
    # figure-ground
    s.append(box(670, 100, 280, 340, "#fbfcfe", PNK))
    s.append(txt(810, 132, "③ 图形—背景", 16, PNK, weight="bold"))
    s.append(f'<path d="M 760 180 C 700 230 700 330 760 370 C 820 330 820 230 760 180 Z" fill="{PNK}" opacity="0.55"/>')
    s.append(circle(735, 265, 26, "#ffffff", PNK, 3))
    s.append(circle(785, 265, 26, "#ffffff", PNK, 3))
    s.append(txt(810, 400, "花瓶，还是两张侧脸？", 13, INK))
    s.append(txt(810, 428, "同一刺激，两种组织", 12, GRY))
    s.append(txt(500, 500, "格式塔的结论：组织是自动的、先于元素的；代价是它很难被分解与计算。", 13, GRY))
    save("fig-gestalt", s)


# ------------------------------------------------------------------ 5 冰山
def fig_iceberg():
    W, H = 1000, 620
    s = head(W, H, "弗洛伊德的三个模型：地形学与结构模型",
             "意识 / 前意识 / 无意识；本我 / 自我 / 超我")
    s.append(DEFS)
    # water line
    s.append(line(80, 260, 920, 260, BLU, 2, "8,5"))
    s.append(txt(90, 248, "意识的水面", 13, BLU, "start"))
    # 三层
    bands = [("意识", 100, 150, "#eaf2fb", BLU), ("前意识", 250, 520, "#f3f7fc", BLU),
             ("无意识", 520, 900, "#e8eef7", "#5b7fa8")]
    for name, y1, y2, fill, stroke in bands:
        s.append(f'<rect x="220" y="{y1}" width="560" height="{y2-y1}" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
        s.append(txt(250, y1 + 30, name, 16, stroke, "start", "bold"))
    # 结构模型三块
    s.append(f'<ellipse cx="360" cy="470" rx="90" ry="70" fill="#fdecea" stroke="{RED}" stroke-width="2"/>')
    s.append(txt(360, 476, "本我", 17, RED, weight="bold"))
    s.append(f'<ellipse cx="520" cy="330" rx="100" ry="60" fill="#fff8e1" stroke="{GLD}" stroke-width="2"/>')
    s.append(txt(520, 336, "自我", 17, GLD, weight="bold"))
    s.append(f'<ellipse cx="650" cy="440" rx="95" ry="55" fill="#f3e9f7" stroke="{PNK}" stroke-width="2"/>')
    s.append(txt(650, 446, "超我", 17, PNK, weight="bold"))
    s.append(txt(500, 580, "地形学讲“在哪一层”，结构模型讲“谁和谁冲突”；两者不是替代，是两套坐标。", 13, GRY))
    save("fig-iceberg", s)


# ------------------------------------------------------------------ 6 三种深度
def fig_depths():
    W, H = 1000, 600
    s = head(W, H, "三种“深度”：弗洛伊德、荣格、阿德勒",
             "同一个词，三种不同的对象")
    s.append(DEFS)
    cards = [
        ("弗洛伊德", "个人无意识", "童年经验、性驱力、压抑", "解码：梦、移情、自由联想", BLU),
        ("荣格", "集体无意识", "原型、神话、宗教象征", "解码：跨文化比较、象征学", PNK),
        ("阿德勒", "生活风格", "自卑、补偿、社会兴趣", "解码：目标、行为模式、教育观察", GRN),
    ]
    for i, (name, core, content, method, col) in enumerate(cards):
        x = 60 + i * 310
        s.append(box(x, 110, 280, 380, "#fbfcfe", col, 10))
        s.append(txt(x + 140, 150, name, 20, col, weight="bold"))
        s.append(txt(x + 140, 190, core, 16, INK, weight="bold"))
        s.append(txt(x + 140, 230, content, 12, GRY))
        s.append(line(x + 30, 255, x + 250, 255, "#dddddd", 1))
        s.append(txt(x + 140, 285, "解释权在谁手里？", 12, GRY))
        s.append(txt(x + 140, 315, method, 12, INK))
        s.append(txt(x + 140, 430, ["诊所里的分析师", "博学的象征学家", "教师与家长"][i], 13, col, weight="bold"))
    s.append(txt(500, 550, "三个人都相信“深度”；分歧在于深度在哪里、谁有资格解释它。", 13, GRY))
    save("fig-depths", s)


# ------------------------------------------------------------------ 7 两个位置
def fig_positions():
    W, H = 1000, 560
    s = head(W, H, "克莱因的两个位置：从分裂到整合",
             "不是两个阶段，而是两种组织经验的方式；成人也会在两者之间来回")
    s.append(DEFS)
    s.append(line(90, 250, 910, 250, "#cccccc", 2))
    for x, lab in [(220, "出生"), (500, "约 6 个月"), (780, "成人生活")]:
        s.append(circle(x, 250, 6, GRY, GRY))
        s.append(txt(x, 282, lab, 12, GRY))
    s.append(box(110, 110, 300, 110, "#fdecea", RED))
    s.append(txt(260, 145, "偏执—分裂位置", 17, RED, weight="bold"))
    s.append(txt(260, 175, "全好 / 全坏；分裂、投射", 12, INK))
    s.append(txt(260, 200, "核心焦虑：被害", 12, GRY))
    s.append(box(590, 110, 300, 110, "#eef7f0", GRN))
    s.append(txt(740, 145, "抑郁位置", 17, GRN, weight="bold"))
    s.append(txt(740, 175, "好与坏在同一个对象里", 12, INK))
    s.append(txt(740, 200, "核心焦虑：因攻击而失去", 12, GRY))
    s.append(arrow(410, 165, 590, 165, GLD, 2.2))
    s.append(txt(500, 150, "整合", 13, GLD))
    s.append(arrow(590, 330, 410, 330, GRY, 1.6, "6,4"))
    s.append(txt(500, 356, "压力下退回", 12, GRY))
    s.append(txt(500, 450, "成人政治里的非黑即白、网暴、追星，都是偏执—分裂位置的回声（C）。", 13, GRY))
    save("fig-positions", s)


# ------------------------------------------------------------------ 8 陌生情境
def fig_strange():
    W, H = 1000, 520
    s = head(W, H, "陌生情境：八个小节，二十分钟",
             "分离与重聚被压缩成一次可观察的压力测试")
    s.append(DEFS)
    eps = [("母子\n进入", 0, 2, BLU), ("母亲\n坐下", 2, 4, BLU), ("陌生人\n进入", 4, 6, ORG),
           ("母亲\n离开", 6, 8, RED), ("陌生人\n安抚", 8, 10, ORG), ("母亲\n回来", 10, 12, GRN),
           ("母亲\n再离开", 12, 14, RED), ("陌生人\n回来", 14, 16, ORG), ("母亲\n回来", 16, 20, GRN)]
    x0, x1 = 80, 920
    for i, (lab, a, b, col) in enumerate(eps):
        xa = x0 + (x1 - x0) * a / 20
        xb = x0 + (x1 - x0) * b / 20
        s.append(f'<rect x="{xa:.0f}" y="140" width="{xb-xa:.0f}" height="70" fill="{col}" opacity="0.18" stroke="{col}" stroke-width="1.2"/>')
        s.append(txt((xa + xb) / 2, 172, lab.replace("\n", " "), 11, col, weight="bold"))
        s.append(txt((xa + xb) / 2, 196, f"{a}—{b}′", 10, GRY))
    s.append(line(x0, 240, x1, 240, GRY, 2))
    s.append(txt(x0, 268, "0 分钟", 11, GRY, "start"))
    s.append(txt(x1, 268, "20 分钟", 11, GRY, "end"))
    # 反应曲线
    s.append(txt(500, 320, "孩子的反应（示意）", 14, INK, weight="bold"))
    pts = [(80, 360), (250, 360), (330, 400), (420, 420), (500, 400), (580, 370), (660, 420), (740, 430), (820, 375), (920, 370)]
    d = "M " + " L ".join(f"{x} {y}" for x, y in pts)
    s.append(f'<path d="{d}" fill="none" stroke="{PNK}" stroke-width="2.5"/>')
    s.append(txt(420, 450, "分离 → 焦虑/哭泣", 12, RED))
    s.append(txt(820, 350, "重聚 → 被安抚", 12, GRN))
    s.append(txt(500, 490, "四种类型（安全/回避/矛盾/混乱）描述的是“如何用照顾者作为安全基地”，不是人格类型。", 12, GRY))
    save("fig-strange", s)


# ------------------------------------------------------------------ 9 三界
def fig_registers():
    W, H = 1000, 600
    s = head(W, H, "拉康的三界：想象、象征、实在",
             "三个环互相扣住；主体在它们的交界处被构成")
    s.append(DEFS)
    cx, cy, r = 500, 300, 130
    centers = [(cx - 70, cy - 55, BLU, "想象界", "形象 / 自恋 / 二元"),
               (cx + 70, cy - 55, GRN, "象征界", "语言 / 法则 / 大他者"),
               (cx, cy + 75, PNK, "实在界", "无法象征化的剩余")]
    for x, y, col, name, sub in centers:
        s.append(circle(x, y, r, "none", col, 2.6))
        s.append(txt(x, y - 10, name, 19, col, weight="bold"))
        s.append(txt(x, y + 18, sub, 11, GRY))
    s.append(txt(500, 520, "三界不是三个房间，而是三种“被结构”的方式；病理取决于哪一界出了故障（C）。", 13, GRY))
    save("fig-registers", s)


# ------------------------------------------------------------------ 10 翻译
def fig_translation():
    W, H = 1000, 640
    s = head(W, H, "翻译是有损的：弗洛伊德概念与现代对应",
             "被翻译的部分进入实验室；未被翻译的部分留在文本里")
    s.append(DEFS)
    left = [("接触屏障", 120), ("压抑", 180), ("事后性", 240), ("移情", 300), ("梦＝愿望满足", 360), ("死本能", 420)]
    right = [("突触可塑性", 120), ("记忆抑制", 180), ("记忆再巩固", 240), ("关系图式/预期", 300), ("REM 情绪加工（争议）", 360), ("无稳定对应", 420)]
    s.append(txt(200, 92, "弗洛伊德的概念", 15, BLU, weight="bold"))
    s.append(txt(800, 92, "现代对应", 15, GRN, weight="bold"))
    for (a, y), (b, _) in zip(left, right):
        s.append(box(40, y - 24, 300, 44, "#f7f9fc", BLU))
        s.append(txt(190, y + 4, a, 14, INK))
        s.append(box(660, y - 24, 300, 44, "#f7fbf8", GRN))
        s.append(txt(810, y + 4, b, 13, INK))
        s.append(arrow(345, y - 2, 655, y - 2, GRY, 1.4))
    s.append(txt(500, 480, "证据较强的翻译：接触屏障、事后性、移情（B）", 13, GRN))
    s.append(txt(500, 510, "几乎没有被翻译：梦的愿望满足、死本能（C）", 13, RED))
    s.append(txt(500, 560, "“被证实”通常只指左边最上面那几行；把整列都算作“弗洛伊德被证明”，是过度推销。", 12, GRY))
    save("fig-translation", s)


# ------------------------------------------------------------------ 11 IQ 分布
def fig_iq():
    W, H = 1000, 560
    s = head(W, H, "离差智商：一个位置，不是一个人的本质",
             "均值 100，标准差 15；约 68% 在 85—115，约 95% 在 70—130")
    s.append(DEFS)
    cx, base = 500, 420
    # 近似正态曲线
    pts = []
    for i in range(0, 241):
        x = 80 + i * 3.5
        z = (x - cx) / 90.0
        y = base - 280 * math.exp(-0.5 * z * z)
        pts.append((x, y))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    s.append(f'<path d="{d}" fill="none" stroke="{BLU}" stroke-width="2.6"/>')
    s.append(line(80, base, 920, base, GRY, 2))
    for val, x in [(70, cx - 180), (85, cx - 90), (100, cx), (115, cx + 90), (130, cx + 180)]:
        s.append(line(x, base, x, base + 8, GRY, 1.4))
        s.append(txt(x, base + 28, str(val), 12, GRY))
    s.append(txt(cx, base + 52, "分数", 12, GRY))
    # 阴影 68%
    s.append(f'<path d="M {cx-90} {base} L {cx-90} {base-280*math.exp(-0.5)} L ' + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts if cx - 90 <= x <= cx + 90) + f' L {cx+90} {base} Z" fill="{BLU}" opacity="0.15"/>')
    s.append(txt(cx, 160, "68%", 18, BLU, weight="bold"))
    s.append(txt(cx - 180, 300, "70", 11, GRY))
    s.append(txt(cx + 180, 300, "130", 11, GRY))
    s.append(txt(500, 520, "分数描述“在这套测验上的位置”；它不描述价值、未来，也不解释因果。", 13, GRY))
    save("fig-iq", s)


# ------------------------------------------------------------------ 12 S-R vs S-O-R
def fig_sor():
    W, H = 1000, 520
    s = head(W, H, "从 S—R 到 S—O—R：内部状态被划回来",
             "行为主义只看两端；认知主义在中间加了一个“黑箱”")
    s.append(DEFS)
    # 上：S-R
    s.append(txt(80, 120, "行为主义", 17, ORG, "start", "bold"))
    s.append(box(180, 92, 180, 64, "#fff3e0", ORG))
    s.append(txt(270, 132, "刺激 S", 16, INK))
    s.append(box(640, 92, 180, 64, "#fff3e0", ORG))
    s.append(txt(730, 132, "反应 R", 16, INK))
    s.append(arrow(365, 124, 635, 124, ORG, 2.4))
    s.append(txt(500, 112, "强化 / 惩罚", 12, GRY))
    # 下：S-O-R
    s.append(txt(80, 300, "认知主义", 17, BLU, "start", "bold"))
    s.append(box(180, 272, 180, 64, "#eaf2fb", BLU))
    s.append(txt(270, 312, "刺激 S", 16, INK))
    s.append(box(410, 272, 180, 64, "#eaf2fb", BLU))
    s.append(txt(500, 304, "内部 O", 16, INK))
    s.append(txt(500, 324, "表征 / 加工", 11, GRY))
    s.append(box(640, 272, 180, 64, "#eaf2fb", BLU))
    s.append(txt(730, 312, "反应 R", 16, INK))
    s.append(arrow(365, 304, 405, 304, BLU, 2.2))
    s.append(arrow(595, 304, 635, 304, BLU, 2.2))
    s.append(txt(500, 430, "S—O—R 不是“多了一个盒子”，而是“多了一个必须被推断的过程”。", 13, GRY))
    save("fig-sor", s)


# ------------------------------------------------------------------ 13 强化程序
def fig_schedules():
    W, H = 1000, 640
    s = head(W, H, "四种强化程序：为什么老虎机比工资更会留住人",
             "曲线越高越陡，行为越频繁；可变比率的消退最慢")
    s.append(DEFS)
    panels = [("固定比率 FR", "每 N 次给一次", "计件工资", BLU), ("可变比率 VR", "平均 N 次，不确定", "老虎机 / 抽卡", RED),
              ("固定间隔 FI", "每隔 T 时间给一次", "月薪", GRN), ("可变间隔 VI", "平均 T 时间，不确定", "查邮件", ORG)]
    for i, (name, rule, ex, col) in enumerate(panels):
        x = 50 + (i % 2) * 480
        y = 100 + (i // 2) * 250
        s.append(box(x, y, 420, 200, "#fbfcfe", col))
        s.append(txt(x + 18, y + 30, name, 16, col, "start", "bold"))
        s.append(txt(x + 18, y + 54, rule + "　例：" + ex, 11, GRY, "start"))
        # 累积曲线
        bx, by = x + 40, y + 170
        s.append(line(bx, by, bx + 340, by, GRY, 1.2))
        s.append(line(bx, by, bx, by - 100, GRY, 1.2))
        if i == 0:
            pts = [(0, 0)]
            for k in range(1, 7):
                pts.append((k * 48, (k - 1) * 16 + 4))
                pts.append((k * 48, k * 16))
            pts.append((340, 96))
        elif i == 1:
            pts = [(0, 0), (30, 14), (70, 36), (110, 40), (150, 62), (200, 68), (250, 84), (300, 90), (340, 98)]
        elif i == 2:
            pts = []
            for k in range(4):
                pts.append((k * 85, k * 25))
                pts.append((k * 85 + 60, k * 25 + 22))
            pts.append((340, 96))
        else:
            pts = [(0, 0), (40, 10), (80, 30), (140, 40), (200, 66), (260, 82), (340, 98)]
        d = "M " + " L ".join(f"{bx+px} {by-py}" for px, py in pts)
        s.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2.2"/>')
    s.append(txt(500, 600, "“消退最慢”的是可变比率：奖励不确定，行为最顽固。", 13, GRY))
    save("fig-schedules", s)


# ------------------------------------------------------------------ 14 暴露
def fig_exposure():
    W, H = 1000, 540
    s = head(W, H, "暴露：焦虑不会一次消失，但峰谷会逐渐下移",
             "抑制性学习：旧恐惧还在，新的“安全学习”逐渐占上风")
    s.append(DEFS)
    bx, by = 100, 420
    s.append(line(bx, by, 900, by, GRY, 1.6))
    s.append(line(bx, by, bx, 120, GRY, 1.6))
    s.append(txt(bx - 20, 130, "焦虑", 12, GRY, "end"))
    s.append(txt(900, 448, "时间 / 重复暴露", 12, GRY, "end"))
    pts = [(0, 0)]
    peaks = [210, 180, 150, 125, 105]
    for k, p in enumerate(peaks):
        x0 = 100 + k * 150
        pts += [(x0, 0), (x0 + 50, p), (x0 + 110, p * 0.45), (x0 + 150, 0)]
    d = "M " + " L ".join(f"{x} {420-y}" for x, y in pts)
    s.append(f'<path d="{d}" fill="none" stroke="{RED}" stroke-width="2.2"/>')
    for k, p in enumerate(peaks):
        x = 150 + k * 150
        s.append(line(x, 420, x, 420 - p, GRY, 1, "4,4"))
        s.append(txt(x + 6, 420 - p - 6, f"第{k+1}次", 10, GRY, "start"))
    s.append(txt(500, 500, "关键不是“待得够久”，而是“预期被违反”；安全行为会让违反失效。", 13, GRY))
    save("fig-exposure", s)


# ------------------------------------------------------------------ 15 信息加工
def fig_ip():
    W, H = 1000, 520
    s = head(W, H, "信息加工模型：内部被写成一条流水线",
             "输入 → 编码 → 存储 → 提取 → 输出；每一段都有容量限制")
    s.append(DEFS)
    boxes = [("输入", "刺激 / 任务", BLU), ("感觉登记", "几百毫秒", GRN), ("短时/工作记忆", "约 4 个组块", ORG),
             ("长时记忆", "编码 / 提取", PNK), ("输出", "反应 / 报告", RED)]
    x = 50
    for i, (name, sub, col) in enumerate(boxes):
        s.append(box(x, 160, 160, 110, "#fbfcfe", col, 10))
        s.append(txt(x + 80, 200, name, 15, col, weight="bold"))
        s.append(txt(x + 80, 228, sub, 11, GRY))
        if i < len(boxes) - 1:
            s.append(arrow(x + 162, 215, x + 188, 215, GRY, 1.8))
        x += 190
    # 注意门
    s.append(arrow(310, 320, 360, 275, ORG, 1.6, "5,4"))
    s.append(txt(310, 345, "注意：选择谁进来", 12, ORG))
    s.append(arrow(500, 320, 500, 275, PNK, 1.6, "5,4"))
    s.append(txt(500, 345, "复述：让它留下来", 12, PNK))
    s.append(txt(500, 440, "这套模型的得：可计算、可检验；失：意义、身体、第一人称。", 13, GRY))
    save("fig-ip", s)


# ------------------------------------------------------------------ 16 阶段 vs 连续
def fig_stages():
    W, H = 1000, 560
    s = head(W, H, "阶段还是连续：两种发展曲线",
             "左：皮亚杰式台阶；右：连续增长 + 若干相变")
    s.append(DEFS)
    # 左
    s.append(txt(260, 100, "阶段论", 16, BLU, weight="bold"))
    s.append(line(90, 420, 430, 420, GRY, 1.4))
    s.append(line(90, 420, 90, 130, GRY, 1.4))
    steps = [(110, 380, 170, 380), (170, 380, 170, 330), (170, 330, 240, 330), (240, 330, 240, 270),
             (240, 270, 320, 270), (320, 270, 320, 190), (320, 190, 400, 190)]
    for x1, y1, x2, y2 in steps:
        s.append(line(x1, y1, x2, y2, BLU, 2.6))
    for lab, x in [("感知运动", 140), ("前运算", 205), ("具体运算", 280), ("形式运算", 360)]:
        s.append(txt(x, 450, lab, 10, GRY))
    # 右
    s.append(txt(740, 100, "动态系统 / 连续", 16, GRN, weight="bold"))
    s.append(line(560, 420, 900, 420, GRY, 1.4))
    s.append(line(560, 420, 560, 130, GRY, 1.4))
    pts = []
    for i in range(0, 341, 5):
        x = 560 + i
        y = 410 - 230 / (1 + math.exp(-(i - 170) / 40.0)) - 10 * math.sin(i / 22.0)
        pts.append((x, y))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    s.append(f'<path d="{d}" fill="none" stroke="{GRN}" stroke-width="2.4"/>')
    for x in [650, 735, 820]:
        s.append(circle(x, 410 - 230 / (1 + math.exp(-(x - 730) / 40.0)) - 10 * math.sin((x - 560) / 22.0), 6, GLD, GLD))
    s.append(txt(735, 450, "相变点（不是固定年龄）", 10, GLD))
    s.append(txt(500, 510, "两者都能解释“质变”；分歧在于质变是“换台阶”，还是“参数空间里的分岔”。", 13, GRY))
    save("fig-stages", s)


# ------------------------------------------------------------------ 17 方法时间线
def fig_methods():
    W, H = 1000, 560
    s = head(W, H, "认知神经科学：方法的升级",
             "从损伤到成像；精度、因果性与伦理各不相同")
    s.append(DEFS)
    s.append(line(80, 300, 920, 300, GRY, 2))
    items = [("1861", "损伤研究", "布洛卡", BLU), ("1924", "EEG", "伯格", GRN), ("1930s", "电刺激", "彭菲尔德", ORG),
             ("1950s", "单细胞记录", "休伯尔/维泽尔", PNK), ("1970s", "PET", "代谢/血流", GLD),
             ("1990", "fMRI", "BOLD", RED), ("1985", "TMS", "暂时扰乱", "#5b7fa8")]
    for i, (yr, name, sub, col) in enumerate(items):
        x = 90 + i * 118
        up = i % 2 == 0
        y = 230 if up else 330
        s.append(line(x, 300, x, y, col, 1.6))
        s.append(circle(x, 300, 6, col, col))
        s.append(txt(x, y - 12 if up else y + 30, yr, 12, col, weight="bold"))
        s.append(txt(x, y - 34 if up else y + 52, name, 12, INK))
        s.append(txt(x, y + 48 if up else y + 72, sub, 10, GRY))
    s.append(txt(500, 500, "方法越强，越要问：它测的是神经活动，还是血流？是相关，还是因果？", 13, GRY))
    save("fig-methods", s)


# ------------------------------------------------------------------ 18 人—情境
def fig_person_situation():
    W, H = 1000, 520
    s = head(W, H, "人—情境交互：强情境压制差异，弱情境允许差异",
             "行为不是“人”或“情境”的单独函数，而是两者的交互")
    s.append(DEFS)
    s.append(line(90, 420, 900, 420, GRY, 1.6))
    s.append(line(90, 420, 90, 120, GRY, 1.6))
    s.append(txt(80, 130, "行为差异", 12, GRY, "end"))
    s.append(txt(900, 448, "情境强度", 12, GRY, "end"))
    s.append(f'<path d="M 110 170 C 300 180 500 300 880 390" fill="none" stroke="{BLU}" stroke-width="2.6"/>')
    s.append(txt(300, 170, "强情境：大家表现差不多", 13, BLU))
    s.append(txt(720, 380, "弱情境：个体差异显现", 13, BLU))
    s.append(f'<rect x="110" y="140" width="240" height="60" fill="{ORG}" opacity="0.12"/>')
    s.append(txt(230, 260, "从众、服从、紧急事件", 11, ORG))
    s.append(txt(700, 300, "日常选择、兴趣、关系", 11, GRN))
    s.append(txt(500, 490, "“情境的力量”与“个体差异”不是对立，是同一个交互的两端。", 13, GRY))
    save("fig-person-situation", s)


# ------------------------------------------------------------------ 19 需求层次
def fig_needs():
    W, H = 1000, 560
    s = head(W, H, "需求层次：不是金字塔，是“优势性”",
             "低层长期匮乏时占优势；满足后，高层才更容易浮现（统计性，非铁律）")
    s.append(DEFS)
    rows = [("自我实现", "成为自己能成为的样子", GLD, 0.35),
            ("尊重", "被看见、被认可、有能力", PNK, 0.48),
            ("归属与爱", "关系、群体、被接纳", GRN, 0.61),
            ("安全", "稳定、可预测、免受威胁", BLU, 0.74),
            ("生理", "食物、睡眠、住所、健康", ORG, 0.87)]
    for i, (name, sub, col, w) in enumerate(rows):
        width = 760 * w
        x = 500 - width / 2
        y = 110 + i * 78
        s.append(box(x, y, width, 60, "#fbfcfe", col))
        s.append(txt(500, y + 26, name, 15, col, weight="bold"))
        s.append(txt(500, y + 47, sub, 11, GRY))
    s.append(txt(500, 530, "注：金字塔图形是后来的管理学教材加的，马斯洛本人没有用过。", 12, GRY))
    save("fig-needs", s)


# ------------------------------------------------------------------ 20 意义的时间
def fig_meaning_time():
    W, H = 1000, 520
    s = head(W, H, "意义的时间结构：过去、现在、未来",
             "抑郁常是未来塌陷；焦虑常是未来过载；创伤常是过去入侵")
    s.append(DEFS)
    s.append(arrow(100, 300, 900, 300, GRY, 2))
    for x, lab, col in [(220, "过去", BLU), (500, "现在", GRN), (780, "未来", GLD)]:
        s.append(circle(x, 300, 10, col, col))
        s.append(txt(x, 340, lab, 18, col, weight="bold"))
    s.append(txt(220, 230, "可讲述的故事", 12, BLU))
    s.append(txt(500, 230, "可投入的行动", 12, GRN))
    s.append(txt(780, 230, "可期待的方向", 12, GLD))
    s.append(txt(220, 400, "创伤：过去入侵", 11, RED))
    s.append(txt(500, 430, "空虚：现在脱节", 11, RED))
    s.append(txt(780, 400, "抑郁/焦虑：未来塌陷/过载", 11, RED))
    s.append(txt(500, 480, "存在主义治疗的工作：不是消除症状，而是重建三个维度（C）。", 13, GRY))
    save("fig-meaning-time", s)


# ------------------------------------------------------------------ 21 毕生发展
def fig_lifespan():
    W, H = 1000, 560
    s = head(W, H, "毕生发展：获得与失去同时发生",
             "不同能力的轨迹不同；没有哪一段是纯粹的“增长”或“衰退”")
    s.append(DEFS)
    s.append(line(90, 420, 900, 420, GRY, 1.6))
    s.append(line(90, 420, 90, 120, GRY, 1.6))
    s.append(txt(80, 130, "能力水平", 12, GRY, "end"))
    s.append(txt(900, 448, "年龄 →", 12, GRY, "end"))
    curves = [("晶体知识", 300, 20, 0.55, BLU), ("加工速度", 300, 40, -0.75, RED),
              ("情绪调节", 280, 30, 0.45, GRN), ("记忆（情景）", 310, 45, -0.35, ORG)]
    for name, y0, amp, slope, col in curves:
        pts = []
        for i in range(0, 340, 4):
            x = 130 + i
            y = y0 - amp * math.tanh((i - 150) / 90.0) * 0.5 - slope * i * 0.35
            pts.append((x, y))
        d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
        s.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2.2"/>')
        s.append(txt(870, pts[-1][1] + 5, name, 11, col, "end"))
    s.append(txt(500, 510, "SOC 模型：选择少数领域、优化资源、补偿损失——在有限中维持功能。", 13, GRY))
    save("fig-lifespan", s)


# ------------------------------------------------------------------ 22 家庭系统
def fig_system():
    W, H = 1000, 600
    s = head(W, H, "被认定的病人：症状在一个人身上，模式在全家人之间",
             "实线＝亲近；虚线＝疏远；锯齿线＝冲突")
    s.append(DEFS)
    # 人物
    s.append(circle(300, 160, 34, "#eaf2fb", BLU))
    s.append(txt(300, 166, "父", 18, INK))
    s.append(circle(700, 160, 34, "#fdecea", RED))
    s.append(txt(700, 166, "母", 18, INK))
    s.append(circle(500, 330, 38, "#fff8e1", GLD))
    s.append(txt(500, 336, "女", 18, INK))
    s.append(txt(500, 390, "被认定的病人", 12, RED, weight="bold"))
    # 关系线
    s.append(line(334, 160, 666, 160, RED, 2.4))
    for k in range(8):
        x = 380 + k * 36
        s.append(line(x, 150, x + 12, 170, RED, 1.6))
    s.append(line(320, 190, 470, 300, BLU, 2.2))
    s.append(line(680, 190, 530, 300, BLU, 2.2))
    s.append(line(300, 160, 480, 310, "#999999", 1.4, "6,5"))
    s.append(txt(600, 130, "夫妻冲突", 12, RED))
    s.append(txt(380, 260, "亲近", 11, BLU))
    s.append(txt(620, 260, "亲近", 11, BLU))
    s.append(txt(370, 330, "疏远", 11, GRY))
    # 循环箭头
    s.append(arrow(430, 420, 300, 420, GRY, 1.6, "5,4"))
    s.append(arrow(300, 420, 430, 420, GRY, 1.6, "5,4"))
    s.append(txt(365, 450, "症状加重 → 父母暂时合作", 10, GRY))
    s.append(txt(500, 530, "系统治疗的提问：如果女儿好了，这个家会失去什么？", 13, GRY))
    save("fig-system", s)


# ------------------------------------------------------------------ 23 阈值
def fig_threshold():
    W, H = 1000, 520
    s = head(W, H, "阈值：连续分布上的两条切线",
             "同一群人，门槛放在 4 项或 6 项，得到不同的“病人”数量")
    s.append(DEFS)
    cx, base = 500, 400
    pts = []
    for i in range(0, 241):
        x = 80 + i * 3.5
        z = (x - cx) / 110.0
        y = base - 250 * math.exp(-0.5 * z * z)
        pts.append((x, y))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    s.append(f'<path d="{d}" fill="none" stroke="{BLU}" stroke-width="2.4"/>')
    s.append(line(80, base, 920, base, GRY, 1.6))
    s.append(txt(80, 430, "症状少", 11, GRY, "start"))
    s.append(txt(920, 430, "症状多", 11, GRY, "end"))
    for x, lab, col in [(cx + 60, "门槛 4 项", ORG), (cx + 150, "门槛 6 项", RED)]:
        s.append(line(x, base, x, base - 240, col, 1.8, "6,4"))
        s.append(txt(x, base - 252, lab, 12, col))
    s.append(f'<path d="M {cx+150} {base} L {cx+150} {base-150} L 920 {base-20} L 920 {base} Z" fill="{RED}" opacity="0.10"/>')
    s.append(txt(500, 480, "门槛是约定；改变门槛，就改变了患病率、资源分配与谁被贴上标签（B）。", 13, GRY))
    save("fig-threshold", s)


# ------------------------------------------------------------------ 24 回望
def fig_master():
    W, H = 1000, 640
    s = head(W, H, "六核回望：一条螺旋，不是一条直线",
             "每一部分让出的东西，被下一部分以新的工具拿回来")
    s.append(DEFS)
    labels = [("看见", BLU), ("记住", GRN), ("跟上", ORG), ("选择", GLD), ("讲述", PNK), ("临界", RED)]
    cx, cy = 500, 330
    for i, (lab, col) in enumerate(labels):
        ang = -math.pi / 2 + i * 2 * math.pi / 6
        r = 190 - i * 8
        x = cx + r * math.cos(ang)
        y = cy + r * math.sin(ang)
        s.append(circle(x, y, 40, "#fbfcfe", col, 2.4))
        s.append(txt(x, y + 7, lab, 17, col, weight="bold"))
        # 螺旋弧
        a0 = ang
        a1 = ang + 2 * math.pi / 6
        r0, r1 = r, r - 8
        x0, y0 = cx + r0 * math.cos(a0), cy + r0 * math.sin(a0)
        x1, y1 = cx + r1 * math.cos(a1), cy + r1 * math.sin(a1)
        s.append(f'<path d="M {x0:.1f} {y0:.1f} A {r0} {r0} 0 0 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{col}" stroke-width="2" opacity="0.6"/>')
    s.append(txt(cx, cy - 10, "让出", 16, GLD, weight="bold"))
    s.append(txt(cx, cy + 18, "回归", 16, GLD, weight="bold"))
    s.append(txt(500, 590, "回归不是回到原点：载体变了，翻译有损，问题被重新问了一遍。", 13, GRY))
    save("fig-master", s)


def main():
    fig_structure()
    fig_lineage()
    fig_three_clocks()
    fig_cat()
    fig_gestalt()
    fig_iceberg()
    fig_depths()
    fig_positions()
    fig_strange()
    fig_registers()
    fig_translation()
    fig_iq()
    fig_sor()
    fig_schedules()
    fig_exposure()
    fig_ip()
    fig_stages()
    fig_methods()
    fig_person_situation()
    fig_needs()
    fig_meaning_time()
    fig_lifespan()
    fig_system()
    fig_threshold()
    fig_master()


if __name__ == "__main__":
    main()
