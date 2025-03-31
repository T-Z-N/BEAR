import rdflib
from rdflib import Graph, URIRef
import owlrl

def get_local_name(uri):
    if "#" in uri:
        return uri.split("#")[-1]
    elif "/" in uri:
        return uri.split("/")[-1]
    return str(uri)

# Load the RDF file
g = Graph()
g.parse("PropTest.rdf", format="xml")

BASE = "http://www.semanticweb.org/p42770/ontologies/2025/2/untitled-ontology-173#"

owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g)

deliver = URIRef(BASE + "deliver")

# Define individuals
org0 = URIRef(BASE + "Org0")
a = URIRef(BASE + "A")
b = URIRef(BASE + "B")

for s, p, o in g.triples((org0, deliver, None)):
    print(f"Triple: {get_local_name(s)} {get_local_name(p)} {get_local_name(o)}")

if (org0, deliver, a) in g:
    print(f"Inferred: {get_local_name(org0)} {get_local_name(deliver)} {get_local_name(a)} ")
else:
    print(f"Not inferred: {get_local_name(org0)} {get_local_name(deliver)} {get_local_name(a)}")

