# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from pytest import mark


def test_login_required_add_navigation(webtest, root):
    """ Add view requires login """
    from zope.interface import alsoProvides
    from kotti.interfaces import INavigationRoot
    alsoProvides(root, INavigationRoot)
    resp = webtest.get('/add_action_manager_navigation')
    assert resp.status_code == 302


def test_login_required_add_header(webtest, root):
    """ Add view requires login """
    from zope.interface import alsoProvides
    from kotti.interfaces import INavigationRoot
    alsoProvides(root, INavigationRoot)
    resp = webtest.get('/add_action_manager_header')
    assert resp.status_code == 302


def test_login_required_add_footer(webtest, root):
    """ Add view requires login """
    from zope.interface import alsoProvides
    from kotti.interfaces import INavigationRoot
    alsoProvides(root, INavigationRoot)
    resp = webtest.get('/add_action_manager_footer')
    assert resp.status_code == 302


@mark.user('admin')
def test_add_inavigation_action(webtest, root):
    """ Not INavigationRoot"""
    assert '/add_action_manager_navigation' not in webtest.get('/').body

    from zope.interface import alsoProvides
    from kotti.interfaces import INavigationRoot
    alsoProvides(root, INavigationRoot)
    assert '/add_action_manager_navigation' in webtest.get('/').body


@mark.user('admin')
def test_add_navigation_action(webtest, root):
    from zope.interface import alsoProvides
    from kotti.interfaces import INavigationRoot
    alsoProvides(root, INavigationRoot)

    resp = webtest.get('/add_action_manager_navigation')

    # submit empty form
    form = resp.forms['deform']
    assert form['title'].value
    resp = form.submit('save')
    assert resp.status_code == 302
    resp = resp.follow()
    assert 'Item was added.' in resp.body


@mark.user('admin')
def test_add_header_action(webtest, root):
    from zope.interface import alsoProvides
    from kotti.interfaces import INavigationRoot
    alsoProvides(root, INavigationRoot)

    resp = webtest.get('/add_action_manager_header')

    # submit empty form
    form = resp.forms['deform']
    assert form['title'].value
    resp = form.submit('save')
    assert resp.status_code == 302
    resp = resp.follow()
    assert 'Item was added.' in resp.body


@mark.user('admin')
def test_add_footer_action(webtest, root):
    from zope.interface import alsoProvides
    from kotti.interfaces import INavigationRoot
    alsoProvides(root, INavigationRoot)

    resp = webtest.get('/add_action_manager_footer')

    # submit empty form
    form = resp.forms['deform']
    assert form['title'].value
    resp = form.submit('save')
    assert resp.status_code == 302
    resp = resp.follow()
    assert 'Item was added.' in resp.body


@mark.user('admin')
def test_add_navigation_action_one_time(webtest, root):
    """ portlet manager can be added just one time.
    """
    from zope.interface import alsoProvides
    from kotti.interfaces import INavigationRoot
    alsoProvides(root, INavigationRoot)

    assert '/add_action_manager_navigation' in webtest.get('/').body

    resp = webtest.get('/add_action_manager_navigation')

    # submit empty form
    form = resp.forms['deform']
    assert form['title'].value
    resp = form.submit('save')
    assert resp.status_code == 302
    resp = resp.follow()
    assert 'Item was added.' in resp.body

    assert '/add_action_manager_navigation' not in webtest.get('/').body


@mark.user('admin')
def test_add_header_action_one_time(webtest, root):
    """ portlet manager can be added just one time
    """
    from zope.interface import alsoProvides
    from kotti.interfaces import INavigationRoot
    alsoProvides(root, INavigationRoot)

    assert '/add_action_manager_header' in webtest.get('/').body

    resp = webtest.get('/add_action_manager_header')

    # submit empty form
    form = resp.forms['deform']
    assert form['title'].value
    resp = form.submit('save')
    assert resp.status_code == 302
    resp = resp.follow()
    assert 'Item was added.' in resp.body

    assert '/add_action_manager_header' not in webtest.get('/').body


@mark.user('admin')
def test_edit_navigation_action(webtest, root):
    """ Action managers should be editable"""

    from kotti_actions.resources import NavigationActionManager

    root['cc'] = NavigationActionManager(title=u'Action Title')

    resp = webtest.get('/cc/@@edit')
    form = resp.forms['deform']
    assert form['title'].value == u'Action Title'
    form['title'] = u'Bazinga'
    resp = form.submit('save').maybe_follow()
    assert u'Your changes have been saved.' in resp.body
    assert u'Bazinga' in resp.body


@mark.user('admin')
def test_edit_header_action(webtest, root):
    """ Action managers should be editable"""

    from kotti_actions.resources import HeaderActionManager

    root['cc'] = HeaderActionManager(title=u'Action Title')

    resp = webtest.get('/cc/@@edit')
    form = resp.forms['deform']
    assert form['title'].value == u'Action Title'
    form['title'] = u'Bazinga'
    resp = form.submit('save').maybe_follow()
    assert u'Your changes have been saved.' in resp.body
    assert u'Bazinga' in resp.body


@mark.user('admin')
def test_edit_footer_action(webtest, root):
    """ Action managers should be editable"""

    from kotti_actions.resources import FooterActionManager

    root['cc'] = FooterActionManager(title=u'Action Title')

    resp = webtest.get('/cc/@@edit')
    form = resp.forms['deform']
    assert form['title'].value == u'Action Title'
    form['title'] = u'Bazinga'
    resp = form.submit('save').maybe_follow()
    assert u'Your changes have been saved.' in resp.body
    assert u'Bazinga' in resp.body


@mark.user('admin')
def test_edit_navigation_default_view(webtest, root):
    """ @@contents view is the default view for managers """

    from kotti_actions.resources import NavigationActionManager

    root['cc'] = NavigationActionManager(title=u'Action Title')

    resp = webtest.get('/cc')
    assert 'No content items are contained here.' in resp.body


@mark.user('admin')
def test_edit_header_default_view(webtest, root):
    """ @@contents view is the default view for managers """

    from kotti_actions.resources import HeaderActionManager

    root['cc'] = HeaderActionManager(title=u'Action Title')

    resp = webtest.get('/cc')
    assert 'No content items are contained here.' in resp.body


@mark.user('admin')
def test_edit_footer_default_view(webtest, root):
    """ @@contents view is the default view for managers """

    from kotti_actions.resources import FooterActionManager

    root['cc'] = FooterActionManager(title=u'Action Title')

    resp = webtest.get('/cc')
    assert 'No content items are contained here.' in resp.body
