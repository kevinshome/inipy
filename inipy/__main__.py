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

def inipy_init(p_type, p_name):
    project_type = p_type
    project_name = p_name
    if project_type.lower() == "basic":
        basic_init(project_name)
    if project_type.lower() == "django":
        import pkgutil
        if pkgutil.find_loader("django"):
            import re
            from django.core.management import execute_from_command_line
            sys.argv = ['django-admin', 'startproject', project_name]
            sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
            execute_from_command_line()
        else:
            print("It seems that django is not installed...")
            yn = input("Would you like to install it now? (y/n): ")
            if yn.lower() == "y":
                import subprocess
                subprocess.check_call([sys.executable, "-m", "pip", "install", "django"])
                inipy_init(p_type, p_name)
            else:
                exit(2)

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
TYPE        project type ( basic, django )\n\
NAME        project name\n\
\n\
written in 2020 by kevinshome\n\
released under the terms of the MIT License")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        inipy_init(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2 and sys.argv[1] == "help":
        help()
    else:
        print("unrecognized/invalid input...")
        exit("run 'inipy help' for the help menu")