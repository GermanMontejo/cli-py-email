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


As of now, --type only includes image, but soon I'll be adding support for audio and other file types for attachment.
