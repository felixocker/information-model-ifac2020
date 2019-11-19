# information-model-ifac2020
Source files for the paper "A Knowledge Based System for Managing Heterogeneous Sources of Engineering Information" submitted to the IFAC World Congress 2020. The paper is authored by Felix Ocker, Matthias Seitz, Christiaan J. J. Paredis, and Birgit Vogel-Heuser.

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

# License
For now, the following license holds:

Copyright © 2019 Technical University of Munich - Institute of Automation and Information Systems. <http://www.ais.mw.tum.de/en/institute/>

All rights reserved. Contact: [felix.ocker@tum.de](mailto:felix.ocker@tum.de)
