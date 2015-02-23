# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from zope.interface import implements
from kotti.resources import Document
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from kotti_actions.interfaces import ILinkAction
from kotti_actions.interfaces import IActionWorkflow


class LinkAction(Document):
    implements(IActionWorkflow, ILinkAction)

    id = Column(Integer, ForeignKey('documents.id'), primary_key=True)
    link = Column(Unicode(1000))

    type_info = Document.type_info.copy(
        name=u'LinkAction',
        title=u'LinkAction',
        add_view=u'add_link_action',
        addable_to=['LinkAction']  # updated at startup time
        )

    def __init__(self, link=u"", **kwargs):
        super(LinkAction, self).__init__(**kwargs)
        self.link = link
        self.in_navigation = False
