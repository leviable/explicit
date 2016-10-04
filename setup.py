'''
explicit setup
'''
import versioneer
from setuptools import setup, find_packages

install_requires = ['versioneer', ]

setup(
    name='explicit',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    test_suite="tests",
)
