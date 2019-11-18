#!/usr/bin/env python3
"""integrate metamodel and instance model for br"""

import mbse
import xppu

IRI = "http://david.org/informationmodel.owl"
METAFILE = "mbse-information-model.owl"
INSTANCEFILE = "xppu-information-model.owl"

def main():
    """call submodules"""
    mbse.im_mbse(IRI, METAFILE)
    xppu.im_xppu(IRI, INSTANCEFILE)

if __name__ == "__main__":
    main()
