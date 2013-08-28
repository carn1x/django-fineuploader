#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
try:
    from setuptools import setup
except:
    from distutils.core import setup

README = open(path.join(path.dirname(__file__), 'README.rst')).read()


setup(
    name='django-fineuploader',
    version='0.1',
    packages=['fineuploader'],
    include_package_data=True,
    license='MIT License',
    description='A simple and useless django integration with fineuploader',
    long_description=README,
    url='https://github.com/marsam/django-fineuploader',
    author='Mario Rodas',
    author_email='rodasmario2@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
