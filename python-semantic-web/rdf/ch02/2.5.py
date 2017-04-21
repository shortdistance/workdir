from rdflib import Literal
from rdflib.namespace import XSD

print Literal(2, datatype=XSD.int) == Literal(2, datatype=XSD.float)
print Literal(2, datatype=XSD.int).eq(Literal(2, datatype=XSD.float))
