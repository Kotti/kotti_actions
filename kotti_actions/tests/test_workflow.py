def test_workflow_elector_document():
    from kotti_actions.workflow import elector
    from kotti.resources import Document
    assert elector(Document()) is False


def test_workflow_elector_manager():
    from kotti_actions.workflow import elector
    from kotti_actions.resources import NavigationActionManager
    assert elector(NavigationActionManager()) is True


def test_workflow_elector_action():
    from kotti_actions.workflow import elector
    from kotti_actions.resources import LinkAction
    assert elector(LinkAction()) is True


def test_workflow_permission(config):
    from repoze.workflow import get_workflow
    from kotti_actions.resources import LinkAction

    config.include('pyramid_zcml')
    config.include('kotti_actions')
    context = LinkAction()
    wf = get_workflow(context, 'security', context=context)
    assert wf.__dict__['_state_data']['public']['system.Everyone'] == \
        u'viewaction'
