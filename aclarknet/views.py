from email.mime.text import MIMEText
import deform
import smtplib
from .forms import ContactFormSchema


SENDGRID_HOST = os.environ.get('SENDGRID_HOST', 'smtp.sendgrid.net')
SENDGRID_USER = os.environ.get('SENDGRID_USER', 'user')
SENDGRID_PASS = os.environ.get('SENDGRID_PASS', 'pass')



def contact(request):
    """
    Create and render deform form containing colander schema
    """
    form = deform.Form(ContactFormSchema(), buttons=('Send', ))
    to = 'info@aclark.net'
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
        lead = appstruct['email']
        body = appstruct['message']
        body = body.encode('utf-8')
        body = str(body)
        msg = MIMEText(body)
        msg['Subject'] = 'New lead'
        msg['To'] = to
        msg['From'] = lead
        msg = msg.as_string()
        to = list(to)
        try:
            s = smtplib.SMTP(SENDGRID_HOST)
            s.starttls()
            s.login(SENDGRID_USER, SENDGRID_PASS)
            s.sendmail(lead, to, msg)
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
