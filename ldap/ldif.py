import ldif
 
class testParser(ldif.LDIFParser):
    def __init__(self,input_file,ignored_attr_types=None,max_entries=0,process_url_schemes=None,line_sep='\n' ):
      ldif.LDIFParser.__init__(self,input_file,ignored_attr_types,max_entries,process_url_schemes,line_sep)
     
    def handle(self,dn,entry):
        if 'person' in entry['objectclass']:
            print "Identifier = ",entry['uid'][0]
            print "FirstName = ",entry.get('givenname',[''])[0]
            print "LastName = ",entry.get('sn',[''])[0]
            print
 
f = open('sitech.ldif','r')
ldif_parser = testParser(f)
ldif_parser.parse()
