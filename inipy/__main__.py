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

import os
import sys

def inipy_init():
    project_type = sys.argv[1]
    project_name = sys.argv[2]
    if project_type.lower() == "basic":
        basic_init(project_name)

def basic_init(project_name):
    os.mkdir(project_name)
    os.chdir(project_name)
    open("__init__.py", "w").close()
    open("__main__.py", "w").close()

def help():
    print("iniPy 0.1\n\
a lightweight python project initializer\n\
usage: inipy [TYPE] [NAME]\n\
\n\
PARAMETERS:\n\
\n\
TYPE        project type ( basic )\n\
NAME        project name\n\
\n\
written in 2020 by kevinshome\n\
released under the terms of the MIT License")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        inipy_init()
    elif len(sys.argv) == 2 and sys.argv[1] == "help":
        help()
    else:
        print("unrecognized/invalid input...")
        exit("run 'inipy help' for the help menu")