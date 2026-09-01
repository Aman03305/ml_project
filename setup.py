from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> List[str]:

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#")]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements
setup(
    name="ml_project",
    version="0.1.0",
    author="Aman Gupta",
    author_email="guptaama0000@gmail.com",
    description="A machine learning project",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)