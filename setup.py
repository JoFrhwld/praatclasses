from setuptools import setup

import os
long_description = 'A bunch of praat object classes for python'
if os.path.exists('README.rst'):
    long_description = open('README.rst').read()

setup(name='praatclasses',
      version='0.1',
      description='A bunch of praat object classes for python',
      long_description = long_description,
      url='http://github.com/jofrhwld/praatclasses',
      author='Ingrid Rosenfelder',
      maintainer = 'Josef Fruehwald',
      maintainer_email = 'jofrhwld@gmail.com',
      license='MIT',
      packages=['praatclasses'],
      zip_safe=False)