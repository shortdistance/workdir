__author__ = 'Raychang'
# -*- coding:utf-8 -*-
DB_USER = 'dbquery'
DB_PASS = 'Jl_Crm6.0T'
DB_IP = '10.162.201.105'
DB_TNS = 'thradb'
DBLinkString = '%s/%s@%s/%s' % (DB_USER, DB_PASS, DB_IP, DB_TNS)
ROW_COUNT = 50000

sqlTemp = u"""
    SELECT distinct a.phone_no,a.cust_id,a.id_no FROM ur_user_info PARTITION(REG_PART_04) a,ur_userprc_info b,cs_userdetail_info c
    WHERE a.id_no = b.id_no
    and a.id_no = c.id_no
    and b.prod_prcid != '22CAZ01843'
    and c.run_code = 'A'
    and a.master_serv_id = '1001'
"""
filePathTemp = "d:/1.txt"

sql_sp_ZhuZiFei = u"""
    SELECT phone_no,cust_id,id_no FROM ur_user_info
"""


"""
主资费
phoneno,custid,idno,group_id

附加资费
phoneno,custid,idno,groupid

订购彩铃
phoneno

退订彩铃
phone_no,prodpricins_id
"""