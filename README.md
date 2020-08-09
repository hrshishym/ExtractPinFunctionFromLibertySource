# ExtractPinFunctionFromLibertySource
Extract Pin and Function information from Synopsys Liberty (.lib)
This script is mainly used for generating liberty for [Yosys](https://github.com/YosysHQ/yosys) + [netlistsvg](https://github.com/nturley/netlistsvg) environment.

## Need Module

* [Liberty-parser](https://pypi.org/project/liberty-parser/)

```
pip install liberty-parser
```

## Usage

```
extract_pin_function_from_liberty.py INPUTFILE > OUTPUTFILE
```
