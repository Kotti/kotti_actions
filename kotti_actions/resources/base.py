# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from pyramid.util import DottedNameResolver
from kotti import DBSession
from kotti.resources import Content
from kotti.resources import TypeInfo
from kotti.interfaces import INavigationRoot
from kotti.security import view_permitted
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from zope.interface import implements

from kotti_actions.interfaces import IActionManager
from kotti_actions.interfaces import IActionWorkflow


class ActionManagerTypeInfo(TypeInfo):
    """ Our action manager containers should be addable
        only in item types that provides the INavigationRoot
        interface.
    """

    def addable(self, context, request):
        resolver = DottedNameResolver()
        if hasattr(self, 'dotted_class'):
            resource_class = resolver.maybe_resolve(self.dotted_class)

            if resource_class:
                already_exists_action = DBSession.query(resource_class).\
                    filter(resource_class.parent_id == context.id).first()
                if already_exists_action is not None:
                    return False
            else:
                return False
        else:
            return False

        if INavigationRoot.providedBy(context) and \
           view_permitted(context, request, self.add_view):
            return True
        else:
            return False

    def copy(self, **kwargs):
        """

        :result: a copy of the current TypeInfo instance
        :rtype: :class:`~kotti.resources.TypeInfo`
        """

        d = self.__dict__.copy()
        d.update(kwargs)
        # the parent's .copy don't preserve the addable method
        # (it returns the original TypeInfo class)
        return self.__class__(**d)

data = dict(addable_to=[u'Document'],)
action_manager_type_info_data = Content.type_info.copy(
    **data
    ).__dict__.copy()
action_manager_type_info = ActionManagerTypeInfo(
    **action_manager_type_info_data)


class BaseActionManager(Content):
    """ """
    implements(IActionWorkflow, IActionManager)

    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)

    type_info = action_manager_type_info

    def __init__(self, **kwargs):
        super(BaseActionManager, self).__init__(**kwargs)
        self.in_navigation = False
