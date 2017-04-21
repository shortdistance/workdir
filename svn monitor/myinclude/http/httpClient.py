#!/usr/bin/python
#-*- coding:utf-8 -*-

import httplib
import urllib
import json

def http_post(host, port, url, params, timeout=10):
    '''
        #HTTP POST json,eg:
        url = 'http://172.21.1.30:51900/esbWS/rest/SHPOCRouteTest'
        host, port, suburl = analyseUrl(url)
        params = """
        {"ROOT":{"HEADER":{"POOL_ID":"11","DB_ID":"","ENV_ID":"","CHANNEL_ID":"02","ROUTING":{"ROUTE_KEY":10,"ROUTE_VALUE":"15799881753"}},"BODY":{ "PHONE_NO":"","TEST":""}}}
        """
        statusCode, responseMsg = http_post(host, port, suburl, params, timeout=10)
        print statusCode
        print responseMsg
        #d1 = json.dumps(responseMsg,sort_keys=True,indent=4,ensure_ascii=False,separators=(',',':')) 
        #print d1 
    
    
        #HTTP POST soap,eg:
        url = 'http://172.21.0.30:51300/esbWS/services/pinReturn?wsdl'
        host,port,suburl = analyseUrl(url)
        params = """
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
                <SOAP-ENV:Body>
                        <m:callService xmlns:m="http://ws.sitech.com">
                                <m:pin><![CDATA[<?xml version="1.0" encoding="GBK"?> <ROOT><CHN_SOURCE type="string">16</CHN_SOURCE><END_RECORD type="string">12</END_RECORD><ESOP_PROVINCE type="string">10014</ESOP_PROVINCE><LOGIN_ACCEPT type="string">0</LOGIN_ACCEPT><LOGIN_NO type="string">aavg38</LOGIN_NO><LOGIN_PWD type="string">b81455f68e11ae78</LOGIN_PWD><OPER_TYPE type="string">1</OPER_TYPE><OP_CODE type="string"/><PB_NAME type="string"/><PB_NUMBER type="string"/><PHONE_NO type="string"/><START_RECORD type="string">0</START_RECORD><USER_PWD type="string"/><srvName type="string">s1052Qry</srvName></ROOT>]]></m:pin>
                        </m:callService>
                </SOAP-ENV:Body>
        </SOAP-ENV:Envelope>
    
        """
        statusCode, responseMsg = http_post(host, port, suburl, params, timeout=10) 
        print statusCode
        if 'UTF-8' in responseMsg:
            print responseMsg.decode('utf8')
    '''
    httpClient = None
    try:
        headers = {"Content-type":"application/json"}
        httpClient = httplib.HTTPConnection(host, int(port), timeout=10)
        httpClient.request('POST', url, params, headers)
        response = httpClient.getresponse()
        code = response.status
        msg = response.read()

    except Exception, e:
        code = -1
        msg = e.message
        
    finally:
        if httpClient:
            httpClient.close()
        return code, msg

def http_get(host, port, url, timeout=10):
    '''
        #HTTP GET
        eg:
        url = 'http://172.21.2.83:29080/dform/CRM6/page/nbase/login/crmlogin.html'
        host, port, suburl = analyseUrl(url)
        statusCode, responseMsg = http_get(host, port, suburl, timeout=10)    
        print statusCode
        print responseMsg
    '''
    httpClient = None
    code = -1
    msg = ''
    try:
        httpClient = httplib.HTTPConnection(str(host), int(port), timeout)
        httpClient.request('GET', url)
        response = httpClient.getresponse()
        code = response.status
        msg = response.read()

    except Exception,e:
        code = -1
        msg = e.message
        print msg
        
    finally:
        if httpClient:
            httpClient.close()
        return code, msg   

def analyseUrl(url):
    '''
    eg:
    url = 'http://172.21.1.30:51900/esbWS/rest/SHPOCRouteTest'
    host, port, suburl = analyseUrl(url)
    '''
    host = ''
    port = ''
    sub_url = ''
    host_port = url.split('://')[1].split('/')[0]
    if len(host_port.split(':')) ==2:
        host = host_port.split(':')[0]
        port = host_port.split(':')[1]
    else:
        host = host_port.split(':')[0]
        port = '80'
    
    sub_url_list = []
    sub_url_list = url.split('://')[1].split('/')[1:]
    sub_url = '/'+'/'.join(sub_url_list)
    
    return host, port, sub_url

    
if __name__ == '__main__':
    '''
    #HTTP GET
    url = 'http://192.168.1.103:11001/Comment/Create'
    host, port, suburl = analyseUrl(url)
    statusCode, responseMsg = http_get(host, port, suburl, timeout=10)    
    print statusCode
    print responseMsg    
    '''
    
    
    #pass
    #HTTP POST json报文
    url = 'http://20.26.19.36:10080/message'
    host, port, suburl = analyseUrl(url)
    
    params = 'topic=mk_simple_0&message=13454008077|13454008078|3|2015-02-26 11:36:32|2015-02-26 11:57:39|12|f1|1426810802530&key=17'
    statusCode, responseMsg = http_post(host, port, suburl, params, timeout=160)
    print statusCode
    print responseMsg   
    

    '''
    {"ROOT":{"HEADER":{"POOL_ID":"11","DB_ID":"","ENV_ID":"","CHANNEL_ID":"02","ROUTING":{"ROUTE_KEY":10,"ROUTE_VALUE":"15799881753"}},"BODY":{ "PHONE_NO":"","TEST":""}}}
    """
    statusCode, responseMsg = http_post(host, port, suburl, params, timeout=10)
    print statusCode
    print responseMsg
    #d1 = json.dumps(responseMsg,sort_keys=True,indent=4,ensure_ascii=False,separators=(',',':')) 
    #print d1    
    

    #HTTP GET
    url = 'http://172.21.2.83:29080/dform/CRM6/page/nbase/login/crmlogin.html'
    host, port, suburl = analyseUrl(url)
    statusCode, responseMsg = http_get(host, port, suburl, timeout=10)    
    print statusCode
    print responseMsg
    '''
    '''
    #HTTP POST soap报文
    url = 'http://172.21.0.30:51300/esbWS/services/pinReturn?wsdl'
    host,port,suburl = analyseUrl(url)
    params = """
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
            <SOAP-ENV:Body>
                    <m:callService xmlns:m="http://ws.sitech.com">
                            <m:pin><![CDATA[<?xml version="1.0" encoding="GBK"?> <ROOT><CHN_SOURCE type="string">16</CHN_SOURCE><END_RECORD type="string">12</END_RECORD><ESOP_PROVINCE type="string">10014</ESOP_PROVINCE><LOGIN_ACCEPT type="string">0</LOGIN_ACCEPT><LOGIN_NO type="string">aavg38</LOGIN_NO><LOGIN_PWD type="string">b81455f68e11ae78</LOGIN_PWD><OPER_TYPE type="string">1</OPER_TYPE><OP_CODE type="string"/><PB_NAME type="string"/><PB_NUMBER type="string"/><PHONE_NO type="string"/><START_RECORD type="string">0</START_RECORD><USER_PWD type="string"/><srvName type="string">s1052Qry</srvName></ROOT>]]></m:pin>
                    </m:callService>
            </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>

    """
    statusCode, responseMsg = http_post(host, port, suburl, params, timeout=10) 
    print statusCode
    if 'UTF-8' in responseMsg:
        print responseMsg.decode('utf8')
    else:
        print responseMsg
    '''