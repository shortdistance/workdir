# -*- coding: GBK -*-
# filename: multiprocessreadfile.py

import datetime
import os
import multiprocessing
# from multiprocessing import Process, Queue, Array, RLock
from config import *

"""
����̷ֿ��ȡ�ļ�
"""

WORKERS = 4
BLOCKSIZE = 100000000  # �ֽڣ��ӽ�100MB
FILE_SIZE = 0
Summary = {}


def getFilesize(file):
    """
        ��ȡҪ��ȡ�ļ��Ĵ�С
    """
    global FILE_SIZE
    fstream = open(file, 'r')
    fstream.seek(0, os.SEEK_END)
    FILE_SIZE = fstream.tell()
    fstream.close()


# =================����ʱ�� ip:[10.161.253.145] pa[CRM6/page/nbase/login/crmlogin.html] s[com_sitech_basemng_atom_inter_login_ILoginCheckSvc_loginCheck] [165]
def analyseLine(line):
    global Summary
    if line.find(QryArr['MonitorStr1']) != -1 and line.find(QryArr['MonitorStr2']) != -1:
        Page = line.split(QryArr['SplitStr1'])[1].split(QryArr['SplitStr2'])[0]
        Srv = line.split(QryArr['SplitStr2'])[1].split(QryArr['SplitStr3'])[0]
        ResTime = line.split(QryArr['SplitStr3'])[1].split(QryArr['SplitStr4'])[0]
        SrvType = Page + '|' + Srv
        if Summary.has_key(SrvType):
            Summary[SrvType]['SrvCount'] += 1
            Summary[SrvType]['TotalTime'] += int(ResTime)
            Summary[SrvType]['AvgTime'] = int(
                float(Summary[SrvType]['TotalTime']) / float(Summary[SrvType]['SrvCount']))
            if int(ResTime) > Summary[SrvType]['MaxTime']:
                Summary[SrvType]['MaxTime'] = int(ResTime)
        else:
            Summary[SrvType] = {}
            Summary[SrvType]['SrvCount'] = 1
            Summary[SrvType]['TotalTime'] = int(ResTime)
            Summary[SrvType]['AvgTime'] = int(ResTime)
            Summary[SrvType]['MaxTime'] = int(ResTime)


def printAnalyseRes():
    global Summary
    for key in Summary:
        if Summary[key]['SrvCount'] > 100 and Summary[key]['AvgTime'] > 500:
            print key + ', ���ô�����' + str(Summary[key]['SrvCount']) + ', ƽ����Ӧʱ�䣺' + str(
                Summary[key]['AvgTime']) + ', �����Ӧʱ�䣺' + str(
                Summary[key]['MaxTime'])


def process_found(pid, array, file, rlock, rlock1):
    global FILE_SIZE
    global JOB
    global PREFIX
    """
        ���̴���
        Args:
            pid:���̱��
            array:���̼乲����У����ڱ�Ǹ������������ļ������λ��
            file:�����ļ�����
        ���������ȴ�array�л�ȡ��ǰ����ֵΪ��ʼλ��startpossition
        ������λ��endpossition (startpossition+BLOCKSIZE) if (startpossition+BLOCKSIZE)<FILE_SIZE else FILE_SIZE
        if startpossition==FILE_SIZE����̽���
        if startpossition==0���0��ʼ��ȡ
        if startpossition!=0Ϊ��ֹ�б�block�ضϵ�������ȶ�һ�в���������һ�п�ʼ��ʽ����
        if ��ǰλ�� <=endpossition ��readline
        ����Խ���߽磬�ʹ��²���array�е����ֵ
    """
    getFilesize(file)
    fstream = open(file, 'r')
    while True:
        rlock.acquire()
        startpossition = max(array)
        endpossition = array[pid] = (startpossition + BLOCKSIZE) if (
                                                                        startpossition + BLOCKSIZE) < FILE_SIZE else FILE_SIZE
        print 'pid%s' % pid, ','.join([str(v) for v in array])
        rlock.release()

        if startpossition == FILE_SIZE:  # end of the file
            print '===============pid%s end===============' % (pid)
            printAnalyseRes()
            break
        elif startpossition != 0:
            fstream.seek(startpossition)
            fstream.readline()
        pos = ss = fstream.tell()

        # ostream = open('d:/tmp_pid%s_jobs%s' % (str(pid), str(endpossition)), 'w')
        while pos < endpossition:
            # ����line
            line = fstream.readline()
            rlock1.acquire()
            analyseLine(line)
            rlock1.release()
            # ostream.write(line)
            pos = fstream.tell()

        # ostream.flush()
        # ostream.close()
        ee = fstream.tell()
    fstream.close()


def main():
    global FILE_SIZE

    print datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S")
    file = LogFile
    getFilesize(file)
    print FILE_SIZE

    rlock = multiprocessing.RLock()
    rlock1 = multiprocessing.RLock()
    array = multiprocessing.Array('l', WORKERS, lock=rlock)

    threads = []
    for i in range(WORKERS):
        p = multiprocessing.Process(target=process_found, args=[i, array, file, rlock, rlock1])
        threads.append(p)

    for i in range(WORKERS):
        threads[i].start()

    for i in range(WORKERS):
        threads[i].join()

    print datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S")


if __name__ == '__main__':
    main()
