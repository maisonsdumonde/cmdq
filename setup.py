from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='cmdq',
      version=version,
      description="Simple command queue.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[],
      entry_points="""
          [console_scripts]
          cmdq = cmdq.cli:main
      """,
      )
