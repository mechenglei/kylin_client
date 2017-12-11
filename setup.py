# -*- coding: utf-8 -*-

__author__ = 'chenglei'

from setuptools import setup, find_packages

setup(
    name='kylin_client',
    version='0.1.1',
    description=(
        'kylin api client'
    ),
    long_description=open('README.rst').read(),
    author='chenglei',
    author_email='mechenglei@163.com',
    license='BSD License',
    packages=find_packages(),
    platforms=['win7', 'linux'],
    url='https://github.com/mechenglei/kylin_client',
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries'
    ]
)
