from rdflib.namespace import RDF, RDFS
from rdflib import Graph,BNode
from rdflib.collection import Collection
from pprint import pformat

g = Graph()
a = BNode('foo')
b = BNode('bar')

c = BNode('baz')
g.add((a, RDF.first, RDF.type))
g.add((a, RDF.rest, b))
g.add((b, RDF.first, RDFS.label))
g.add((b, RDF.rest, c))
g.add((c, RDF.first, RDFS.comment))
g.add((c, RDF.rest, RDF.nil))


print len(g)
def listAncestry(node, graph):
    for i in graph.subjects(RDF.rest, node):
        yield i
print [str(node.n3()) for node in g.transitiveClosure(listAncestry, RDF.nil)]

lst = Collection(g, a)
print len(lst)
b == lst._get_container(1)
c == lst._get_container(2)
del lst[1]
print len(lst)
print len(g)


from rdflib.graph import Graph, Literal
listName = BNode()
g = Graph('IOMemory')
listItem1 = BNode()
listItem2 = BNode()
g.add((listName, RDF.first, Literal(1)))
g.add((listName, RDF.rest, listItem1))
g.add((listItem1, RDF.first, Literal(2)))
g.add((listItem1, RDF.rest, listItem2))
g.add((listItem2, RDF.first, Literal(3)))
g.add((listItem2, RDF.rest, RDF.nil))
c = Collection(g, listName)
print(c.n3())
print Literal(1) in c


g2 = Graph()
src = '''
 @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
 @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
 [ a rdf:Statement ;
 rdf:subject <http://rdflib.net/store#ConjunctiveGraph>;
 rdf:predicate rdfs:label;
 rdf:object "Conjunctive Graph" ] .
 '''
g2 = g2.parse(data=src, format='n3')
print g2
print(len(g2))