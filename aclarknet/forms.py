import colander
import deform


class ContactFormSchema(colander.MappingSchema):
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
