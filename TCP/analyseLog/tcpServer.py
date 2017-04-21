#!/usr/bin/env python
# -*-coding:gbk -*-
import socket
import subprocess
from config import *
import time


def getHostIP():
    p = subprocess.Popen('ifconfig', shell=True, stdout=subprocess.PIPE)
    (stdoutput, erroutput) = p.communicate()
    ipinfo = stdoutput

    ip = ''
    for row in ipinfo.split('\n'):
        if row.find('inet addr') >= 0 and row.find('127.0.0.1') == -1:
            ip = row.split(':')[1].split()[0]
            break
    return ip


# =================服务时间 ip:[10.161.250.24] pa[CRM6/page/npage/score/s1250/s1250main.html] s[com_sitech_score_atom_inter_IScoreParamAoSvc_queryScoreParamList] [59]
def analyseFile(line):
    if line.find(MonitorStr1) != -1 and line.find(MonitorStr2) != -1:
        Page = line.split(SplitStr1)[1].split(SplitStr2)[0]
        Srv = line.split(SplitStr2)[1].split(SplitStr3)[0]
        ResTime = line.split(SplitStr3)[1].split(SplitStr4)[0]
        if int(ResTime) > ResponseTime:
            return Page + '|' + Srv + '|' + ResTime + '\r\n'
    return None


def TCPServer():
    MyHost = getHostIP()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((MyHost, Port))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        file = open(LogFile, 'rb')
        while True:
            line = file.readline()

            if line:
                retInfo = analyseFile(line)
                if retInfo:
                    try:
                        conn.send(retInfo)
                    except Exception:
                        print 'client is disconnected!!'
                        break
            else:
                time.sleep(2)
        file.close()
        conn.close()


if __name__ == '__main__':
    TCPServer()
