from pyramid.settings import aslist


def get_items_from_settings(settings, key):
    """ Returns a list of items from settings
        from a string with \n
    """
    raw_items = settings.get(key)
    items = aslist(raw_items)
    return items


def get_managers(settings):
    """ Managers from settings.
        Returns a list of plugin.resources.Something """
    return get_items_from_settings(settings, 'kotti_actions.managers')


def get_actions(settings):
    """ Actions from settings
        Returns a list of plugin.resources.Something """
    return get_items_from_settings(settings, 'kotti_actions.actions')
