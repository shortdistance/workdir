# -*- coding: cp936 -*-

import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
import datetime
import time


TODAY = datetime.date.today()
CURRENTDAY=TODAY.strftime('%Y%m%d')
def sendattachmail ():
    msg = MIMEMultipart()
    att = MIMEText(open(r'D:\\1.txt', 'rb').read(), 'base64', 'gb2312') #���ø�����Ŀ¼
    att['content-type'] = 'application/octet-stream'
    att['content-disposition'] = 'attachment;filename="1.txt"' #���ø���������
    msg.attach(att)

    content = '��������ա�' #��������
    body = MIMEText(content,'plain','GBK') #�����ַ�����
    msg.attach(body)

    msgto = ['zhangleid@si-tech.com.cn; 183800313@qq.com'] # �ռ��˵�ַ �����ϵ�ˣ���ʽ��['aa@163.com'; 'bb@163.com']
    msgfrom = 'zhangleid@si-tech.com.cn' # �����˵�ַ ,
    msg['subject'] = 'IMD_EBM_'+CURRENTDAY  #����
    msg['date']=time.ctime() #ʱ��
    msg['Cc']='zhanglei520vip@163.com' #�����˵�ַ �����ַ��������


    mailuser = 'zhangleid@si-tech.com.cn'  #�û���
    mailpwd = '1qaz2wsx' #����

    try:

        smtp = smtplib.SMTP()
        smtp.connect('smtp.si-tech.com.cn', 25)# smtp����
        smtp.esmtp_features["auth"]="AUTH_PLAIN"        
        smtp.login(mailuser, mailpwd) #��¼

        smtp.sendmail(msgfrom, msgto, msg.as_string()) #����
        smtp.close()
    except Exception, e:
        print e
   

if __name__ == '__main__':
    sendattachmail()
