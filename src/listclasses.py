#!/usr/bin/env python3
"""SPARQL query for listing all classes"""

import executequery as xq

ONTOFILE = "file://./xppu-information-model.owl"

QUERY = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX : <http://david.org/informationmodel.owl#>
        SELECT DISTINCT ?class WHERE {
        ?class rdf:type owl:Class . 
        }"""

def find():
    return(xq.executequery(ONTOFILE, QUERY))

if __name__ == "__main__":
    print(find())
