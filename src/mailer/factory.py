import smtplib
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

        # set server settings
        server_config = json.load(open(config_filepath))["server"]
        self.port = server_config["port"]
        self.hostname = server_config["hostname"]

        # set user settings, used for login
        user_config = json.load(open(config_filepath))["user"]
        self.email = user_config["email"]
        encrypted_password = user_config["encrypted_password"]
        self.password = self.crypto.decrypt_text_with_password(encrypted_password, password)
    
    def __str__(self):
        return(f"{self.email}@{self.hostname}:{self.port}")

    def send_message(self, message):
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.migadu.com", self.port, context=context) as server:
            server.login(self.email, self.password)
            #the below won't work
            server.sendmail(message.sender, message.receivers, message.as_string())
            print('mail successfully sent')
