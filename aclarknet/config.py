import os


FORM_ERROR = os.environ.get(
    'FORM_ERROR',
    'Server error: failed to send message! Please try again later.')
FORM_RECIPIENT = os.environ.get(
    'FORM_RECIPIENT', 'info@aclark.net')
FORM_SUBJECT = os.environ.get(
    'FORM_SUBJECT', 'This just in: new lead!')
FORM_SUCCESS = os.environ.get(
    'FORM_SUCCESS',
    'Message sent! Please expect to hear from us within 24 hours.')

RESPONSE_BODY = os.environ.get(
    'RESPONSE_BODY',
    """
Thanks for contacting us! We'll be in touch within 24 hours.

The ACLARK.NET, LLC team.
    """)
RESPONSE_SUBJECT = os.environ.get(
    'RESPONSE_SUBJECT',
    'Thank you for contacting ACLARK.NET, LLC')

SENDGRID_HOSTNAME = os.environ.get('SENDGRID_HOSTNAME', 'smtp.sendgrid.net')
SENDGRID_PASSWORD = os.environ.get('SENDGRID_PASSWORD', 'password')
SENDGRID_USERNAME = os.environ.get('SENDGRID_USERNAME', 'username')
