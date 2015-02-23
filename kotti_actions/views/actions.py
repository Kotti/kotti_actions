from pyramid.view import view_config
from kotti_actions.interfaces import IAction


@view_config(context=IAction, name='portlet', permission='viewaction',
             renderer='kotti_actions:views/templates/action.pt')
def action_view(context):
    return {}
