#!/usr/bin/env python

import smtplib
import ssl
from email.mime.text import MIMEText


sender = 'jon@jrickman.net'
receivers = 'Julian.c.currie@gmail.com'

port = 465
user = 'jon@jrickman.net'
password = "yup."

msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail. Hello from python!'
msg['From'] = sender
msg['To'] = receivers

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.migadu.com", port, context=context) as server:

    server.login(user, password)
    server.sendmail(sender, receivers, msg.as_string())
    print('mail successfully sent')
