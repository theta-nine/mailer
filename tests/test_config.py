import os

TEST_CONFIG_FILEPATH = 'tests/test_config.conf'


def test_config_file_exists():
    assert os.path.exists(TEST_CONFIG_FILEPATH)


def test_config_file(config):
    assert config is not None
