from setuptools import find_packages,setup
from typing import List



def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        # drop blanks, comments, and pip options that aren't valid deps
        requirements = [
            req for req in requirements
            if req and not req.startswith(('#', '-r', '--', '-e'))
        ]

        

    return requirements

setup(
name='ML_student_performance',
version='0.0.1',
author='Vicky',
author_email='vicky1jat6376831267@gmail.com',
packages=find_packages(),##search file which have __init__.py in them and treat them as packages
install_requires=get_requirements('requirements.txt')
)