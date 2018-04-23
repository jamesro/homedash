from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    homedashlicense = f.read()

setup(
    name='homedash',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license=homedashlicense,
    author='James Robinson',
    author_email='',
    description='A Dashboard for A Home with Live London Public Transport, Air Quality, Weather Updates',
    long_description=readme

)
