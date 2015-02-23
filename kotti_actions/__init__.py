# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from pyramid.i18n import TranslationStringFactory
from kotti import FALSE_VALUES
from kotti_actions.registry import action_manager_registry
from kotti_actions.registry import action_registry
from kotti_actions.util import get_managers
from kotti_actions.util import get_actions

_ = TranslationStringFactory('kotti_actions')


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_actions.kotti_configure

        to enable the ``kotti_actions`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' kotti_actions'

    # register addable types
    managers = get_managers(settings)
    actions = get_actions(settings)
    addable_types = managers + actions
    addable_types_string = ''.join([' %s' % item for item in addable_types])
    settings['kotti.available_types'] += addable_types_string

    if not settings.get('kotti_actions', None):
        settings['kotti_actions.use_workflow'] = \
            'kotti_actions:workflow.zcml'

    settings['kotti.fanstatic.view_needed'] += \
        ' kotti_actions.fanstatic.css_and_js'


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    # register managers
    managers = get_managers(config.registry.settings)
    action_manager_registry.register_components(managers)
    # register actions (updates addable_to)
    actions = get_actions(config.registry.settings)
    action_registry.register_components(actions)

    workflow = config.registry.settings.get('kotti_actions.use_workflow',
                                            None)
    if workflow and workflow.lower() not in FALSE_VALUES:
        config.begin()

        config.hook_zca()
        config.include('pyramid_zcml')
        config.load_zcml(workflow)
        config.commit()

    # translations
    config.add_translation_dirs('kotti_actions:locale')

    # add static view
    config.add_static_view('static-kotti_actions', 'kotti_actions:static')

    # we want to provide the standard @@contents view as default view
    # for our action managers
    from kotti_actions.resources import BaseActionManager
    config.add_view('kotti.views.edit.actions.contents',
                    name=u'view',
                    context=BaseActionManager,
                    permission=u'view',
                    renderer='kotti:templates/edit/contents.pt',
                    )

    config.scan(__name__)
