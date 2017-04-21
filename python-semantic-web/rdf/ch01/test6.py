from rdflib import Graph, BNode, Literal, URIRef
from rdflib import RDF, RDFS
from rdflib.namespace import FOAF, DC, XSD

g = Graph()
donna = BNode()
bob = BNode()
# Add triples using store's add method.
g.add((donna, RDF.type, FOAF.Person))
g.add((donna, FOAF.nick, Literal("donna", lang="foo")))
g.add((donna, FOAF.name, Literal("Donna Fales")))
g.add((donna, FOAF.mbox, URIRef("mailto:donna@example.org")))

for s, p, o in g:
    print (s, p, o)

# For each foaf:Person in the store print out its mbox property.
print("--- printing mboxes ---")
for person in g.subjects(RDF.type, FOAF.Person):
    for mbox in g.objects(person, FOAF.mbox):
        print mbox
# Bind a few prefix, namespace pairs for more readable output
g.bind("dc", DC)
g.bind("foaf", FOAF)

"""
g.subjects(p, o)
g.predicates(s, o)
g.objects(s, p)
"""
for s in g.subjects(None, None):
    print s
for p in g.predicates(donna, None):
    print p
for o in g.objects(donna, None):
    print o

print '~~~~~~~~~~~~~~~~~'
print g.subject_objects(None)
print '~~~~~~~~~~~~~~~~~'
print g.predicate_objects(None)

"""
g.triples(s, p, o)
"""
for s, p, o in g.triples((donna, RDF.type, FOAF.Person)):
    print (s, p, o)


"""
g.value(s, p)
"""
name = g.value(donna, FOAF.name)
print name


"""
RDFS.label
"""
from rdflib import ConjunctiveGraph, URIRef, RDFS, Literal
from rdflib.namespace import SKOS
from pprint import pprint
g = ConjunctiveGraph()
u = URIRef(u'http://example.com/foo')
g.add([u, RDFS.label, Literal('foo')])
g.add([u, RDFS.label, Literal('bar')])
pprint(sorted(g.preferredLabel(u)))

g.add([u, SKOS.prefLabel, Literal('bla')])
pprint(g.preferredLabel(u))

g.add([u, SKOS.prefLabel, Literal('blubb', lang='en')])
sorted(g.preferredLabel(u))
pprint(g.preferredLabel(u))

pprint(g.preferredLabel(u))
g.add([u, SKOS.prefLabel, Literal('blubb', lang='en')])
sorted(g.preferredLabel(u))
g.preferredLabel(u, lang='')
pprint(g.preferredLabel(u, lang='en'))

g.serialize("test6.rdf",format="xml")
