'''
explicit setup
'''
import sys
from setuptools import setup, find_packages

install_requires = []

py_version = sys.version_info[:3]

# # argparse and futures were only added after 3.x
# if py_version < (3,):
#     install_requires += ['argparse', 'futures']


setup(
    name='explicit',
    version='0.0.1',
    author='Levi Noecker',
    author_email='levi.noecker@gmail.com',
    url='https://github.com/levi-rs/explicit',
    packages=find_packages(),
    description='Easy explicit wait helpers for Selenium',
    install_requires=install_requires,
    tests_require=[
        'mock',
        'pytest',
    ],
    classifiers=[
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.x',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    test_suite="tests",
)
