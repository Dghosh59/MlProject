from setuptools import find_packages,setup
from typing import List

E_DOT = "-e ."

def get_requirements(file_path : str) -> List[str]:

    with open(file_path,"r") as f:

        requirements = f.readlines()

    requirements =  [i.replace("\n","") for i in requirements]

    if E_DOT in requirements :
        requirements.remove(E_DOT)
        
    return requirements

setup(
    name = "MlProject",
    version = "0.0.1",
    author = "Debrup",
    author_email="debrupghosh59@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")

)