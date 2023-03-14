from setuptools import find_packages,setup

from typing import List
def get_requirements(file_path:str)->List[str]:
    #
    #the function takes the txt file and returns the strings in list, also readlines() has /n at
     #the end which we don't need, use listcompre to get rid of it
     
    
    HYPHEN_E_Dot='-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n"," ") for req in requirements] 

        # requirementsTXT conection automatic running maintenance
        if HYPHEN_E_Dot in requirements:
            requirements.remove(HYPHEN_E_Dot)

    return requirements

setup(
    name='mlp2023',
    version='0.1',
    author='gt',
    packages=find_packages(),
    ## install_requires=['pandas','numpy','seaborn ']
    install_requires=get_requirements('requirements.txt')
)