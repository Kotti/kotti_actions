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
EMAIL_RE = "^mailto:[a-zA-Z0-9._%!#$%&'*+-/=?^_`{|}~()]+@[a-zA-Z0-9]+([.-][a-zA-Z0-9]+)*\.[a-zA-Z]{2,22}$"
LINK_REGEXP = "%s|%s" % (URL_REGEXP, EMAIL_RE)


def link_validator(node, value):
    """ Raise a colander.Invalid exception if the provided url
        is not valid
    """
    def raise_invalid_url(node, value):
        raise colander.Invalid(
            node, _(u"You must provide a valid url or email."))
    if value:
        if not re.match(LINK_REGEXP, value):
            raise_invalid_url(node, value)
