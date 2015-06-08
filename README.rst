kotti_actions
***************

This is a backend only extension that allows to add one or more
action manager groups (navigation, header and footer links).
Links can be nested. A sort of simple Plone's portal_actions implementation.

|build status|_

`Find out more about Kotti`_

Development happens at https://github.com/Kotti/kotti_actions

.. |build status| image:: https://secure.travis-ci.org/Kotti/kotti_actions.png?branch=master
.. _build status: http://travis-ci.org/Kotti/kotti_actions
.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti

You can add action managers only on navigation roots in this release.

This is a plugin that helps you to build a complex tree menu. Three different
menu areas are available:

* NavigationActionManager, for navigation links
* HeaderActionManager, for header links
* FooterActionManager, for footer links

The following areas are only containers that may contain LinkAction items.
LinkAction items are folderish links that could be nested, with a title, a description
and an optional link field.

The link field acceps the following values:

* external urls (eg: http://google.com)
* internal urls (eg: /about)

The link field is not mandatory since you may want to create nested groups of sublinks or
not clickable link groups.

This plugin is intended to be used with Kotti as a backend administration area, with 
a completely independent frontend.

Funding
=======

Developed with the support of:

* MIP (International Business School of Politecnico di Milano) - http://www.mip.polimi.it
