# cli-py-email
This is a command-line program that allows users to send email directly from the command-line/terminal.

Usage:

usage: pymailcli.py [-h] [--recipient RECIPIENT [RECIPIENT ...]] [--body BODY]
                    [--subject SUBJECT] [--attachment ATTACHMENT]
                    [--type TYPE]

This is a python email sender which can be used from the command line.

optional arguments:
  -h, --help            show this help message and exit
  --recipient RECIPIENT [RECIPIENT ...], -r RECIPIENT [RECIPIENT ...]
  --body BODY, -b BODY
  --subject SUBJECT, -s SUBJECT
  --attachment ATTACHMENT, -a ATTACHMENT
  --type TYPE, -t TYPE

Sample:

python pymailcli.py --recipient 'johndoe@gmail.com' --body 'Hello world!' --subject 'Test email' --attachment '/root/Pictures/indie4.jpg' --type 'image'

As of now, --type only includes image, but soon I'll be adding support for audio and other file types for attachment.

You need to add these environment variables in your ~/.bashrc or ~/.bash_profile configuration:

export EMAIL_HOST='smtp.gmail.com'
export EMAIL_PORT=587
export USERNAME='<gmail username>'
export PASSWORD='<gmail password>'

You can use another email service provider like Yahoo, MSN, etc. Just make sure to swap these variables with the correct host, port, username, and password configuration. Also, ensure that your bash config file has been loaded to the shell after editing it. You can run . ~/.bashrc or . ~/.bash_profile.

If you go with gmail, please ensure that you allow less secure apps: https://support.google.com/accounts/answer/6010255?hl=en.
