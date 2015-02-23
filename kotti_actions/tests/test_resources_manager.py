# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""


def test_add_navigationactionmanager(root, db_session):
    from kotti_actions.resources import NavigationActionManager

    cc = NavigationActionManager()

    root['cc'] = cc
    assert cc.name == 'cc'


def test_add_headeractionmanager(root, db_session):
    from kotti_actions.resources import HeaderActionManager

    cc = HeaderActionManager()

    root['cc'] = cc
    assert cc.name == 'cc'


def test_custom_type_info(root, config):
    """ We test if our object type info is our custom
        implementation
    """
    from kotti_actions.resources import NavigationActionManager
    from kotti_actions.resources import ActionManagerTypeInfo

    action = NavigationActionManager()
    assert isinstance(action.type_info, ActionManagerTypeInfo)


def test_custom_type_info_copy(root, config):
    """ When you copy our custom type info you should
        obtain an instance of our custom class (and not
        the original TypeInfo class)
    """
    from kotti_actions.resources import ActionManagerTypeInfo
    type_info = ActionManagerTypeInfo()
    assert isinstance(type_info, ActionManagerTypeInfo)

    copied_type_info = type_info.copy()
    assert isinstance(copied_type_info, ActionManagerTypeInfo)


def test_baseaction_not_addable(root, db_session, config):
    """ The base action object should not be addable """
    from kotti.testing import DummyRequest
    from kotti_actions.resources import BaseActionManager

    config.include('kotti_actions')
    action = BaseActionManager()
    # base action is addable, ok
    assert not action.type_info.addable(root, DummyRequest())


def test_navigationaction_addable_in_root_one_time(root, db_session, config):
    """ The navigationaction object should be addable in root
        just one time
    """
    from kotti.testing import DummyRequest
    from kotti_actions.resources import NavigationActionManager
    from kotti.interfaces import INavigationRoot
    from zope.interface import alsoProvides
    alsoProvides(root, INavigationRoot)

    config.include('kotti_actions')
    action = NavigationActionManager()
    # navigation action is addable, ok
    assert action.type_info.addable(root, DummyRequest())

    # ok, let's add it
    root['action'] = action

    # navigation action is no addable anymore (on root)
    another_action = NavigationActionManager()
    assert not another_action.type_info.addable(root, DummyRequest())


def test_headeraction_addable_in_root_one_time(root, db_session, config):
    """ The headeraction object should be addable in root
        just one time
    """
    from kotti.testing import DummyRequest
    from kotti_actions.resources import HeaderActionManager
    from kotti.interfaces import INavigationRoot
    from zope.interface import alsoProvides
    alsoProvides(root, INavigationRoot)

    config.include('kotti_actions')
    action = HeaderActionManager()
    # header action is addable, ok
    assert action.type_info.addable(root, DummyRequest())

    # ok, let's add it
    root['action'] = action

    # header action is no addable anymore (on root)
    another_action = HeaderActionManager()
    assert not another_action.type_info.addable(root, DummyRequest())
