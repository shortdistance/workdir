# -*- coding: gbk -*-  

import xml.etree.ElementTree as ET
import subprocess
import os,sys
from datetime import datetime, timedelta
import time
import calendar
import cx_Oracle
from loggingConf import *
from myinclude.monitor import svn_monitor


def TimeFormatTransfer(input):
		TIME_OFFSET = 8 # 0 for GMT, 1 for BST
		return (datetime.strptime(input, '%Y-%m-%d %H:%M:%S') + timedelta(hours=TIME_OFFSET)).strftime('%Y%m%d%H%M%S')

def InputStrChangeFormat(dtStr):
    return datetime.strptime(dtStr,'%Y-%m-%d').strftime('%Y%m%d')

def DateDelta(startDateStr, endDateStr):
    d1 = datetime.strptime(startDateStr,'%Y-%m-%d')
    d2 = datetime.strptime(endDateStr,'%Y-%m-%d')
    
    delta = d2 - d1
    return delta.days

def datetime_toString(dt):  
    return dt.strftime("%Y%m%d%H%M%S")  

def read_tb_ato_svn_repository():
    try:
        con=cx_Oracle.connect("bnms","bnms","bnmsdb")
        cur=con.cursor()
        cur.execute("select KBP_ID, PROJECT_SVNURL from tb_ato_svn_repository")
        rows = cur.fetchall()
        cur.close()
        con.close()
        repos_info = {}
	repos_list = []
        reposStr = ''
        for row in rows:
            if row[0] and row[1]:
		repos_info=dict(kpi_id=row[0].strip(), repos_url=row[1].strip())
		repos_list.append(repos_info)
        return repos_list
    except Exception as err:
        logger.error(str(err))
        return {}

def insertorupdate_tb_ato_svn_ver_monitor(kbp_id, num, to_day):
    try:
        con=cx_Oracle.connect("bnms","bnms","bnmsdb")
        cur=con.cursor()
        param = {}
        param['kbp_id']=str(kbp_id)
        param['to_day'] = to_day
        
        
        cur.execute("select count(1) from TB_ATO_SVN_VER_MONITOR a where a.KBP_ID = :kbp_id and a.CURRENT_DATE = :to_day", param)
        strNum = cur.fetchone()
        param['num']=int(num)

        if int(strNum[0])>0:
            cur.execute("update TB_ATO_SVN_VER_MONITOR a set a.VERSION_COUNT = :num where a.KBP_ID = :kbp_id and a.CURRENT_DATE = :to_day", param)
        else:
            cur.execute("insert into TB_ATO_SVN_VER_MONITOR (VERSION_MONITOR_ID, KBP_ID, CURRENT_DATE, VERSION_COUNT) values (svn_ver_monitor_sequence.NEXTVAL, :kbp_id, :to_day, :num)",param)
        
        con.commit()
        cur.close()
        con.close()
        
    except Exception as err:
        logger.error(str(err))
        if cur:
            cur.close()
        
        if con:
            con.close()   
  
            
def getUserAndPasswd(url):
    if str('172.16.9.156') in url:
        return 'shenzq','123456'
    elif str('172.16.9.106') in url:
        return 'zhangleid','1qaz2wsx'
    else:
        return '',''

def executeAnalysis(url, username, passwd, startDate, endDate):
    try:
        svnmon = svn_monitor.SVNMonitor(url, username, passwd)
        ret = svnmon.svn_log(startDate, endDate)
        return ret.count('<logentry')
    except Exception,e:
        return 0

def submitResult(startDate, endDate, to_day):
    username = passwd = ''
    kbp_id = repos_url = ''
    num = 0
    repos_list = read_tb_ato_svn_repository()
    if repos_list:
        for repos_info in repos_list:
            kbp_id = repos_info['kpi_id']
	    repos_url = repos_info['repos_url']
            username ,passwd = getUserAndPasswd(repos_url)
	    if username and passwd:
		num =  executeAnalysis(repos_url, username, passwd, startDate, endDate)
		insertorupdate_tb_ato_svn_ver_monitor(kbp_id, num, to_day)    

if __name__ == '__main__':

    def Usage():
        print 'Usage1: python svnlog_log_author_date.py     #一直运行, 每天定时执行'
	print 'Usage1: python svnlog_log_author_date.py 2014-10-01    #采集某天的数据'
        print 'Usage2: python svnlog_log_author_date.py 2014-10-01 2014-10-31  #采集从开始日期2014-10-01到结束日期2014-10-31的结果'
    
    
    if len(sys.argv) not in [1,2,3]:
        Usage()
        sys.exit(0)
    
    if len(sys.argv) == 1:
        dt1 = dt2 = None
        startdateStr = enddateStr = timeStr = ''
        while 1:
            dt1 = datetime.now()
	    startdateStr = '%4d-%02d-%02d' % (dt1.year,dt1.month,dt1.day)
	    dt2 = dt1 + timedelta(1)
	    enddateStr = '%4d-%02d-%02d' % (dt2.year,dt2.month,dt2.day)
	    timeStr = '%02d:%02d:%02d' % (dt1.hour, dt1.minute, dt1.second)
	    
	    if timeStr > '23:00:00' and  timeStr < '23:59:59':
		print '~~~~~~~~~~start~~~~~~~~~~'
		submitResult(startdateStr, enddateStr, startdateStr)
		print '~~~~~~~~~~end~~~~~~~~~~'
		
            time.sleep(600)

    elif len(sys.argv) == 2:
        dt1 = dt2 = None
	startdateStr = enddateStr = ''
	
	dt1 =  datetime.strptime(sys.argv[1].strip(),'%Y-%m-%d')
	startdateStr =  '%4d-%02d-%02d' % (dt1.year,dt1.month,dt1.day)
	dt2 = dt1 + timedelta(1)
	
	enddateStr =  '%4d-%02d-%02d' % (dt2.year,dt2.month,dt2.day)
	print '~~~~~~~~~~start~~~~~~~~~~'
	submitResult(startdateStr, enddateStr, startdateStr)
	print '~~~~~~~~~~end~~~~~~~~~~'
	

    elif len(sys.argv) == 3:
	s1 = sys.argv[1].strip()
	s2 = sys.argv[2].strip()
	dt1 = datetime.strptime(s1,'%Y-%m-%d')
	delta = DateDelta(s1, s2)
	retList = [(x,x+1) for x in xrange(delta + 1)]
	dtList = [ ('%4d-%02d-%02d' % ((dt1 + timedelta(t[0])).year, (dt1 + timedelta(t[0])).month, (dt1 + timedelta(t[0])).day), '%4d-%02d-%02d' % ((dt1 + timedelta(t[1])).year, (dt1 + timedelta(t[1])).month, (dt1 + timedelta(t[1])).day))  for t in retList ]
	print '~~~~~~~~~~start~~~~~~~~~~'
	for dt in dtList:
            dateStr =  dt[0]
            enddateStr = dt[1]
	    submitResult(dateStr, enddateStr, dateStr)

        print '~~~~~~~~~~end~~~~~~~~~~'