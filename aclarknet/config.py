import os

FORM_ERROR = 'Server error: failed to send message! Please try again later.'
FORM_SUCCESS = 'Message sent! Please expect to hear from us within 24 hours.'

MIME_ONE_RECIPIENT = 'info@aclark.net'
MIME_ONE_SUBJECT = 'This just in: new lead!'
MIME_TWO_MESSAGE = \
    """
Thanks for contacting us! We'll be in touch within 24 hours.

The ACLARK.NET, LLC team.
    """
MIME_TWO_SUBJECT = 'Thank you for contacting ACLARK.NET, LLC'

SENDGRID_HOSTNAME = 'smtp.sendgrid.net'
SENDGRID_PASSWORD = os.environ.get('SENDGRID_PASSWORD', 'password')
SENDGRID_USERNAME = os.environ.get('SENDGRID_USERNAME', 'username')
