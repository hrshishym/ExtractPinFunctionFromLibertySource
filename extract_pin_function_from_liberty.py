#!/usr/bin/env python

### Setting 
cell_attributes = ["clock_gating_integrated_cell"]
ff_attributes   = []
pin_attributes  = ["direction", "clock", "function", "state_function"]

import os
import sys
import re

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("-d", "--debug", action="store_true")
args = parser.parse_args()

from liberty.parser import parse_liberty

tdata = re.sub("\\\\\n", "", open(args.input).read())
tlib = parse_liberty(tdata)

if args.debug:
    import pprint
    pprint.pprint(tlib)

# library (sxlib013) {
print("library ({}) {{".format(tlib.args[0]))

for eachlib in tlib.groups:
    if eachlib.group_name != "cell":
        continue
    cellname = eachlib.args[0]
    # cell(a2_x2) { /* 2008-01-10:21h05 */
    print("cell({}) {{".format(cellname))

    if args.debug:
        print("==")
        pprint.pprint(eachlib)
        print("==")
        pprint.pprint(eachlib.attributes)
        print("==")

    ### Print cell attributes
    for eachattr in eachlib.attributes:
        for eachattr in cell_attributes:
            if eachattr in eachlib.attributes.keys():
                print("  {} : {} ;".format(eachattr, eachlib.attributes[eachattr]))

    ### Print sub group
    for eachgroup in eachlib.groups:
        if args.debug:
            print("====")
            pprint.pprint(eachgroup)
            print("====")
        if eachgroup.group_name == "ff":
            # ff
            print("  ff({}) {{ ".format(",".join(eachgroup.args)))
            for eachkey in eachgroup.attributes.keys():
                print("    {} : {} ;".format(eachkey, eachgroup.attributes[eachkey]))
            print("  }")
        elif eachgroup.group_name == "pin":
            ## pin
            print("  pin({}) {{".format(eachgroup.args[0]))
            for eachattr in pin_attributes:
                if eachattr in eachgroup.attributes.keys():
                    print("    {} : {} ;".format(eachattr, eachgroup.attributes[eachattr]))
            print("  }")
        elif eachgroup.group_name == "statetable":
            ## statetable
            tarr = []
            for i in eachgroup.args:
                tarr.append(str(i))
            print("  statetable( {} ) {{".format(" , ".join(tarr)))
            if "table" in eachgroup.attributes.keys():
                print("    {} : {} ;".format("table", re.sub(",", ", \\\n", str(eachgroup.attributes["table"]))))
            print("  }")
    print("}")
print("}")

