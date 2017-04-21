from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='package',
      version=version,
      description="my package",
      long_description="""\
my package""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='package',
      author='carlshen',
      author_email='xiangfeng.shen@gmail.com',
      url='http://localhost',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
