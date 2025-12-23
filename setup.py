'''
The setup.py file is used to define the metadata of the project and the dependencies required to run the project.
The setup.py file is an essential part of packaging and distributing python projects. 
It is used by setuptools (or distutils in older python versions) to define the configuration of your projects ,
 such as its metadata , dependencies , and more
'''

from setuptools import setup , find_packages

from typing import List

import os

def get_requirements()->List[str]:
    '''
    This function will return the list of requirements
    '''
    HYPHEN_E = '-e .'
    try:
        with open('requirements.txt','r') as file:
            ## Read lines from the file
            requirements = file.readlines()
            ## process the lines 
            requirements = [req.replace("\n","") for req in requirements]
            if HYPHEN_E in requirements:
                requirements.remove(HYPHEN_E)
        

    except Exception as e:
        print("The requirements.txt file is not found")
    return requirements

setup(
    name="network_security_project",
    version="0.0.1",
    author="Vasu",
    author_email="vasunavadiya21@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
print(get_requirements())



