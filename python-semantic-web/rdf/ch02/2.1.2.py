from rdflib import URIRef
aref = URIRef('http://www.baidu.com')
print aref
aref = URIRef('http://example.com')
print aref
print URIRef(u'http://example.com')
print aref.n3()