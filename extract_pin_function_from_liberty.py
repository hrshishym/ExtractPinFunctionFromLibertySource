#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input")
args = parser.parse_args()

from liberty.parser import parse_liberty

tlib = parse_liberty(open(args.input).read())

# library (sxlib013) {
print("library ({}) {{".format(tlib.args[0]))

for eachlib in tlib.groups:
    if eachlib.group_name != "cell":
        continue
    cellname = eachlib.args[0]
    # cell(a2_x2) { /* 2008-01-10:21h05 */
    print("cell({}) {{".format(cellname))

    for eachgroup in eachlib.groups:
        if eachgroup.group_name == "ff":
            # ff
            print("  ff({}) {{ ".format(",".join(eachgroup.args)))
            for eachkey in eachgroup.attributes.keys():
                print("    {} : {} ;".format(eachkey, eachgroup.attributes[eachkey]))
            print("  }")
        elif eachgroup.group_name == "pin":
            ## pin
            print("  pin({}) {{".format(eachgroup.args[0]))
            if "direction" in eachgroup.attributes.keys():
                print("    {} : {} ;".format("direction", eachgroup.attributes["direction"]))
            if "clock" in eachgroup.attributes.keys():
                print("    {} : {} ;".format("clock", eachgroup.attributes["clock"]))
            if "function" in eachgroup.attributes.keys():
                print("    {} : {} ;".format("function", eachgroup.attributes["function"]))
            print("  }")
    print("}")
print("}")

