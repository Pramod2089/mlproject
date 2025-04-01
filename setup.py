from setuptools import find_packages, setup
from typing import List

HYPHON_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Strip instead of replace("\n", "")

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Pramod',
    author_email='pramodkumar.rgec@gmail.com',
    packages=find_packages(),  # Fixed typo: "find_package()" → "find_packages()"
    install_requires=get_requirements('requirements.txt')
)
