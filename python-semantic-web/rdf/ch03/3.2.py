#coding:utf-8
from rdflib import Graph
from rdflib.namespace import Namespace,NamespaceManager
from rdflib.namespace import OWL as OWL_NS

g1 = Graph()
g2 = Graph()
EX = Namespace("http://example.com/")
namespace_manager = NamespaceManager(g1)
namespace_manager.bind('ex', EX, override=False)
namespace_manager = NamespaceManager(g2)
namespace_manager.bind('ex', EX, override=False)
print g1.serialize(format="xml")

# coding:utf8
import rdflib

graph = rdflib.Graph('Sleepycat', identifier='lhq')

# first time create the store:
graph.open('db', create=True)

# work with the graph:
s = rdflib.URIRef('牛膝')
p = rdflib.URIRef('功效属性')
o = rdflib.URIRef('活血')

graph.add((s, p, o))

# when done!
graph.close()

g_t = rdflib.Graph('Sleepycat', identifier='lhq')  # 新建图，指定数据库
g_t.open('db')  # 打开数据库并进行操作
print len(g_t)
g_t.close()