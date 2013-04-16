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
        # This is the form contents
        email = appstruct['email']
        message = appstruct['message']
        message = message.encode('utf-8')
        message = str(message)

        # This is the mail to info@aclark.net
        mime_document_one = MIMEText(message)
        mime_document_one['Subject'] = FORM_SUBJECT
        mime_document_one['To'] = FORM_RECIPIENT
        mime_document_one['From'] = email
        mime_document_one = mime_document_one.as_string()

        # This is the mail to the new lead
        mime_document_two = MIMEText(RESPONSE_BODY)
        mime_document_two['Subject'] = RESPONSE_SUBJECT
        mime_document_two['To'] = email
        mime_document_two['From'] = FORM_RECIPIENT
        mime_document_two = mime_document_two.as_string()

        try:
            smtp_server = smtplib.SMTP(SENDGRID_HOSTNAME)
            smtp_server.starttls()
            smtp_server.login(SENDGRID_USERNAME, SENDGRID_PASSWORD)
            smtp_server.sendmail(email, FORM_RECIPIENT, mime_document_one)
            smtp_server.sendmail(FORM_RECIPIENT, email, mime_document_two)
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
