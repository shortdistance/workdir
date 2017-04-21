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
                rowContent['M'] = row[12]
                contentList.append(rowContent)
        return contentList
    else:
        return []

  def wExcelNewReq(self, infile, sheetname, contentList):
      oldWb = xlrd.open_workbook(infile)
      newWb = copy(oldWb)
      newWs = newWb.get_sheet(0)
      
      for record in contentList:
          newWs.write(int(record['index']), 14, record['intKF'])
          newWs.write(int(record['index']), 15, record['intSC'])
          newWs.write(int(record['index']), 16, record['intFB'])
          print "record %d finished!!" % int(record['index'])
      
      infileNew = infile.split('.')[0] + '_'+ sheetname+'.xls'
      newWb.save(infileNew)
      print "save success!!"
      
  
    
def analyseData(dataList):
  if type(dataList) is not type([]):
    return None
  
  strBaseUrl = 'http://172.16.9.106:9001/svn'
  strKF = '开发库'
  strSC = '受控库'
  strFB = '产品库'
  
  for data in dataList:
    print u'start execute %s record!!' % data['index']
    urlKF = urlSC = urlFB = ''
    intKF = intSC = intFB = 0
    
    reposName = ''
    if data['M']:
        reposName = data['M'].strip()
        urlKF = '%s/%s/%s' % (strBaseUrl, reposName, strKF)
        intKF = int(getSvnLog(urlKF))
        
        urlSC = '%s/%s/%s' % (strBaseUrl, reposName, strSC)
        intSC = int(getSvnLog(urlSC))

        urlFB = '%s/%s/%s' % (strBaseUrl, reposName, strFB)
        intFB = int(getSvnLog(urlFB))
        
    data['intKF'] = intKF
    data['intSC'] = intSC
    data['intFB'] = intFB
    
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
      
def getSvnLog(svnUrl):
    svn_bin='.\\svn\\svn.exe'
    svn_user, svn_passwd,  = getUserAndPasswd(svnUrl)
    svnUrl = svnUrl.encode("gbk", 'ignore')
    if svn_user and svn_passwd:
        try:
            cmd = '%s log  --xml --username %s --password %s --no-auth-cache \"%s\"'%(svn_bin, svn_user, svn_passwd, svnUrl)
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
    contentList = analyseData(retList)
    t.wExcelNewReq(infile, sheetname, contentList)    
    

if __name__ == '__main__':
  
    def Usage():
        print 'Usage0: python TestExcel1.py'

    if len(sys.argv) != 1:
        Usage()
        sys.exit(0)
    
    
    infile = 'D:\[Proj]\Python\workdir\wangzj\持续迭代（工程、研发项目）明细数据.xlsx'
    sheetnameNewReq = '201503'
    
    NewReq(infile, sheetnameNewReq)
  
  