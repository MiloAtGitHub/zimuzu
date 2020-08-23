#-*- codeing = utf-8 -*-
#@Time : 2020-08-21 14:50
#@File : excel.py

import xlwt

excel = xlwt.Workbook(encoding="utf-8")
sheet = excel.add_sheet('sheet1')
sheet.write(0,0,'hello')
excel.save("test.xls")