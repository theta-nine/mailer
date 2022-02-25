import pytest
from mailer.crypto_helpers import CryptoHelper
from cryptography.fernet import InvalidToken


def test_encrypt_text_with_password(config_filepath):
    crypto_helper = CryptoHelper(config_filepath)
    text = "foo"
    password = "bar"
    encrypted = crypto_helper.encrypt_text_with_password(text, password)
    decrypted = crypto_helper.decrypt_text_with_password(encrypted, password)
    assert decrypted == text


def test_bad_decrypt_text_with_password(config_filepath):
    crypto_helper = CryptoHelper(config_filepath)
    text = "foo"
    password = "bar"

    with pytest.raises(InvalidToken):
        crypto_helper.decrypt_text_with_password(text, password)
