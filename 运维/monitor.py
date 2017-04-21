#-*-coding:utf-8-*-
import psutil
import time
from datetime import datetime
import os

import socket  
import fcntl  
import struct 

def get_ip_address(ifname):  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    return socket.inet_ntoa(fcntl.ioctl(  
        s.fileno(),  
        0x8915, # SIOCGIFADDR  
        struct.pack('256s', ifname[:15])  
    )[20:24])  

def get_ip():
    eth_flag = os.popen('ifconfig -s|grep -v Iface|grep -v lo|awk \'{print $1}\'|head -1')
    ifname = eth_flag.readlines()[0].split('\n')[0]
    ip = get_ip_address(ifname)
    return ip

def get_cpu_count():
    
    return dict(logical_count=psutil.cpu_count(), count=psutil.cpu_count(logical=False))
    
def get_cpu_percent():
    
    cpu_times = psutil.cpu_times()
    u = cpu_times.user
    s = cpu_times.system
    i = cpu_times.idle            
    
    u_percent = 100 * u / (u + s + i ) 
    s_percent = 100 * s / (u + s + i ) 
    i_percent = 100 * i / (u + s + i ) 
    
    return dict(used='%.1f%%' % u_percent, sys='%.1f%%' % s_percent,  idle='%.1f%%' % i_percent)
    
def get_mem():
    mem = psutil.virtual_memory()
    
    return dict(total='%.1fM' % (mem.total/(1024*1024)), used='%.1f%%' % mem.percent)
    
    
def get_disk():
    
    disk = psutil.disk_partitions()
    diskinfo = []
    for sdiskpart in disk:
        mp = sdiskpart.mountpoint
        p_du = psutil.disk_usage(mp)
        diskinfo.append(dict(path=mp, total=round(p_du.total/(1024*1024*1024)), percent=p_du.percent))
    return diskinfo


def get_monitor_info():
    ip = get_ip()
    strdt = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    monitor_info = dict(datetime=strdt, ip=ip, cpu_info=get_cpu_percent(), mem_info=get_mem(), disk_info=get_disk())
    return monitor_info
    
    
if __name__ == '__main__':
    print get_monitor_info()