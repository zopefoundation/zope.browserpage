=========
 Changes
=========

6.0 (2025-09-12)
================

- Replace ``pkg_resources`` namespace with PEP 420 native namespace.


5.1 (2025-06-26)
================

- Add support for Python 3.12, 3.13.

- Drop support for Python 3.7, 3.8.

5.0 (2023-01-19)
================

- Drop support for Python 2.7, 3.5, 3.6.

- Add support for Python 3.8, 3.9, 3.10, 3.11.

- Drop support for running the tests using ``python setup.py test``.
  (`#11 <https://github.com/zopefoundation/zope.browserpage/issues/11>`_)


4.4.0 (2019-06-18)
==================

- Fix regression in ``allowed_attributes`` and ``allowed_interface``.
  (`#7 <https://github.com/zopefoundation/zope.browserpage/pull/7>`_)

- Drop support for Python 3.4.


4.3.0 (2018-10-05)
==================

- Add support for Python 3.7.


4.2.0 (2017-08-02)
==================

- Add support for Python 3.5 and 3.6.

- Drop support for Python 2.6 and 3.3.


4.1.0 (2014-12-24)
==================

- Fix deprecated unittest methods.

- Add explicit support for Python 3.4.

- Add explicit support for PyPy.


4.1.0a1 (2013-02-22)
====================

- Add support for Python 3.3.


4.0.0 (2012-07-04)
==================

- When registering views, no longer pass the deprecated 'layer' agrument
  to ``zope.component.registerAdapter``.  Instead, pass ``(for_, layer)``
  as expected (forward-compatibility with ``zope.component`` 4.0.0).

- Replace deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Drop support for Python 2.4 and 2.5.


3.12.2 (2010-05-24)
===================

- Fix unit tests broken under Python 2.4 by the switch to the standard
  library ``doctest`` module.


3.12.1 (2010-04-30)
===================

- Prefer the standard library's ``doctest`` module to the one from
  ``zope.testing``.


3.12.0 (2010-04-26)
===================

- Move the implementation of ``tales:expressiontype`` here from
  ``zope.app.pagetemplate``.


3.11.0 (2009-12-22)
===================

- Move the named template implementation here from ``zope.app.pagetemplate``.


3.10.1 (2009-12-22)
===================

- Depend on the ``untrustedpython`` extra of ``zope.security``, since we
  import from ``zope.pagetemplate.engine``.


3.10.0 (2009-12-22)
===================

- Remove the dependency on ``zope.app.pagetemplate`` by moving
  ``viewpagetemplatefile``, ``simpleviewclass`` and
  ``metaconfigure.registerType`` into this package.


3.9.0 (2009-08-27)
==================

- Initial release. This package was split off from ``zope.app.publisher``.
