========
Overview
========

*This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the*
`Zope Toolkit project <http://docs.zope.org/zopetoolkit/>`_.

This package provides ZCML directives for configuring browser views.
More specifically it defines the following ZCML directives:

 * browser:page
 * browser:pages
 * browser:view

These directives also support menu item registration for pages, when
``zope.browsermenu`` package is installed. Otherwise, they simply ignore
the menu attribute.
