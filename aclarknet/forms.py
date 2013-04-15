import colander
import deform


class ContactFormSchema(colander.MappingSchema):
    """
    Contact form schema, built with colander, to be used with deform form
    library
    """
    email = colander.SchemaNode(
        colander.String(),
        title="Your email address",
    )
    msg = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.TextAreaWidget(rows=20, cols=120),
        validator=colander.Length(1),
        title="Your message",
    )
