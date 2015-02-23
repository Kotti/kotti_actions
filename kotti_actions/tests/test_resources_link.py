# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""


def test_add_link(root, db_session):
    from kotti_actions.resources import NavigationActionManager

    cc = NavigationActionManager()

    root['cc'] = cc

    from kotti_actions.resources import LinkAction
    link = LinkAction()
    cc['link'] = link
    assert cc['link'].name == 'link'


def test_add_link_with_link(root, db_session):
    from kotti_actions.resources import NavigationActionManager

    cc = NavigationActionManager()

    root['cc'] = cc

    from kotti_actions.resources import LinkAction
    link = LinkAction(link=u'http://google.com')
    cc['link'] = link
    assert cc['link'].name == 'link'
    assert cc['link'].link == u'http://google.com'


def test_base_not_addable_in_root(root, db_session, config):
    """ The base action object should not be addable """
    from kotti.testing import DummyRequest
    from kotti_actions.resources import LinkAction

    config.include('kotti_actions')
    action = LinkAction()
    # action is addable, ok
    assert not action.type_info.addable(root, DummyRequest())
