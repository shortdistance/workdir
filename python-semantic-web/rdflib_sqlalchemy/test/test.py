import os
import shutil

try:
    from commands import getoutput
except ImportError:
    # Python 3
    from subprocess import getoutput

from rdflib import (
    BNode,
    Graph,
    Literal,
    RDF,
    RDFS,
    URIRef,
    plugin,
    store
)
from rdflib.store import Store

plugin.register(
    "SQLAlchemy",
    store.Store,
    "rdflib_sqlalchemy.store",
    "SQLAlchemy",
)


# Work in progress


def investigate_len_issue():
    store = plugin.get("SQLAlchemy", Store)(
        identifier=URIRef("rdflib_test"),
        configuration=Literal("sqlite:///%(here)s/development.sqlite" % {
            "here": os.getcwd()}))
    g0 = Graph("Sleepycat")
    g0.open("e:/1.txt", create=True)
    g1 = Graph(store)
    statementId = BNode()
    g0.add((statementId, RDF.type, RDF.Statement))
    g1.add((statementId, RDF.type, RDF.Statement))
    g0.add((statementId, RDF.subject, URIRef(u"http://rdflib.net/store/ConjunctiveGraph")))
    g1.add((statementId, RDF.subject, URIRef(u"http://rdflib.net/store/ConjunctiveGraph")))
    g0.add((statementId, RDF.predicate, RDFS.label))
    g1.add((statementId, RDF.predicate, RDFS.label))
    g0.add((statementId, RDF.object, Literal("Conjunctive Graph")))
    g1.add((statementId, RDF.object, Literal("Conjunctive Graph")))
    getoutput("cp development.sqlite devcopy.sqlite")
    g0.remove((statementId, RDF.type, RDF.Statement))
    g1.remove((statementId, RDF.type, RDF.Statement))
    g0.close()
    shutil.rmtree("e:/1.txt")
    g1.close()


if __name__ == "__main__":
    investigate_len_issue()
