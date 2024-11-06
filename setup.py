from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e."

def get_requirememts(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # just 1 time gets all names
        requirements = [req.replace("\n","") for req in requirements] # nl is replaced by nothingness
    
    # to remove -e.
    if(HYPEN_E_DOT in requirements):
        requirements.remove(HYPEN_E_DOT)
        # as this is a command we dont need it in requirements
    
    return requirements
    
setup(
    name='Fault Detection',
    version='0.0.1',
    author='shaik shuaib aakif',
    author_email='aakif9866@gmail.com',
    install_requirements= get_requirememts('requirements.txt'), 
    # for above fn param is txt file
    packages=find_packages(),
    
)