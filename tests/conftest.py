import json
import pytest 

@pytest.fixture(scope="session")
def config_filepath():
    return 'tests/test_config.conf'


@pytest.fixture(scope="session")
def config(config_filepath):
    with open(config_filepath, 'r') as test_config_file:
        yield json.load(test_config_file)

