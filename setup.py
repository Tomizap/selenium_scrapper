from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

DESCRIPTION = """
Simple Python Package
"""

setup(
    name="selenium_driver",
    # version="0.0.1",
    author="TZ",
    author_email="zaptom.pro@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["selenium", "selenium_driver"],
    dependency_link=[
        "git+git://github.com/Tomizap/selenium-scrapper.git"
    ],
    keywords=[],
    classifiers=[]
)
