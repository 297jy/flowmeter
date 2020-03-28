import traceback

from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics, ttfonts
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.piecharts import Pie

# 注意data的类型，
# 每一个数据点是一个元组
# 一条曲线对应一个存储数据点元组的元组
# 一个图形可以包含多条曲线，用列表存储曲线元组
data = [
    ((1, 100), (2, 200), (3, 300), (4, 400), (5, 500)),
    ((1, 50), (2, 80), (3, 400), (4, 40), (5, 70))
]

drawing = Drawing(500, 1000)

# 坐标轴中心坐标
lp = LinePlot()
lp.x = 50
lp.y = 80
lp.height = 250
lp.width = 400
lp.data = data
lp.joinedLines = 1
lp.lines.symbol = makeMarker('FilledCircle')

lp.xValueAxis.valueMin = 1
lp.xValueAxis.valueMax = 5
lp.xValueAxis.valueStep = 1

lp.yValueAxis.valueMin = 0
lp.yValueAxis.valueMax = 500
lp.yValueAxis.valueStep = 100
drawing.add(lp)
# 坐标轴中心坐标
lp = LinePlot()
lp.x = 50
lp.y = 300
lp.height = 250
lp.width = 400
lp.data = data
lp.joinedLines = 1
lp.lines.symbol = makeMarker('FilledCircle')

lp.xValueAxis.valueMin = 1
lp.xValueAxis.valueMax = 5
lp.xValueAxis.valueStep = 1

lp.yValueAxis.valueMin = 0
lp.yValueAxis.valueMax = 500
lp.yValueAxis.valueStep = 100
drawing.add(lp)

title = Label()
# 若需要显示中文，需要先注册一个中文字体
pdfmetrics.registerFont(ttfonts.TTFont("haha", "simsun.ttc"))
title.fontName = "haha"
title.fontSize = 12
title_text = '你好'
# title_text = "abc"
title._text = title_text
title.x = 50
title.y = 30
title.textAnchor = 'middle'
drawing.add(title)

Xlabel = Label()
Xlabel._text = '月份'
Xlabel.fontSize = 12
Xlabel.x = 480
Xlabel.y = 30
Xlabel.textAnchor = 'middle'
drawing.add(Xlabel)

Ylabel = Label()
Ylabel._text = "年份"
Ylabel.fontSize = 12
Ylabel.x = 40
Ylabel.y = 295
Ylabel.textAnchor = 'middle'
drawing.add(Ylabel)


# **这种方法可以给边框中的图例添加颜色说明**

def autoLegender(chart, categories=[], use_colors=[], title=''):
    width = 448
    height = 230
    d = Drawing(width, height)
    lab = Label()
    lab.x = 220  # x和y是title文字的位置坐标
    lab.y = 210
    lab.setText(title)
    # lab.fontName = 'song' #增加对中文字体的支持
    lab.fontSize = 20
    d.add(lab)
    d.background = Rect(0, 0, width, height, strokeWidth=1, strokeColor="#868686", fillColor=None)  # 边框颜色
    d.add(chart)
    # 颜色图例说明等
    leg = Legend()
    leg.x = 500  # 说明的x轴坐标
    leg.y = 0  # 说明的y轴坐标
    leg.boxAnchor = 'se'
    # leg.strokeWidth = 4
    leg.strokeColor = None
    leg.subCols[1].align = 'right'
    leg.columnMaximum = 10  # 图例说明一列最多显示的个数

    # leg.fontName = 'song'
    leg.alignment = 'right'
    # leg.colorNamePairs = zip(use_colors, tuple(categories))  # 增加颜色说明
    d.add(leg)
    return d


def draw_2bar_chart(min, max, x_list, data, array, x_label_angle=0, bar_color=None, height=125, width=280):
    '''
    :param min: 设置y轴的最小值
    :param max: 设置y轴的最大值
    :param x_list: x轴上的标签
    :param data: y轴对应标签的值
    :param x_label_angle: x轴上标签的倾斜角度
    :param bar_color: 柱的颜色  可以是含有多种颜色的列表
    :param height: 柱状图的高度
    :param width: 柱状图的宽度
    :return:
    '''
    bc = VerticalBarChart()
    bc.x = 50  # x和y是柱状图在框中的坐标
    bc.y = 150
    bc.height = height  # 柱状图的高度
    bc.width = width  # 柱状图的宽度
    bc.data = data

    # 图形柱上标注文字
    bc.barLabels.nudge = -5  # 文字在图形柱的上下位置
    bc.barLabelArray = array  # 要添加的文字
    bc.barLabelFormat = 'values'

    for j in range(len(data)):
        setattr(bc.bars[j], 'fillColor', bar_color[j])  # bar_color若含有多种颜色在这里分配bar_color[j]
    # 调整step
    # minv = min * 0.5
    minv = 0
    maxv = max * 1.5
    maxAxis = int(height / 10)
    # 向上取整
    minStep = int((maxv - minv + maxAxis - 1) / maxAxis)

    bc.valueAxis.valueMin = 0  # 设置y轴的最小值
    bc.valueAxis.valueMax = max * 1.5  # 设置y轴的最大值
    bc.valueAxis.valueStep = (max - min) / 4  # 设置y轴的最小度量单位
    if bc.valueAxis.valueStep < minStep:
        bc.valueAxis.valueStep = minStep
    if bc.valueAxis.valueStep == 0:
        bc.valueAxis.valueStep = 1
    bc.categoryAxis.labels.boxAnchor = 'ne'  # x轴下方标签坐标的开口方向
    bc.categoryAxis.labels.dx = -5  # x和y是x轴下方的标签距离x轴远近的坐标
    bc.categoryAxis.labels.dy = -5
    bc.categoryAxis.labels.angle = x_label_angle  # x轴上描述文字的倾斜角度
    # bc.categoryAxis.labels.fontName = 'song'
    bc.categoryAxis.style = 'stacked'
    x_real_list = []
    if len(x_list) > 10:
        for i in range(len(x_list)):
            tmp = '' if i % 5 != 0 else x_list[i]
            x_real_list.append(tmp)
    else:
        x_real_list = x_list
    bc.categoryAxis.categoryNames = x_real_list
    return bc


#    制柱状图
Style = getSampleStyleSheet()
n = Style['Normal']
my_color = [HexColor('#E13C3C'), HexColor('#BE0000')]
z = autoLegender(draw_2bar_chart(100, 300, ['a', 'b', 'c'],
                                 [(100, 200, 120), (150, 50, 130)],
                                 bar_color=my_color,
                                 array=[['100', '200', '120'], ['150', '50', '130']]),
                 categories=['first', 'last'],
                 use_colors=my_color
                 )
drawing.add(z)
try:
    drawing.save(formats=['pdf'], outDir=".", fnRoot="abc")
except:
    traceback.print_exc()
