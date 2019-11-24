#!/usr/bin/env python3
"""using the owlready2 built-in reasoner HermiT to check ontology consistency"""

from owlready2 import *
import types

ONTOFILE = "file://./xppu-information-model.owl"

def main():
    onto = get_ontology(ONTOFILE).load()
    sync_reasoner()
    text = "inconsistent classes are:"
    if not list(default_world.inconsistent_classes()):
        text = "no inconsistent classes"
    else:
        for i in range(len(list(default_world.inconsistent_classes()))):
            text += "\n\t"
            text += str(list(default_world.inconsistent_classes())[i])
    return text

if __name__ == "__main__":
    print(main())
