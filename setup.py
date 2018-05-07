#!/usr/bin/python
# -*- coding: UTF-8 -*-
from setuptools import setup

from oshino_hw.version import get_version

setup(name="oshino-hw",
      version=get_version(),
      description="An agent to retrieve HW info",
      author="Šarūnas Navickas",
      packages=["oshino_hw"],
      install_requires=["psutil==5.2.2", "oshino"],
      test_suite="pytest",
      tests_require=["pytest", "pytest-cov", "pytest-asyncio"],
      setup_requires=["pytest-runner"]
      )
