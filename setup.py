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
        "Development Status :: 5 - Production/Stable",
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
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=["netbox", "netbox-plugin"],
    name="netbox-old-search",
    packages=find_packages(include=["netbox_old_search", "netbox_old_search.*"]),
    url="https://github.com/kkthxbye-code/netbox-old-search",
    version="1.0.0",
    zip_safe=False,
)
