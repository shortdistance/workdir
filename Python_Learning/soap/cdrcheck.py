# coding: utf-8
from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod
from soaplib.serializers.clazz import ClassSerializer
from soaplib.serializers.primitive import String, Integer, Array, DateTime


'''
This is a simple cdrcheck program writing using soaplib, 
starting a server, and creating a service client. 
'''

class Cdrstatus(ClassSerializer):
    """
    the class the soapmethod will return.
    """
    class types:
        hostname = String
        ip = String
        cdrtype = String
        status = Integer
        comment = String
        reporttime = String
        sn = String


class CdrstatusService(SimpleWSGISoapApp):
    
    @soapmethod(String, _returns=Array(Cdrstatus))
    def get_Cdrstatus(self,user):
    	'''
        Docstrings for service methods appear as documentation in the wsdl
        <b>return the status of each kind of cdrs</b>
	    @return the Cdrstatus.
	    这个方法接受一个参数，客户端在调用这个方法时，必须传一个参数
	    返回值是一个列表，列表中的元素是Cdrstatus类的实例
    	'''
                
        from cdrstat import cdr_stat
        
        cdr_status_dict = cdr_stat()
        
        cdr_status = []

        for probe_info in cdr_status_dict.keys():
            for cdrtype in cdr_status_dict[probe_info].keys():
                #实例化Cdrstatus类
                c = Cdrstatus()
                c.hostname = probe_info[1]
                c.ip = probe_info[2]
                c.cdrtype = cdrtype
                c.status = cdr_status_dict[probe_info][cdrtype][1]
                c.comment = cdr_status_dict[probe_info][cdrtype][2]
                c.reporttime = cdr_status_dict[probe_info][cdrtype][0]
                c.sn = cdr_status_dict[probe_info][cdrtype][3]
    
                cdr_status.append(c)

        return cdr_status

def make_client():
    """
        这个函数是这个web service的客户端，在服务端程序中不是必须的。
    """
    from soaplib.client import make_service_client
    #client = make_service_client('http://10.168.68.18:8000/',CdrstatusService())
    client = make_service_client('http://10.168.86.169:7889/',CdrstatusService())
    return client
    
if __name__=='__main__':
    try:
        from wsgiref.simple_server import make_server
        #10.168.86.169，7889为服务绑定的IP地址和端口
        #这个WS的WSDL的URL为http://10.168.86.169:7889/cdrcheck?wsdl
        server = make_server('10.168.86.169', 7889, CdrstatusService())
        server.serve_forever()
    except ImportError:
        #wsgiref这个模块需要python2.5以上的版本，可以使用其它服务器进行部署
        print "Error: example server code requires Python >= 2.5"