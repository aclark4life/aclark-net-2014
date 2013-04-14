import colander
import deform


class ContactFormSchema(colander.MappingSchema):
    """
    Contact form schema built with colander, to be used with deform form
    library
    """
    subject = colander.SchemaNode(colander.String())
    body = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.TextAreaWidget(
            rows=20, cols=120),
        validator=colander.Length(1))
