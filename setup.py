'''setup.py'''

from setuptools import setup, find_packages


with open("requirements.txt") as reqs_file:
    REQS = [line.rstrip() for line in reqs_file.readlines() if line[0] not in ['\n', '-', '#']]

setup(
    name =  'dummy',
    description = 'A package to do nothing.',
    url =  'https://github.com/gorkazl/NetDynFlow',
    version =  '0.0.0',
    #license =  'Apache License 2.0',

    author =  'Nobody',
    #author_email =  'galib@zamora-lopez.xyz',

    install_requires =  REQS,
    packages =  find_packages(exclude=['doc', '*tests*']),
    scripts =  [],
    include_package_data =  True,

    keywords =  'graph theory, complex networks, network analysis, weighted networks',
    classifiers =  [
        #'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        #'Intended Audience :: Education',
        #'Intended Audience :: Science/Research',
        #'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        #'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
