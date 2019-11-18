#!/usr/bin/env python3
"""SPARQL query for identifying duplicate information in the information model"""

import executequery as xq

ONTOFILE = "file://./xppu-information-model.owl"
QUERY = """PREFIX : <http://david.org/informationmodel.owl#>
        SELECT DISTINCT ?info ?conc ?carrier WHERE {
        ?info a/rdfs:subClassOf* :information . 
        ?conc :concretizes ?info . 
        ?carrier :captures ?conc . 
        {
            SELECT ?info (COUNT (?concs) AS ?count) WHERE {
                ?concs :concretizes ?info . 
            }
            GROUP BY ?info
        }
        FILTER (?count > 1)}"""

def returnresults(li):
    """print query results in an easily interpretable way"""
    print("duplicate info:")
    print(li[0][0],"contained in",li[0][1],"stored in",li[0][2])
    for a, b in zip(li[1:], li):
        if a[0] == b[0]:
            print("\talso contained in",a[1],"stored in",a[2])
        else:
            print(a[0],"contained in",a[1],"stored in",a[2])

def main():
    returnresults(xq.executequery(ONTOFILE, QUERY))

if __name__ == "__main__":
    main()
