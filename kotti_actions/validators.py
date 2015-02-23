# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

import re
import colander
from kotti_actions import _

VALID_PROTOCOLS = ('http',)
URL_REGEXP = r'((%s)s?:/)?/[^\s\r\n]+' % '|'.join(VALID_PROTOCOLS)


def link_validator(node, value):
    """ Raise a colander.Invalid exception if the provided url
        is not valid
    """
    def raise_invalid_url(node, value):
        raise colander.Invalid(
            node, _(u"You must provide a valid url."))
    if value:
        if not re.match(URL_REGEXP, value):
            raise_invalid_url(node, value)
