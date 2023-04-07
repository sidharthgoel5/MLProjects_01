from setuptools import find_packages,setup
from typing import List


Hpyen_E_dot = '-e.'
def get_requirements(file_path:str) ->List[str]:
    '''This function will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements ]

        if Hpyen_E_dot in requirements:
            requirements.remove(Hpyen_E_dot)

    return requirements        


setup(
    name='MLProjects',
    version='0.0.1',
    author='Siddharth Goyal',
    author_email='Sidharthgoel5@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)