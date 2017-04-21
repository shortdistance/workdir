import telnetlib, sys
import string

def telnetdo(HOST=None, PORT=80):

	if not HOST:
		try:
			HOST = sys.argv[1]
			PORT = sys.argv[2]
	
		except:
			print "Usage: telnet.py host port"
			return
	try:
	    tn = telnetlib.Telnet(HOST, int(PORT))
	except Exception,e:
	    tn = None
	    
	if tn:
	    return 0
	else:
	    return -1
	

if __name__ == '__main__':
	print telnetdo()