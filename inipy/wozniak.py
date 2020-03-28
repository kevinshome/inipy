#!/usr/bin/python3
'''
iniPy

a lightweight python project initalizer

'wozniak.py'
named after Steve Wozniak, inventor of the first real Personal Computer

this module deals with the initialization for iniPy

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

def inipy_init(p_type, p_name, no_main=False) -> bool :
    '''

    # function inipy_init()

    # arguments:
    p_type, p_name

    p_type         type of project to be initialized
    p_name         name of project to be initialized

    # description:
    the inipy_init() function takes in the given project type and name
    and uses that info to construct either a basic project folder, or
    a django project folder

    '''
    if p_type.lower() == "basic": # basic folder creation
        try:
            os.mkdir(p_name)
        except:
            exit("Error creating project folder...")
        os.chdir(p_name)
        try:
            open("__init__.py", "w").close()
            if not no_main:
                open("__main__.py", "w").close()
        except:
            exit("Error creating project files...")
    if p_type.lower() == "django": # django folder creation (necessary?)
        import pkgutil
        if pkgutil.find_loader("django"):
            import re
            from django.core.management import execute_from_command_line
            sys.argv = ['django-admin', 'startproject', p_name]
            sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
            execute_from_command_line()
        else: # either install django for user or exit code 2
            print("It seems that django is not installed...")
            yn = input("Would you like to install it now? (y/n): ")
            if yn.lower() == "y":
                import subprocess
                subprocess.check_call([sys.executable, "-m", "pip", "install", "django"])
                inipy_init(p_type, p_name)
            else:
                exit(2)

def help() -> None : # display help menu on command line
    print("iniPy 0.2\n\
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