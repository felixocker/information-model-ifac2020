#!/usr/bin/env python3
"""SPARQL query for finding information concretizations and carriers that capture information"""

import executequery as xq

ONTOFILE = "file://./xppu-information-model.owl"

# todo: possibly also allow user to specify language

def confquery(infokind, system):
    query = """PREFIX : <http://david.org/informationmodel.owl#>
            SELECT DISTINCT ?conc ?carrier WHERE {
            ?conc a :information_concretization . 
            ?info a/rdfs:subClassOf* """ + infokind + """ . 
            ?info :describes """ + system + """ . 
            ?conc :concretizes ?info . 
            ?carrier :captures ?conc . 
            ?carrier a :information_carrier . 
            }"""
    return query

def returnresults(li):
    """print query results in an easily interpretable way"""
    if not li:
        text = "no info available"
    else:
        text = "info is available in:"
        for i in li:
            newline = "\n"+str(i[0])+" stored here: "+str(i[1])
            text += newline
    return text

def main(infokind, system):
    return returnresults(xq.executequery(ONTOFILE, confquery(infokind, system)))

if __name__ == "__main__":
    print(main(infokind=":structural_information", system=":PPU"))
