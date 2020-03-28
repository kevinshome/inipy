#!/usr/bin/python3
'''
iniPy

a lightweight python project initalizer

/// MIT LICENSE ///

Copyright 2020 kevinshome

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE 
AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF 
OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import sys

from inipy.wozniak import inipy_init, help

if len(sys.argv) == 3:
    # if required amount of args are given, use them to create
    # new project
    inipy_init(sys.argv[1], sys.argv[2]) 
elif len(sys.argv) == 2 and sys.argv[1] == "help": # 'inipy help'
    help()
elif len(sys.argv) == 2 and sys.argv[1] == "help": # 'inipy help'
    print("Saucy (0.2)")
else: # if no args / wrong amount of args are given
    print("unrecognized/invalid input...")
    exit("run 'inipy help' for the help menu")