# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages


setup(
    name='django-google-product-feeder',
    version='0.0.1dev',
    author=u'René Fleschenberg',
    author_email='rene@fleschenberg.net',
    packages=find_packages(),
    url='',
    license='All rights reserved',
    description='Django app for feeding products to Google',
    long_description='Django app for feeding products to Google',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Django>=1.6'
    ],
)
