#-*- coding:utf-8 -*-
import pysftp
import sys
import time


Hadoop_NameNode ={
    'Host':'10.112.103.101',
    'Port': 22,
    'User':'root',
    'Passwd':'123456', 
    'JAVA_HOME':'/e3base/jdk1.7',
    'HADOOP_HOME':'/e3base/hadoop'
}


def Conn_Hadoop():
    try:
        host = Hadoop_NameNode['Host']
        user = Hadoop_NameNode['User']
        passwd = Hadoop_NameNode['Passwd']
        port = int(Hadoop_NameNode['Port'])
        srv = pysftp.Connection(host=host, 
                            username=user,
                            password=passwd,
                            port = port)
        
        return srv
    except:
        return None


def Disconn_Hadoop(srv):
    if srv:
        srv.close()
        

def getHadoopExampleJar(srv):
    ret = srv.execute('cd %s;find . -name hadoop-examples*.jar' % Hadoop_NameNode['HADOOP_HOME'])
    if ret:
        hadoopTestJar = '%s/%s' % (Hadoop_NameNode['HADOOP_HOME'],ret[0].split('\n')[0])
        srv.execute('chmod 755 %s' % hadoopTestJar)
        return hadoopTestJar
    else:
        return None

def getHadoopTestJar(srv):
    ret = srv.execute('cd %s;find . -name hadoop-test*.jar' % Hadoop_NameNode['HADOOP_HOME'])
    if ret:
        hadoopTestJar = '%s/%s' % (Hadoop_NameNode['HADOOP_HOME'],ret[0].split('\n')[0])
        srv.execute('chmod 755 %s' % hadoopTestJar)
        return hadoopTestJar
    else:
        return None    

def hadoop_teragen(srv, hadoopTestJar, rowcount):
    srv.execute('. ~/.bash_profile; %s/bin/hadoop dfsadmin -safemode leave; %s/bin/hadoop fs -rmdir terasort/1T-input' % (Hadoop_NameNode['HADOOP_HOME'],Hadoop_NameNode['HADOOP_HOME']))
    srv.execute('. ~/.bash_profile; %s/bin/hadoop dfsadmin -safemode leave; %s/bin/hadoop jar %s teragen -Dmapred.map.tasks=100 %d terasort/1T-input' % (Hadoop_NameNode['HADOOP_HOME'],Hadoop_NameNode['HADOOP_HOME'],hadoopTestJar, rowcount))
    retList = srv.execute('. ~/.bash_profile; %s/bin/hadoop fs -ls terasort/1T-input' % Hadoop_NameNode['HADOOP_HOME'])
    for ret in retList:
        print ret
    
def hadoop_terasort(srv, hadoopTestJar):
    srv.execute('. ~/.bash_profile; %s/bin/hadoop jar %s terasort -Dmapred.reduce.tasks=50 terasort/1T-input terasort/1T-output' % (Hadoop_NameNode['HADOOP_HOME'],hadoopTestJar))
    retList = srv.execute('. ~/.bash_profile; %s/bin/hadoop fs -ls terasort/1T-output' % Hadoop_NameNode['HADOOP_HOME'])
    for ret in retList:
        print ret
    
def hadoop_teravalidate(srv, hadoopTestJar):
    srv.execute('. ~/.bash_profile; %s/bin/hadoop jar %s teravalidate terasort/1T-output terasort/1T-validate' % (Hadoop_NameNode['HADOOP_HOME'],hadoopTestJar))
    retList = srv.execute('. ~/.bash_profile; %s/bin/hadoop fs -ls terasort/1T-validate' % Hadoop_NameNode['HADOOP_HOME'])
    for ret in retList:
        print ret 
    
    retList = srv.execute('. ~/.bash_profile; %s/bin/hadoop fs -cat terasort/1T-validate/part-r-*' % Hadoop_NameNode['HADOOP_HOME'])
    for ret in retList:
        print ret 
    
def hadoop_wordcount(srv, hadoopTestJar):
    srv.execute('cd ~; echo "hello world">file1.txt; echo "hello hadoop">file2.txt')
    srv.execute('. ~/.bash_profile; %s/bin/hadoop fs -mkdir input; %s/bin/hadoop fs -rm -r -f output' % (Hadoop_NameNode['HADOOP_HOME'],Hadoop_NameNode['HADOOP_HOME']))    
    srv.execute('. ~/.bash_profile; %s/bin/hadoop fs -put ~/file*.txt input' % Hadoop_NameNode['HADOOP_HOME'])
    retList = srv.execute('. ~/.bash_profile; %s/bin/hadoop jar %s wordcount  -Dmapred.map.tasks=50 -Dmapred.reduce.tasks=50 input output' % (Hadoop_NameNode['HADOOP_HOME'], hadoopTestJar))
    for ret in retList:
        print ret     
    
    retList = srv.execute('. ~/.bash_profile; %s/bin/hadoop fs -cat output/*' % Hadoop_NameNode['HADOOP_HOME'])
    for ret in retList:
        print ret 

def hadoop_dfsio(srv, hadoopTestJar, filecount=1, filesize=512, buffersize=1024000):    
    retList = srv.execute('. ~/.bash_profile; %s/bin/hadoop jar %s TestDFSIO -Dmapred.map.tasks=50 -Dmapred.reduce.tasks=50 -write -nrFiles %d -size %dB -bufferSize %d' % (Hadoop_NameNode['HADOOP_HOME'], hadoopTestJar, filecount, filesize, buffersize))
    for ret in retList:
        print ret      
        
if __name__ == '__main__':
    srv = Conn_Hadoop()
    if not srv:
        print u'cant connect to hadoop host!!'
        sys.exit(0)     
        
    hadoopExampleJar = getHadoopExampleJar(srv)
    hadoopTestJar = getHadoopTestJar(srv)
    if not hadoopExampleJar:
        print u'cant find hadoop Example jar!!'
        sys.exit(0)

    if not hadoopTestJar:
        print u'cant find hadoop Test jar!!'
        sys.exit(0)        

    hadoop_teragen(srv, hadoopExampleJar, 3000)
    hadoop_terasort(srv, hadoopExampleJar)
    hadoop_teravalidate(srv, hadoopExampleJar)
    
    
    #hadoop_wordcount(srv, hadoopExampleJar)
    
    #hadoop_dfsio(srv, hadoopTestJar)
    
    Disconn_Hadoop(srv)