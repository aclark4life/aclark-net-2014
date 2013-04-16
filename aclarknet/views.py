from email.mime.text import MIMEText
import deform
import smtplib
from .config import CONTACT_FORM_ERROR
from .config import CONTACT_FORM_RECIPIENT
from .config import CONTACT_FORM_SUBJECT
from .config import CONTACT_FORM_SUCCESS
from .config import CONTACT_RESPONSE_BODY
from .config import CONTACT_RESPONSE_SUBJECT
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
        msg = MIMEText(body)
        msg['Subject'] = CONTACT_FORM_SUBJECT
        msg['To'] = CONTACT_FORM_RECIPIENT
        msg['From'] = sender
        msg = msg.as_string()
        response = MIMEText(CONTACT_RESPONSE_BODY)
        response['Subject'] = CONTACT_RESPONSE_SUBJECT
        response['To'] = sender
        response['From'] = CONTACT_FORM_RECIPIENT
        response = response.as_string()
        try:
            smtp_server = smtplib.SMTP(SENDGRID_HOSTNAME)
            smtp_server.starttls()
            smtp_server.login(SENDGRID_USERNAME, SENDGRID_PASSWORD)
            smtp_server.sendmail(sender, CONTACT_FORM_RECIPIENT, msg)
            smtp_server.sendmail(CONTACT_FORM_RECIPIENT, sender, response)
            smtp_server.quit()
            request.session.flash(CONTACT_FORM_SUCCESS)
        except:
            request.session.flash(CONTACT_FORM_ERROR)
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
