from email.mime.text import MIMEText
import deform
import smtplib
from .forms import ContactFormSchema


def contact(request):
    """
    Send mail from contact form to info@aclark.net
    """
    form = deform.Form(ContactFormSchema(), buttons=('Send', ))
    if 'Send' in request.POST:
        controls = request.POST.items()
        try:
            appstruct = form.validate(controls)
        except(deform.ValidationFailure, e):
            return {
                'appstruct': appstruct,
                'form': e.render(),
            }  # re-render the form with an exception
        # the form submission succeeded, we have the data
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
    This is the default view, to be used with every route since we provide
    no content editing functionality yet. Even then, maybe a default view
    could still be used.
    """
    return {}
