import colander
import deform


# HT: http://deformdemo.repoze.org/pyramid_csrf_demo/


@colander.deferred
def deferred_csrf_default(node, kw):
    request = kw.get('request')
    csrf_token = request.session.get_csrf_token()
    return csrf_token


@colander.deferred
def deferred_csrf_validator(node, kw):
    def validate_csrf(node, value):
        request = kw.get('request')
        csrf_token = request.session.get_csrf_token()
        if value != csrf_token:
            raise ValueError('Bad CSRF token')
    return validate_csrf


class CSRFSchema(colander.Schema):
    csrf = colander.SchemaNode(
        colander.String(),
        default=deferred_csrf_default,
        validator=deferred_csrf_validator,
        widget=deform.widget.HiddenWidget(),
    )


class ContactFormSchema(CSRFSchema):
    """
    Contact form schema, built with colander, to be used with the deform form
    library
    """
    email = colander.SchemaNode(
        colander.String(),
        title="Your email address",
        validator=colander.Email(),
    )
    message = colander.SchemaNode(
        colander.String(),
        title="How can we help you",
        validator=colander.Length(1),
        widget=deform.widget.TextAreaWidget(rows=20, cols=120),
    )
