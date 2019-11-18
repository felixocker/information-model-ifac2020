#!/usr/bin/env python3
"""information model for BMBF DAVID, xppu module"""

import types
from owlready2 import *
from datetime import datetime

def im_xppu(input, output):
    """definition of information instance model"""
    onto = get_ontology(input).load()
    with onto:
# specific classes
        class cad_tool(onto.tool): pass
        class ide(onto.tool): pass
        class presentationsoftware(onto.tool): pass
        class production_system(onto.system): pass
        class spreadsheet(onto.tool): pass
        class texteditor(onto.tool): pass
        class wordprocessor(onto.tool): pass

# reusable individuals
## languages
    AML = onto.language("AML")
    AML.comment = ["Automation Markup Language"]
    AML.comment.append("AML is considered a language instead of a doc-format because its specification, primarily the Role Classes standardized, include semantics that go beyond a Markup Language")
    CATIA_language = onto.language("CATIA_language")
    Inventor_language = onto.language("Inventor_language")
    Natural_language = onto.language("Natural_language")
    OWL = onto.language("OWL")
    OWL.comment = ["Web Ontology Language, cp. W3C specification"]
    Python = onto.language("Python")
    SysML = onto.language("SysML")
    SysML.comment = ["Systems Modeling Language"]
    UML = onto.language("UML")
    UML.comment = ["Unified Modeling Language"]
    UML_class_diagram = onto.language("UML_class_diagram")
    UML_object_diagram = onto.language("UML_object_diagram")
    UML_package_diagram = onto.language("UML_package_diagram")
    UML_composite_structure_diagram = onto.language("UML_composite_structure_diagram")
    UML_component_diagram = onto.language("UML_component_diagram")
    UML_deployment_diagram = onto.language("UML_deployment_diagram")
    UML_profile_diagram = onto.language("UML_profile_diagram")
    UML_use_case_diagram = onto.language("UML_use_case_diagram")
    UML_activity_diagram = onto.language("UML_activity_diagram")
    UML_state_machine_diagram = onto.language("UML_state_machine_diagram")
    UML_interaction_diagram = onto.language("UML_interaction_diagram")
    UML_sequence_diagram = onto.language("UML_sequence_diagram")
    UML_communication_diagram = onto.language("UML_communication_diagram")
    UML_timing_diagram = onto.language("UML_timing_diagram")
    UML_interaction_overview_diagram = onto.language("UML_interaction_overview_diagram")
    XML = onto.language("XML")
    XML.comment = ["Extensible Markup Language"]
    IEC_61131 = onto.language("IEC_61131")
    Ladder_diagram = onto.language("Ladder_diagram")
    Function_block_diagram = onto.language("Function_block_diagram")
    Structured_text = onto.language("Structured_text")
    Instruction_list = onto.language("Instruction_list")
    Sequential_function_chart = onto.language("Sequential_function_chart")
## views
    Electrics = onto.discipline("Electrics")
    Mechanics = onto.discipline("Mechanics")
    Software = onto.discipline("Software")
## tools
    Adobe_acrobat_reader = onto.tool("Adobe_acrobat_reader")
    Catia = onto.tool("Catia")
    Codesys = onto.ide("Codesys")
    Eclipse = onto.ide("Eclipse")
    Eplan = onto.tool("Eplan")
    Foxit_reader = onto.tool("Foxit_reader")
    Inventor = onto.cad_tool("Inventor")
    Matlab = onto.tool("Matlab")
    Simulink = onto.tool("Simulink")
#    Twincat = onto.ide("Twincat")
    Excel = onto.spreadsheet("Excel")
    Notepadpp = onto.texteditor("Notepadpp")
    Powerpoint = onto.presentationsoftware("Powerpoint")
    SoMachine = onto.tool("SoMachine")
    Word = onto.wordprocessor("Word")

    Mechanics.has.extend([Catia,Inventor])
    Electrics.has.append(Eplan)
    Software.has.extend([Codesys,SoMachine])
## formats
    CATPart = onto.doc_format("CATPart")
    CATPart.comment = ["CATIA format for part files"]
    CATProduct = onto.doc_format("CATProduct")
    CATProduct.comment = ["CATIA format for assembly files"]
    Codesys_proprietary = onto.doc_format("Codesys_proprietary")
    Codesys_proprietary.comment = ["proprietary format Codesys uses to store IEC 61131-3 code"]
    CSV = onto.doc_format("CSV")
    CSV.comment = ["comma separated values"]
    Docx = onto.doc_format("Docx")
    IAM = onto.doc_format("IAM")
    IAM.comment = ["Inventor format for assembly files"]
    IPT = onto.doc_format("IPT")
    IPT.comment = ["Inventor format for part files"]
    PapyrusUML = onto.doc_format("PapyrusUML")
    Pdf = onto.doc_format("Pdf")
    PLCopenXML = onto.doc_format("PLCopenXML")
    Step = onto.doc_format("Step")
    Text = onto.doc_format("Text")
    Turtle = onto.doc_format("Turtle")
    Turtle.comment = ["serialization for OWL"]
    Twincat_proprietary = onto.doc_format("Twincat_proprietary")
    Twincat_proprietary.comment = ["proprietary format Beckhoff uses to store IEC 61131-3 code created w Twincat 3"]
    Xls = onto.doc_format("Xls")
    Xlsx = onto.doc_format("Xlsx")
    XML.is_a.append(onto.doc_format)
## tool support
    Adobe_acrobat_reader.supports.extend([Pdf])
    Catia.supports.extend([CATPart, CATProduct, Step])
    Codesys.supports.extend([Codesys_proprietary, PLCopenXML])
    Eclipse.supports.append(PapyrusUML)
    Excel.supports.extend([Xls,Xlsx,CSV])
    Foxit_reader.supports.extend([Pdf])
    Inventor.supports.extend([IAM, IPT, Step])
#    Twincat.supports.extend([Twincat_proprietary])
    Word.supports.extend([Docx,Text])
    Notepadpp.supports.extend([CSV,Text,Turtle,XML])
## refinements
    Codesys_proprietary.based_on.append(XML)
    IEC_61131.part = [Ladder_diagram, Function_block_diagram, Structured_text, Instruction_list, Sequential_function_chart]
    PapyrusUML.based_on.append(XML)
    UML.part.extend([UML_class_diagram, UML_object_diagram, UML_package_diagram, UML_composite_structure_diagram, UML_component_diagram, UML_deployment_diagram, UML_profile_diagram, UML_use_case_diagram, UML_activity_diagram, UML_state_machine_diagram, UML_interaction_diagram])
    UML_interaction_diagram.part.extend([UML_sequence_diagram, UML_communication_diagram, UML_timing_diagram, UML_interaction_overview_diagram])
    Twincat_proprietary.based_on.append(XML)

# individuals - organization
    Companyx = onto.company("Companyx")
    TUM = onto.university("TUM")
    AIS = onto.organizational_unit("AIS")
    TUM.part.append(AIS)
    IFF = onto.organizational_unit("IFF")
    Companyx.part.append(IFF)
    Eve = onto.person("Eve")
    Felix = onto.person("Felix")
    Matthias = onto.person("Matthias")
    Xenia = onto.person("Xenia")

# organizational licenses
    TUM.has_license_for.extend([Adobe_acrobat_reader,Codesys,Eclipse,Inventor,Word])

## PPU structure
    PPU = onto.production_system("PPU")
    PPU_crane = onto.system("PPU_crane")
    PPU_crane_monostable_cylinder = onto.system("PPU_crane_monostable_cylinder")
    PPU_crane_turning_table = onto.system("PPU_crane_turning_table")
    PPU_crane_vacuum_gripper = onto.system("PPU_crane_vacuum_gripper")
    PPU_stack = onto.system("PPU_stack")
    PPU_stamp = onto.system("PPU_stamp")
    PPU_conveyor = onto.system("PPU_conveyor")
## PPU info
    PPU_behavior = onto.behavioral_information("PPU_behavior")
    PPU_codesys_instructions = onto.information("PPU_codesys_instructions")
    PPU_crane_behavior = onto.behavioral_information("PPU_crane_behavior")
    PPU_crane_geometry = onto.structural_information("PPU_crane_geometry")
    PPU_crane_structure = onto.structural_information("PPU_crane_structure")
    PPU_structure = onto.structural_information("PPU_structure")
    PPU_structure.comment = ["structural decomposition of the PPU"]
## information concretizations
    ic_PPU_BOM = onto.information_concretization("ic_PPU_BOM")
    ic_PPU_BOM.concretizes.append(PPU_structure)
    ic_PPU_BOM.expressed_in.append(Natural_language)
    ic_PPU_BOM.stored_as.append(Pdf)

    ic_PPU_behavior_ST_plcopen = onto.information_concretization("ic_PPU_behavior_ST_plcopen")
    ic_PPU_behavior_ST_plcopen.concretizes.append(PPU_behavior)
    ic_PPU_behavior_ST_plcopen.expressed_in.append(Structured_text)
    ic_PPU_behavior_ST_plcopen.stored_as.append(PLCopenXML)

    ic_PPU_codesys_instructions_NL_Pdf = onto.information_concretization("ic_PPU_codesys_instructions_NL_Pdf")
    ic_PPU_codesys_instructions_NL_Pdf.concretizes.append(PPU_codesys_instructions)
    ic_PPU_codesys_instructions_NL_Pdf.expressed_in.append(Natural_language)
    ic_PPU_codesys_instructions_NL_Pdf.stored_as.append(Pdf)

    ic_PPU_codesys_instructions_NL_Docx = onto.information_concretization("ic_PPU_codesys_instructions_NL_Docx")
    ic_PPU_codesys_instructions_NL_Docx.concretizes.append(PPU_codesys_instructions)
    ic_PPU_codesys_instructions_NL_Docx.expressed_in.append(Natural_language)
    ic_PPU_codesys_instructions_NL_Docx.stored_as.append(Docx)

    ic_PPU_crane_geometry_CATProduct = onto.information_concretization("ic_PPU_crane_geometry_CATProduct")
    ic_PPU_crane_geometry_CATProduct.concretizes.append(PPU_crane_geometry)
    ic_PPU_crane_geometry_CATProduct.expressed_in.append(CATIA_language)
    ic_PPU_crane_geometry_CATProduct.stored_as.append(CATProduct)

    ic_PPU_crane_geometry_IAM = onto.information_concretization("ic_PPU_crane_geometry_IAM")
    ic_PPU_crane_geometry_IAM.concretizes.append(PPU_crane_geometry)
    ic_PPU_crane_geometry_IAM.expressed_in.append(Inventor_language)
    ic_PPU_crane_geometry_IAM.stored_as.append(IAM)

    ic_PPU_crane_behavior_UMLact_PapyrusUML = onto.information_concretization("ic_PPU_crane_behavior_UMLact_PapyrusUML")
    ic_PPU_crane_behavior_UMLact_PapyrusUML.concretizes.append(PPU_crane_behavior)
    ic_PPU_crane_behavior_UMLact_PapyrusUML.expressed_in.append(UML_activity_diagram)
    ic_PPU_crane_behavior_UMLact_PapyrusUML.stored_as.append(PapyrusUML)

    ic_PPU_crane_behavior_UMLact_Pdf = onto.information_concretization("ic_PPU_crane_behavior_UMLact_Pdf")
    ic_PPU_crane_behavior_UMLact_Pdf.concretizes.append(PPU_crane_behavior)
    ic_PPU_crane_behavior_UMLact_Pdf.expressed_in.append(UML_activity_diagram)
    ic_PPU_crane_behavior_UMLact_Pdf.stored_as.append(Pdf)

    ic_PPU_crane_behavior_ST_codesys = onto.information_concretization("ic_PPU_crane_behavior_ST_codesys")
    ic_PPU_crane_behavior_ST_codesys.concretizes.append(PPU_crane_behavior)
    ic_PPU_crane_behavior_ST_codesys.expressed_in.append(Structured_text)
    ic_PPU_crane_behavior_ST_codesys.stored_as.append(Codesys_proprietary)
    ic_PPU_crane_behavior_ST_codesys.status_complete = [True]
    ic_PPU_crane_behavior_ST_codesys.timestamp = [datetime(year = 2019, month = 10, day = 10, hour = 23, minute = 7, second = 33)]

    ic_PPU_crane_behavior_ST_plcopen = onto.information_concretization("ic_PPU_crane_behavior_ST_plcopen")
    ic_PPU_crane_behavior_ST_plcopen.concretizes.append(PPU_crane_behavior)
    ic_PPU_crane_behavior_ST_plcopen.expressed_in.append(Structured_text)
    ic_PPU_crane_behavior_ST_plcopen.stored_as.append(PLCopenXML)

    ic_PPU_crane_behavior_ST_twincat = onto.information_concretization("ic_PPU_crane_behavior_ST_twincat")
    ic_PPU_crane_behavior_ST_twincat.concretizes.append(PPU_crane_behavior)
    ic_PPU_crane_behavior_ST_twincat.expressed_in.append(Structured_text)
    ic_PPU_crane_behavior_ST_twincat.stored_as.append(Twincat_proprietary)

    ic_PPU_crane_structure_UMLclass_PapyrusUML = onto.information_concretization("ic_PPU_crane_structure_UMLclass_PapyrusUML")
    ic_PPU_crane_structure_UMLclass_PapyrusUML.concretizes.append(PPU_crane_structure)
    ic_PPU_crane_structure_UMLclass_PapyrusUML.expressed_in.append(UML_class_diagram)
    ic_PPU_crane_structure_UMLclass_PapyrusUML.stored_as.append(PapyrusUML)

    ic_PPU_crane_structure_UMLclass_Pdf = onto.information_concretization("ic_PPU_crane_structure_UMLclass_Pdf")
    ic_PPU_crane_structure_UMLclass_Pdf.concretizes.append(PPU_crane_structure)
    ic_PPU_crane_structure_UMLclass_Pdf.expressed_in.append(UML_class_diagram)
    ic_PPU_crane_structure_UMLclass_Pdf.stored_as.append(Pdf)

    ic_PPU_structure_UMLclass_PapyrusUML = onto.information_concretization("ic_PPU_structure_UMLclass_PapyrusUML")
    ic_PPU_structure_UMLclass_PapyrusUML.concretizes.append(PPU_structure)
    ic_PPU_structure_UMLclass_PapyrusUML.expressed_in.append(UML_class_diagram)
    ic_PPU_structure_UMLclass_PapyrusUML.stored_as.append(PapyrusUML)

    ic_PPU_techreport_Docx = onto.information_concretization("ic_PPU_techreport_Docx")
    ic_PPU_techreport_Docx.part.extend([ic_PPU_crane_behavior_UMLact_Pdf, ic_PPU_crane_structure_UMLclass_Pdf])
    ic_PPU_techreport_Docx.stored_as.append(Docx)

    ic_PPU_techreport_Pdf = onto.information_concretization("ic_PPU_techreport_Pdf")
    ic_PPU_techreport_Pdf.part.extend([ic_PPU_crane_behavior_UMLact_Pdf, ic_PPU_crane_structure_UMLclass_Pdf])
    ic_PPU_techreport_Pdf.stored_as.append(Pdf)

## information carriers
    Harddrive1 = onto.information_carrier("Harddrive1")
    Harddrive2 = onto.information_carrier("Harddrive2")
## information carrier relations
    Harddrive1.captures.extend([ic_PPU_BOM, ic_PPU_crane_geometry_IAM, ic_PPU_crane_geometry_CATProduct, ic_PPU_behavior_ST_plcopen, 
        ic_PPU_crane_behavior_UMLact_PapyrusUML, ic_PPU_crane_behavior_ST_codesys, ic_PPU_crane_behavior_ST_plcopen, 
        ic_PPU_structure_UMLclass_PapyrusUML, ic_PPU_codesys_instructions_NL_Pdf, ic_PPU_codesys_instructions_NL_Docx])
    Harddrive2.captures.extend([ic_PPU_crane_geometry_IAM, ic_PPU_crane_behavior_UMLact_PapyrusUML, ic_PPU_crane_behavior_ST_twincat])

## PPU relations
    PPU.part = [PPU_conveyor, PPU_crane, PPU_stack, PPU_stamp]
    PPU_behavior.part.append(PPU_crane_behavior)
    PPU_crane.part = [PPU_crane_monostable_cylinder, PPU_crane_turning_table, PPU_crane_vacuum_gripper]
    PPU_crane_behavior.describes.append(PPU_crane)
    PPU_crane_geometry.describes.append(PPU_crane)
    PPU_crane_structure.describes.append(PPU_crane)
    PPU_structure.describes.append(PPU)

## relations between information concretizations and actors
    Eve.subscribes.extend([ic_PPU_crane_behavior_ST_codesys])
    Felix.subscribes.extend([ic_PPU_BOM,ic_PPU_crane_behavior_UMLact_PapyrusUML])
    Matthias.subscribes.extend([ic_PPU_BOM,ic_PPU_crane_behavior_UMLact_PapyrusUML])

# save onto
    onto.save(file=output)
