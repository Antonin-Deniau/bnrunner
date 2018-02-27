from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bnrunner',
    version='1.0.0',
    description='Run binaryninja scripts.',
    long_description=long_description,
    url='https://github.com/Antonin-Deniau/bnrunner',
    author='DENIAU Antonin',
    author_email='antonin.deniau@protonmail.com',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='reverse engineering cracking hacking malware',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[],

    extras_require={},

    entry_points={
      'console_scripts': [
        'bnrunner=bnrunner.main:main',
      ],
    },
)