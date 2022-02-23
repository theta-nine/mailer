from .test_config import config
from mailer.models import Message, MailServer


def test_create_message(config):
    message = Message(**config['msg_details'])
    assert str(message) == \
         f"Email from {message.sender} to {message.recipient} with subject {message.subject}\n{message.message}"


def test_create_mail_server(config):
    mail_server = MailServer(**config['mail_server'])
    assert str(mail_server) == \
        f"{mail_server.username}@{mail_server.server}:{mail_server.port_number}"
