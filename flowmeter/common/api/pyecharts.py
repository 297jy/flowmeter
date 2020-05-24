# coding=utf-8
from pyecharts import Line, Grid, Page


class ChartInfo:
    def __init__(self, x_list, y_list, title=""):
        # 横坐标列表
        self.x_list = x_list
        # 纵坐标列表
        self.y_list = y_list
        # 图表标题
        self.title = title


class ReportForm:
    def __init__(self, width=1200, height=500):
        self.charts = []
        self.width = width
        self.height = height

    def add_chart(self, chart_info):
        """添加需要打印的图表"""
        self.charts.append(chart_info)

    def save(self, path):
        """
        将图表保存成文件
        :param path: 保存的文件路径
        :return:
        """
        page = Page()
        for chart in self.charts:
            line = Line(chart.title)
            line.add(
                "",
                chart.x_list,
                chart.y_list,
                mark_point=["max", "min"],
                mark_line=["average"],
                legend_pos="20%",
            )
            grid = Grid(width=self.width, height=self.height)
            grid.add(line, grid_top="20%")
            page.add_chart(grid)

        page.render(path)