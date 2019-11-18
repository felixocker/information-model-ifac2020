#!/usr/bin/env python3
"""using the owlready2 built-in reasoner HermiT to check ontology consistency"""

from owlready2 import *
import types

ONTOFILE = "file://./xppu-information-model.owl"

def main():
    onto = get_ontology(ONTOFILE).load()
    sync_reasoner()
    print("inconsistent classes are:",list(default_world.inconsistent_classes()))

if __name__ == "__main__":
    main()
