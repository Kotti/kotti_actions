# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

import colander
from deform.widget import SelectWidget
from kotti.views.edit import DocumentSchema
from kotti.views.edit.content import DocumentEditForm
from kotti.views.edit.content import DocumentAddForm
from pyramid.view import view_config

from kotti_actions import _
from kotti_actions.resources import LinkAction
from kotti_actions.interfaces import ILinkAction
from kotti_actions.validators import link_validator


class LinkActionSchema(DocumentSchema):

    link = colander.SchemaNode(
        colander.String(),
        title=_('Link'),
        validator=link_validator,
        missing=u'',
        )
    target = colander.SchemaNode(
        colander.String(),
        title=_('Target'),
        widget=SelectWidget(values=[('', ''), ('_blank', '_blank')]),
        missing=u'',
        )

    def after_bind(self, node, kw):
        del node['body']
        del node['tags']


@view_config(name='edit', permission='edit',
             context=ILinkAction,
             renderer='kotti:templates/edit/node.pt')
class LinkActionEditForm(DocumentEditForm):
    schema_factory = LinkActionSchema


@view_config(name=LinkAction.type_info.add_view, permission='add',
             renderer='kotti:templates/edit/node.pt')
class LinkActionAddForm(DocumentAddForm):
    item_type = _(u"Link Action")
    add = LinkAction
    schema_factory = LinkActionSchema
