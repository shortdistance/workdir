#-*-coding:utf-8-*-
import os
import sys
import time


fileList = [
{'s':'/dmmdb/cdmdb1/shell/phonesim001.dat','d':'C:\\LR\\kaihu\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim002.dat','d':'C:\\LR\\kaihu-01\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim003.dat','d':'C:\\LR\\kaihu-02\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim004.dat','d':'C:\\LR\\kaihu-03\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim005.dat','d':'C:\\LR\\kaihu-04\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim006.dat','d':'C:\\LR\\kaihu-05\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim007.dat','d':'C:\\LR\\kaihu-06\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim008.dat','d':'C:\\LR\\kaihu-07\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim009.dat','d':'C:\\LR\\kaihu-08\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim010.dat','d':'C:\\LR\\kaihu-09\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim011.dat','d':'C:\\LR\\kaihu-10\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim012.dat','d':'C:\\LR\\kaihu-11\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim013.dat','d':'C:\\LR\\kaihu-12\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim014.dat','d':'C:\\LR\\kaihu-13\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim015.dat','d':'C:\\LR\\kaihu-14\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim016.dat','d':'C:\\LR\\kaihu-15\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim017.dat','d':'C:\\LR\\kaihu-16\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim018.dat','d':'C:\\LR\\kaihu-17\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim019.dat','d':'C:\\LR\\kaihu-18\\phoneNo.dat'},
{'s':'/dmmdb/cdmdb1/shell/phonesim020.dat','d':'C:\\LR\\kaihu-19\\phoneNo.dat'},

]

print u'~~~~~~~~~start~~~~~~~~~'
for f in fileList:
    os.system('pscp.exe -pw cdmdb1 cdmdb1@172.16.212.186:%s %s' % (f['s'], f['d']))
print u'~~~~~~~~~end~~~~~~~~~'
