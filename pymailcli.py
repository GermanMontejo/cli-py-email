from mail_service import MailService
from argparse import ArgumentParser
from mail_service import MailService


class PyMailCli():

    def __init__(self):
        self.parser = ArgumentParser(description='This is a python email sender which can be used from the command line.')
        self.parser.add_argument('--recipient', '-r', nargs='+', type=str)
        self.parser.add_argument('--body', '-b', type=str)

        self.parser.add_argument('--subject', '-s', type=str)
        self.parser.add_argument('--attachment', '-a', type=str)
        self.parser.add_argument('--type', '-t', type=str)

        self.args = self.parser.parse_args()

        self.recipients = self.args.recipient
        self.body = self.args.body
        self.subject = self.args.subject

        self.attachment = self.args.attachment
        self.type = self.args.type
        print(self.args)
        self.mail_service = MailService(self.recipients)
        

    def send_mail(self):
        self.mail_service.send_email(self.body, self.subject, self.attachment, self.type)

def main():
    py_mail = PyMailCli()
    cli_mail = MailService(py_mail.recipients)
    py_mail.send_mail()


if __name__ == '__main__':
    main()
