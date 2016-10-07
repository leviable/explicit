'''
explicit setup
'''
from os import path

import versioneer
from setuptools import setup, find_packages

here = path.dirname(path.abspath(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

install_requires = ['selenium']

setup(
    name='explicit',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Levi Noecker',
    author_email='levi.noecker@gmail.com',
    url='https://github.com/levi-rs/explicit',
    keywords=['selenium', 'explicit', 'wait', 'implicit'],
    packages=find_packages(),
    description='Easy explicit wait helpers for Selenium',
    license='MIT',
    long_description=long_description,
    install_requires=install_requires,
    tests_require=[
        'mock',
        'pytest',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    test_suite="tests",
)
