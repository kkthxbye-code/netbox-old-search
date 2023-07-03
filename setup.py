#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    author="kkthxbye-code",
    author_email="festll234@gmail.com",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    description="Brings back the old search functionality to NetBox",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords=["netbox", "netbox-plugin"],
    name="netbox-old-search",
    packages=find_packages(),
    url="https://github.com/kkthxbye-code/netbox-old-search",
    version="0.1.0",
    zip_safe=False,
)
