# -*-coding:utf-8 -*-
__author__ = 'Raychang'
from config import *

Summary = {}

def analyseMonitorLog():
    file = open(LocalFile, 'r')
    while 1:
        line = file.readline()
        if not line:
            break
        analyseLine(line)

def analyseLine(line):
    SrvType = '|'.join(line.split('|')[:-1])
    ResTime = line.split('|')[-1]
    if Summary.has_key(SrvType):
        Summary[SrvType]['SrvCount'] += 1
        Summary[SrvType]['TotalTime'] += int(ResTime)
        Summary[SrvType]['AvgTime'] = int(float(Summary[SrvType]['TotalTime']) / float(Summary[SrvType]['SrvCount']))
        if int(ResTime) > Summary[SrvType]['MaxTime']:
            Summary[SrvType]['MaxTime'] = int(ResTime)
    else:
        Summary[SrvType] = {}
        Summary[SrvType]['SrvCount'] = 1
        Summary[SrvType]['TotalTime'] = int(ResTime)
        Summary[SrvType]['AvgTime'] = int(ResTime)
        Summary[SrvType]['MaxTime'] = int(ResTime)


def analyseRawFile(line):
    pass

if __name__ == '__main__':
    analyseMonitorLog()

    for key in Summary:
        print key + '|' + str(Summary[key]['SrvCount']) + '|' + str(Summary[key]['AvgTime']) + '|' + str(
            Summary[key]['MaxTime']) + ' \r\n'
