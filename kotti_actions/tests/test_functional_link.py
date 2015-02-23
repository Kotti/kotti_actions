# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from pytest import mark
from pytest import fixture


@fixture
def dummy_manager(root):

    from kotti_actions.resources import NavigationActionManager

    root['navigation'] = cc = NavigationActionManager()

    return cc


def test_login_required_add_link(webtest, root):
    """ Add view requires login """
    resp = webtest.get('/add_link_action')
    assert resp.status_code == 302


def test_login_required_add_left(webtest, dummy_manager):
    """ Add view requires login """
    resp = webtest.get('/navigation/add_link_action')
    assert resp.status_code == 302


@mark.user('admin')
def test_add_navigation_action(webtest, dummy_manager):

    resp = webtest.get('/navigation/add_link_action')

    # submit empty form
    form = resp.forms['deform']
    form['title'] = u'new action'
    resp = form.submit('save')
    assert resp.status_code == 302
    resp = resp.follow()
    assert 'Item was added.' in resp.body


@mark.user('admin')
def test_edit_action(webtest, dummy_manager):
    """ Action should be editable"""

    from kotti_actions.resources import LinkAction

    dummy_manager['cc'] = LinkAction(title=u'Action Title')

    resp = webtest.get('/navigation/cc/@@edit')
    form = resp.forms['deform']
    assert form['title'].value == u'Action Title'
    form['title'] = u'Bazinga'
    form['description'] = u'This is the description'
    form['link'] = u'/en/link'
    resp = form.submit('save').maybe_follow()
    assert u'Your changes have been saved.' in resp.body
    assert u'This is the description' in resp.body
    assert dummy_manager['cc'].link == u'/en/link'
