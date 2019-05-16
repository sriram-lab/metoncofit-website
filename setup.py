"""
Setup for MetOncoFit application environment
@author: Scott Campit
"""

from setuptools import setup
setup(
    name='metoncofit',
    packages=['metoncofit'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pandas',
        'numpy',
        'ploty',
        'dash',
        'dash_bootstrap_components'
    ],
)
