import os

FORM_ERROR = 'Server error: failed to send message! Please try again later.'
FORM_SUCCESS = 'Message sent! Please expect to hear from us within 24 hours.'

GMAIL_HOSTNAME = 'smtp.gmail.com'
GMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD', 'password')
GMAIL_USERNAME = os.environ.get('GMAIL_USERNAME', 'username')

MIME_ONE_RECIPIENT = 'sales@aclark.net'
MIME_ONE_SUBJECT = 'New contact'
MIME_TWO_MESSAGE = \
    """
Thank you for contacting us! You will receive a reply within 24 hours.

The ACLARK.NET, LLC team.
    """
MIME_TWO_SUBJECT = 'Thank you for contacting ACLARK.NET, LLC'

SENDGRID_HOSTNAME = 'smtp.sendgrid.net'
SENDGRID_PASSWORD = os.environ.get('SENDGRID_PASSWORD', 'password')
SENDGRID_USERNAME = os.environ.get('SENDGRID_USERNAME', 'username')
