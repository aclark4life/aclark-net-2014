from setuptools import find_packages
from setuptools import setup

setup(
    entry_points={
        'paste.app_factory': 'main=aclarknet:main',
    },
    install_requires=[
        'deform',
        'deform_bootstrap',
        'pyramid',
        'waitress',
    ],
    name='aclarknet',
    packages=find_packages(),
)
