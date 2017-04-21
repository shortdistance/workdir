#-*- coding:utf-8-*-
import pycurl
import StringIO
import urllib


def PostData(url, post_data):
    crl = pycurl.Curl()
    crl.setopt(pycurl.VERBOSE,1)
    crl.setopt(pycurl.FOLLOWLOCATION, 1)
    crl.setopt(pycurl.MAXREDIRS, 5)
    crl.setopt(pycurl.AUTOREFERER,1)

    crl.setopt(pycurl.CONNECTTIMEOUT, 60)
    crl.setopt(pycurl.TIMEOUT, 300)
    #crl.setopt(pycurl.PROXY,proxy)
    crl.setopt(pycurl.HTTPPROXYTUNNEL,1)
    #crl.setopt(pycurl.NOSIGNAL, 1)
    crl.fp = StringIO.StringIO()
    crl.setopt(pycurl.USERAGENT,"testing mechine")

    # Option -d/--data <data> HTTP POST data
    crl.setopt(crl.POSTFIELDS,  post_data)
    crl.setopt(pycurl.URL, url)
    crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
    crl.perform()
    
    reponseStr = crl.fp.getvalue()
    return  reponseStr
    
if __name__ == '__main__':

    url ="http://172.21.2.56:9007/EmobileBPM/soap/WFSService"
    url1 = 'http://172.21.1.30:51900/esbWS/rest/SHPOCRouteTest'
    post_data = '''
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <SOAP-ENV:Body>
    <m:handsShake xmlns:m="http://webservices.bpm.emobile.com">
    <m:in0><![CDATA[ 
    <msg xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> 
    <head> 
    <eventType>ASYN</eventType> 
    <_eID>S0014</_eID> 
    <serialNo>101</serialNo> 
    </head> 
    <body> 
    <basic> 
    <event_id>PROC_START</event_id> 
    <ext_work_id>12014112400000513</ext_work_id> 
    <work_item_id>0</work_item_id> 
    <step_id>0</step_id> 
    <rela_work_item_id>0</rela_work_item_id> 
    <direction_id xsi:nil="true"/> 
    <alarm_date xsi:nil="true"/> 
    <pre_alarm_date xsi:nil="true"/> 
    <hasten_date xsi:nil="true"/> 
    <process_sts>PS_RUNNING</process_sts> 
    <work_item_asgn_time xsi:nil="true"/> 
    <expt_from_work_item_id>0</expt_from_work_item_id> 
    <activity_id>0</activity_id> 
    </basic> 
    </body> 
    <ret/> 
    </msg> 
    ]]></m:in0>
    </m:handsShake>
    </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>

    '''

    post_data1 = '''
    {"ROOT":{"HEADER":{"POOL_ID":"11","DB_ID":"","ENV_ID":"","CHANNEL_ID":"02","ROUTING":{"ROUTE_KEY":10,"ROUTE_VALUE":"15799881753"}},"BODY":{ "PHONE_NO":"","TEST":""}}}
    '''
    reponseStr = PostData(url, post_data)
    if 'encoding=\'UTF-8\'' in reponseStr:
        reponseStr = reponseStr.decode('utf-8')
    print reponseStr