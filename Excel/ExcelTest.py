#-*- coding:GBK �C*-
import  xdrlib ,sys
import xlrd
def open_excel(file= 'file.xls'):
	try:
		data = xlrd.open_workbook(file)
		return data
	except Exception,e:
		print str(e)


data = open_excel('excelFile.xls')
table = data.sheet_by_name(u'��2') #ͨ�����ƻ�ȡ

nrows = table.nrows
ncols = table.ncols

for i in range(nrows ):
	for j in range(ncols ):
		cellVale = table.cell(i,j).value
		print cellVale

# ���� 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
row = 0
col = 3
ctype = 1
value = u'hello world'
xf = 0# ��չ�ĸ�ʽ��
table.put_cell(row, col, ctype, value, xf)

import xlwt 
wbk = xlwt.Workbook() 
sheet = wbk.add_sheet('sheet 1')
sheet.write(0,1,'test text')
wbk.save('test.xls')