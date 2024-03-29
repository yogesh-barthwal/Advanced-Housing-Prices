from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT= '-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    This will return a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(

    name= 'Advanced Housing Prices-End to End',
    version= '1.0',
    author= 'Yogesh',
    email= 'barthwal.yogesh@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')

)