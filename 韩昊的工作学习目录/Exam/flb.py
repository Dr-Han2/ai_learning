# -*- coding: utf-8 -*-
"""
生成《RLS（递推最小二乘）及工程应用》PPT
依赖: pip install python-pptx
运行: python make_rls_ppt.py
输出: RLS_递推最小二乘及工程应用.pptx
"""

from make_pptx import Presentation
from make_pptx.util import Inches, Pt
from make_pptx.dml.color import RGBColor
from make_pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from make_pptx.enum.shapes import MSO_SHAPE
from make_pptx.oxml.ns import qn

# ============================================================
# 配色 & 字体
# ============================================================
PRIMARY    = RGBColor(0x1F, 0x4E, 0x79)   # 深蓝
PRIMARY_D  = RGBColor(0x15, 0x36, 0x56)   # 更深
ACCENT     = RGBColor(0x2E, 0x86, 0xAB)   # 中蓝
ACCENT2    = RGBColor(0xE8, 0x7A, 0x2B)   # 橙色
TEXT       = RGBColor(0x2B, 0x2B, 0x2B)
TEXT_SUB   = RGBColor(0x5A, 0x5A, 0x5A)
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
BG_SOFT    = RGBColor(0xF2, 0xF6, 0xFA)   # 浅蓝底
BG_SOFT2   = RGBColor(0xFC, 0xF3, 0xE8)   # 浅橙底
CODE_BG    = RGBColor(0x1E, 0x28, 0x32)
CODE_FG    = RGBColor(0xDC, 0xE3, 0xEA)

FONT_CN   = '微软雅黑'
FONT_MATH = 'Cambria Math'
FONT_CODE = 'Consolas'

SW_IN, SH_IN = 13.333, 7.5
SW, SH = Inches(SW_IN), Inches(SH_IN)


# ============================================================
# 基础工具
# ============================================================
def _set_font(run, name):
    """同时设置 latin / ea / cs 字体，保证中英文都生效"""
    run.font.name = name
    rPr = run._r.get_or_add_rPr()

    # 先移除已有的 a:ea / a:cs
    for tag in ('a:ea', 'a:cs'):
        for el in rPr.findall(qn(tag)):
            rPr.remove(el)

    # 找到 a:latin（由 run.font.name 自动写入）
    latin = rPr.find(qn('a:latin'))
    if latin is None:
        return

    idx = list(rPr).index(latin) + 1
    for tag in ('a:ea', 'a:cs'):
        el = rPr.makeelement(qn(tag), {'typeface': name})
        rPr.insert(idx, el)
        idx += 1


def blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def add_rect(slide, l, t, w, h, color, shape=MSO_SHAPE.RECTANGLE, line=None):
    s = slide.shapes.add_shape(shape, Inches(l), Inches(t), Inches(w), Inches(h))
    s.fill.solid()
    s.fill.fore_color.rgb = color
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
    try:
        s.shadow.inherit = False
    except Exception:
        pass
    return s


def add_footer(slide, page_no):
    """页脚：左侧标签 + 右侧页码"""
    tb = slide.shapes.add_textbox(Inches(0.78), Inches(7.02), Inches(6.0), Inches(0.35))
    tf = tb.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = 'RLS 递推最小二乘及工程应用'
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(0x9A, 0xA6, 0xB2)
    _set_font(r, FONT_CN)

    tb2 = slide.shapes.add_textbox(Inches(12.0), Inches(7.02), Inches(0.6), Inches(0.35))
    tf2 = tb2.text_frame
    p2 = tf2.paragraphs[0]
    p2.alignment = PP_ALIGN.RIGHT
    r2 = p2.add_run()
    r2.text = str(page_no)
    r2.font.size = Pt(10)
    r2.font.color.rgb = RGBColor(0x9A, 0xA6, 0xB2)
    _set_font(r2, 'Arial')


def add_header(slide, title):
    """标准内容页页眉"""
    add_rect(slide, 0, 0, SW_IN, 1.02, PRIMARY)
    add_rect(slide, 0, 1.02, SW_IN, 0.055, ACCENT2)
    tb = slide.shapes.add_textbox(Inches(0.6), Inches(0.08), Inches(12.1), Inches(0.86))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = title
    r.font.size = Pt(25)
    r.font.bold = True
    r.font.color.rgb = WHITE
    _set_font(r, FONT_CN)


def add_body(slide, items, left=0.78, top=1.42, width=11.8, height=5.7):
    """
    items: list of dict
      {'t': 文本, 'size':18, 'bold':False, 'color':TEXT, 'font':FONT_CN,
       'level':0, 'after':6, 'before':0, 'align':PP_ALIGN.LEFT, 'ls':1.15,
       'runs': [...]  # 可选，混排
      }
    """
    tb = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    first = True
    for it in items:
        if isinstance(it, str):
            it = {'t': it}
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.level = min(it.get('level', 0), 4)
        p.space_after = Pt(it.get('after', 6))
        p.space_before = Pt(it.get('before', 0))
        p.alignment = it.get('align', PP_ALIGN.LEFT)
        p.line_spacing = it.get('ls', 1.18)

        if 'runs' in it:
            for rk in it['runs']:
                r = p.add_run()
                r.text = rk.get('t', '')
                r.font.size = Pt(rk.get('size', it.get('size', 18)))
                r.font.bold = rk.get('bold', False)
                r.font.italic = rk.get('italic', False)
                r.font.color.rgb = rk.get('color', it.get('color', TEXT))
                _set_font(r, rk.get('font', it.get('font', FONT_CN)))
        else:
            r = p.add_run()
            r.text = it.get('t', '')
            r.font.size = Pt(it.get('size', 18))
            r.font.bold = it.get('bold', False)
            r.font.italic = it.get('italic', False)
            r.font.color.rgb = it.get('color', TEXT)
            _set_font(r, it.get('font', FONT_CN))
    return tb


def add_formula(slide, lines, left=0.78, top=1.45, width=11.8, size=19,
                bg=BG_SOFT, color=TEXT):
    """公式卡片，返回底部 y 坐标（英寸）"""
    line_h = size * 1.75 / 72.0
    h = 0.28 + line_h * len(lines)
    box = add_rect(slide, left, top, width, h, bg, MSO_SHAPE.ROUNDED_RECTANGLE)
    try:
        box.adjustments[0] = 0.06
    except Exception:
        pass
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = Inches(0.22)
    tf.margin_right = Inches(0.22)
    tf.margin_top = Inches(0.08)
    tf.margin_bottom = Inches(0.08)
    first = True
    for ln in lines:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = PP_ALIGN.CENTER
        p.space_after = Pt(2)
        p.line_spacing = 1.05
        r = p.add_run()
        r.text = ln
        r.font.size = Pt(size)
        r.font.color.rgb = color
        _set_font(r, FONT_MATH)
    return top + h + 0.12


def add_code(slide, lines, left=0.78, top=1.45, width=11.8, height=None,
             size=12.5, bg=CODE_BG, fg=CODE_FG):
    """深色代码块，返回底部 y 坐标（已修复左对齐）"""
    if height is None:
        height = 0.245 * len(lines) + 0.35
    box = add_rect(slide, left, top, width, height, bg, MSO_SHAPE.ROUNDED_RECTANGLE)
    try:
        box.adjustments[0] = 0.035
    except Exception:
        pass
    tf = box.text_frame
    tf.word_wrap = False
    tf.vertical_anchor = MSO_ANCHOR.TOP
    tf.margin_left = Inches(0.22)
    tf.margin_right = Inches(0.15)
    tf.margin_top = Inches(0.13)
    tf.margin_bottom = Inches(0.13)
    first = True
    for ln in lines:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = PP_ALIGN.LEFT          # <--- 关键修复：强制左对齐
        p.space_after = Pt(0)
        p.line_spacing = 1.0
        r = p.add_run()
        r.text = ln if ln else ' '
        r.font.size = Pt(size)
        r.font.color.rgb = fg
        _set_font(r, FONT_CODE)
    return top + height + 0.12


def add_table(slide, data, left=0.78, top=1.6, width=11.8, height=None,
              font_size=15, header_bg=PRIMARY, header_fg=WHITE,
              alt_bg=BG_SOFT, base_bg=WHITE, first_col_bold=True):
    rows, cols = len(data), len(data[0])
    if height is None:
        height = 0.42 * rows
    gt = slide.shapes.add_table(rows, cols, Inches(left), Inches(top),
                                Inches(width), Inches(height))
    tbl = gt.table
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            cell = tbl.cell(i, j)
            cell.margin_left = Inches(0.1)
            cell.margin_right = Inches(0.1)
            cell.margin_top = Inches(0.02)
            cell.margin_bottom = Inches(0.02)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf = cell.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            r = p.add_run()
            r.text = str(val)
            r.font.size = Pt(font_size)
            if i == 0:
                r.font.bold = True
                r.font.color.rgb = header_fg
                cell.fill.solid()
                cell.fill.fore_color.rgb = header_bg
            else:
                r.font.color.rgb = TEXT
                cell.fill.solid()
                cell.fill.fore_color.rgb = alt_bg if i % 2 == 0 else base_bg
                if first_col_bold and j == 0:
                    r.font.bold = True
            _set_font(r, FONT_CN)
    return gt


# ============================================================
# 页面模板
# ============================================================
def page_title(prs):
    slide = blank(prs)
    add_rect(slide, 0, 0, SW_IN, SH_IN, PRIMARY)
    add_rect(slide, 0, 0, SW_IN, 0.28, ACCENT2)
    add_rect(slide, 0, SH_IN - 0.16, SW_IN, 0.16, ACCENT)

    tb = slide.shapes.add_textbox(Inches(1.0), Inches(2.15), Inches(11.3), Inches(1.5))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = 'RLS 递推最小二乘及工程应用'
    r.font.size = Pt(46)
    r.font.bold = True
    r.font.color.rgb = WHITE
    _set_font(r, FONT_CN)

    tb2 = slide.shapes.add_textbox(Inches(1.05), Inches(3.65), Inches(11.3), Inches(0.9))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    r2 = p2.add_run()
    r2.text = '从自适应滤波到大模型增量微调'
    r2.font.size = Pt(22)
    r2.font.color.rgb = RGBColor(0xBF, 0xD6, 0xE8)
    _set_font(r2, FONT_CN)

    add_rect(slide, 1.05, 4.55, 2.2, 0.05, ACCENT2)

    # 封面底部：讲解人
    tb3 = slide.shapes.add_textbox(Inches(1.05), Inches(4.85), Inches(11.3), Inches(0.8))
    tf3 = tb3.text_frame
    p3 = tf3.paragraphs[0]
    r3 = p3.add_run()
    r3.text = '讲解人: 韩佳欣'
    r3.font.size = Pt(18)
    r3.font.color.rgb = RGBColor(0xBF, 0xD6, 0xE8)
    _set_font(r3, FONT_CN)

    return slide


def page_section(prs, num, title, sub=''):
    slide = blank(prs)
    add_rect(slide, 0, 0, SW_IN, SH_IN, PRIMARY)
    add_rect(slide, 0, 0, 0.22, SH_IN, ACCENT2)

    tb = slide.shapes.add_textbox(Inches(1.15), Inches(2.55), Inches(2.15), Inches(1.9))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT
    r = p.add_run()
    r.text = num
    r.font.size = Pt(92)
    r.font.bold = True
    r.font.color.rgb = ACCENT2
    _set_font(r, 'Arial')

    add_rect(slide, 3.55, 2.72, 0.055, 1.75, WHITE)

    tb2 = slide.shapes.add_textbox(Inches(3.95), Inches(2.72), Inches(8.6), Inches(1.05))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    r2 = p2.add_run()
    r2.text = title
    r2.font.size = Pt(38)
    r2.font.bold = True
    r2.font.color.rgb = WHITE
    _set_font(r2, FONT_CN)

    if sub:
        tb3 = slide.shapes.add_textbox(Inches(4.0), Inches(3.82), Inches(8.6), Inches(0.9))
        tf3 = tb3.text_frame
        tf3.word_wrap = True
        p3 = tf3.paragraphs[0]
        r3 = p3.add_run()
        r3.text = sub
        r3.font.size = Pt(17)
        r3.font.color.rgb = RGBColor(0xBF, 0xD6, 0xE8)
        _set_font(r3, FONT_CN)
    return slide


def page_end(prs):
    slide = blank(prs)
    add_rect(slide, 0, 0, SW_IN, SH_IN, PRIMARY)
    add_rect(slide, 0, 0, SW_IN, 0.28, ACCENT2)

    tb = slide.shapes.add_textbox(Inches(1.0), Inches(2.6), Inches(11.3), Inches(1.3))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = '谢  谢'
    r.font.size = Pt(56)
    r.font.bold = True
    r.font.color.rgb = WHITE
    _set_font(r, FONT_CN)

    tb2 = slide.shapes.add_textbox(Inches(1.0), Inches(4.0), Inches(11.3), Inches(1.2))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    for i, txt in enumerate(['RLS：递推最小二乘',
                             '从自适应滤波到大模型增量微调',
                             '免回放、零遗忘的路由选择方案']):
        p2 = tf2.paragraphs[0] if i == 0 else tf2.add_paragraph()
        p2.alignment = PP_ALIGN.CENTER
        p2.space_after = Pt(4)
        r2 = p2.add_run()
        r2.text = txt
        r2.font.size = Pt(17)
        r2.font.color.rgb = RGBColor(0xBF, 0xD6, 0xE8)
        _set_font(r2, FONT_CN)
    return slide


# ============================================================
# 内容构造
# ============================================================
def build(prs, page_counter):
    """page_counter 是一个可变的列表，用于累计页码"""

    def next_page(slide):
        page_counter[0] += 1
        add_footer(slide, page_counter[0])

    # ---------- 1 封面 ----------
    page_title(prs)

    # ---------- 2 目录 ----------
    s = blank(prs)
    add_header(s, '目录  Contents')
    toc = [
        ('01', 'RLS 解决什么问题'),
        ('02', '数学推导：从最小二乘到递推'),
        ('03', '算法流程、初始化与一维算例'),
        ('04', '注意事项：激励、遗忘因子、数值稳定性'),
        ('05', '工程应用：滤波 / 通信 / 辨识 / 控制'),
        ('06', '大模型增量微调中的 RLS 路由'),
        ('07', 'Python 代码示例'),
        ('08', '总结与核心公式速查'),
        ('09', '附录：矩阵求逆引理证明'),
    ]
    items = []
    for num, t in toc:
        items.append({
            'runs': [
                {'t': num + '   ', 'size': 19, 'bold': True, 'color': ACCENT2, 'font': 'Arial'},
                {'t': t, 'size': 19, 'color': TEXT, 'font': FONT_CN},
            ],
            'after': 11, 'ls': 1.0,
        })
    add_body(s, items, top=1.5, height=5.6)
    next_page(s)

    # ---------- 3 章节 1 ----------
    page_section(prs, '01', 'RLS 解决什么问题',
                 'Recursive Least Squares  ·  递推最小二乘法')

    # ---------- 4 RLS 的目标 ----------
    s = blank(prs)
    add_header(s, '1.1  RLS 的目标')
    add_body(s, [
        {'runs': [
            {'t': '在每个时刻 ', 'size': 19, 'color': TEXT},
            {'t': 'n', 'size': 19, 'italic': True, 'color': ACCENT, 'font': FONT_MATH},
            {'t': '，寻找滤波器系数 ', 'size': 19, 'color': TEXT},
            {'t': 'w(n)', 'size': 19, 'italic': True, 'color': ACCENT, 'font': FONT_MATH},
            {'t': '，使从初始时刻到当前时刻的', 'size': 19, 'color': TEXT},
            {'t': '加权误差平方和最小', 'size': 19, 'bold': True, 'color': ACCENT2},
            {'t': '。', 'size': 19, 'color': TEXT},
        ], 'after': 14},
    ], height=0.8)

    y = add_formula(s, [
        'e(n) = d(n) − y(n)',
        'y(n) = xᵀ(n)·w(n)',
        'e(n) = d(n) − xᵀ(n)·w(n)',
    ], top=2.30, size=21)

    add_body(s, [
        {'runs': [
            {'t': 'd(n)', 'size': 18, 'italic': True, 'color': ACCENT, 'font': FONT_MATH},
            {'t': '  期望信号（目标输出）', 'size': 18, 'color': TEXT},
        ], 'after': 7},
        {'runs': [
            {'t': 'x(n)', 'size': 18, 'italic': True, 'color': ACCENT, 'font': FONT_MATH},
            {'t': '  输入向量 / 回归向量', 'size': 18, 'color': TEXT},
        ], 'after': 7},
        {'runs': [
            {'t': 'w(n)', 'size': 18, 'italic': True, 'color': ACCENT, 'font': FONT_MATH},
            {'t': '  滤波器系数（待估参数）', 'size': 18, 'color': TEXT},
        ], 'after': 7},
        {'runs': [
            {'t': 'y(n)', 'size': 18, 'italic': True, 'color': ACCENT, 'font': FONT_MATH},
            {'t': '  滤波器输出', 'size': 18, 'color': TEXT},
        ], 'after': 7},
    ], top=y + 0.02, height=2.6)
    next_page(s)

    # ---------- 5 目标函数与遗忘因子 ----------
    s = blank(prs)
    add_header(s, '1.2  目标函数与遗忘因子 λ')
    y = add_formula(s, [
        'J(n) = Σᵢ₌₁ⁿ λⁿ⁻ⁱ · [ d(i) − xᵀ(i)·w(n) ]²',
    ], top=1.42, size=22)

    add_body(s, [
        {'t': '遗忘因子 λ', 'size': 19, 'bold': True, 'color': PRIMARY, 'after': 8},
        {'t': '•  0 < λ ≤ 1，对过去数据指数加权，越旧权重越小', 'size': 17, 'level': 0, 'after': 6},
        {'t': '•  λ = 1：所有历史数据等权，适合平稳系统', 'size': 17, 'level': 0, 'after': 6},
        {'t': '•  0 < λ < 1：指数遗忘旧数据，适合非平稳 / 时变系统', 'size': 17, 'level': 0, 'after': 6},
        {'t': '•  常用范围：0.95 ~ 0.999', 'size': 17, 'level': 0, 'after': 6},
    ], top=y + 0.05, height=2.3)

    add_formula(s, [
        'N_eff ≈ 1 / (1 − λ)        例：λ = 0.99 → 有效记忆 ≈ 100 个样本',
    ], top=y + 2.45, size=18, bg=BG_SOFT2)
    next_page(s)

    # ---------- 6 章节 2 ----------
    page_section(prs, '02', '数学推导',
                 '从加权最小二乘到递推更新  ·  矩阵求逆引理')

    # ---------- 7 加权最小二乘与正规方程 ----------
    s = blank(prs)
    add_header(s, '2.1  加权最小二乘与正规方程')
    add_body(s, [
        {'t': '对 J(n) 关于 w(n) 求导并令其为零：', 'size': 18, 'after': 8},
    ], top=1.35, height=0.6)
    y = add_formula(s, [
        '∂J(n)/∂w(n) = −2 Σᵢ₌₁ⁿ λⁿ⁻ⁱ x(i) [ d(i) − xᵀ(i) w(n) ] = 0',
    ], top=1.85, size=18)
    add_body(s, [
        {'t': '整理得到正规方程：', 'size': 18, 'after': 8},
    ], top=y + 0.02, height=0.5)
    add_formula(s, [
        '( Σᵢ₌₁ⁿ λⁿ⁻ⁱ x(i) xᵀ(i) ) · w(n)  =  Σᵢ₌₁ⁿ λⁿ⁻ⁱ x(i) d(i)',
    ], top=y + 0.52, size=19)
    next_page(s)

    # ---------- 8 定义 R / p / P ----------
    s = blank(prs)
    add_header(s, '2.2  定义 R(n)、p(n)、P(n)')
    y = add_formula(s, [
        'R(n) = Σᵢ₌₁ⁿ λⁿ⁻ⁱ x(i) xᵀ(i)        （加权自相关矩阵）',
        'p(n) = Σᵢ₌₁ⁿ λⁿ⁻ⁱ x(i) d(i)          （加权互相关向量）',
    ], top=1.4, size=19)

    add_body(s, [
        {'t': '正规方程：', 'size': 18, 'after': 6},
    ], top=y + 0.02, height=0.45)
    y2 = add_formula(s, [
        'R(n)·w(n) = p(n)    ⟹    w(n) = R⁻¹(n)·p(n)',
    ], top=y + 0.5, size=20)
    add_body(s, [
        {'t': '定义  P(n) = R⁻¹(n)：', 'size': 18, 'bold': True, 'color': PRIMARY, 'after': 6},
        {'t': '•  P(n) 可理解为参数估计的协方差矩阵', 'size': 17, 'after': 4},
        {'t': '•  表示当前参数的不确定性大小', 'size': 17, 'after': 4},
        {'t': '•  P(n) 越大 → 不确定性越大 → 增益越大 → 修正越猛', 'size': 17, 'after': 4},
    ], top=y2 + 0.05, height=2.4)
    next_page(s)

    # ---------- 9 递推关系 ----------
    s = blank(prs)
    add_header(s, '2.3  递推关系')
    add_body(s, [
        {'t': '加入新数据 x(n), d(n) 后：', 'size': 18, 'after': 8},
    ], top=1.35, height=0.5)
    y = add_formula(s, [
        'R(n) = λ·R(n−1) + x(n)·xᵀ(n)',
        'p(n) = λ·p(n−1) + x(n)·d(n)',
    ], top=1.85, size=21)

    add_body(s, [
        {'runs': [
            {'t': '问题：', 'size': 18, 'bold': True, 'color': ACCENT2},
            {'t': '直接对 R(n) 求逆，每次都是 O(N³)，计算量太大。', 'size': 18, 'color': TEXT},
        ], 'after': 10},
        {'runs': [
            {'t': '解决：', 'size': 18, 'bold': True, 'color': ACCENT2},
            {'t': '用矩阵求逆引理，从 P(n−1) 直接递推 P(n)，降到 O(N²)。', 'size': 18, 'color': TEXT},
        ], 'after': 10},
    ], top=y + 0.05, height=2.0)
    next_page(s)

    # ---------- 10 矩阵求逆引理 ----------
    s = blank(prs)
    add_header(s, '2.4  矩阵求逆引理 (A + BCD)⁻¹')
    y = add_formula(s, [
        '(A + BCD)⁻¹  =  A⁻¹ − A⁻¹B (C⁻¹ + DA⁻¹B)⁻¹ DA⁻¹',
    ], top=1.42, size=20)

    add_body(s, [
        {'t': '在 RLS 中取：', 'size': 18, 'bold': True, 'color': PRIMARY, 'after': 8},
    ], top=y + 0.05, height=0.5)
    y2 = add_formula(s, [
        'A = λ·R(n−1)      B = x(n)      C = 1      D = xᵀ(n)',
        'A⁻¹ = (1/λ)·P(n−1)',
    ], top=y + 0.55, size=19)

    add_body(s, [
        {'t': '代入引理并整理，即可得到 RLS 的协方差矩阵递推公式。', 'size': 18, 'color': TEXT_SUB, 'after': 6},
    ], top=y2 + 0.05, height=0.7)
    next_page(s)

    # ---------- 11 协方差矩阵递推 ----------
    s = blank(prs)
    add_header(s, '2.5  协方差矩阵递推')
    y = add_formula(s, [
        'P(n) = (1/λ) [ P(n−1) − P(n−1)x(n)xᵀ(n)P(n−1) / (λ + xᵀ(n)P(n−1)x(n)) ]',
    ], top=1.42, size=17)

    add_body(s, [
        {'t': '定义增益向量：', 'size': 18, 'bold': True, 'color': PRIMARY, 'after': 6},
    ], top=y + 0.05, height=0.45)
    y2 = add_formula(s, [
        'k(n) = P(n−1)x(n) / ( λ + xᵀ(n)P(n−1)x(n) )',
    ], top=y + 0.5, size=20, bg=BG_SOFT2)
    add_body(s, [
        {'t': '则协方差更新可简写为：', 'size': 18, 'after': 6},
    ], top=y2 + 0.02, height=0.45)
    add_formula(s, [
        'P(n) = (1/λ) [ P(n−1) − k(n)·xᵀ(n)·P(n−1) ]',
    ], top=y2 + 0.5, size=20)
    next_page(s)

    # ---------- 12 参数更新 ----------
    s = blank(prs)
    add_header(s, '2.6  参数更新与新息')
    add_body(s, [
        {'t': '先计算先验误差（也称新息，innovation）：', 'size': 18, 'after': 8},
    ], top=1.35, height=0.5)
    y = add_formula(s, [
        'α(n) = d(n) − xᵀ(n)·w(n−1)',
    ], top=1.85, size=22)

    add_body(s, [
        {'t': '然后更新滤波器系数：', 'size': 18, 'after': 8},
    ], top=y + 0.02, height=0.5)
    y2 = add_formula(s, [
        'w(n) = w(n−1) + k(n)·α(n)',
    ], top=y + 0.52, size=22, bg=BG_SOFT2)

    add_body(s, [
        {'t': '核心直觉', 'size': 19, 'bold': True, 'color': PRIMARY, 'after': 8},
        {'t': '•  新息 α(n)：当前模型对本次样本的预测误差', 'size': 17, 'after': 5},
        {'t': '•  增益 k(n)：由参数不确定性决定修正幅度', 'size': 17, 'after': 5},
        {'t': '•  协方差 P(n)：在线更新参数不确定性，随数据增多而下降', 'size': 17, 'after': 5},
    ], top=y2 + 0.05, height=2.4)
    next_page(s)

    # ---------- 13 算法流程 ----------
    s = blank(prs)
    add_header(s, '2.7  算法流程')
    add_body(s, [
        {'t': '对每个时刻 n = 1, 2, … 依次执行：', 'size': 18, 'bold': True, 'color': PRIMARY, 'after': 10},
    ], top=1.32, height=0.5)

    y = add_formula(s, [
        '①  α(n) = d(n) − xᵀ(n)·w(n−1)                        （先验误差）',
        '②  k(n) = P(n−1)x(n) / ( λ + xᵀ(n)P(n−1)x(n) )       （增益向量）',
        '③  w(n) = w(n−1) + k(n)·α(n)                         （参数更新）',
        '④  P(n) = (1/λ)[ P(n−1) − k(n)xᵀ(n)P(n−1) ]          （协方差更新）',
    ], top=1.85, size=16)

    add_formula(s, [
        '⑤  工程中强制对称：P(n) ← [ P(n) + Pᵀ(n) ] / 2',
    ], top=y + 0.02, size=17, bg=BG_SOFT2)
    next_page(s)

    # ---------- 14 初始化 ----------
    s = blank(prs)
    add_header(s, '2.8  初始化')
    y = add_formula(s, [
        'w(0) = 0            P(0) = δ·I',
    ], top=1.45, size=23)

    add_body(s, [
        {'t': 'δ 常取 10² ~ 10⁶', 'size': 18, 'bold': True, 'color': ACCENT2, 'after': 12},
        {'runs': [
            {'t': 'δ 大：', 'size': 18, 'bold': True, 'color': PRIMARY},
            {'t': '初始不确定性大，初始增益大，收敛快，但可能震荡', 'size': 18, 'color': TEXT},
        ], 'after': 10},
        {'runs': [
            {'t': 'δ 小：', 'size': 18, 'bold': True, 'color': PRIMARY},
            {'t': '初始更新慢，收敛平稳，但前期跟踪能力弱', 'size': 18, 'color': TEXT},
        ], 'after': 10},
        {'runs': [
            {'t': '工程提示：', 'size': 18, 'bold': True, 'color': ACCENT2},
            {'t': '若已知参数大致范围，可用 w(0) 给出更好的起点。', 'size': 18, 'color': TEXT},
        ], 'after': 10},
    ], top=y + 0.05, height=3.2)
    next_page(s)

    # ---------- 15 章节 3 ----------
    page_section(prs, '03', '算法流程与一维算例',
                 '用最简单的一维参数估计理解 RLS 的每一步')

    # ---------- 16 算例设定 ----------
    s = blank(prs)
    add_header(s, '3.1  一维算例设定')
    add_body(s, [
        {'t': '设定：λ = 0.9，w(0) = 0，P(0) = 1，真实参数 w = 2', 'size': 18, 'bold': True,
         'color': PRIMARY, 'after': 10},
    ], top=1.28, height=0.5)

    add_table(s, [
        ['n', 'x(n)', 'd(n)'],
        ['1', '1', '2'],
        ['2', '2', '4'],
        ['3', '3', '6'],
    ], left=0.78, top=1.82, width=5.4, font_size=16)

    add_formula(s, [
        'α(n) = d(n) − x(n)·w(n−1)',
        'k(n) = P(n−1)x(n) / ( λ + x²(n)P(n−1) )',
        'w(n) = w(n−1) + k(n)·α(n)',
        'P(n) = (1/λ)[ P(n−1) − k(n)x(n)P(n−1) ]',
    ], left=6.55, top=1.82, width=6.03, size=15)
    next_page(s)

    # ---------- 17 n=1 ----------
    s = blank(prs)
    add_header(s, '3.2  一维算例：n = 1')
    add_formula(s, [
        'α(1) = 2 − 1 × 0 = 2',
        'k(1) = (1 × 1) / (0.9 + 1² × 1) = 1 / 1.9 ≈ 0.5263',
        'w(1) = 0 + 0.5263 × 2 ≈ 1.0526',
        'P(1) = (1/0.9)[ 1 − 0.5263 × 1 × 1 ] ≈ 0.5263',
    ], top=1.55, size=21)
    next_page(s)

    # ---------- 18 n=2 ----------
    s = blank(prs)
    add_header(s, '3.3  一维算例：n = 2')
    add_formula(s, [
        'α(2) = 4 − 2 × 1.0526 ≈ 1.8948',
        'k(2) = (0.5263 × 2) / (0.9 + 2² × 0.5263) ≈ 0.3503',
        'w(2) = 1.0526 + 0.3503 × 1.8948 ≈ 1.7163',
        'P(2) = (1/0.9)[ 0.5263 − 0.3503 × 2 × 0.5263 ] ≈ 0.1751',
    ], top=1.55, size=21)
    next_page(s)

    # ---------- 19 n=3 ----------
    s = blank(prs)
    add_header(s, '3.4  一维算例：n = 3')
    add_formula(s, [
        'α(3) = 6 − 3 × 1.7163 ≈ 0.8511',
        'k(3) = (0.1751 × 3) / (0.9 + 3² × 0.1751) ≈ 0.2122',
        'w(3) = 1.7163 + 0.2122 × 0.8511 ≈ 1.8969',
        'P(3) = (1/0.9)[ 0.1751 − 0.2122 × 3 × 0.1751 ] ≈ 0.0707',
    ], top=1.55, size=21)
    next_page(s)

    # ---------- 20 结果对比 ----------
    s = blank(prs)
    add_header(s, '3.5  结果对比')
    add_table(s, [
        ['n', '估计值 w(n)', '真实值', '误差 |w(n) − 2|'],
        ['0', '0', '2', '2.0000'],
        ['1', '1.0526', '2', '0.9474'],
        ['2', '1.7163', '2', '0.2837'],
        ['3', '1.8969', '2', '0.1031'],
    ], top=1.65, width=11.0, font_size=16)

    add_body(s, [
        {'t': '结论', 'size': 19, 'bold': True, 'color': PRIMARY, 'after': 8},
        {'t': '•  估计值逐渐逼近真实值 2', 'size': 17, 'after': 5},
        {'t': '•  协方差 P(n) 从 1 → 0.0707 逐渐减小', 'size': 17, 'after': 5},
        {'t': '•  参数不确定性随数据积累而下降，修正幅度随之变小', 'size': 17, 'after': 5},
    ], top=4.35, height=2.6)
    next_page(s)

    # ---------- 21 章节 4 ----------
    page_section(prs, '04', '注意事项',
                 '持续激励 · 遗忘因子 · 初值 · 数值稳定性 · 复杂度')

    # ---------- 22 持续激励与遗忘因子 ----------
    s = blank(prs)
    add_header(s, '4.1  持续激励与遗忘因子')

    add_body(s, [
        {'t': '持续激励条件（Persistent Excitation）', 'size': 19, 'bold': True,
         'color': PRIMARY, 'after': 8},
        {'t': '•  输入向量 x(n) 必须满足持续激励', 'size': 17, 'after': 5},
        {'t': '•  否则 R(n) 可能奇异，参数不可辨识', 'size': 17, 'after': 5},
        {'t': '•  估计值可能发散，P(n) 失去正定性', 'size': 17, 'after': 5},
    ], top=1.32, height=2.1)

    add_body(s, [
        {'t': '遗忘因子 λ 的选择', 'size': 19, 'bold': True, 'color': PRIMARY, 'after': 8},
        {'runs': [
            {'t': 'λ = 1：', 'size': 17, 'bold': True, 'color': ACCENT},
            {'t': '适合平稳系统，跟踪时变参数能力弱', 'size': 17, 'color': TEXT},
        ], 'after': 5},
        {'runs': [
            {'t': '0 < λ < 1：', 'size': 17, 'bold': True, 'color': ACCENT},
            {'t': '指数遗忘旧数据，适合非平稳 / 时变系统', 'size': 17, 'color': TEXT},
        ], 'after': 5},
        {'runs': [
            {'t': 'λ 越小：', 'size': 17, 'bold': True, 'color': ACCENT},
            {'t': '跟踪越快，但噪声敏感、参数抖动大', 'size': 17, 'color': TEXT},
        ], 'after': 5},
        {'runs': [
            {'t': 'λ 越大：', 'size': 17, 'bold': True, 'color': ACCENT},
            {'t': '平滑越好，但跟踪越慢', 'size': 17, 'color': TEXT},
        ], 'after': 5},
        {'t': '常用范围：0.95 ~ 0.999', 'size': 17, 'bold': True, 'color': ACCENT2, 'after': 5},
    ], top=3.55, height=3.5)
    next_page(s)

    # ---------- 23 初值与数值稳定性 ----------
    s = blank(prs)
    add_header(s, '4.2  初值与数值稳定性')

    add_body(s, [
        {'t': '初值选择', 'size': 19, 'bold': True, 'color': PRIMARY, 'after': 8},
        {'t': '•  w(0) 和 P(0) 影响收敛速度', 'size': 17, 'after': 5},
        {'t': '•  P(0) = δI，δ 过大 → 初始震荡；δ 过小 → 初始收敛慢', 'size': 17, 'after': 5},
    ], top=1.32, height=1.7)

    add_body(s, [
        {'t': '数值稳定性问题', 'size': 19, 'bold': True, 'color': PRIMARY, 'after': 8},
        {'t': '•  P(n) 失去对称性', 'size': 17, 'after': 5},
        {'t': '•  P(n) 失去正定性', 'size': 17, 'after': 5},
        {'t': '•  数值误差累积导致发散', 'size': 17, 'after': 5},
    ], top=3.15, height=1.9)

    add_body(s, [
        {'t': '工程处理手段', 'size': 19, 'bold': True, 'color': ACCENT2, 'after': 8},
        {'t': '•  强制对称：P ← (P + Pᵀ)/2', 'size': 17, 'after': 5},
        {'t': '•  正则化 / 加 jitter（对角线加载）：P ← P + δI', 'size': 17, 'after': 5},
        {'t': '•  UD 分解 RLS：P = UDUᵀ，只更新 U、D，结构上保证正定', 'size': 17, 'after': 5},
        {'t': '•  QR-RLS、平方根 RLS', 'size': 17, 'after': 5},
        {'t': '•  不要随意 inv，用 solve / lstsq / Cholesky', 'size': 17, 'after': 5},
    ], top=5.15, height=2.2)
    next_page(s)

    # ---------- 24 复杂度与关系 ----------
    s = blank(prs)
    add_header(s, '4.3  计算复杂度与算法关系')

    add_body(s, [
        {'t': '计算复杂度（滤波器长度 N）', 'size': 19, 'bold': True, 'color': PRIMARY, 'after': 8},
        {'t': '•  每次更新计算复杂度：O(N²)', 'size': 18, 'after': 6},
        {'t': '•  存储复杂度：O(N²)', 'size': 18, 'after': 6},
    ], top=1.32, height=1.6)

    add_body(s, [
        {'t': '与 LMS 相比', 'size': 19, 'bold': True, 'color': PRIMARY, 'after': 8},
        {'t': '•  RLS 收敛更快、精度更高', 'size': 17, 'after': 5},
        {'t': '•  RLS 计算量更大（LMS 为 O(N)）', 'size': 17, 'after': 5},
    ], top=3.05, height=1.5)

    add_body(s, [
        {'t': '与 Kalman 滤波相比', 'size': 19, 'bold': True, 'color': PRIMARY, 'after': 8},
        {'t': '•  RLS 可看作参数为常数时的 Kalman 滤波特例', 'size': 17, 'after': 5},
        {'t': '•  遗忘因子 λ 可理解为引入过程噪声', 'size': 17, 'after': 5},
        {'t': '•  使算法具备跟踪时变参数的能力', 'size': 17, 'after': 5},
    ], top=4.65, height=2.1)
    next_page(s)

    # ---------- 25 章节 5 ----------
    page_section(prs, '05', '工程应用',
                 '自适应滤波 · 通信 · 系统辨识 · 自适应控制 · 信号处理')

    # ---------- 26 应用领域 ----------
    s = blank(prs)
    add_header(s, '5.1  典型应用领域')

    left_items = [
        {'t': '① 自适应滤波', 'size': 19, 'bold': True, 'color': ACCENT, 'after': 6},
        {'t': '•  回声消除', 'size': 16, 'after': 4},
        {'t': '•  自适应噪声抵消', 'size': 16, 'after': 4},
        {'t': '•  线性预测', 'size': 16, 'after': 14},
        {'t': '② 通信系统', 'size': 19, 'bold': True, 'color': ACCENT, 'after': 6},
        {'t': '•  信道估计', 'size': 16, 'after': 4},
        {'t': '•  信道均衡', 'size': 16, 'after': 4},
        {'t': '•  接收机自适应处理', 'size': 16, 'after': 14},
        {'t': '③ 系统辨识', 'size': 19, 'bold': True, 'color': ACCENT, 'after': 6},
        {'t': '•  ARX / ARMAX 模型在线辨识', 'size': 16, 'after': 4},
        {'t': '•  机械、化工、电力系统参数监测', 'size': 16, 'after': 4},
    ]
    right_items = [
        {'t': '④ 自适应控制', 'size': 19, 'bold': True, 'color': ACCENT, 'after': 6},
        {'t': '•  自校正调节器', 'size': 16, 'after': 4},
        {'t': '•  模型参考自适应控制中的参数估计', 'size': 16, 'after': 14},
        {'t': '⑤ 信号处理', 'size': 19, 'bold': True, 'color': ACCENT, 'after': 6},
        {'t': '•  时变 AR 模型', 'size': 16, 'after': 4},
        {'t': '•  谱估计', 'size': 16, 'after': 4},
        {'t': '•  传感器校准', 'size': 16, 'after': 14},
        {'t': '⑥ 大模型增量微调中的路由选择', 'size': 19, 'bold': True, 'color': ACCENT2, 'after': 6},
        {'t': '•  用 RLS 训练路由器，为每个任务选择独立 LoRA 子空间', 'size': 16, 'after': 4},
        {'t': '•  免回放旧数据，理论零遗忘', 'size': 16, 'after': 4},
        {'t': '•  典型方案：Any-SSR、RLSEdit、KRLS-Attn、ATS', 'size': 16, 'after': 4},
    ]
    add_body(s, left_items, left=0.78, top=1.35, width=5.75, height=5.8)
    add_body(s, right_items, left=6.9, top=1.35, width=5.7, height=5.8)
    next_page(s)

    # ---------- 27 工程建议 ----------
    s = blank(prs)
    add_header(s, '5.2  工程实践建议')

    add_body(s, [
        {'t': '①  输入输出先归一化、去均值', 'size': 19, 'after': 12},
        {'t': '②  时变快时选较小 λ；时变慢或平稳时选较大 λ', 'size': 19, 'after': 12},
        {'t': '③  高精度场景使用 QR-RLS 或 UD-RLS', 'size': 19, 'after': 12},
        {'t': '④  监控 P(n) 的条件数，异常时重置', 'size': 19, 'after': 12},
        {'t': '⑤  不要随意求逆，用 solve / lstsq / Cholesky 分解', 'size': 19, 'after': 12},
        {'t': '⑥  高维场景先降维，或用对角 / 低秩 RLS', 'size': 19, 'after': 12},
        {'t': '⑦  P 强制对称，加 jitter 防奇异', 'size': 19, 'after': 12},
    ], top=1.55, height=5.4)
    next_page(s)

    # ---------- 28 章节 6 ----------
    page_section(prs, '06', '大模型增量微调中的 RLS 路由',
                 '灾难性遗忘 · LoRA 子空间隔离 · 免回放路由器')

    # ---------- 29 灾难性遗忘 ----------
    s = blank(prs)
    add_header(s, '6.1  问题：灾难性遗忘')

    add_formula(s, [
        '顺序微调多个任务 ⟹ 新任务梯度覆盖旧任务最优参数 ⟹ 旧任务性能骤降',
    ], top=1.5, size=19, bg=BG_SOFT2)

    add_body(s, [
        {'t': '专业描述', 'size': 19, 'bold': True, 'color': PRIMARY, 'after': 8},
        {'t': '•  顺序微调多个任务时，参数被新任务主导', 'size': 17, 'after': 5},
        {'t': '•  旧任务的最优解被覆盖，性能不可逆下降', 'size': 17, 'after': 5},
        {'t': '•  回放旧数据代价高，甚至不可得（隐私 / 存储）', 'size': 17, 'after': 12},
    ], top=2.55, height=2.2)

    add_body(s, [
        {'t': '通俗理解', 'size': 19, 'bold': True, 'color': ACCENT2, 'after': 8},
        {'t': '•  像狗熊掰棒子，掰一个丢一个', 'size': 17, 'after': 5},
        {'t': '•  像多人共用笔记本，新内容擦掉旧内容', 'size': 17, 'after': 5},
    ], top=4.85, height=1.9)
    next_page(s)

    # ---------- 30 隔离 + RLS 路由 ----------
    s = blank(prs)
    add_header(s, '6.2  思路：隔离 + RLS 路由')

    add_body(s, [
        {'t': '隔离', 'size': 20, 'bold': True, 'color': ACCENT, 'after': 8},
        {'t': '•  每个任务独立 LoRA 子空间，互不干扰', 'size': 17, 'after': 5},
        {'t': '•  底层共享特征，上层任务专用参数', 'size': 17, 'after': 14},
    ], top=1.35, height=1.9)

    add_body(s, [
        {'t': '路由', 'size': 20, 'bold': True, 'color': ACCENT, 'after': 8},
        {'t': '•  用 RLS 训练路由器', 'size': 17, 'after': 5},
        {'t': '•  根据输入特征 f(x) 选择正确的 LoRA', 'size': 17, 'after': 5},
        {'t': '•  score = f(x) @ W_router，argmax 选 LoRA', 'size': 17, 'after': 14},
    ], top=3.25, height=2.1)

    add_body(s, [
        {'t': 'RLS 的三大优势', 'size': 20, 'bold': True, 'color': ACCENT2, 'after': 8},
        {'t': '•  递归更新，免回放旧数据', 'size': 17, 'after': 5},
        {'t': '•  顺序训练 ≡ 联合训练', 'size': 17, 'after': 5},
        {'t': '•  理论零遗忘', 'size': 17, 'after': 5},
    ], top=5.35, height=1.9)
    next_page(s)

    # ---------- 31 典型方案 Any-SSR ----------
    s = blank(prs)
    add_header(s, '6.3  典型方案：Any-SSR')

    add_body(s, [
        {'t': '架构组成', 'size': 19, 'bold': True, 'color': PRIMARY, 'after': 10},
        {'t': '①  底层冻结，提取共享特征', 'size': 18, 'after': 8},
        {'t': '②  上层每任务独立 LoRA 子空间', 'size': 18, 'after': 8},
        {'t': '③  RLS 路由器：score = f(x) @ W_router，argmax 选 LoRA', 'size': 18, 'after': 8},
        {'t': '④  路由器只更新自身参数，不更新大模型权重', 'size': 18, 'after': 8},
    ], top=1.4, height=3.0)

    add_formula(s, [
        '效果：路由准确率 ≈ 100%   ·   旧任务保留近完美性能',
    ], top=4.55, size=19, bg=BG_SOFT2)
    next_page(s)

    # ---------- 32 核心更新（极简） ----------
    s = blank(prs)
    add_header(s, '6.4  RLS 路由器核心更新（极简版）')
    y = add_code(s, [
        'e = target - f.T @ W                       # 新息',
        'k = P @ f / (lam + f.T @ P @ f)            # 增益向量',
        'W = W + k @ e                              # 参数更新',
        'P = (P - k @ f.T @ P) / lam                # 协方差更新',
        'P = (P + P.T) / 2                          # 强制对称',
    ], top=1.55, size=15, height=2.4)

    add_body(s, [
        {'runs': [
            {'t': 'f', 'size': 18, 'italic': True, 'color': ACCENT, 'font': FONT_MATH},
            {'t': '：冻结特征向量（backbone 输出）', 'size': 18, 'color': TEXT},
        ], 'after': 8},
        {'runs': [
            {'t': 'W', 'size': 18, 'italic': True, 'color': ACCENT, 'font': FONT_MATH},
            {'t': '：路由器权重矩阵（feat_dim × n_tasks）', 'size': 18, 'color': TEXT},
        ], 'after': 8},
        {'runs': [
            {'t': 'P', 'size': 18, 'italic': True, 'color': ACCENT, 'font': FONT_MATH},
            {'t': '：协方差矩阵，表示路由参数不确定性', 'size': 18, 'color': TEXT},
        ], 'after': 8},
        {'runs': [
            {'t': 'λ', 'size': 18, 'italic': True, 'color': ACCENT, 'font': FONT_MATH},
            {'t': '：遗忘因子，增量微调中常取 0.99 ~ 1.0', 'size': 18, 'color': TEXT},
        ], 'after': 8},
    ], top=y + 0.05, height=3.0)
    next_page(s)

    # ---------- 33 注意事项与一句话 ----------
    s = blank(prs)
    add_header(s, '6.5  注意事项与一句话')

    add_body(s, [
        {'t': '注意事项', 'size': 20, 'bold': True, 'color': PRIMARY, 'after': 10},
        {'t': '•  不要随意 inv，用 solve / lstsq / Cholesky', 'size': 17, 'after': 6},
        {'t': '•  P 强制对称，λ 取 0.99 ~ 1.0，加 jitter', 'size': 17, 'after': 6},
        {'t': '•  高维特征先降维，或用对角 / 低秩 RLS', 'size': 17, 'after': 6},
        {'t': '•  监控 P 的条件数，异常时重置', 'size': 17, 'after': 6},
        {'t': '•  路由目标建议用 one-hot，配合特征归一化', 'size': 17, 'after': 6},
    ], top=1.38, height=3.2)

    add_formula(s, [
        'RLS 在增量微调中做免回放路由器：',
        '任务子空间隔离  +  顺序学习不遗忘',
    ], top=4.85, size=20, bg=BG_SOFT2)
    next_page(s)

    # ---------- 34 章节 7 ----------
    page_section(prs, '07', 'Python 代码示例',
                 'RLS 类  ·  大模型增量微调模拟  ·  RLS 路由器')

    # ---------- 35 RLS 类核心代码 ----------
    s = blank(prs)
    add_header(s, '7.1  RLS 类核心代码')
    add_code(s, [
        'import numpy as np',
        '',
        'class RLS:',
        '    def __init__(self, n, lam=0.99, delta=1e3):',
        '        self.w = np.zeros((n, 1))          # 滤波器系数',
        '        self.P = delta * np.eye(n)         # 协方差矩阵',
        '        self.lam = lam                     # 遗忘因子',
        '',
        '    def update(self, x, d):',
        '        x = np.asarray(x, dtype=float).reshape(-1, 1)',
        '        d = float(np.asarray(d).item())',
        '',
        '        e   = d - (x.T @ self.w).item()                 # 新息',
        '        den = self.lam + (x.T @ self.P @ x).item()      # 标量分母',
        '        k   = (self.P @ x) / den                        # 增益',
        '',
        '        self.w = self.w + k * e                         # 参数更新',
        '        self.P = (self.P - k @ x.T @ self.P) / self.lam # 协方差更新',
        '        self.P = (self.P + self.P.T) / 2                # 强制对称',
        '',
        '        return self.w.ravel().copy(), e',
    ], top=1.35, size=12.5)
    next_page(s)

    # ---------- 36 大模型模拟结构 ----------
    s = blank(prs)
    add_header(s, '7.2  大模型增量微调模拟：整体结构')

    add_body(s, [
        {'t': '①  FrozenBackbone（模拟冻结的大模型底层）', 'size': 18, 'bold': True,
         'color': ACCENT, 'after': 6},
        {'t': '   输入 in_dim → 隐藏层 → 输出 feat_dim 特征，参数全部冻结', 'size': 16, 'after': 12},

        {'t': '②  TaskHead（模拟 LoRA 模块）', 'size': 18, 'bold': True,
         'color': ACCENT, 'after': 6},
        {'t': '   每个任务一个独立线性头，只训练自己的参数', 'size': 16, 'after': 12},

        {'t': '③  RLSRouter（任务路由器）', 'size': 18, 'bold': True,
         'color': ACCENT, 'after': 6},
        {'t': '   输入冻结特征 f，输出任务选择；参数由 RLS 递推更新', 'size': 16, 'after': 12},

        {'t': '④  顺序增量训练', 'size': 18, 'bold': True, 'color': ACCENT, 'after': 6},
        {'t': '   依次训练任务 0 → 1 → 2 → …，训练新任务时不访问旧任务数据', 'size': 16, 'after': 12},
    ], top=1.35, height=5.6)
    next_page(s)

    # ---------- 37 RLS 路由器核心代码 ----------
    s = blank(prs)
    add_header(s, '7.3  RLS 路由器核心代码')
    add_code(s, [
        'class RLSRouter:',
        '    def __init__(self, feat_dim, n_tasks, lam=1.0, delta=1e3):',
        '        self.W   = np.zeros((feat_dim, n_tasks))   # 路由器权重',
        '        self.P   = delta * np.eye(feat_dim)        # 协方差矩阵',
        '        self.lam = lam',
        '',
        '    def update(self, f, target):',
        '        f      = f.reshape(-1, 1)          # 列向量',
        '        target = target.reshape(1, -1)     # 行向量',
        '',
        '        den  = self.lam + float(f.T @ self.P @ f)',
        '        k    = (self.P @ f) / den',
        '        pred = f.T @ self.W',
        '',
        '        self.W = self.W + k @ (target - pred)          # 外积更新',
        '        self.P = (self.P - k @ f.T @ self.P) / self.lam',
        '        self.P = (self.P + self.P.T) / 2               # 强制对称',
        '',
        '    def predict(self, f):',
        '        return np.argmax(f @ self.W, axis=-1)',
    ], top=1.35, size=12.5)
    next_page(s)

    # ---------- 38 运行结果示意 ----------
    s = blank(prs)
    add_header(s, '7.4  运行结果示意')

    add_table(s, [
        ['任务', '路由准确率', 'MSE'],
        ['任务 0', '99.50%', '0.0123'],
        ['任务 1', '100.00%', '0.0098'],
        ['任务 2', '99.00%', '0.0156'],
        ['整体', '—', '0.0126'],
    ], top=1.6, width=8.0, font_size=16)

    add_body(s, [
        {'t': '关键点', 'size': 19, 'bold': True, 'color': PRIMARY, 'after': 8},
        {'t': '•  路由器只更新自身参数，不更新大模型权重', 'size': 17, 'after': 6},
        {'t': '•  顺序训练时不访问旧任务数据，实现免回放', 'size': 17, 'after': 6},
        {'t': '•  旧任务性能不下降，理论零遗忘', 'size': 17, 'after': 6},
        {'t': '•  真实场景：FrozenBackbone → 冻结 Transformer 底层，TaskHead → LoRA', 'size': 17, 'after': 6},
    ], top=4.5, height=2.8)
    next_page(s)

    # ---------- 39 章节 8 ----------
    page_section(prs, '08', '总结与核心公式速查',
                 'RLS = 在线最小化加权误差平方和 + 指数遗忘 + 递推矩阵逆 + 新息修正')

    # ---------- 40 核心公式速查 ----------
    s = blank(prs)
    add_header(s, '8.1  核心公式速查')
    add_formula(s, [
        '增益：      k(n) = P(n−1)x(n) / ( λ + xᵀ(n)P(n−1)x(n) )',
        '参数更新：  w(n) = w(n−1) + k(n)[ d(n) − xᵀ(n)w(n−1) ]',
        '协方差更新：P(n) = (1/λ)[ P(n−1) − k(n)xᵀ(n)P(n−1) ]',
        '初始化：    w(0) = 0,    P(0) = δ·I',
    ], top=1.75, size=19)
    next_page(s)

    # ---------- 41 总结一句话 ----------
    s = blank(prs)
    add_header(s, '8.2  总结')

    add_body(s, [
        {'t': 'RLS 核心思想', 'size': 20, 'bold': True, 'color': PRIMARY, 'after': 10},
        {'t': '•  在每个时刻最小化加权误差平方和', 'size': 18, 'after': 7},
        {'t': '•  用遗忘因子 λ 对历史数据指数加权', 'size': 18, 'after': 7},
        {'t': '•  通过增益向量 k(n) 按新息修正滤波器系数', 'size': 18, 'after': 7},
        {'t': '•  通过协方差矩阵 P(n) 表示参数不确定性', 'size': 18, 'after': 7},
        {'t': '•  递推更新，避免每次重新求矩阵逆', 'size': 18, 'after': 7},
    ], top=1.4, height=3.4)

    add_formula(s, [
        'RLS = 在线最小化加权误差平方和  +  指数遗忘',
        '          +  递推矩阵逆  +  新息修正',
    ], top=5.0, size=19, bg=BG_SOFT2)
    next_page(s)

    # ---------- 42 附录 1 ----------
    s = blank(prs)
    add_header(s, '附录 A：矩阵求逆引理')
    add_body(s, [
        {'t': '设：', 'size': 18, 'after': 8},
        {'t': 'A ∈ ℝⁿˣⁿ，C ∈ ℝᵐˣᵐ 可逆，B ∈ ℝⁿˣᵐ，D ∈ ℝᵐˣⁿ', 'size': 17,
         'color': TEXT_SUB, 'font': FONT_MATH, 'after': 8},
        {'t': '且 A + BCD 与 C⁻¹ + DA⁻¹B 均可逆，则：', 'size': 18, 'after': 8},
    ], top=1.35, height=1.6)

    add_formula(s, [
        '(A + BCD)⁻¹  =  A⁻¹ − A⁻¹B (C⁻¹ + DA⁻¹B)⁻¹ DA⁻¹',
    ], top=2.85, size=21)

    add_body(s, [
        {'t': '该引理又名：Sherman–Morrison–Woodbury 公式。', 'size': 17,
         'color': TEXT_SUB, 'after': 8},
        {'t': 'RLS 用它把「每次求 O(N³) 的矩阵逆」变成「O(N²) 的递推更新」。', 'size': 17,
         'color': TEXT_SUB, 'after': 8},
    ], top=4.3, height=1.8)
    next_page(s)

    # ---------- 43 附录 2 分块矩阵证明 ----------
    s = blank(prs)
    add_header(s, '附录 B：分块矩阵证明')
    add_body(s, [
        {'t': '构造分块矩阵：', 'size': 17, 'bold': True, 'color': PRIMARY, 'after': 6},
    ], top=1.28, height=0.45)
    y = add_formula(s, [
        'M = [ A  B ; −D  C⁻¹ ]',
    ], top=1.75, size=20)

    add_body(s, [
        {'t': '① 第一种消元：左乘 [ I 0 ; DA⁻¹ I ]，得', 'size': 16, 'after': 4},
    ], top=y + 0.02, height=0.45)
    y2 = add_formula(s, [
        '[ A  B ; 0  C⁻¹ + DA⁻¹B ]    ⟹  (1,1) 块 = A⁻¹ − A⁻¹B S⁻¹ DA⁻¹，S = C⁻¹ + DA⁻¹B',
    ], top=y + 0.45, size=14)

    add_body(s, [
        {'t': '② 第二种消元：左乘 L = [ I −BC ; 0 I ]，得', 'size': 16, 'after': 4},
    ], top=y2 + 0.02, height=0.45)
    y3 = add_formula(s, [
        'LM = [ A + BCD  0 ; −D  C⁻¹ ]    ⟹  (1,1) 块 = (A + BCD)⁻¹',
    ], top=y2 + 0.45, size=14)

    add_body(s, [
        {'t': '两者相等，引理得证。', 'size': 16, 'bold': True, 'color': ACCENT2, 'after': 4},
    ], top=y3 + 0.05, height=0.5)
    next_page(s)

    # ---------- 44 附录 3 在 RLS 中的应用 ----------
    s = blank(prs)
    add_header(s, '附录 C：在 RLS 中的应用')
    y = add_formula(s, [
        '取  A = λ·R(n−1),   B = x(n),   C = 1,   D = xᵀ(n)',
        '则  A⁻¹ = (1/λ)·P(n−1)',
    ], top=1.5, size=19)

    add_body(s, [
        {'t': '代入引理：', 'size': 18, 'after': 6},
    ], top=y + 0.02, height=0.45)
    y2 = add_formula(s, [
        'P(n) = (1/λ) [ P(n−1) − P(n−1)x(n)xᵀ(n)P(n−1) / (λ + xᵀ(n)P(n−1)x(n)) ]',
    ], top=y + 0.5, size=16, bg=BG_SOFT2)

    add_body(s, [
        {'t': '这正是 RLS 协方差矩阵的递推公式，也是算法能够在 O(N²) 复杂度下在线运行的关键。',
         'size': 17, 'color': TEXT_SUB, 'after': 6},
    ], top=y2 + 0.05, height=1.2)
    next_page(s)

    # ---------- 45 结束页 ----------
    page_end(prs)


# ============================================================
def main():
    prs = Presentation()
    prs.slide_width = SW
    prs.slide_height = SH
    page_counter = [0]
    build(prs, page_counter)
    out = 'RLS_递推最小二乘及工程应用.pptx'
    prs.save(out)
    print(f'[OK] 已生成: {out}')
    print(f'     共 {len(prs.slides)} 页')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        import traceback
        print('[ERROR] 生成失败:')
        traceback.print_exc()