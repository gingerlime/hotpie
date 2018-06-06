#!/usr/bin/env python

from setuptools import setup, find_packages
import os

try:
    from pypandoc import convert

    def read_md(readme_file):
        return convert(readme_file, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")

    def read_md(readme_file):
        with open(readme_file, 'r') as f:
            return f.read()

setup(
    name='hotpie',
    version=open('VERSION').read().strip(),
    description='OATH HOTP/TOTP implementation in python',
    long_description=read_md('README.md'),
    author='Yoav Aner',
    author_email='yoav@gingerlime.com',
    url='https://github.com/gingerlime/hotpie',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    zip_safe=False,
    license=open("LICENSE").read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
)