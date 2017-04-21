#-*-coding:gbk-*-
import xlrd
import xlwt
from xlutils.copy import copy
import sys
import os


class OperExcel():
  #读取Excel表
  def rExcelNewReq(self, infile, sheetname):
    reload(sys)
    sys.setdefaultencoding('gbk')    

    contentList = []
    rfile = xlrd.open_workbook(infile)
    #创建索引顺序获取一个工作表
    #table = rfile.sheet_by_index(0)
    #其他方式
    #table = rfile.sheets()[0]
    table = rfile.sheet_by_name(sheetname)

    #获取行数和列数
    nrows = table.nrows
    ncols = table.ncols
    
    if nrows>1 and ncols>=1:
        for rownum in range(1,nrows):
            row = table.row_values(rownum)
            if row:
                rowContent = {}
                rowContent['index'] = rownum
                rowContent['N'] = row[13]
                rowContent['O'] = row[14]
                rowContent['P'] = row[15]
                contentList.append(rowContent)
        return contentList
    else:
        return []

  def wExcelNewReq(self, infile, sheetname, contentList):
      oldWb = xlrd.open_workbook(infile)
      newWb = copy(oldWb)
      newWs = newWb.get_sheet(0)
      
      for record in contentList:
          newWs.write(int(record['index']), 19, record['intN'])
          newWs.write(int(record['index']), 20, record['intO'])
          newWs.write(int(record['index']), 21, record['intP'])
          print "record %d finished!!" % int(record['index'])
      
      infileNew = infile.split('.')[0] + '_'+ sheetname+'.xls'
      newWb.save(infileNew)
      print "save success!!"
      
  
    
def analyseData(dataList, startDate, endDate):
  if type(dataList) is not type([]):
    return None
  
  for data in dataList:
    print u'start execute %s record!!' % data['index']
    strN = StrO = StrP = ''
    intN = intO = intP = 0
    if data['N']:
        strN = data['N'].strip()
        intN = int(getSvnLog(strN, startDate, endDate))
        
    if data['O']:
        strO = data['O'].strip()
        intO = int(getSvnLog(strO, startDate, endDate))
        
    if data['P']:
        strP = data['P'].strip()
        intP = int(getSvnLog(strP, startDate, endDate))
        
    data['intN'] = intN
    data['intO'] = intO
    data['intP'] = intP
    
  return dataList
 
def getUserAndPasswd(url):
    if str('172.16.9.156') in url:
        return 'shenzq','123456'
    elif str('172.16.9.106') in url:
        return 'zhangleid','1qaz2wsx'
    else:
        return None,None

def datetime_toString(dt):  
    return dt.strftime("%Y%m%d%H%M%S")  
      
def getSvnLog(svnUrl, start_date, end_date):
    svn_bin='.\\svn\\svn.exe'
    svn_user, svn_passwd,  = getUserAndPasswd(svnUrl)
    svnUrl = svnUrl.encode("gbk", 'ignore')
    
    if svn_user and svn_passwd:
        cmd = '%s log -r {%s}:{%s} --xml --username %s --password %s --no-auth-cache \"%s\"' % (svn_bin, start_date, end_date, svn_user, svn_passwd, svnUrl)
        try:
            fp = os.popen(cmd)
            retStr = fp.read()
            return retStr.count('<logentry')
        except Exception,e:
            print '%s 禁止访问!!' % svnUrl
            return 0
    else:
        return 0
       
def NewReq(infile, sheetname):
    t = OperExcel()
    retList = []
    retList = t.rExcelNewReq(infile, sheetname)
    contentList = analyseData(retList, startDate, endDate)
    t.wExcelNewReq(infile, sheetname, contentList)    
    

if __name__ == '__main__':
  
    def Usage():
        print 'Usage0: python TestExcel.py 20150301 20150401'

    if len(sys.argv) != 3:
        Usage()
        sys.exit(0)
    
    startDate = sys.argv[1]
    endDate = sys.argv[2]
    
    infile = 'D:\[Proj]\Python\workdir\wangzj\持续迭代（新需求）明细数据_miso.xlsx'
    sheetnameNewReq = '201504'
    
    NewReq(infile, sheetnameNewReq)
  
  
