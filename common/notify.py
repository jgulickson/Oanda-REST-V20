# !/usr/bin/env python

#
# Imports
#
try:
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
except ImportError:
    raise ImportError("Import failed to load in notify.py.")


#
# Email Class
#
class Notify:
    def __init__(self):
        self.content = None
        self.sender = None
        self.recipient = None
        self.subject = None
        self.body = None

        self.message = None
        self.password = None
        self.smtp_address = None
        self.smtp_port = None

    #
    # Compose Email
    #
    def compose_email(self, sender, recipient, subject, body):
        self.content = MIMEMultipart()
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body

        self.content["From"] = self.sender
        self.content["To"] = self.recipient
        self.content["Subject"] = self.subject
        self.content.attach(MIMEText(self.body, "plain"))
        print("compose_email completed")

    #
    # Send Email
    #
    def send_email(self, password, smtp_address, smtp_port):
        self.password = password
        self.smtp_address = smtp_address
        self.smtp_port = smtp_port

        self.message = smtplib.SMTP(self.smtp_address, self.smtp_port)
        self.message.starttls()
        self.message.login(self.sender, self.password)
        self.message.sendmail(self.sender, self.recipient, self.content.as_string())
        self.message.quit()
        print("send_email completed")
