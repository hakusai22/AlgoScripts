# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/15 23:23
import ast

import openpyxl
import json
import io


# excel表格转json文件
def excel_to_json(excel_file, json_f_name):
    jd = []
    heads = []
    book = openpyxl.load_workbook(excel_file)
    sheet = book[u'yinpeng']

    max_row = sheet.max_row
    max_column = sheet.max_column
    # 解析表头
    for column in range(max_column):
        heads.append(sheet.cell(1, column + 1).value)
    # 遍历每一行
    for row in range(max_row):
        if row < 1:
            continue
        one_line = {}
        # 遍历一行中的每一个单元格
        for column in range(max_column):
            k = heads[column]
            if k is None:
                continue
            v1 = sheet.cell(row + 1, column + 1).value
            print(type(v1))

            if "fat" in k or "carbs" in k or "protein" in k:
                one_line[k] = v1
            elif "quantity" in k:
                one_line[k] = v1.replace("'", "")
            elif "kcal" in k:
                one_line[k] = "[" + str(v1).replace("[", "").replace("]", "") + "]"
            else:
                v = str(v1)
                one_line[k] = v

        jd.append(one_line)

    print(jd)
    book.close()
    # 将json保存为文件
    save_json_file(jd, json_f_name)


# 将json保存为文件
def save_json_file(jd, json_f_name):
    f = io.open(json_f_name, 'w', encoding='utf-8', newline='\n')
    f.write("[" + '\n')
    for j in range(len(jd)):
        txt = json.dumps(jd[j], ensure_ascii=False)
        if j != len(jd) - 1:
            f.write(txt + "," + '\n')
        else:
            f.write(txt + '\n')
    f.write("]" + '\n')
    f.close()


if __name__ == '__main__':
    excel_to_json(u'./十万.xlsx', '十万.txt')
