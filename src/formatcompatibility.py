#!/usr/bin/env python3
"""SPARQL query for finding information carriers that cannot be accessed with the tools available, 
    either bc the company does not have appropriate licenses or bc there is no appropriate tool"""

import executequery as xq

ONTOFILE = "file://./xppu-information-model.owl"

# parameters
ORGANIZATION = ":TUM"

QUERY = """PREFIX : <http://david.org/informationmodel.owl#>
        SELECT DISTINCT ?conc ?tool ?format WHERE {
        ?conc a/rdfs:subClassOf* :information_concretization ; 
            :stored_as ?format . 
        OPTIONAL { ?tool :supports ?format . }
        FILTER NOT EXISTS {
            """ + ORGANIZATION + """ :has_license_for/:supports ?format . 
        }
        }"""

def returnresults(li):
    for i in li:
        if not i[1]:
            print(i[0], "- no tool available for format ", i[2])
        else:
            print(i[0], "- no license available for tool", i[1])

def main():
    returnresults(xq.executequery(ONTOFILE, QUERY))

if __name__ == "__main__":
    main()
