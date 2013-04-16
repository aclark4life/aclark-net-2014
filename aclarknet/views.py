from email.mime.text import MIMEText
import deform
import smtplib
from .config import FORM_ERROR
from .config import FORM_RECIPIENT
from .config import FORM_SUBJECT
from .config import FORM_SUCCESS

from .config import RESPONSE_BODY
from .config import RESPONSE_SUBJECT

from .config import SENDGRID_HOSTNAME
from .config import SENDGRID_PASSWORD
from .config import SENDGRID_USERNAME

from .forms import ContactFormSchema


def contact(request):
    """
    Create and render deform form containing colander schema. Provide
    sendgrid integration for marketing.
    """
    form = deform.Form(ContactFormSchema(), buttons=('Send', ))
    if 'Send' in request.POST:
        controls = request.POST.items()
        try:
            appstruct = form.validate(controls)
        except deform.ValidationFailure:
            return {
                'form': form.render(),
                'request': request,
            }
        sender = appstruct['email']
        body = appstruct['msg']
        body = body.encode('utf-8')
        body = str(body)

        incoming = MIMEText(body)
        incoming['Subject'] = FORM_SUBJECT
        incoming['To'] = FORM_RECIPIENT
        incoming['From'] = sender
        incoming = incoming.as_string()

        response = MIMEText(RESPONSE_BODY)
        response['Subject'] = RESPONSE_SUBJECT
        response['To'] = sender
        response['From'] = FORM_RECIPIENT
        response = response.as_string()

        try:
            smtp_server = smtplib.SMTP(SENDGRID_HOSTNAME)
            smtp_server.starttls()
            smtp_server.login(SENDGRID_USERNAME, SENDGRID_PASSWORD)
            smtp_server.sendmail(sender, FORM_RECIPIENT, incoming)
            smtp_server.sendmail(FORM_RECIPIENT, sender, response)
            smtp_server.quit()
            request.session.flash(FORM_SUCCESS)
        except:
            request.session.flash(FORM_ERROR)
        return {
            'form': form.render(),
            'request': request,
        }
    return {
        'form': form.render(),
        'request': request,
    }


def default(request):
    """
    This is the default view, to be used with most routes since we do not
    provide any content editing ability yet. Even then, maybe a default view
    would still be helpful.
    """
    return {}
