import urllib2
import rdflib
import rdflib_jsonld
# Code from Fetching Data and Parsing Data examples
uri = 'http://www.worldcat.org/oclc/82671871'
request_headers = {'Accept': 'application/rdf+xml'}
request = urllib2.Request(uri, headers = request_headers)
response = urllib2.urlopen(request).read()
graph = rdflib.Graph()
graph.parse(data=response, format='xml')
# Grab a list of all of the Predicates in the graph
graph.serialize("test5.rdf",format="xml")
predicates = graph.predicates(subject=None, object=None)
# For each item in the predicates generator, print it out
for predicate in predicates:
    print(predicate)