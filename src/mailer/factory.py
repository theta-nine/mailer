import smtplib
import imaplib
import ssl
import json
from email.mime.text import MIMEText
from mailer.crypto_helpers import CryptoHelper

class Factory():
    """
    Class to handle sending messages and server admin
    """
    def __init__(self, config_filepath, password):
        # this crypto helper is used to encrypting / decrypting 
        self.crypto = CryptoHelper(config_filepath)

        config = json.load(open(config_filepath))

        # set server settings
        self.port = config["server"]["port"]
        self.hostname = config["server"]["hostname"]

        # set the email and password
        self.email = config["user"]["email"]
        self.password = password
    
    def __str__(self):
        return(f"{self.email}@{self.hostname}:{self.port}")

    def send_message(self, message: MIMEText):
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(self.hostname, self.port, context=context) as server:
            server.login(self.email, self.password)
            # #the below won't work
            # server.sendmail(message["From"], message["To"], message.as_string())
            print('mail successfully sent')

    def get_messages(self):
        context = ssl.create_default_context()

        with imaplib.IMAP4_SSL("imap.migadu.com", 993 ,ssl_context=context) as server:
            server.login(self.email, self.password)
            server.select('Inbox')
            _, data = server.search(None, 'ALL')
            mail_ids = list()
            for block in data:
                mail_ids += block.split()
                print(mail_ids)