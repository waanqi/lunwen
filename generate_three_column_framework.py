from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 2140
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

FONT = r"C:\Windows\Fonts\msyh.ttc"
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"

def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT, size)

F_H = font(30, True)
F_B = font(24, True)
F_M = font(23, True)
F_S = font(21)
INK = "#202020"
GRAY = "#bec2c6"
GOAL = "#f0f3f9"

def box(x1, y1, x2, y2, fill="white", radius=0, width=2):
    if radius:
        d.rounded_rectangle((x1, y1, x2, y2), radius=radius, fill=fill, outline=INK, width=width)
    else:
        d.rectangle((x1, y1, x2, y2), fill=fill, outline=INK, width=width)

def center_text(cx, cy, lines, f=F_S, spacing=10):
    if isinstance(lines, str):
        lines = [lines]
    boxes = [d.textbbox((0, 0), line, font=f) for line in lines]
    heights = [b[3] - b[1] for b in boxes]
    total = sum(heights) + spacing * (len(lines) - 1)
    y = cy - total / 2
    for line, b, h in zip(lines, boxes, heights):
        tw = b[2] - b[0]
        d.text((cx - tw / 2, y), line, font=f, fill=INK)
        y += h + spacing

def arrow(x1, y1, x2, y2):
    d.line((x1, y1, x2, y2), fill=INK, width=2)
    if abs(x2-x1) >= abs(y2-y1):
        if x2 >= x1:
            d.line((x2-10, y2-7, x2, y2), fill=INK, width=2)
            d.line((x2-10, y2+7, x2, y2), fill=INK, width=2)
        else:
            d.line((x2+10, y2-7, x2, y2), fill=INK, width=2)
            d.line((x2+10, y2+7, x2, y2), fill=INK, width=2)
    else:
        if y2 >= y1:
            d.line((x2-7, y2-10, x2, y2), fill=INK, width=2)
            d.line((x2+7, y2-10, x2, y2), fill=INK, width=2)
        else:
            d.line((x2-7, y2+10, x2, y2), fill=INK, width=2)
            d.line((x2+7, y2+10, x2, y2), fill=INK, width=2)

def section_bar(y, text):
    box(380, y, 1160, y+55, GRAY, radius=5)
    center_text(770, y+28, text, F_M)

def goal_box(y1, y2, lines):
    box(1260, y1, 1550, y2, GOAL)
    center_text(1405, (y1+y2)//2, lines, F_S, 9)

# headers and dividers
box(55, 28, 275, 84, GRAY, radius=28)
center_text(165, 56, "研究框架", F_H)
box(690, 28, 910, 84, GRAY, radius=28)
center_text(800, 56, "研究内容", F_H)
box(1300, 28, 1520, 84, GRAY, radius=28)
center_text(1410, 56, "阶段目标", F_H)
for x in (330, 1210):
    y = 98
    while y < 2105:
        d.line((x, y, x, min(y+8, 2105)), fill=INK, width=3)
        y += 16

# left column
left = [
    (120, 305, ["研究背景与", "问题提出"]),
    (350, 550, ["理论基础与", "研究现状"]),
    (595, 855, ["用户需求研究", "与设计策略"]),
    (900, 1160, ["刚柔耦合", "Kresling 腕关节", "设计"]),
    (1205, 1595, ["健侧手控制", "模块化假肢", "腕部系统设计"]),
    (1640, 1880, ["系统评价与", "结果分析"]),
    (1925, 2085, ["总结与", "展望"]),
]
for i, (y1, y2, lines) in enumerate(left):
    box(50, y1, 280, y2)
    center_text(165, (y1+y2)//2, lines, F_B, 11)
    if i < len(left)-1:
        arrow(165, y2, 165, left[i+1][0]-6)

# center: chapter 1
section_bar(120, "第一章　研究背景与问题界定")
for x1, x2, lines in [
    (380,625,["研究背景及","选题来源"]),
    (647,892,["假肢腕部的","现实问题"]),
    (914,1160,["研究目的、内容","方法与创新点"]),
]:
    box(x1,190,x2,282,"white",5)
    center_text((x1+x2)//2,236,lines,F_S,7)
arrow(625,236,642,236); arrow(892,236,909,236)

# center: chapter 2
section_bar(350, "第二章　相关理论与研究现状")
for x1, y1, x2, y2, text in [
    (380,422,750,477,"假肢腕关节设计研究"),
    (790,422,1160,477,"Kresling 与刚柔耦合结构"),
    (380,492,750,547,"模块化末端工具研究"),
    (790,492,1160,547,"健侧肢体控制方式研究"),
]:
    box(x1,y1,x2,y2,"white",5); center_text((x1+x2)//2,(y1+y2)//2,text,F_S)

# center: chapter 3
section_bar(595, "第三章　用户需求与系统设计策略")
for x1, x2, lines in [
    (380,625,["用户调研","访谈、观察","典型任务"]),
    (647,892,["需求分析","用户旅程","优先级评价"]),
    (914,1160,["设计转译","系统定位","设计策略"]),
]:
    box(x1,668,x2,786,"white",5); center_text((x1+x2)//2,727,lines,F_S,5)
arrow(625,727,642,727); arrow(892,727,909,727)
box(380,802,1160,855,"white",5)
center_text(770,829,"形成“结构—模块—交互”三层系统设计要素",F_S)

# center: chapter 4
section_bar(900, "第四章　刚柔耦合 Kresling 腕关节设计")
for x1, x2, lines in [
    (380,625,["构型设计","刚性杆件","活动底边"]),
    (647,892,["运动设计","相反手性折纸层","模式与绳驱关系"]),
    (914,1160,["原型验证","样机制作","基础功能测试"]),
]:
    box(x1,974,x2,1092,"white",5); center_text((x1+x2)//2,1033,lines,F_S,5)
arrow(625,1033,642,1033); arrow(892,1033,909,1033)
box(380,1105,1160,1160,"white",5)
center_text(770,1133,"输出：运动模式可切换的刚柔耦合 Kresling 腕关节",F_S)

# center: chapter 5
section_bar(1205, "第五章　健侧手控制的模块化假肢腕部系统设计")
for x1, x2, title, lines in [
    (380,625,"健侧手控制",["健侧腕部姿态采集","连续运动跟随","手指／按键模式指令"]),
    (647,892,"模块化工具",["统一连接接口","假肢手掌／夹具","其他专用工具头"]),
    (914,1160,"系统整合",["控制映射与逻辑","软硬件系统集成","整机原型实现"]),
]:
    box(x1,1280,x2,1495,"white",5)
    center_text((x1+x2)//2,1315,title,F_M)
    d.line((x1+22,1340,x2-22,1340),fill=INK,width=2)
    center_text((x1+x2)//2,1412,lines,F_S,12)
arrow(625,1388,642,1388); arrow(892,1388,909,1388)
box(380,1512,1160,1595,"white",5)
center_text(770,1554,["三项创新协同：刚柔耦合结构创新＋末端工具模块创新", "＋健侧连续跟随与离散指令结合的交互创新"],F_S,7)

# center: evaluation
section_bar(1640, "系统评价与结果分析")
for x1, x2, lines in [
    (380,625,["结构与功能测试","运动、负载、换装"]),
    (647,892,["ADL 任务评价","典型日常活动"]),
    (914,1160,["用户主观评价","可用性与体验"]),
]:
    box(x1,1715,x2,1820,"white",5); center_text((x1+x2)//2,1768,lines,F_S,8)
box(380,1835,1160,1880,"white",5)
center_text(770,1858,"综合验证系统的有效性、适配性与设计价值",F_S)

# center: conclusion
section_bar(1925, "第六章　总结与展望")
for x1, x2, text in [
    (380,625,"研究成果与结论"),
    (647,892,"创新点归纳与讨论"),
    (914,1160,"局限与后续展望"),
]:
    box(x1,1995,x2,2065,"white",5); center_text((x1+x2)//2,2030,text,F_S)

# right column
goals = [
    (145,275,["明确研究意义、","目的与总体路线"]),
    (380,510,["明确研究空白","与设计机会"]),
    (630,780,["提取用户需求，","形成系统设计策略","与评价依据"]),
    (930,1080,["完成核心腕关节","结构原型与","功能验证"]),
    (1265,1435,["完成健侧手控制、","模块化工具与","整机原型设计"]),
    (1675,1825,["验证产品的","有效性、适配性","与可用性"]),
    (1958,2088,["凝练研究结论，","提出后续方向"]),
]
for i, (y1,y2,lines) in enumerate(goals):
    goal_box(y1,y2,lines)
    if i < len(goals)-1:
        arrow(1405,y2,1405,goals[i+1][0]-10)

center_text(800,2115,"研究主线：需求驱动 → 结构创新 → 模块整合 → 交互实现 → 情境验证",F_S)

img.save(r"D:\Desk\折纸\kresling大论文\codex老师辅助\研究框架图_三栏式.png", dpi=(300,300))
