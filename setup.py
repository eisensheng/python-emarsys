#!/usr/bin/env python
from setuptools import setup, find_packages

CLASSIFIERS = ["Development Status :: 2 - Pre-Alpha",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: Apache Software License",
               "Natural Language :: English",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Programming Language :: Python :: 2",
               "Programming Language :: Python :: 2.7",
               "Programming Language :: Python :: 3",
               "Programming Language :: Python :: 3.5",
               "Programming Language :: Python :: Implementation :: CPython",
               "Topic :: Software Development :: Libraries :: Python Modules"]

KEYWORDS = "emarsys api wrapper"

REPO_URL = "https://github.com/eugene-wee/python-emarsys"

setup(name="python-emarsys",
      version='0.2',
      description="""Emarsys REST API wrapper for Python.""",
      author='Eugene Wee',
      url=REPO_URL,
      packages=find_packages(),
      download_url=REPO_URL + "/tarball/master",
      classifiers=CLASSIFIERS,
      keywords=KEYWORDS,
      zip_safe=True,
      install_requires=["six", "requests", "pytz"])
