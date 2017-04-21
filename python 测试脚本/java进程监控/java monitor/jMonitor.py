__author__ = 'Raychang'
#-*- coding:utf-8 -*-
import subprocess

javaTaget = [
    'dform|weblogic|java|10110',
    'dform|weblogic|java|10120',
    'dform|weblogic|java|10130',
    'dform|weblogic|java|10140',
]
pidList = []

def getJavaPID():
    cmdStr = ''
    pid = ''
    dic = {}
    for jT in javaTaget:
        cmdStr = 'ps -ef|grep -v grep'
        pid = ''
        dic = {}
        for c in jT.split('|'):
            cmdStr = cmdStr + '|grep %s' % c
        cmdStr = cmdStr + "|awk \'{print $2}\'"
        #print cmdStr
        p = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE)
        pid = p.stdout.readlines()
        if pid:
            dic['index'] = jT
            dic['pid'] = pid[0].split('\n')[0]
            pidList.append(dic)
        else:
            print '[',jT,'] pid not exists!'

def getJavaMap():
    cmdStr = ''
    for piddict in pidList:
        cmdStr = 'jmap -histo:live %s|head ' % piddict['pid']
        print '[',piddict['index'],']', cmdStr
        p = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE)
        for ret in p.stdout.readlines():
            print ret

def getJavaGC():
    cmdStr = ''
    for piddict in pidList:
        cmdStr = 'jstat -gcutil %s ' % piddict['pid']
        print '[',piddict['index'],']', cmdStr
        p = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE)
        for ret in p.stdout.readlines():
            print ret

if __name__ == '__main__':
    getJavaPID()
    if pidList:
        print u'-------get map info-------'
        getJavaMap()
        print u'-------get gc info-------'
        getJavaGC()



