import os


CONTACT_FORM_RECIPIENT = os.environ.get('CONTACT_RECIPIENT', 'info@aclark.net')
CONTACT_FORM_SUBJECT = os.environ.get('CONTACT_SUBJECT', 'This just in: new lead!')
SENDGRID_HOSTNAME = os.environ.get('SENDGRID_HOSTNAME', 'smtp.sendgrid.net')
SENDGRID_PASSWORD = os.environ.get('SENDGRID_PASSWORD', 'password')
SENDGRID_USERNAME = os.environ.get('SENDGRID_USERNAME', 'username')
