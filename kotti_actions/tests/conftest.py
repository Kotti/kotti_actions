# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from pytest import fixture

pytest_plugins = "kotti"


@fixture(scope='session')
def custom_settings():
    import kotti_actions.resources
    kotti_actions.resources  # make pyflakes happy
    return {
        'kotti.configurators': 'kotti_tinymce.kotti_configure '
                               'kotti_actions.kotti_configure',
        'kotti_actions.managers':
            'kotti_actions.resources.NavigationActionManager '
            'kotti_actions.resources.HeaderActionManager '
            'kotti_actions.resources.FooterActionManager ',
        'kotti_actions.actions':
            'kotti_actions.resources.LinkAction ',
        'kotti.use_workflow': 'kotti:workflow.zcml',
        'kotti_actions.use_workflow': 'kotti_actions:workflow.zcml',
        }
