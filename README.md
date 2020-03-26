# iniPy: a lightweight python project initalizer
iniPy is a lightweight script that automatically creates a new python project according to your given specifications.

## Usage
Using iniPy is as simple as it gets, it's all based on command line arguments.

For example:

`$ python3 -m inipy basic daffodil`

will create a new basic Python project (directory with `__init__.py` and `__main__.py`) with the name __daffodil__.

## Support
As of 03.26.2020, iniPy supports building the following project types:
- basic tree (basic):
    - `project`
        - `__init__.py`
        - `__main__.py`
- <a href="https://github.com/django/django/tree/master/django/conf/project_template">django tree</a> (django)

## Installation
You can install iniPy with pip using the following command:<br/><br/>
`pip3 install git+https://github.com/kevinshome/inipy.git`
