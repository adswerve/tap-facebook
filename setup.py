#!/usr/bin/env python

from setuptools import setup

setup(name='tap-facebook',
      version='1.12.8',
      description='Singer.io tap for extracting data from the Facebook Ads API',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_facebook'],
      install_requires=[
          'attrs~=20.3.0',
          'backoff~=1.8.0',
          'pendulum==2.1.2',
          'facebook_business==21.0.5',
          'requests~=2.26.0',
          'singer-python~=5.12.1',
      ],
      extras_require={
          'dev': [
              'pylint',
              'ipdb',
              'nose',
          ]
      },
      entry_points='''
          [console_scripts]
          tap-facebook=tap_facebook:main
      ''',
      packages=['tap_facebook'],
      package_data = {
          'tap_facebook/schemas': [
              # add schema.json filenames here
          ],
          'tap_facebook/schemas/shared': [
          ]
      },
      include_package_data=True,
)
