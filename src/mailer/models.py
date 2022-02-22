from pydantic import BaseModel
from typing import Optional


class Message(BaseModel):
    recipient: str
    sender: str
    subject: Optional[str] = None
    message: Optional[str] = None

    def __str__(self):
        return f"Email from {self.sender} to {self.recipient} with subject {self.subject}\n{self.message}"

    def __repr__(self):
        return str({
            'recipient': {self.recipient},
            'sender': {self.sender},
            'subject': {self.subject},
            'message': {self.message}
        })


class MailServer(BaseModel):
    port_number: int
    server: str
    username: str
    password: str
