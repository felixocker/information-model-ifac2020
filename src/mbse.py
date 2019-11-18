#!/usr/bin/env python3
"""information model for BMBF DAVID, mbse module"""

from owlready2 import *
import types

def im_mbse(iri, output):
    """generic information model for MBSE"""
    onto = get_ontology(iri)
    with onto:
    # universals
        class actor(Thing):
            comment = ["anyone and anything that provides or requires information"]
        class doc_format(Thing):
            comment = ["concrete syntax some information concretization is stored in; e.g., plain text or pdf; indicates the information concretization's structure and how it has to be interpreted"]
        class event(Thing): pass
        class information(Thing):
            comment = ["the communication or reception of knowledge [Merriam Webster]"]
        class information_carrier(Thing):
            comment = ["physical artifact that captures some information concretization"]
            # how to handle fiat boundaries in information carriers? eg, several folders on the same hard drive, which capture the same information concretizations
        class information_concretization(Thing):
            comment = ["notion to express concretization of some information, i.e., some information being expressed in some language and possibly serialized in some format"]
            comment.append("an information concretization refers to the combination of information expressed in at least one specific language. combinations of languages may be necessary, e.g., UML and English")
        class language(Thing):
            comment = ["set of valid sentences that can be used to express information"]
        class organization(Thing): pass
        class organizational_unit(Thing): pass
        class project(Thing):
            comment = ["an endeavor with start and finish dates undertaken to create a product or service in accordance with specified resources and requirements [INCOSE SE Handbook]"]
        class role(Thing): pass
        class system(Thing):
            comment = ["a combination of interacting elements organized to achieve one more stated purposes [INCOSE SE Handbook]"]
        class task(Thing): pass
        class viewpoint(Thing): pass
    # dependent universals
        class behavioral_information(information):
            comment = ["defines the behavior of a system"]
        class requirement(information):
            comment = ["condition or capability that must be possessed by a system or system component to satisfy a contract, standard, specification, or other formally imposed information carriers (IEEE glossary)"]
        class structural_information(information):
            comment = ["defines the structure of a system"]
        class function(behavioral_information): pass
        class company(organization): pass
        class discipline(viewpoint): pass
        class functional_requirement(requirement):
            comment = ["requirement that specifies a function that a system or system component must be able to perform (IEEE glossary)"]
        class non_functional_requirement(requirement):
            comment = ["opposed to functional requirements, a non-functional requirement specifies (IEEE glossary)"]
        class person(actor): pass
        class tool(actor): pass
        class university(organization): pass
    # object properties
        class authored_by(information_concretization >> actor):
            comment = ["every information-concretization has some author, some information-concretizations, e.g., books, may have several authors"]
        class based_on(doc_format >> doc_format): pass
        class can_perform(system >> function): pass
        class captures(information_carrier >> information_concretization):
            comment = ["an information carrier may capture several information concretizations"]
        class concretizes(information_concretization >> information):
            comment = ["an information concretizations concretizes information"]
        class defines(project >> requirement): pass
        class describes(ObjectProperty): pass
        class expressed_in(information_concretization >> language):
            comment = ["an information concretization is expressed in at least one language, e.g., UML and English might be used together"]
        class has(ObjectProperty): pass
        class has_license_for(organization >> tool): pass
        class has_right(ObjectProperty): pass
        class part(Thing >> Thing, TransitiveProperty): pass
        class performs(system >> function): pass
        class possesses(person >> information): pass
        class predecessor(information_concretization >> information_concretization):
            comment = ["predecessor relation between information-concretizations for versioning support"]
        class provides(actor >> information): pass
        class publishes(actor >> information_concretization): pass
        class requires(actor >> information): pass
        class restricts(non_functional_requirement >> system): pass
        class satisfies(system >> requirement): pass
        class specifies(functional_requirement >> function): pass
        class stored_as(information_concretization >> doc_format): pass
        class subscribes(actor >> information_concretization): pass
        class supports(tool >> doc_format): pass
    # dependent object properties
        class has_read_right(has_right): pass
        class has_write_right(has_right): pass
        class has_execute_right(has_right): pass
        class submitted_by(authored_by):
            comment = ["every document is submitted by a corresponding author, of which there is exactly one per information concretization"]
    # datatype properties
        class status_complete(DataProperty):
            domain = [information_concretization]
            range = [bool]
            comment = ["status of a information carrier: either complete or incomplete"]
            # todo: consider changing this to an enum
        class timestamp(DataProperty):
            domain = [information_concretization]
            range = [datetime.datetime]
            comment = ["date of the last change to a information carrier"]
    # axioms - added down here to make sure that all classes are already defined
        information_concretization.is_a.append(concretizes.some(information))
        information_concretization.is_a.append(expressed_in.min(1, language))
        actor.is_a.append(has.some(viewpoint))
        organizational_unit.is_a.append(Inverse(part).some(organization))
        information_carrier.is_a.append(captures.some(information_concretization))
        information_concretization.is_a.append(authored_by.some(actor))
        information_concretization.is_a.append(submitted_by.exactly(1, actor))
        information_concretization.is_a.append(status_complete.some(bool))
        information_concretization.is_a.append(timestamp.some(datetime.datetime))
        system.is_a.append(performs.some(function))
        functional_requirement.is_a.append(specifies.some(function))
        non_functional_requirement.is_a.append(restricts.some(system))
        information.is_a.append(describes.some(system))
        project.is_a.append(defines.some(requirement))
    # save file
    onto.save(file = output)
