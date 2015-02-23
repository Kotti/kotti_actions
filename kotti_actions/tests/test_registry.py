def test_manager_registry_names():
    """ Default managers should be registered (name)"""
    from kotti_actions.registry import action_manager_registry

    assert 'NavigationActionManager' in \
           action_manager_registry.get_component_names()
    assert 'HeaderActionManager' in \
           action_manager_registry.get_component_names()
    assert 'FooterActionManager' in \
           action_manager_registry.get_component_names()


def test_action_registry_names():
    """ Default actions should be registered (name)"""
    from kotti_actions.registry import action_registry

    assert 'LinkAction' in action_registry.get_component_names()


def test_manager_registry_names_count():
    """ Default actions should be registered (unique list)"""
    from kotti_actions.registry import action_manager_registry

    assert action_manager_registry.get_component_names().\
        count('HeaderActionManager') == 1
    assert action_manager_registry.get_component_names().\
        count('NavigationActionManager') == 1


def test_common_registry_names_count():
    """ Default actions should be registered (unique list)"""
    from kotti_actions.registry import action_registry

    assert action_registry.get_component_names().count('LinkAction') == 1


def test_manager_registry_dotted():
    """ Default managers should be registered (dotted)"""
    from kotti_actions.registry import action_manager_registry

    assert 'kotti_actions.resources.managers.NavigationActionManager' in \
        action_manager_registry.get_dotted_components()
    assert 'kotti_actions.resources.managers.HeaderActionManager' in \
        action_manager_registry.get_dotted_components()
    assert 'kotti_actions.resources.managers.FooterActionManager' in \
        action_manager_registry.get_dotted_components()


def test_action_registry_dotted():
    """ Default managers should be registered (dotted)"""
    from kotti_actions.registry import action_registry

    assert 'kotti_actions.resources.actions.link.LinkAction' in \
        action_registry.get_dotted_components()


def test_manager_registry_components():
    """ Default managers should be registered (components)"""
    from kotti_actions.registry import action_manager_registry

    import kotti_actions
    assert kotti_actions.resources.NavigationActionManager in \
        action_manager_registry.get_components()
    assert kotti_actions.resources.HeaderActionManager in \
        action_manager_registry.get_components()
    assert kotti_actions.resources.FooterActionManager in \
        action_manager_registry.get_components()


def test_action_registry_components():
    """ Default managers should be registered (components)"""
    from kotti_actions.registry import action_registry

    import kotti_actions
    assert kotti_actions.resources.LinkAction in \
        action_registry.get_components()


def test_manager_register_component():
    """ Register a new component """
    from kotti_actions.registry import action_manager_registry
    from kotti_actions.interfaces import IActionManager
    from kotti_actions.resources import NavigationActionManager
    from zope.interface import implements

    class FakeActionManager:
        implements(IActionManager)
        type_info = NavigationActionManager.type_info.copy(
            name='FakeActionManager',
            dotted_class='kotti_actions.resources.FakeActionManager',
            )

    assert FakeActionManager not in action_manager_registry.get_components()

    action_manager_registry.register_component(FakeActionManager)
    assert FakeActionManager in action_manager_registry.get_components()
    assert 'FakeActionManager' in action_manager_registry.get_component_names()


def test_action_register_component():
    """ Register a new component """
    from kotti_actions.registry import action_registry
    from kotti_actions.interfaces import IAction
    from kotti_actions.resources import LinkAction
    from zope.interface import implements

    class FakeAction:
        implements(IAction)
        type_info = LinkAction.type_info.copy(
            name='FakeAction',
            addable_to=['FakeAction'],
            )

    assert FakeAction not in action_registry.get_components()

    action_registry.register_component(FakeAction)
    assert FakeAction in action_registry.get_components()
    assert 'FakeAction' in action_registry.get_component_names()
    assert 'NavigationActionManager' in FakeAction.type_info.addable_to
