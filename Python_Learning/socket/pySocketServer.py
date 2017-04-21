#coding=utf8

from ftplib import FTP

ftp_user = 'developer'
ftp_passwd = '123456'
ftp = FTP('172.16.9.144')
ftp.login(ftp_user,ftp_passwd)
ls_path = ftp.nlst()
print ls_path
ftp.quit()
