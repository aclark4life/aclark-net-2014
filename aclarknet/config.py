import os


CONTACT_FORM_ERROR = os.environ.get(
    'CONTACT_FORM_ERROR',
    'Server error: failed to send message! Please try again later.')
CONTACT_FORM_RECIPIENT = os.environ.get(
    'CONTACT_FORM_RECIPIENT', 'info@aclark.net')
CONTACT_FORM_SUBJECT = os.environ.get(
    'CONTACT_FORM_SUBJECT', 'This just in: new lead!')
CONTACT_FORM_SUCCESS = os.environ.get(
    'CONTACT_FORM_SUCCESS',
    'Message sent! Please expect to hear from us within 24 hours.')
SENDGRID_HOSTNAME = os.environ.get('SENDGRID_HOSTNAME', 'smtp.sendgrid.net')
SENDGRID_PASSWORD = os.environ.get('SENDGRID_PASSWORD', 'password')
SENDGRID_USERNAME = os.environ.get('SENDGRID_USERNAME', 'username')
