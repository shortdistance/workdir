from xmlrpclib import ServerProxy

if __name__ == '__main__':
    s = ServerProxy("http://192.168.56.101:9010")
    #print s.add(3, 4)
    print  s