from rdflib import Namespace
n = Namespace("http://www.baidu.com/")
print n.World # as attribute
print n['Hello']
print n.title