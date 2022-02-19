import json
from mailer.models import Message

# will be populated from the test conf file
test_config = dict()

with open('tests/test_config.conf', 'r') as test_config_file:
    test_config = json.load(test_config_file)

def test_create_message():
    msg_details = test_config['msg_details']
    message = Message(**msg_details)
    assert message

