#-*-coding:utf-8-*-
import xlrd
import xlwt
import sys


class OperExcel():
  #读取Excel表
  def read_excel(self,infile):
    reload(sys)
    sys.setdefaultencoding('utf-8')    

    contentList = []
    rfile = xlrd.open_workbook(infile)
    #创建索引顺序获取一个工作表
    table = rfile.sheet_by_index(0)
    #其他方式
    #table = rfile.sheets()[0]
    #table = rfile.sheet_by_name(u'Sheet1')

    #获取行数和列数
    nrows = table.nrows
    ncols = table.ncols

    if nrows>1 and ncols>=1:
        for rownum in range(1,nrows):
            row = table.row_values(rownum)
            if row:
                rowContent = {}
                for colnum in range(ncols):       	                
                    rowContent[u'%d' % colnum] = row[colnum].decode('utf-8')
                contentList.append(rowContent)
        return contentList
    else:
        return []
  
  def get_param_by_tcname(self, inList, ts, tc, splitChar=' '):
    tcList = [];
    if type(inList) is not type([]):
      return 0,[]
    elif len(inList)==0:
      return 0,[]
    else:
      for i in range(0, len(inList)):
        if inList[i][u'0']==str(ts) and inList[i][u'1']==str(tc):
          inParams = inList[i][u'2']
          inParamList = inParams.strip().split(splitChar)
          tcList.append(inParamList)
      return len(tcList),tcList
    
'''
if __name__ == '__main__':

  t = OperExcel()
  ls = []
  ls = t.rExcel('C:\\Users\\raychang\\Desktop\\TestCase.xls')
  print ls
  ts = u'G网'
  tc = u'G网开户'
  n = 0
  Params = []
  n, Params = t.getParam(ls, ts, tc)
  print n
  print Params
'''
