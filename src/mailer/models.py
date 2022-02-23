import smtplib
from pydantic import BaseModel
from typing import Optional


"""
Model for Messages
"""


class Message(BaseModel):
    recipient: str
    sender: str
    subject: Optional[str] = None
    message: Optional[str] = None

    def __str__(self):
        return f"Email from {self.sender} to {self.recipient} with subject {self.subject}\n{self.message}"

    def __post_init__(self):
        self.header = f'To: {self.recipient}\n\
        From: {self.sender}\n\
        subject: {self.subject}\n'

        self.content = self.header + self.content


"""
Model for MailServer
"""


class MailServer(BaseModel, smtplib.SMTP):
    port_number: int
    server: str
    username: str
    password: str

    def __str__(self):
        return f"{self.username}@{self.server}:{self.port_number}"

    def __post_init__(self):
        self.login(self.username, self.password)
