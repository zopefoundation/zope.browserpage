##############################################################################
#
# Copyright (c) 2007 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""zope.browserpage setup
"""
from setuptools import setup, find_packages, Extension

long_description = (open('README.txt').read() + '\n\n' +
                    open('CHANGES.txt').read())

setup(name='zope.browserpage',
      version = '3.9.0dev',
      url='http://pypi.python.org/pypi/zope.browserpage/',
      author='Zope Corporation and Contributors',
      author_email='zope-dev@zope.org',
      classifiers = ['Environment :: Web Environment',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: Zope Public License',
                     'Programming Language :: Python',
                     'Operating System :: OS Independent',
                     'Topic :: Internet :: WWW/HTTP',
                     'Framework :: Zope3',
                     ],
      description='ZCML directives for configuration browser views for Zope 3.',
      long_description=long_description,

      packages=find_packages('src'),
      package_dir={'': 'src'},

      namespace_packages=['zope'],
      include_package_data=True,
      install_requires=['setuptools',
                        'zope.app.pagetemplate',
                        'zope.browser',
                        'zope.component>=3.7.0',
                        'zope.configuration',
                        'zope.interface',
                        'zope.publisher>=3.8.0',
                        'zope.schema',
                        'zope.security',
                        'zope.traversing>3.7.0',
                        ],
      extras_require={
          'menu': ['zope.browsermenu'],
          'test': ['zope.testing', 'zope.browsermenu'],
          },

      zip_safe = False,
      )