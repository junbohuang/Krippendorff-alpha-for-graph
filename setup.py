from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='krippendorff-graph',
    version='0.1.3',
    description='A Python package for computing krippendorffs alpha for graph (modified from https://github.com/grrrr/krippendorff-alpha/blob/master/krippendorff_alpha.py)',
    url='anonymous url',
    author='anonymous author',
    author_email='anonymous email',
    license='Apache 2 License',
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=["krippendorff_graph"]
)
