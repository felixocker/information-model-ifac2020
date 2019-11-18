#!/usr/bin/env python3
"""module to preprocess query results: only use class / instance name and put a colon before it"""

def pp(li):
    newlist=[]
    for i in li:
        tempelement = str(i[0])
        templist = tempelement.split(".")
        newlist.append(":"+templist[-1])
    return newlist
