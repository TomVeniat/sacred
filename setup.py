#!/usr/bin/env python
# coding=utf-8

from setuptools import setup
import sacred

classifiers = """
Development Status :: 3 - Alpha
Intended Audience :: Science/Research
License :: OSI Approved :: GNU General Public License v3 (GPLv3)
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.2
Programming Language :: Python :: 3.4
Programming Language :: Python :: Implementation :: PyPy
Topic :: Utilities
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Artificial Intelligence
Topic :: Software Development :: Libraries
Topic :: Software Development :: Quality Assurance
"""


setup(
    name='sacred',
    version=sacred.__version__,

    author='Klaus Greff',
    author_email='qwlouse@gmail.com',

    packages=['sacred'],
    test_suite="tests",
    scripts=[],
    install_requires=[
        "pymongo >= 2.0", 'pytest',
    ],

    classifiers=filter(None, classifiers.split('\n')),
    description='Facilitates reproducible research.',
    long_description=open('README.md').read(),
    license='LICENSE',
)
