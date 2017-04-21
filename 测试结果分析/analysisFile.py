#-*- coding:utf-8 -*-

import os
import sys
import Queue
import time
import threading
import re

q=Queue.Queue()
THREAD_NUM = 5

count_0_5sec = 0
count_5_10sec = 0
count_10_15sec = 0
count_15_20sec = 0
count_20_25sec = 0
count_25_30sec = 0
count_30_35sec = 0
count_35_40sec = 0
count_40_45sec = 0
count_45_50sec = 0
count_50_55sec = 0
count_55_60sec = 0
count_60_65sec = 0
count_65_70sec = 0
count_70_75sec = 0
count_75_80sec = 0
count_80_85sec = 0
count_85_90sec = 0
count_90_95sec = 0
count_95_100sec = 0
count_100_200sec = 0
count_200_500sec = 0
count_500_1000sec = 0
count_lg_1000sec = 0

total = 0
totalfileLen = 0

SEPARATORList = ['----', '\t']
dest_SEPARATOR = '|'

#判断字符串是否有中文     
def has_chinese_charactar(content):     
    '''     python判断是否是中文需要满足u'[\u4e00-\u9fa5]+'，     
    需要注意如果正则表达式的模式中使用unicode，那么     
    要匹配的字符串也必须转换为unicode，否则肯定会不匹配。     
    '''    
    iconvcontent = unicode(content)     
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')     
    match = zhPattern.search(iconvcontent)     
    res = False    
    if match:         
        res = True    
    return res 


def IsSubString(SubStrList,Str):
    flag=False
    for substr in SubStrList:
        if substr in Str:
            flag=True
            return substr
    if flag == False:
        return ''

def GetFileList(FindPath):
    FileList = []
    if os.path.exists(FindPath):
        for f in os.listdir(FindPath):
            FileList.append(os.path.join(FindPath,f))
    else:
        return []

    if (len(FileList)>0):
        FileList.sort()
        return FileList

class ReadRule():
    def __init__(self, includingRuleFilePath, excludingRuleFilePath):
        self.includingRuleFilePath = includingRuleFilePath
        self.excludingRuleFilePath = excludingRuleFilePath
        self.includingRuleList = []
        self.excludingRuleList = []

    def readRuleFile(self):
        if type(self.includingRuleFilePath) != type(u'') or type(self.excludingRuleFilePath) != type(u''):
            print u'入参类型不正确!!'
            return

        if os.path.exists(self.includingRuleFilePath) == False or os.path.isfile(self.includingRuleFilePath) == False:
            print u'文件路径不存在或者不是文件!!'
            return

        if os.path.exists(self.excludingRuleFilePath) == False or os.path.isfile(self.excludingRuleFilePath) == False:
            print u'文件路径不存在或者不是文件!!'
            return

        for line in open(self.includingRuleFilePath):
            self.includingRuleList.append(line.strip('\n').lower())

        for line in open(self.excludingRuleFilePath):
            self.excludingRuleList.append(line.strip('\n').lower())


class FileList():
    def __init__(self, dataFileFolder):
        self.dataFileFolder = dataFileFolder
        self.fileList = []

    def getFilesListInFolder(self):
        if os.path.exists(self.dataFileFolder) == False or os.path.isdir(self.dataFileFolder) == False:
            return
        self.fileList = GetFileList(self.dataFileFolder)

    def putFileListIntoQueue(self):
        global q
        for filepath in self.fileList:
            q.put(filepath)
            print u'Init Queue:  %s' % filepath

class LogAnalyse():
    def __init__(self, filepath, inRuleList, exRuleList):
        self.filepath = filepath
        self.inRuleList = inRuleList
        self.exRuleList = exRuleList

    def analysisFileByRule(self):
        self.retList = []
        print u'开始处理文件%s' % self.filepath
        try:

            fp = open(self.filepath,'r')
            alllines=fp.readlines();
            fp.close()

            for eachline in alllines:
                SEPARATOR = IsSubString(SEPARATORList, eachline)
                if SEPARATOR:
                    tempList = eachline.split(SEPARATOR)
                    if IsSubString(self.inRuleList,tempList[0].lower()) != '' and IsSubString(self.exRuleList,tempList[0].lower()) == '' and len(tempList[-1])>6 and '@' in tempList[0] and '@' not in tempList[-1]:
                        self.retList.append(dest_SEPARATOR.join(tempList))
            filepathOk = '%s\\%s_OK.txt' % (os.path.dirname(self.filepath), os.path.basename(self.filepath).split('.')[0])
            f = open(filepathOk,'w')
            f.writelines(self.retList)
            f.close()

        except Exception,e:
            print u'处理出错： %s, 错误信息： %s' % (self.filepath,e)


class runLogAnalyse(threading.Thread):
    def __init__(self,i, inRuleList, exRuleList):
        threading.Thread.__init__(self,name="doLogAnalyse Thread-%d" % i)
        self.inRuleList = inRuleList
        self.exRuleList = exRuleList

    def run(self):
        global q

        while True:
            for i in range(5):
                if q.qsize() == 0:
                    return

                else:
                    filepath=q.get()
                    la = LogAnalyse(filepath, self.inRuleList, self.exRuleList)
                    la.analysisFileByRule()

def analysisLogFolder(file):
    
    global count_0_5sec
    global count_5_10sec
    global count_10_15sec
    global count_15_20sec
    global count_20_25sec
    global count_25_30sec
    global count_30_35sec
    global count_35_40sec
    global count_40_45sec
    global count_45_50sec
    global count_50_55sec
    global count_55_60sec
    global count_60_65sec
    global count_65_70sec
    global count_70_75sec
    global count_75_80sec
    global count_80_85sec
    global count_85_90sec
    global count_90_95sec
    global count_95_100sec
    global count_100_200sec
    global count_200_500sec
    global count_500_1000sec
    global count_lg_1000sec

    global total 
    global totalfileLen  
    
    singleTotal = 0
    filelen = 0    
    
    if os.path.exists(file) and str(file).find('worker')>0:
        try:
            fp = open(file,'r')
            for line in fp:
                lineline = line.rstrip('\n')
                if lineline.find('[INFO] all time:')>0:
                    sec = abs(int(lineline.split('ms')[0].split('all time:')[1]))
                    singleTotal = singleTotal + sec
                    filelen = filelen  + 1
                    
                    if 0 < sec <= 5:
                        count_0_5sec = count_0_5sec + 1
                    elif 5 < sec <= 10:
                        count_5_10sec = count_5_10sec + 1
                    elif 10 < sec <= 15:
                        count_10_15sec = count_10_15sec + 1
                    elif 15 < sec <= 20:
                        count_15_20sec = count_15_20sec + 1
                    elif 20 < sec <= 25:
                        count_20_25sec = count_20_25sec + 1
                    elif 25 < sec <= 30:
                        count_25_30sec = count_25_30sec + 1
                    elif 30 < sec <= 35:
                        count_30_35sec = count_30_35sec + 1
                    elif 35 < sec <= 40:
                        count_35_40sec = count_35_40sec + 1  
                    elif 40 < sec <= 45:
                        count_40_45sec = count_40_45sec + 1  
                    elif 45 < sec <= 50:
                        count_45_50sec = count_45_50sec + 1  
                    elif 50 < sec <= 55:
                        count_50_55sec = count_50_55sec + 1    
                    elif 55 < sec <= 60:
                        count_55_60sec = count_55_60sec + 1    
                    elif 60 < sec <= 65:
                        count_60_65sec = count_60_65sec + 1
                    elif 65 < sec <= 70:
                        count_65_70sec = count_65_70sec + 1      
                    elif 70 < sec <= 75:
                        count_70_75sec = count_70_75sec + 1      
                    elif 75 < sec <= 80:
                        count_75_80sec = count_75_80sec + 1  
                    elif 80 < sec <= 85:
                        count_80_85sec = count_80_85sec + 1  
                    elif 85 < sec <= 90:
                        count_85_90sec = count_85_90sec + 1  
                    elif 90 < sec <= 95:
                        count_90_95sec = count_90_95sec + 1
                    elif 95 < sec <= 100:
                        count_95_100sec = count_95_100sec + 1    
                    elif 100 < sec <= 200:
                        count_100_200sec = count_100_200sec + 1   
                    elif 200 < sec <= 500:
                        count_200_500sec = count_200_500sec + 1
                    elif 500 < sec <= 1000:
                        count_500_1000sec = count_500_1000sec + 1  
                    elif sec > 1000:
                        count_lg_1000sec = count_lg_1000sec + 1
                    
        except Exception,e:
            print u'%s error!' % file
    
    if filelen > 0 and singleTotal >0:
        total = total + singleTotal
        totalfileLen = totalfileLen + filelen


class runAnalysisLogFolder(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self,name="doLogAnalyse Thread-%d" % i)

    def run(self):
        global q

        while True:
            for i in range(5):
                if q.qsize() == 0:
                    return

                else:
                    filepath=q.get()
                    analysisLogFolder(filepath)
                    

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')

    def Usage():
        print 'Usage0: python analysisFile.py'  
    

    if len(sys.argv) != 1:
        Usage()
        sys.exit(0)
    
    
    #fileList = GetFileList('.')
    fileList = ['mylog.log']
    
    for file in fileList:
        analysisLogFolder(file)

    '''
    for filepath in fileList:
        q.put(filepath)
    
    threadList = []
    for i in range(THREAD_NUM):
        p=runAnalysisLogFolder(i)
        threadList.append(p)  
        p.start()
    
    for i in threadList:  
        i.join()  
    '''
    if totalfileLen > 0 and total > 0:
        print '----------------------------------------'
        print u'%d files, total %d records, total time:%d, avg time:%.2f' % (len(fileList), totalfileLen, total,  total/totalfileLen)
        print '----------------------------------------'
        print 'Group\tAvg Time\tPercent'
        print '[0~5]:%d\t\t\t[%.1f%%]'   % (count_0_5sec,   count_0_5sec*100/totalfileLen)
        print '[5~10]:%d\t\t[%.1f%%]'  % (count_5_10sec,  count_5_10sec*100/totalfileLen)
        print '[10~15]:%d\t\t[%.1f%%]' % (count_10_15sec, count_10_15sec*100/totalfileLen)
        print '[15~20]:%d\t\t[%.1f%%]' % (count_15_20sec, count_15_20sec*100/totalfileLen)
        print '[20~25]:%d\t\t[%.1f%%]' % (count_20_25sec, count_20_25sec*100/totalfileLen)
        print '[25~30]:%d\t\t[%.1f%%]' % (count_25_30sec, count_25_30sec*100/totalfileLen)
        print '[30~35]:%d\t\t[%.1f%%]' % (count_30_35sec, count_30_35sec*100/totalfileLen)
        print '[35~40]:%d\t\t[%.1f%%]' % (count_35_40sec, count_35_40sec*100/totalfileLen)
        print '[40~45]:%d\t\t[%.1f%%]' % (count_40_45sec, count_40_45sec*100/totalfileLen)
        print '[45~50]:%d\t\t[%.1f%%]' % (count_45_50sec, count_45_50sec*100/totalfileLen)
        print '[50~55]:%d\t\t[%.1f%%]' % (count_50_55sec, count_50_55sec*100/totalfileLen)
        print '[55~60]:%d\t\t[%.1f%%]' % (count_55_60sec, count_55_60sec*100/totalfileLen)
        print '[60~65]:%d\t\t[%.1f%%]' % (count_60_65sec, count_60_65sec*100/totalfileLen)
        print '[65~70]:%d\t\t[%.1f%%]' % (count_65_70sec, count_65_70sec*100/totalfileLen)
        print '[70~75]:%d\t\t[%.1f%%]' % (count_70_75sec, count_70_75sec*100/totalfileLen)
        print '[75~80]:%d\t\t[%.1f%%]' % (count_75_80sec, count_75_80sec*100/totalfileLen)
        print '[80~85]:%d\t\t[%.1f%%]' % (count_80_85sec, count_80_85sec*100/totalfileLen)
        print '[85~90]:%d\t\t[%.1f%%]' % (count_85_90sec, count_85_90sec*100/totalfileLen)
        print '[90~95]:%d\t\t[%.1f%%]' % (count_90_95sec, count_90_95sec*100/totalfileLen)
        print '[95~100]:%d\t\t[%.1f%%]' % (count_95_100sec, count_95_100sec*100/totalfileLen)
        print '[100~200]:%d\t\t[%.1f%%]' % (count_100_200sec, count_100_200sec*100/totalfileLen)
        print '[200~500]:%d\t\t[%.1f%%]' % (count_200_500sec, count_200_500sec*100/totalfileLen)
        print '[500~1000]:%d\t\t[%.1f%%]' % (count_500_1000sec, count_500_1000sec*100/totalfileLen)
        print    '[>1000]:%d\t\t[%.1f%%]' % ( count_lg_1000sec, count_lg_1000sec*100/totalfileLen)
        print 
    else:
        print u'has not records!!'
        