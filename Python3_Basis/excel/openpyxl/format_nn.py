# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/15 23:23
import ast

import openpyxl
import json
import io

# excel表格转json文件
def excel_to_json(excel_file):
    book = openpyxl.load_workbook(excel_file)
    sheet = book[u'Sheet1']
    max_row = sheet.max_row
    max_column = sheet.max_column
    print(max_row, max_column)
    # 遍历每一行
    for col in range(1, max_column + 1):
        for row in range(1, max_row + 1):
            print(json.dumps(sheet.cell(row, col).value).removeprefix("\"").removesuffix("\""))
            sheet.cell(row, col).value = (json.dumps(sheet.cell(row, col).value).removeprefix("\"").removesuffix(
                "\"").replace("\n", "\n\n").replace(
                "\\u2019", "’").replace("\\u2014", "-")
                                          .replace("\\\"", "\"").replace("\\u201c","\"").replace("\\u201d","\""))

    book.save("/Users/yinpeng/GoWorkSpace/AlgoScripts/Python3_Basis/excel/openpyxl/output4.xlsx")
    book.close()

if __name__ == '__main__':
    excel_to_json(u'/Users/yinpeng/GoWorkSpace/AlgoScripts/Python3_Basis/excel/openpyxl/intro_end4.xlsx')
