kotti_actions
***************

.. |build status stable| image:: https://img.shields.io/travis/truelab/kotti_actions/master.svg?style=flat-square
.. _build status stable: http://travis-ci.org/truelab/kotti_actions

This is a backend only extension that allows to add one or more
action manager groups (navigation, header and footer links).
Links can be nested. A sort of simple Plone's portal_actions implementation.

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
