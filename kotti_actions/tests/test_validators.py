from pytest import raises


def test_validate_ok():
    from kotti_actions.validators import link_validator

    assert link_validator({}, 'http://google.it') is None
    assert link_validator({}, 'https://google.it') is None
    assert link_validator({}, '/en/section') is None


def test_validate_ko():
    from kotti_actions.validators import link_validator
    import colander

    with raises(colander.Invalid):
        assert link_validator({}, 'ahttp://google.it') is None
    with raises(colander.Invalid):
        assert link_validator({}, 'https:google.it') is None
    with raises(colander.Invalid):
        assert link_validator({}, 'en/section') is None
