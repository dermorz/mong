# coding: utf-8

import re
from setuptools import setup

with open("mong/mong.py") as f:
    version = re.search(
        r'^__version__\s*=\s*"(.*)"$',
        f.read(),
        re.M
    ).group(1)


with open("README.md", "rb") as f:
    try:
        import pypandoc
        description = pypandoc.convert('README.md', 'rst')
    except (IOError, ImportError):
        description = f.read()


setup(
    name="mong",
    packages=["mong"],
    entry_points={
        'gui_scripts': ['mong = mong.mong:main']
    },
    version=version,
    description="GUI client for mongodb.",
    long_description=description,
    author="Moritz Pein",
    author_email="moritz.pein@gmail.com",
    url="https://github.com/moritzpein/mong",
)
