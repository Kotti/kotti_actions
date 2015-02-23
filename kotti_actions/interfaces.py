from zope.interface import Interface
from kotti.interfaces import IDefaultWorkflow


class IActionWorkflow(IDefaultWorkflow):
    """ Custom workflow for action related types """


class IActionCommon(Interface):
    """ Base interface for action-related interfaces """


class IActionManager(IActionCommon):
    """ Marker interface """


class IAction(IActionCommon):
    """ Marker interface for
        action elements addable to a
        action manager container
    """


class ILinkAction(IAction):
    """ """


class IBaseRegistry(Interface):
    """ This is the base related action components registry.
        When you define a new action manager or action, you
        should register it calling the register.

       If you provide the kotti_actions.managers and
       kotti_actions.actions settings, no need to use this
       registry. kotti_actions will register your components
       for you.
    """

    def register_component(component):
        """ Adds a action component to the registry
            Accepts a class or a string like
            plugin.resource.Something)
        """

    def register_components(components):
        """ Adds a action component list to the registry.
            Accepts a list of classes or strings like
            plugin.resource.Something
        """

    def get_components():
        """ Returns a list of action component classes """

    def get_dotted_components():
        """ Returns a list of action component dotted
            strings (eg: 'kotti_your.resources.YourAction')
        """

    def get_component_names():
        """ Returns a list of action component names
            from type_info
        """


class IActionManagerRegistry(IBaseRegistry):
    """ Action Manager registry"""


class IActionRegistry(IBaseRegistry):
    """ Action registry """
