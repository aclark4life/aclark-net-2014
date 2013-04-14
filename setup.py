from setuptools import find_packages
from setuptools import setup

setup(
    entry_points={
        'paste.app_factory': 'main=aclarknet:main',
    },
    install_requires=[
        'deform',
        'pyramid',
        'waitress',
    ],
    name='aclarknet',
    packages=find_packages(),
)
