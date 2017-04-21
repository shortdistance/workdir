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
    att = MIMEText(open(r'D:\\1.txt', 'rb').read(), 'base64', 'gb2312') #设置附件的目录
    att['content-type'] = 'application/octet-stream'
    att['content-disposition'] = 'attachment;filename="1.txt"' #设置附件的名称
    msg.attach(att)

    content = '附件请查收。' #正文内容
    body = MIMEText(content,'plain','GBK') #设置字符编码
    msg.attach(body)

    msgto = ['zhangleid@si-tech.com.cn; 183800313@qq.com'] # 收件人地址 多个联系人，格式是['aa@163.com'; 'bb@163.com']
    msgfrom = 'zhangleid@si-tech.com.cn' # 寄信人地址 ,
    msg['subject'] = 'IMD_EBM_'+CURRENTDAY  #主题
    msg['date']=time.ctime() #时间
    msg['Cc']='zhanglei520vip@163.com' #抄送人地址 多个地址不起作用


    mailuser = 'zhangleid@si-tech.com.cn'  #用户名
    mailpwd = '1qaz2wsx' #密码

    try:

        smtp = smtplib.SMTP()
        smtp.connect('smtp.si-tech.com.cn', 25)# smtp设置
        smtp.esmtp_features["auth"]="AUTH_PLAIN"        
        smtp.login(mailuser, mailpwd) #登录

        smtp.sendmail(msgfrom, msgto, msg.as_string()) #发送
        smtp.close()
    except Exception, e:
        print e
   

if __name__ == '__main__':
    sendattachmail()
