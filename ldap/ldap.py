#!/usr/bin/env python
# filename: ldap_cat.py

import os
import sys
import ldap

server = "ldap://mxserver.si-tech.com.cn:389"
admin = "cn=manager,dc=jan,dc=tech"
password = "jakjmax"

username_list = "/home/linyoujushi/usrname_list.txt"
try:
        conn = ldap.initialize(server)
        conn.protocol_version = ldap.VERSION3
        conn.simple_bind_s(admin,password)
        print 'ldap connect successfully'
except ldap.LDAPError, error_message:
        print error_message
        conn.unbind()

baseDN = "ou=Users,domainName=jan.tech,o=domains,dc=jan,dc=tech"
searchScope = ldap.SCOPE_SUBTREE

retrieveAttributes = None
searchFilter = "uid=*"

try:
        ldap_result_id = conn.search(baseDN,searchScope,searchFilter,retrieveAttributes)
        result_set = []
        data = ''
        while 1:
                result_type,result_data = conn.result(ldap_result_id, 0)
                if result_data == []:
                        break
                else:
                        if result_type == ldap.RES_SEARCH_ENTRY:
                                r_a,r_b = result_data[0]
                                #print r_a
                                #print r_b['uid'][0], r_b['cn'][0].decode('utf-8')
                                username = '%s [%s]\n' % (r_b['uid'][0],r_b['cn'][0])
                                data = data + username
        print data
        fp = open("username_list.txt",'w')
        fp.write(data)
        fp.close()


except ldap.LDAPError, error_message:
        print error_message