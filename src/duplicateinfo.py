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
    text = "duplicate info:"
    if not li:
        text = "no duplicate info"
    else:
        newline = "\n"+str(li[0][0])+" contained in "+str(li[0][1])+" stored in "+str(li[0][2])
        text += newline
        for a, b in zip(li[1:], li):
            if a[0] == b[0]:
                newline = "\n\talso contained in "+str(a[1])+" stored in "+str(a[2])
                text += newline
            else:
                newline = "\n"+str(a[0])+" contained in "+str(a[1])+" stored in "+str(a[2])
                text += newline
    return text

def main():
    return returnresults(xq.executequery(ONTOFILE, QUERY))

if __name__ == "__main__":
    print(main())
