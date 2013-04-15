from email.mime.text import MIMEText
import deform
import os
import smtplib
from .config import SENDGRID_HOSTNAME
from .config import SENDGRID_PASSWORD
from .config import SENDGRID_USERNAME
from .forms import ContactFormSchema


def contact(request):
    """
    Create and render deform form containing colander schema
    """
    form = deform.Form(ContactFormSchema(), buttons=('Send', ))
    recipient = 'info@aclark.net'
    if 'Send' in request.POST:
        controls = request.POST.items()
        try:
            appstruct = form.validate(controls)
        except deform.ValidationFailure:
            return {
                'form': form.render(),
            }
        return {
            'form': form.render(),
        }
        sender = appstruct['email']
        body = appstruct['message']
        body = body.encode('utf-8')
        body = str(body)
        msg = MIMEText(body)
        msg['Subject'] = 'New lead'
        msg['To'] = recipient
        msg['From'] = sender
        msg = msg.as_string()
        recipient = list(recipient)
        try:
            s = smtplib.SMTP(SENDGRID_HOSTNAME)
            s.starttls()
            s.login(SENDGRID_USERNAME, SENDGRID_PASSWORD)
            s.sendmail(sender, recipient, msg)
            s.quit()
        except:
            # XXX Do something here
            pass

    return {
        'form': form.render(),
    }


def default(request):
    """
    This is the default view, to be used with most routes since we do not
    provide any content editing ability yet. Even then, maybe a default view
    would still be helpful.
    """
    return {}
