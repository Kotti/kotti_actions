# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from kotti_actions.resources import BaseActionManager


class NavigationActionManager(BaseActionManager):
    """ """

    id = Column(Integer, ForeignKey('base_action_managers.id'),
                primary_key=True)

    type_info = BaseActionManager.type_info.copy(
        name=u'NavigationActionManager',
        title=u'NavigationActionManager',
        add_view=u'add_action_manager_navigation',
        dotted_class='kotti_actions.resources.NavigationActionManager',
        addable_to=('kotti.interfaces.INavigationRoot'),
        )


class HeaderActionManager(BaseActionManager):
    """ """

    id = Column(Integer, ForeignKey('base_action_managers.id'),
                primary_key=True)

    type_info = BaseActionManager.type_info.copy(
        name=u'HeaderActionManager',
        title=u'HeaderActionManager',
        add_view=u'add_action_manager_header',
        dotted_class='kotti_actions.resources.HeaderActionManager',
        addable_to=('kotti.interfaces.INavigationRoot'),
        )


class FooterActionManager(BaseActionManager):
    """ """

    id = Column(Integer, ForeignKey('base_action_managers.id'),
                primary_key=True)

    type_info = BaseActionManager.type_info.copy(
        name=u'FooterActionManager',
        title=u'FooterActionManager',
        add_view=u'add_action_manager_footer',
        dotted_class='kotti_actions.resources.FooterActionManager',
        addable_to=('kotti.interfaces.INavigationRoot'),
        )
