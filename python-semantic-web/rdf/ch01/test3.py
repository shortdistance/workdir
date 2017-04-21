# coding:utf-8

'''
from rdflib import Graph
g = Graph()
g.parse("test2.rdf", format="xml")
len(g) # prints 2
import pprint
for stmt in g:
    pprint.pprint(stmt)
'''

from rdflib import Namespace
from rdflib import Graph, RDF, Literal
from rdflib.namespace import FOAF

# 定义一个命名空间
n = Namespace("http://example.org/people/")

# 定义命名空间下两个subjects
bob = n.bob  # = rdflib.term.URIRef(u'http://example.org/people/bob')
linda = n.linda  # = rdflib.term.URIRef(u'http://example.org/people/eve')

# 创建2个数据节点, subject, predict, object
g = Graph()
g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.name, Literal('bob')))
g.add((bob, FOAF.age, Literal(42)))
g.add((bob, FOAF.knows, linda))

g.add((linda, RDF.type, FOAF.Person))
g.add((linda, FOAF.name, Literal('Linda')))
g.add((linda, FOAF.age, Literal(30)))
# 将文件以xml格式保存到文件里面
g.serialize('test3.rdf', format='xml')

'''
#删除某个节点
g.remove((bob, None, None))
g.serialize('test3.rdf',format='xml')
'''
# 读取数据节点
for subj, pred, obj in g:
    if (subj, pred, obj) not in g:
        raise Exception("It better be!")
    print subj, pred, obj

# 检查某个subject是否存在
# 精确查询
from rdflib import URIRef

bob = URIRef("http://example.org/people/bob")
if (bob, RDF.type, FOAF.Person) in g:
    print "This graph knows that Bob is a person!"

# 模糊查询
if (bob, None, None) in g:
    print "This graph contains triples about Bob!"

# 创建另外一个图

n1 = Namespace("http://example.org/people1/")
bob = n.bob
zhanglei = n1.zhanglei
rourou = n1.rourou
g1 = Graph()

g1.add((bob, RDF.type, FOAF.Person))
g1.add((bob, FOAF.name, Literal('bob')))

g1.add((zhanglei, RDF.type, FOAF.Person))
g1.add((zhanglei, FOAF.name, Literal('zhanglei')))
g1.add((zhanglei, FOAF.age, Literal(34)))
g1.add((zhanglei, FOAF.knows, rourou))

g1.add((rourou, RDF.type, FOAF.Person))
g1.add((rourou, FOAF.name, Literal('zhanglei')))
g1.add((rourou, FOAF.age, Literal(29)))
g1.add((rourou, FOAF.knows, zhanglei))
g1.serialize('test3_1.rdf', format='xml')

# 加
g3 = g1 + g
g3.serialize('test3_2.rdf', format='xml')

# 减
g3 -= g
g3.serialize('test3_3.rdf', format='turtle')

# 交, 存在两边都有的
g4 = g & g1
g4.serialize('test3_4.rdf', format('xml'))

# 异或， 存在两边没有的
g5 = g ^ g1
g5.serialize('test3_5.rdf', format('xml'))


"""
a simple example of query
"""
import rdflib
g = rdflib.Graph()
# ... add some triples to g somehow ...
g.parse("test3.rdf")
qres = g.query(
        """SELECT DISTINCT ?aname ?aage ?bname ?bage
        WHERE {
        ?a ns1:knows ?b .
        ?a ns1:name ?aname .
        ?a ns1:age ?aage .
        ?b ns1:name ?bname .
        ?b ns1:age ?bage .
        }""")
for row in qres:
    #print("%s knows %s" % row)
    print row
    print row[0], row[1], row[2], row[3]


"""
query bind
"""
from rdflib.plugins.sparql import prepareQuery
q = prepareQuery(
    'SELECT ?a WHERE { ?b ns1:knows ?a .}',
    initNs = { "ns1": FOAF })
g = rdflib.Graph()
g.load("test3.rdf")
a = rdflib.URIRef("http://example.org/people/bob")
for row in g.query(q, initBindings={'b': a}):
    print row


"""

"""
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print g[bob]
# same as
print g.predicate_objects(bob)
print g[bob : FOAF.knows]
# same as
print g.objects(bob, FOAF.knows)
print g[bob : FOAF.knows : linda]
# same as
print (bob, FOAF.knows, linda) in g
print g[:FOAF.knows]
# same as
print g.subject_objects(FOAF.knows)