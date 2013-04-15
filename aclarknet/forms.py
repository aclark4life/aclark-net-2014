import colander
import deform


class ContactFormSchema(colander.MappingSchema):
    """
    Contact form schema, built with colander, to be used with deform form
    library
    """
    body = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.TextAreaWidget(rows=20, cols=120),
        validator=colander.Length(1))
    msg = colander.SchemaNode(colander.String())
