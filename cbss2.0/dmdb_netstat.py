#-*- coding:utf-8 -*-
import pysftp
import sys
import time

#host, user, passwd, port
hosts = [ 


    '172.16.212.29|crmappa|crmappa|26622',
    '172.16.212.30|crmappa|crmappa|26622',
    '172.16.212.31|crmappa|crmappa|26622',
    '172.16.212.32|crmappa|crmappa|26622',
    '172.16.212.33|crmappa|crmappa|26622',
    '172.16.212.34|crmappa|crmappa|26622',
    '172.16.212.35|crmappa|crmappa|26622',
    '172.16.212.36|crmappa|crmappa|26622',
    '172.16.212.37|crmappa|crmappa|26622',
    '172.16.212.38|crmappa|crmappa|26622',
    '172.16.212.39|crmappa|crmappa|26622',
    '172.16.212.40|crmappa|crmappa|26622',
    '172.16.212.41|crmappa|crmappa|26622',
    '172.16.212.42|crmappa|crmappa|26622',
    '172.16.212.43|crmappa|crmappa|26622',
    '172.16.212.44|crmappa|crmappa|26622',
    '172.16.212.45|crmappa|crmappa|26622',
    '172.16.212.46|crmappa|crmappa|26622',
    '172.16.212.47|crmappa|crmappa|26622',
    '172.16.212.48|crmappa|crmappa|26622',
    '172.16.212.49|crmappa|crmappa|26622',
    '172.16.212.50|crmappa|crmappa|26622',
    '172.16.212.51|crmappa|crmappa|26622',
    '172.16.212.52|crmappa|crmappa|26622',
    '172.16.212.53|crmappa|crmappa|26622',
    '172.16.212.54|crmappa|crmappa|26622',
    '172.16.212.55|crmappa|crmappa|26622',
    '172.16.212.56|crmappa|crmappa|26622',
    '172.16.212.57|crmappa|crmappa|26622',
    '172.16.212.58|crmappa|crmappa|26622',
    '172.16.212.59|crmappa|crmappa|26622',
    '172.16.212.60|crmappa|crmappa|26622',
    '172.16.212.61|crmappa|crmappa|26622',
    '172.16.212.62|crmappa|crmappa|26622',
    '172.16.212.63|crmappa|crmappa|26622',
    '172.16.212.64|crmappa|crmappa|26622',
    '172.16.212.65|crmappa|crmappa|26622',
    '172.16.212.66|crmappa|crmappa|26622',
    '172.16.212.67|crmappa|crmappa|26622',
    '172.16.212.68|crmappa|crmappa|26622',

    '172.16.212.69|crmappa|crmappa|26622',
    '172.16.212.70|crmappa|crmappa|26622',
    '172.16.212.71|crmappa|crmappa|26622',
    '172.16.212.72|crmappa|crmappa|26622',
    '172.16.212.73|crmappa|crmappa|26622',
    '172.16.212.74|crmappa|crmappa|26622',
    '172.16.212.75|crmappa|crmappa|26622',
    '172.16.212.76|crmappa|crmappa|26622',
    '172.16.212.77|crmappa|crmappa|26622',

    '172.16.212.78|crmappa|crmappa|26622',
    '172.16.212.79|crmappa|crmappa|26622',
    '172.16.212.80|crmappa|crmappa|26622',
    '172.16.212.81|crmappa|crmappa|26622',
    '172.16.212.82|crmappa|crmappa|26622',
    '172.16.212.83|crmappa|crmappa|26622',
    '172.16.212.84|crmappa|crmappa|26622',
    '172.16.212.85|crmappa|crmappa|26622',
    '172.16.212.86|crmappa|crmappa|26622',
    

    '172.16.212.87|crmappa|crmappa|26622',
    '172.16.212.88|crmappa|crmappa|26622',
    '172.16.212.89|crmappa|crmappa|26622',
    '172.16.212.90|crmappa|crmappa|26622',
    '172.16.212.91|crmappa|crmappa|26622',
    '172.16.212.92|crmappa|crmappa|26622',
    '172.16.212.93|crmappa|crmappa|26622',
    '172.16.212.94|crmappa|crmappa|26622',
    '172.16.212.95|crmappa|crmappa|26622',
    
    '172.16.212.96|crmappa|crmappa|26622',
    '172.16.212.97|crmappa|crmappa|26622',
    '172.16.212.98|crmappa|crmappa|26622',
    '172.16.212.99|crmappa|crmappa|26622',
    '172.16.212.100|crmappa|crmappa|26622',
    '172.16.212.101|crmappa|crmappa|26622',
    '172.16.212.102|crmappa|crmappa|26622',
    '172.16.212.103|crmappa|crmappa|26622',
    '172.16.212.104|crmappa|crmappa|26622',
    
    '172.16.212.105|crmappa|crmappa|26622',
    '172.16.212.106|crmappa|crmappa|26622',
    '172.16.212.107|crmappa|crmappa|26622',
    '172.16.212.108|crmappa|crmappa|26622',
    '172.16.212.109|crmappa|crmappa|26622',
    '172.16.212.110|crmappa|crmappa|26622',
    '172.16.212.111|crmappa|crmappa|26622',
    '172.16.212.112|crmappa|crmappa|26622',
    '172.16.212.113|crmappa|crmappa|26622',

    '172.16.212.114|crmappa|crmappa|26622',
    '172.16.212.115|crmappa|crmappa|26622',
    '172.16.212.116|crmappa|crmappa|26622',
    '172.16.212.117|crmappa|crmappa|26622',

    '172.16.212.118|crmappa|crmappa|26622',
    '172.16.212.119|crmappa|crmappa|26622',
    '172.16.212.120|crmappa|crmappa|26622',
    '172.16.212.121|crmappa|crmappa|26622',

    '172.16.212.122|crmappa|crmappa|26622',
    '172.16.212.123|crmappa|crmappa|26622',
    '172.16.212.124|crmappa|crmappa|26622',
    '172.16.212.125|crmappa|crmappa|26622',
 
    '172.16.212.126|crmappa|crmappa|26622',
    '172.16.212.127|crmappa|crmappa|26622',
    '172.16.212.128|crmappa|crmappa|26622',
    '172.16.212.129|crmappa|crmappa|26622',

 
    '172.16.212.130|crmappa|crmappa|26622',
    '172.16.212.131|crmappa|crmappa|26622',
    '172.16.212.132|crmappa|crmappa|26622',
    '172.16.212.133|crmappa|crmappa|26622',

 
    '172.16.212.134|crmappa|crmappa|26622',
    '172.16.212.135|crmappa|crmappa|26622',
    '172.16.212.136|crmappa|crmappa|26622',
    '172.16.212.137|crmappa|crmappa|26622',

 
    '172.16.212.138|crmappa|crmappa|26622',
    '172.16.212.139|crmappa|crmappa|26622',
    '172.16.212.140|crmappa|crmappa|26622',
    '172.16.212.141|crmappa|crmappa|26622',

    '172.16.212.142|crmappa|crmappa|26622',
    '172.16.212.143|crmappa|crmappa|26622',
    '172.16.212.144|crmappa|crmappa|26622',
    '172.16.212.145|crmappa|crmappa|26622',
    '172.16.212.146|crmappa|crmappa|26622',
    '172.16.212.147|crmappa|crmappa|26622',
        

    '172.16.212.148|crmappa|crmappa|26622',
    '172.16.212.149|crmappa|crmappa|26622',
    '172.16.212.150|crmappa|crmappa|26622',
    '172.16.212.151|crmappa|crmappa|26622',
    '172.16.212.152|crmappa|crmappa|26622',
    '172.16.212.153|crmappa|crmappa|26622',
    '172.16.212.154|crmappa|crmappa|26622',
    '172.16.212.155|crmappa|crmappa|26622',
    '172.16.212.156|crmappa|crmappa|26622',
    '172.16.212.157|crmappa|crmappa|26622',
    '172.16.212.158|crmappa|crmappa|26622',
    '172.16.212.159|crmappa|crmappa|26622',
    '172.16.212.160|crmappa|crmappa|26622',
    '172.16.212.161|crmappa|crmappa|26622',
    '172.16.212.162|crmappa|crmappa|26622',
    '172.16.212.163|crmappa|crmappa|26622',
    '172.16.212.164|crmappa|crmappa|26622',
    '172.16.212.165|crmappa|crmappa|26622',
    '172.16.212.166|crmappa|crmappa|26622',
    '172.16.212.167|crmappa|crmappa|26622',
    '172.16.212.168|crmappa|crmappa|26622',
    '172.16.212.169|crmappa|crmappa|26622',
    '172.16.212.170|crmappa|crmappa|26622',
    '172.16.212.171|crmappa|crmappa|26622',
    '172.16.212.172|crmappa|crmappa|26622',
    '172.16.212.173|crmappa|crmappa|26622',
    '172.16.212.174|crmappa|crmappa|26622',
    '172.16.212.175|crmappa|crmappa|26622',
    '172.16.212.176|crmappa|crmappa|26622',
    '172.16.212.177|crmappa|crmappa|26622',

]

if __name__ == '__main__':
    
    srv_list = []    
    for host_info in hosts:
        print host_info
        host = host_info.split('|')[0]
        user = host_info.split('|')[1]
        passwd = host_info.split('|')[2]
        port = int(host_info.split('|')[3])
        srv = pysftp.Connection(host=host, 
                            username=user,
                            password=passwd,
                            port = port) 
        srv_list.append(dict(srv=srv, host=host))
    
    print srv_list        
    
    while 1:
        
        for srv in srv_list:
            
            idel_cpu = srv['srv'].execute('vmstat 2 2|tail -1')[0].split('\n')[0].split()[14]
            free_mem = srv['srv'].execute('free|grep "buffers/cache"')[0].split('\n')[0].split()[-1]
            
            if int(idel_cpu) < 30:
                print 'Host:%s\t free_mem:%.2fg\tidel_cpu:%s%%     BUSY!!BUSY!!' % (srv['host'], float(free_mem)/1024/1024, idel_cpu)
            else:
                print 'Host:%s\t free_mem:%.2fg\tidel_cpu:%s%%' % (srv['host'], float(free_mem)/1024/1024, idel_cpu)
            
        print 
        time.sleep(10)
        
    for srv in srv_list:
        srv['srv'].close()
