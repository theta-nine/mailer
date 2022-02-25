from mailer.factory import Factory


def test_create_factory(config_filepath):
    factory = Factory(config_filepath, "bar")
    assert type(factory) is Factory

def test_create_factory(config_filepath):
    factory = Factory(config_filepath, "bar")
    print(factory)
    assert str(factory) == "jon@jrickman.net@smtp.migadu.com:465"
