from pyramid.config import Configurator
from .redir import blog
from .redir import blog_entry
from .redir import blog_slash


def default(request):
    """
    This is the default view, to be used with every route since we provide
    no content editing functionality yet. Even then, maybe a default view
    could still be used?
    """
    return {}


def main(global_config, **settings):
    """
    Oppan wsgi style! This is the WSGI application, y'all.
    """
    config = Configurator()

    # Redirs for blog shuffle
    config.add_route('blog', '/blog')
    config.add_route('blog_entry', '/blog/{entry:.*}')
    config.add_route('blog_slash', '/blog/')

    # Everything else
    config.add_route('contact', '/contact')
    config.add_route('clients', '/clients')
    config.add_route('projects', '/projects')
    config.add_route('services', '/services')
    config.add_route('team', '/team')
    config.add_route('testimonials', '/testimonials')
    config.add_route('root', '/')

    # Static resources
    config.add_static_view(
        'static', 'aclarknet:static', cache_max_age=3600)

    # XXX Consider using view decorator instead
    config.add_view(  # Redir
        blog,
        route_name='blog')
    config.add_view(  # Redir
        blog_entry,
        route_name='blog_entry')
    config.add_view(  # Redir
        blog_slash,
        route_name='blog_slash')
    config.add_view(
        default,
        renderer='aclarknet:templates/clients.mak',
        route_name='clients')
    config.add_view(
        default,
        renderer='aclarknet:templates/contact.mak',
        route_name='contact')
    config.add_view(
        default,
        renderer='aclarknet:templates/projects.mak',
        route_name='projects')
    config.add_view(
        default,
        renderer='aclarknet:templates/root.mak',
        route_name='root')
    config.add_view(
        default,
        renderer='aclarknet:templates/services.mak',
        route_name='services')
    config.add_view(
        default,
        renderer='aclarknet:templates/testimonials.mak',
        route_name='testimonials')
    config.add_view(
        default,
        renderer='aclarknet:templates/team.mak',
        route_name='team')

    return config.make_wsgi_app()
