import json
import os
import pytest

TEST_CONFIG_FILEPATH = 'tests/test_config.conf'


def test_config_file_exists():
    assert os.path.exists(TEST_CONFIG_FILEPATH)


@pytest.fixture(scope="session")
def config():
    with open('tests/test_config.conf', 'r') as test_config_file:
        yield json.load(test_config_file)


def test_config_file(config):
    assert config is not None
