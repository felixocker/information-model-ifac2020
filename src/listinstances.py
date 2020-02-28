#!/usr/bin/env python3
"""SPARQL query for finding and listing instances of a class"""

import executequery as xq

ONTOFILE = "file://./xppu-information-model.owl"

def confquery(parent="owl:Thing"):
    query = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX : <http://david.org/informationmodel.owl#>
            SELECT DISTINCT ?instance WHERE {
            ?instance a/rdfs:subClassOf* """ + parent + """ . 
            }"""
    return query

def find(parent="owl:Thing"):
    return(xq.executequery(ONTOFILE, confquery(parent)))

if __name__ == "__main__":
    print(find())
