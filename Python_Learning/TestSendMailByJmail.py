#-*- coding:utf-8 -*-
import jpype
import os


def sendattachmail ():
    
    msgto = '183800313@qq.com'
    msgfrom = 'testrobtheserver@sina.com'
    
    subject = '123123'
    body = 'hi, hello world'

    smtpserver = 'smtp.sina.com'     #smtp server
    smtpport = 25
    mailuser = 'testrobtheserver@sina.com'
    mailpwd = '87654321'
    jmailJar = '.\\jmail.jar'
    jpype.startJVM("%s/bin/client/jvm.dll"%(os.environ.get("JAVA_HOME")), "-ea","-Djava.class.path=%s" % jmailJar)
    JDClass = jpype.JClass("com.ykmaiz.mail.MailSupport")
    try:
        jd = jpype.JPackage("com.ykmaiz.mail").MailSupport(smtpserver, mailuser, mailpwd, False)
        jd.send(msgfrom, msgto, subject, body); 

    except Exception, e:
        print e
    jpype.shutdownJVM()  

if __name__ == '__main__':
    sendattachmail()



