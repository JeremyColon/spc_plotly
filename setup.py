from setuptools import find_packages, setup

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="spc_plotly",
    version="0.1.0",
    description="XmR chart with Plotly",
    long_description="""
    This package creates a XmR chart according to the concepts of Statistical Process Control.
    The chart itself is built using Plotly and can be embedded in a dash application.
    """,
    long_description_content_type="text/markdown",
    author="Jeremy Colón",
    author_email="jeremycolon24@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    packages=["spc_plotly"],
    include_package_data=True,
    install_requires=["pandas", "numpy", "plotly"],
)
