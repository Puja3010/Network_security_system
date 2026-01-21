''' 
The setup.py file is an essential part of packaging and 
distributing Python Projects. It is used by setuptools to define the 
configuration of your project such as its metadata dependencies and more.
'''
from setuptools import find_packages,setup #scan through all the folders and where there is __init.py, it is going to consider a package
from typing import List

def get_requirements()->List[str]:
    """
    This funcrion return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            #Process each line 
            for line in lines:
                requirement=line.strip()
                #ignore the empty lines and ignore -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file  not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version ="0.0.1",
    author='Puja3010',
    author_email="puja.rout30@gmail.com",
    packages=find_packages(),
    install_reqiures=get_requirements()
)