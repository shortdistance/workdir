from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import FOAF, NamespaceManager

person = URIRef('http://xmlns.com/foaf/0.1/Person')
print person.n3()
g = Graph()
g.bind("foaf", FOAF)
g.serialize("01.16.06.rdf", format="n3")
print person.n3(g.namespace_manager)
l = Literal(2)
print l.n3()
print l.n3(g.namespace_manager)
