import os
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
lp.height = 650
lp.width = 400
lp.data = data
lp.joinedLines = 1
lp.lines.symbol = makeMarker('FilledCircle')

lp.xValueAxis.valueMin = 1
lp.xValueAxis.valueMax = 5
lp.xValueAxis.valueStep = 1

lp.yValueAxis.valueMin = 0
lp.yValueAxis.valueMax = 5000
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

try:
    drawing.save(formats=['pdf'], outDir=".", fnRoot="abc")
except:
    traceback.print_exc()


print(os.path.split('/test'))
