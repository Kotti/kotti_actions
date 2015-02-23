# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from pyramid.view import view_config
from kotti.views.edit import ContentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from kotti.interfaces import INavigationRoot

from kotti_actions import _
from kotti_actions.resources import NavigationActionManager
from kotti_actions.resources import HeaderActionManager
from kotti_actions.resources import FooterActionManager


class ActionManagerSchema(ContentSchema):
    """ Schema for ActionManager. """

    def after_bind(self, node, kw):
        del node['tags']
        del node['description']


class NavigationActionManagerSchema(ActionManagerSchema):
    """ Schema for ActionManager. """

    def after_bind(self, node, kw):
        super(NavigationActionManagerSchema, self).after_bind(node, kw)
        node['title'].default = _('NavigationActionManager')


class HeaderActionManagerSchema(ActionManagerSchema):
    """ Schema for ActionManager. """

    def after_bind(self, node, kw):
        super(HeaderActionManagerSchema, self).after_bind(node, kw)
        node['title'].default = _('HeaderActionManager')


class FooterActionManagerSchema(ActionManagerSchema):
    """ Schema for ActionManager. """

    def after_bind(self, node, kw):
        super(FooterActionManagerSchema, self).after_bind(node, kw)
        node['title'].default = _('FooterActionManager')


@view_config(name=NavigationActionManager.type_info.add_view, permission='add',
             context=INavigationRoot,
             renderer='kotti:templates/edit/node.pt')
class NavigationActionManagerAddForm(AddFormView):
    """ Form to add a new instance of ActionManager. """

    schema_factory = NavigationActionManagerSchema
    add = NavigationActionManager
    item_type = _(u"NavigationActionManager")


@view_config(name='edit', context=NavigationActionManager, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class NavigationActionManagerEditForm(EditFormView):
    """ Form to edit existing calendars. """

    schema_factory = NavigationActionManagerSchema


@view_config(name=HeaderActionManager.type_info.add_view, permission='add',
             context=INavigationRoot,
             renderer='kotti:templates/edit/node.pt')
class HeaderActionManagerAddForm(AddFormView):
    """ Form to add a new instance of ActionManager. """

    schema_factory = HeaderActionManagerSchema
    add = HeaderActionManager
    item_type = _(u"HeaderActionManager")


@view_config(name='edit', context=HeaderActionManager, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class HeaderActionManagerEditForm(EditFormView):
    """ Form to edit existing calendars. """

    schema_factory = HeaderActionManagerSchema


@view_config(name=FooterActionManager.type_info.add_view, permission='add',
             context=INavigationRoot,
             renderer='kotti:templates/edit/node.pt')
class FooterActionManagerAddForm(AddFormView):
    """ Form to add a new instance of ActionManager. """

    schema_factory = FooterActionManagerSchema
    add = FooterActionManager
    item_type = _(u"FooterActionManager")


@view_config(name='edit', context=FooterActionManager, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class FooterActionManagerEditForm(EditFormView):
    """ Form to edit existing calendars. """

    schema_factory = FooterActionManagerSchema
