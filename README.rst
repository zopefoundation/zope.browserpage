======================
 ``zope.browserpage``
======================

.. image:: https://img.shields.io/pypi/v/zope.browserpage.svg
        :target: https://pypi.python.org/pypi/zope.browserpage/
        :alt: Latest release

.. image:: https://img.shields.io/pypi/pyversions/zope.browserpage.svg
        :target: https://pypi.org/project/zope.browserpage/
        :alt: Supported Python versions

.. image:: https://github.com/zopefoundation/zope.browserpage/actions/workflows/tests.yml/badge.svg
        :target: https://github.com/zopefoundation/zope.browserpage/actions/workflows/tests.yml

.. image:: https://coveralls.io/repos/github/zopefoundation/zope.browserpage/badge.svg?branch=master
        :target: https://coveralls.io/github/zopefoundation/zope.browserpage?branch=master

.. note::

   This package is at present not reusable without depending on a large
   chunk of the Zope Toolkit and its assumptions. It is maintained by the
   `Zope Toolkit project <http://docs.zope.org/zopetoolkit/>`_.

This package provides ZCML directives for configuring browser views.
More specifically it defines the following ZCML directives:

- ``browser:page``
- ``browser:pages``
- ``browser:view``

These directives also support menu item registration for pages, when
``zope.browsermenu`` package is installed. Otherwise, they simply ignore
the menu attribute.
