from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os


class MailService():

    def __init__(self, to_addrs):
        self.host = os.environ['EMAIL_HOST']
        self.port = os.environ['EMAIL_PORT']
        self.email_serv = SMTP(self.host, self.port)
        
        self.username = os.environ['USERNAME']
        self.password = os.environ['PASSWORD']
        self.email_serv.ehlo()

        self.from_addr = self.username
        self.to_addrs = to_addrs

        self.email_serv.starttls()
        print(self.email_serv.login(self.username, self.password))


    def send_email(self, body, subject, attachment, attachment_type):
        print('send_email()')
        text = MIMEText(body, 'plain')
        multipart = MIMEMultipart('alternative')
        multipart['Subject'] = subject

        raw_file = None
        with open(attachment, 'rb') as img_file:
            raw_file = img_file.read()

        print(raw_file)

        if attachment_type == 'image':
            if raw_file != None:
                image = MIMEImage(raw_file, name='Image.jpg')
                multipart.attach(image)

        multipart.attach(text)
        print('multipart: {}'.format(multipart))

        self.email_serv.sendmail(self.from_addr, self.to_addrs, multipart.as_string())

