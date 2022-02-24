import base64
import json
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class CryptoHelper():
    """
    Helpers to encrypt/decrypt text
    """
    def __init__(self, config_filepath):
        crypto_config = json.load(open(config_filepath))["crypto"]
        self.salt = crypto_config["salt"].encode("UTF-8")
        self.iterations = crypto_config["iterations"]

    def generate_password_key(self, unencoded_password):
        encoded_password = unencoded_password.encode()
        derivitive_function = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length = 32, # specifically any other number will cause exception, RTFM
            salt = self.salt,
            iterations = self.iterations,
            backend = default_backend()
        )
        return base64.urlsafe_b64encode(derivitive_function.derive(encoded_password))

    def decrypt_text_with_password(self, text, password):
        # generate the fernet for sym decryption
        fernet = Fernet(self.generate_password_key(password))

        # encode the given text, must have bytes
        encoded_text = text.encode("UTF-8")

        # decrypt the encoded text using the fernet
        decrypted_value = fernet.decrypt(encoded_text)

        # returned value is bytes, make string
        return decrypted_value.decode()

    def encrypt_text_with_password(self, text, password):
        # generate the fernet for sym encryption
        fernet = Fernet(self.generate_password_key(password))
        
        # encode the given text, must have bytes
        encoded_text = text.encode("UTF-8")

        # encrypt the bytes using the fernet
        encrypted_value = fernet.encrypt(encoded_text)

        # returned value is bytes, convert to string
        return encrypted_value.decode()
