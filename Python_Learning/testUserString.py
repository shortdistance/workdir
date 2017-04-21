#-*-coding:utf-8-*-
import UserString
if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8') 
    print UserString.__all__
    s = UserString.UserString(" z,ASD ,asddff,¹þ¹þ,1,2, ,a, dd  ,a")
    print s
    s.capitalize()
    print s.center(40,'~')   
    print s.count('he')
    
    print "endswith","=>", s.endswith(' ')    #ÒÔsuffix½áÎ²
    print "expandtabs(self, tabsize=8)","=>",s.expandtabs(tabsize=10)
    print "find","=>",s.find('za')
    print "index","=>",s.index('z')

    print "isalnum","=>", s.isalnum()

    print "isalpha","=>", s.isalpha()
    
    print "isdigit(self)","=>", s.isdigit()

    print "islower","=>",s.islower()

    #print "isnumeric","=>", s.isnumeric()
    
    print "isspace","=>", s.isspace()

    print "istitle","=>", s.istitle()

    print "isupper","=>", s.isupper()

    print "join","=>",' '.join(s.split(','))

    print "ljust","=>", s.ljust(100)
    print "rjust","=>", s.rjust(100)
    print "lower","=>", s.lower()
    print "lstrip","=>", s.lstrip()
    print "rstrip","=>", s.rstrip()
    print s.partition(' ,a')
    print s.rpartition(' ,a')
    print s.replace('¹þ¹þ', 'haha', maxsplit=-1)
    print s.rfind('as1')
    print s.rindex('as')
    print s.find('as')

    print s.split(' ,a')
    print s.rsplit(' ,a')
    

    mulLine = """Hello!!! 
    Wellcome to Python's world! 
    There are a lot of interesting things! 
    Enjoy yourself. Thank you!""" 

    print ''.join(mulLine.splitlines()) 
    print '------------' 
    print ''.join(mulLine.splitlines(True)) 
    
    print mulLine.startswith('Hello')
    print mulLine.swapcase()
    print mulLine.title()
    print mulLine.__len__()
    print mulLine.zfill(200)

    '''
     |  
     |  join(self, seq)
     |  
     |  ljust(self, width, *args)
     |  
     |  lower(self)
     |  
     |  lstrip(self, chars=None)
     |  
     |  partition(self, sep)
     |  
     |  replace(self, old, new, maxsplit=-1)
     |  
     |  rfind(self, sub, start=0, end=2147483647)
     |  
     |  rindex(self, sub, start=0, end=2147483647)
     |  
     |  rjust(self, width, *args)
     |  
     |  rpartition(self, sep)
     |  
     |  rsplit(self, sep=None, maxsplit=-1)
     |  
     |  rstrip(self, chars=None)
     |  
     |  split(self, sep=None, maxsplit=-1)
     |  
     |  splitlines(self, keepends=0)
     |  
     |  startswith(self, prefix, start=0, end=2147483647)
     |  
     |  strip(self, chars=None)
     |  
     |  swapcase(self)
     |  
     |  title(self)
     |  
     |  translate(self, *args)
     |  
     |  upper(self)
     |  
     |  zfill(self, width)
     |  '''