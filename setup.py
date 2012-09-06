# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

version = '0.1'

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(name='fly.skels',
      version=version,
      description="Skeletons used on fly",
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules"],
      keywords='',
      author='Young King',
      author_email='youngking@flyzen.com',
      url='http://www.flyzen.com',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['fly'],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['Nose'],
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'PasteScript',
          'Cheetah',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      fly_namespace = fly.skels.templates:Namespace
      fly_buildout = fly.skels.templates:Buildout
      fly_full = fly.skels.templates:Full
      """,
      )

