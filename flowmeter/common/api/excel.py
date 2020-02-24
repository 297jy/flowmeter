# coding=utf-8
import xlrd
import xlwt
from flowmeter.exceptions import ValueValidException, ParameterErrorException

import logging
logger = logging.getLogger('log')


class ExcelField:

    def __init__(self, prop, name, is_require):
        # 对象属性名
        self.prop = prop
        # 该属性在excel中的列名
        self.name = name
        self.is_require = is_require

    # 创建必要的域
    @staticmethod
    def require_field(prop, name):
        return ExcelField(prop, name, True)

    @staticmethod
    def optional_field(prop, name):
        return ExcelField(prop, name, False)


class Excel:
    """
    Excel表格实体
    """
    def __init__(self, excel_fields):
        """
        """
        self.excel_fields = excel_fields
        self.obj_dict_list = []

    def is_empty(self):
        """
        判断excel数据是否为空
        :return:
        """
        empty = len(self.obj_dict_list) == 0

        return empty

    def read(self, file_name):
        """
        读取excel表格数据
        :return:
        """
        self.obj_dict_list = ExcelUtils.read(file_name, self.excel_fields)

    def write(self, file_name, sheet_name):
        """
        写入数据到excel表格
        :return:
        """
        ExcelUtils.write(file_name, sheet_name, self.obj_dict_list, self.excel_fields)


class ExcelUtils:
    """
    Excel表格工具处理类，支持xls,xlsx格式
    """
    # 数据在表格中开始的行数
    __DATA_START_LINE_NUM = 1
    # 列名在表格中的行数
    __COL_NAME_LINE_NUM = 0
    # 数据在表格中开始的列数
    __DATA_START_COL_NUM = 0
    # 字符的单位宽度
    __CHAR_WIDTH_UNIT = 800

    __FIRST_WORK_SHEET = 0

    @staticmethod
    def __open_read_sheet(file_name, sheet_name=None):
        """
        打开一个用于读的excel工作表
        :param file_name:
        :return:
        """
        try:
            # 打开文件，获取excel文件的workbook（工作簿）对象
            workbook = xlrd.open_workbook(file_name)
            if sheet_name is None:
                # 默认读取第一个单元格的内容
                worksheet = workbook.sheet_by_index(ExcelUtils.__FIRST_WORK_SHEET)
            else:
                # 通过sheet_name获得一个工作表对象
                worksheet = workbook.sheet_by_name(sheet_name)
            return worksheet
        except Exception as e:
            logging.error(e)
            raise ParameterErrorException("读取EXCEL文件失败，该文件不是EXCEL格式！")

    @staticmethod
    def __open_write_book_and_sheet(sheet_name):
        """
        打开一个用于写的excel工作表
        :param sheet_name:
        :return:
        """
        # 打开文件，获取excel文件的workbook（工作簿）对象
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet(sheet_name)
        return workbook, worksheet

    @staticmethod
    def __get_prop_index_map(props):
        """
        根据属性列表，获取列索引与属性名的映射字典
        :param props:
        :return:
        """
        res = {}

        for index in range(0, len(props)):
            res[index] = props[index]

        return res

    @staticmethod
    def __get_props(worksheet, excel_fields):
        """
        获取工作表格的属性列表
        :param worksheet: 工作表
        :return:
        """
        col_names = worksheet.row_values(0)
        prop_names = []
        for col_name in col_names:
            prop = None
            for field in excel_fields:
                if field.name == col_name:
                    prop = field.prop
                    break
            prop_names.append(prop)

        for field in excel_fields:
            # 对象必要的属性excel表格中没有，则说明excel表格格式错误，抛异常
            if field.is_require and field.prop not in prop_names:
                raise ValueValidException("读取excel表格失败！列名：{}，不存在！".format(field.name))

        return prop_names

    @staticmethod
    def __transfer_object_dict(row_value, name_index_map):
        """
        将某行的列值，转为对象字典
        :param row_value:
        :param name_index_map: 名称与索引之间的映射字典
        :return:
        """
        res = {}
        # 遍历所有列的值
        for index in range(0, len(row_value)):
            # 获取索引对应的列名
            name = name_index_map[index]
            # 将列名与该列的值对应起来
            res[name] = row_value[index]

        return res

    @staticmethod
    def __read_object_dict_list(worksheet, excel_fields):
        """
        :param worksheet: excel表格对象
        :return:
        """

        # 获取工作表的行数，列数
        nrows = worksheet.nrows
        ncols = worksheet.ncols

        prop_names = ExcelUtils.__get_props(worksheet, excel_fields)
        prop_name_index_map = ExcelUtils.__get_prop_index_map(prop_names)

        obj_dicts = []
        for row in range(ExcelUtils.__DATA_START_LINE_NUM, nrows):
            # 获取某行的数据
            values = worksheet.row_values(row)
            obj_dict = {}
            for col in range(ExcelUtils.__DATA_START_COL_NUM, ncols):
                prop_name = prop_name_index_map.get(col)
                if prop_name is not None:
                    obj_dict[prop_name] = values[col]
            obj_dicts.append(obj_dict)

        return obj_dicts

    @staticmethod
    def read(filename, excel_fields):
        """
        读取excel表格中的数据
        :param excel_fields:
        :param filename:
        :return:
        """
        worksheet = ExcelUtils.__open_read_sheet(filename)
        obj_dicts = ExcelUtils.__read_object_dict_list(worksheet, excel_fields)
        return obj_dicts

    class FontName:
        """
        常用的字体样式常量
        """
        TIMES_NEW_ROMAN = 'Times New Roman'

    class FontStyle:
        def __init__(self, name, height, bold=False):
            self.name = name
            self.height = height
            self.bold = bold

        def get_font_style(self):
            font_style = xlwt.Font()  # 为样式创建字体
            font_style.name = self.name  # 'Times New Roman'
            font_style.bold = self.bold
            font_style.height = self.height

            return font_style

    class BorderStyle:
        def __init__(self, left, right, top, bottom):
            self.left = left
            self.right = right
            self.top = top
            self.bottom = bottom

        def get_border_style(self):

            borders = xlwt.Borders()
            borders.left = self.left
            borders.right = self.right
            borders.top = self.top
            borders.bottom = self.bottom

            return borders

    class AlignStyle:
        @staticmethod
        def create_align_center_style():

            alignment = xlwt.Alignment()
            alignment.horz = xlwt.Alignment.HORZ_CENTER
            alignment.vert = xlwt.Alignment.VERT_CENTER

            return alignment

    class Style:
        def __init__(self, font_style, border_style, format_str=''):
            self.font_style = font_style
            self.border_style = border_style
            self.format_str = format_str
            self.alignment = ExcelUtils.AlignStyle.create_align_center_style()

        def get_style(self):

            style = xlwt.XFStyle()  # 初始化样式
            style.font = self.font_style.get_font_style()
            style.borders = self.border_style.get_border_style()
            style.num_format_str = self.format_str
            style.alignment = self.alignment

            return style

    @staticmethod
    def __get_val_width(val):
        """
        获取val在excel表格中的宽度
        :param val:
        :return:
        """

        str_val = str(val)
        col_width = 0
        for char in str_val:
            # 中文为1个宽度单位，其他字符为0.5个宽度单位
            if 0x4e00 <= ord(char) < 0x9fa6:
                char_width = 1
            else:
                char_width = 0.5
            col_width = col_width + char_width

        return int(col_width)

    @staticmethod
    def __get_width_dict_of_col(excel_fields, obj_dict_list):
        """
        获取每一列对应的宽度字典
        :param obj_dict_list 对象字典数组
        :return: dict
        """

        width_dict = {field.prop: len(field.name) for field in excel_fields}
        for obj_dict in obj_dict_list:
            for key, val in obj_dict.items():

                # 取每一列的最长字符长度
                width = width_dict.get(key, 0)
                col_width = ExcelUtils.__get_val_width(val)
                width = max(width, int(col_width))
                width_dict[key] = width

        for key, val in width_dict.items():
            width_dict[key] = val * ExcelUtils.__CHAR_WIDTH_UNIT
        return width_dict

    @staticmethod
    def __set_col_width(worksheet, width_dict, excel_fields):
        """
        设置每一列单元格的宽度
        :param worksheet:
        :param width_dict: 每个属性对应的宽度
        :return:
        """

        for index in range(0, len(excel_fields)):
            name = excel_fields[index].prop
            width = width_dict.get(name, 0)
            worksheet.col(index).width = width

    @staticmethod
    def __get_style():
        """
        获取样式
        :return:
        """
        font_style = ExcelUtils.FontStyle(ExcelUtils.FontName.TIMES_NEW_ROMAN, 220)
        border_style = ExcelUtils.BorderStyle(0, 0, 0, 0)
        style = ExcelUtils.Style(font_style, border_style)
        return style.get_style()

    @staticmethod
    def __write_col_name(worksheet, excel_fields):
        """
        写入列名如：[姓名,年龄]
        :param worksheet:
        :return:
        """
        style = ExcelUtils.__get_style()

        for index in range(0, len(excel_fields)):
            name = excel_fields[index].name
            worksheet.write(ExcelUtils.__COL_NAME_LINE_NUM, index, name, style)

    @staticmethod
    def __write_object_dict_list(worksheet, obj_dict_list, excel_fields):

        style = ExcelUtils.__get_style()

        for row in range(0, len(obj_dict_list)):
            obj_dict = obj_dict_list[row]
            for col in range(0, len(excel_fields)):
                prop = excel_fields[col].prop
                data = obj_dict.get(prop, '')
                worksheet.write(row+1, col, data, style)

    @staticmethod
    def write(filename, sheet_name, obj_dict_list, excel_fields):
        """
        将excel表格中的数据保存在磁盘上
        :return:
        """
        workbook, worksheet = ExcelUtils.__open_write_book_and_sheet(sheet_name)
        # 设置每列的宽度
        width_dict = ExcelUtils.__get_width_dict_of_col(excel_fields, obj_dict_list)
        ExcelUtils.__set_col_width(worksheet, width_dict, excel_fields)

        ExcelUtils.__write_col_name(worksheet, excel_fields)
        ExcelUtils.__write_object_dict_list(worksheet, obj_dict_list, excel_fields)

        workbook.save(filename)


def main():
    props = ['name', 'sex', 'age', 'money']
    names = ['名字', '性别', '年龄', '余额']
    excel_fields = []
    for index in range(0, len(props)):
        excel_fields.append(ExcelField.require_field(prop=props[index], name=names[index]))

    excel = Excel(excel_fields)
    student = {
        "name": "陈伟强",
        "sex": "男",
        "age": 22,
        "money": 10000.123
    }
    excel.obj_dict_list.append(student)
    excel.write("D://test.xls", "测试")
    excel.read('D://test.xls')
    print(excel.obj_dict_list)


if __name__ == "__main__":
    main()


















