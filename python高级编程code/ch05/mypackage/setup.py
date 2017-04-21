from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='mypackage',
      version=version,
      description="My package",
      long_description="""\
This is my first package""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='package my',
      author='carlshen\x1b[D\x1b[D\x1b[D\x1b[D shen',
      author_email='xiangfeng.shen@gmail.com',
      url='http://localhost',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
