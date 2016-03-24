# is set then it will delete the os.link method which triggers a slower, but
# functional, fallback in setuptools/distutils by avoiding the hard links.
import os
if os.getenv('VBOX_MOUNTED'):

   del os.link

from setuptools import setup
from setuptools import find_packages


with open('README.rst', 'r') as readmefile:

   README = readmefile.read()

setup(
   name='IBDB',
   version='0.1.0',
   url='https://github.com/richeyh/cs373-idb.git',
   description='we store books',
   packages=find_packages(exclude=['tests', 'build', 'dist', 'docs']),
   install_requires=[
       'flask'
   ],
   include_package_data=True,
   zip_safe=False,
)