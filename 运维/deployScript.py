#-*- coding:utf-8 -*-
import pysftp
import sys
import time
import os

'''
'10.112.103.101|root|123456|22',
'''
hosts = [ 
    '172.16.9.105|root|1qaz2wsx|22',
]

def conn_host():
    serv_list = []
    for host_info in hosts:
        srv = None
        host = host_info.split('|')[0]
        user = host_info.split('|')[1]
        passwd = host_info.split('|')[2]
        port = int(host_info.split('|')[3])
        try:
            srv = pysftp.Connection(host=host, 
                                username=user,
                                password=passwd,
                                port = port)
            
            serv_list.append(dict(ip=host, srv=srv))
        
        except:
            print '%s conn error!!' % host
            
    return serv_list


def disconn_host(serv_list):
    for srv in serv_list:
        srv['srv'].close()
        

def deploy_script(serv_list, localfile, remotepath='/opt'):
    for srv in serv_list:
        filename = os.path.split(localfile)[-1]
        try:
            srv['srv'].put(localfile, '%s/%s' % (remotepath, filename))
            srv['remotepath']= '%s/%s' % (remotepath, filename)
            print '%s|%s|%s|deploy success!!' % (srv['ip'], localfile, remotepath)
        except:
            print '%s|%s|%s|deploy fail!!' % (srv['ip'], localfile, remotepath)

def execute_cmd(serv_list, cmd):
    for srv in serv_list:
        retList = srv['srv'].execute('. ~/.bash_profile; %s' % cmd)
        for ret in retList:
            print ret
    
    
def start_script(serv_list):
    for srv in serv_list:
        srv['srv'].execute('')

if __name__ == '__main__':
    serv_list = conn_host()
    #deploy_script(serv_list, 'monitor.py', '/harvest_backup')
    deploy_script(serv_list, 'Python-2.7.4.tar.bz2', '/harvest_backup')
    execute_cmd(serv_list, 'cd /harvest_backup; bzip2 -d Python-2.7.4.tar.bz2')
    #需要手动安装python
    
    
    #deploy_script(serv_list, 'hashlib-20081119.zip', '/harvest_backup') 
    #execute_cmd(serv_list, 'cd /harvest_backup; unzip -o hashlib-20081119.zip')
    #需要手动安装setuptools
    
    
    #deploy_script(serv_list, 'pysqlite-2.6.3.tar.gz', '/harvest_backup')
    #execute_cmd(serv_list, 'cd /harvest_backup; tar zxvf pysqlite-2.6.3.tar.gz')
    #execute_cmd(serv_list, 'cd /opt/psutil-1.2.1; python setup.py install')
    
    '''
    deploy_script(serv_list, 'pika-0.9.14.tar.gz', '/opt')
    execute_cmd(serv_list, 'cd /opt; tar zxvf pika-0.9.14.tar.gz')
    execute_cmd(serv_list, 'cd /opt/pika-0.9.14; python setup.py install')
    disconn_host(serv_list)
    '''