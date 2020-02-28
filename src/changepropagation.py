#!/usr/bin/env python3
"""SPARQL query for finding stakeholders that should be notified of changes"""

import executequery as xq
import preprocess_query_results as ppqr

ONTOFILE = "file://./xppu-information-model.owl"

# parameters
INFOCONC_CHANGED = ":ic_PPU_crane_behavior_UMLact_PapyrusUML"

def confquery(infoconc_changed):
    query = """PREFIX : <http://david.org/informationmodel.owl#>
            SELECT DISTINCT ?info ?actor WHERE {
                ?actor a/rdfs:subClassOf* :actor . 
                ?info a/rdfs:subClassOf* :information . 
                """ + infoconc_changed + """ :concretizes ?info . 
                ?infoconc :concretizes ?info . 
                ?actor :subscribes ?infoconc . 
            }"""
    return query

def returnresults(li):
    text = "suggested notifications:"
    if not li:
        text = "no notifications required"
    else:
        for i in li:
            newline = "\nnotify "+str(i[1])+" that "+str(i[0])+" has been changed"
            text += newline
    return text

def main(infoconc):
    return returnresults(xq.executequery(ONTOFILE, confquery(infoconc)))

if __name__ == "__main__":
    print(main(INFOCONC_CHANGED))
