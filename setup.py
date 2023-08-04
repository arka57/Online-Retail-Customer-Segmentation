from setuptools import setup,find_packages
from typing import List 

PROJECT_NAME="Online Retail Customer Segmentation"
VERSION="0.1"
AUTHOR="Arkabrato Chakraborty"
DESCRIPTION="Clustering Project"
AUTHOR_EMAIL="arkabrato@gmail.com"
REQUIREMENTS_FILE_NAME="requirements.txt"

HYPEN_E_DOT="-e ."

def get_requirments_list():
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readlines()
        requirement_list=[ requirement_name.replace("\n","") for requirement_name in requirement_list]

        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)
        return requirement_list    

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires=get_requirments_list()
     )