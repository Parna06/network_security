'''
The setup.py file is a python essential part of packaging and distributing
Python projects. It is a used by setuptools (or distutils in older python version)
to define the configuration of the project, such as its metadata, dependencies, and more
'''
from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return the list of requirements

    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            ## Read lines from the file
            lines = file.readlines()
            ## process each line
            for line in lines:
                requirement = line.strip()
                ## ignore the empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('Requirements.txt file is not found')

    return requirement_lst

setup(
    name = "NetworkSecurity",
    version= "0.0.1",
    author="Parna Das",
    author_email="meparnadas@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)