from setuptools import find_packages,setup
from typing import List

#function will return list of requirements
def get_all_packages(fileName:str)->List[str]:
    package=[]
    with open(fileName) as fileObj:
        package = fileObj.readlines()
        #replace \n with blank as every new line must have \n
        package = [entry.replace("\n","") for entry in package]
        if '-e .' in package:
            package.remove('-e .')

    return package



setup(

    name = "myDSProject",
    version="0.0.1",
    author="Paritosh",
    author_email = "rikkiparitosh43@gmail.com",
    packages=find_packages(),
    #install_requires=['pandas','numpy']
    #instead of writing so many package in single file lets create different file for that
    install_requires= get_all_packages('requirements.txt')
)