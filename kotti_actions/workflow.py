from kotti_actions.interfaces import IActionWorkflow


def elector(context):
    return IActionWorkflow.providedBy(context)
