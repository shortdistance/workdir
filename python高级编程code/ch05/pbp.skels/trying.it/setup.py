from setuptools import setup, find_packages

version = '0.1.0'

setup(name='trying.it',
      version=version,
      description='my trying it',
      long_description="""\
my trying it description""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='trying',
      author='carlshen',
      author_email='xiangfeng.shen@gmail.com',
      url='http://localhost',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['trying'],
      include_package_data=True,
      test_suite='nose.collector',
      test_requires=['Nose'],  
      zip_safe=True,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
