import owlready2
from owlready2 import get_ontology
from rdflib import URIRef

owlready2.JAVA_EXE = r"C:\Users\P42770\Java\jdk-23.0.2\bin\java"

owlready2.reasoning.JAVA_MEMORY = 500

def get_local_name(entity):
    if hasattr(entity, "name"):
        return entity.name
    uri = str(entity)
    if "#" in uri:
        return uri.split("#")[-1]
    elif "/" in uri:
        return uri.split("/")[-1]
    return str(entity)

onto = get_ontology("PropTest.rdf").load()

BASE = "http://www.semanticweb.org/p42770/ontologies/2025/2/untitled-ontology-173#"

with onto:
    #owlready2.sync_reasoner_pellet() # Uncomment this line to use Pellet reasoner
    owlready2.sync_reasoner_hermit()

deliver_prop = onto.search_one(iri=BASE + "deliver")
org0_ind = onto.search_one(iri=BASE + "Org0")
a_ind = onto.search_one(iri=BASE + "A")
b_ind = onto.search_one(iri=BASE + "B")

print("Original triples")
if deliver_prop and org0_ind and hasattr(org0_ind, deliver_prop.name):
    for obj in getattr(org0_ind, deliver_prop.name):
        print(f"Original: {get_local_name(org0_ind)} {get_local_name(deliver_prop)} {get_local_name(obj)}")

if deliver_prop and org0_ind and a_ind and hasattr(org0_ind, deliver_prop.name):
    if a_ind in getattr(org0_ind, deliver_prop.name):
        print(f"Inferred: {get_local_name(org0_ind)} {get_local_name(deliver_prop)} {get_local_name(a_ind)}")
    else:
        print(f"Not inferred: {get_local_name(org0_ind)} {get_local_name(deliver_prop)} {get_local_name(a_ind)}")

print("\nAll relationships with individuals in an ontology:")
for ind in onto.individuals():
    for prop in onto.object_properties():
        if hasattr(ind, prop.name):
            for target in getattr(ind, prop.name):
                print(f"{get_local_name(ind)} {get_local_name(prop)} {get_local_name(target)}")