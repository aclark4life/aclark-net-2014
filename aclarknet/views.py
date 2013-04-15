from email.mime.text import MIMEText
import deform
import smtplib
from .forms import ContactFormSchema


def contact(request):
    """
    Create and render deform form containing colander schema
    """
    form = deform.Form(ContactFormSchema(), buttons=('Send', ))
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
        email = appstruct['email']
        msg = appstruct['message']
    return {
        'form': form.render(),
    }

#        body = appstruct['body']
#        msg = MIMEText(str(body.encode('utf-8')))
#        msg['Subject'] = 'New lead'
#        msg['To'] = 'info@aclark.net'
#        msg['From'] =
#        try:
#            s = smtplib.SMTP(config.GMAIL_HOST)
#            s.starttls()
#            s.login(config.GMAIL_USER, config.GMAIL_PASS)
#            s.sendmail(config.ADMIN_EMAIL, [to], msg.as_string())
#            s.quit()
#        except:
#            pass


def default(request):
    """
    This is the default view, to be used with most routes since we do not
    provide any content editing ability yet. Even then, maybe a default view
    would still be helpful.
    """
    return {}
