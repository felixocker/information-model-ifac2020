# information-model-ifac2020
Source files for the paper "A Knowledge Based System for Managing Heterogeneous Sources of Engineering Information" presented at the IFAC World Congress 2020

# Contents
## knowledge graph creation (OWL)
* mbse.py - module that contains generic and thus reusable notions
* xppu.py - module that contains classes and instances relevant for the feasibility study
* integration.py - integrates mbse.py and xppu.py
## queries (SPARQL)
* consistency.py - checks consistency of the knowledge graph created
* findinfo.py - find information based on the type and system described
* duplicateinfo.py - identify duplicate information
* formatcompatibility.py - identify inaccessible information
* changepropagation.py - identify actors affected by a change
* listclasses.py - query for listing all classes of a knowledge graph
* listinstances.py - query for listing all instances of a certain class
## auxiliary files
* executequery.py - module for executing SPARQL queries
* preprocess_query_results.py - remove prefixes of query results
* simplegui.py - the name says it all

# Requirements
Python 3.7+ is recommended.

# Citation
Please use the following bibtex entry:
```
@inproceedings{ocker2020ifac,
author = {Ocker, Felix and Seitz, Matthias and Paredis, J. J. Christiaan and Vogel-Heuser, Birgit},
booktitle = {IFAC World Congress},
publisher = {Elsevier},
title = {{A Knowledge Based System for Managing Heterogeneous Sources of Engineering Information}},
year = {2020}
}
```

# License
GPL v3.0

# Contact
Felix Ocker - [felix.ocker@tum.de](mailto:felix.ocker@tum.de)\
Technical University of Munich - Institute of Automation and Information Systems <https://www.mw.tum.de/en/ais/homepage/>
