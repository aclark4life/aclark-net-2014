# XXX Why am I putting code in __init__.py?
from pyramid.config import Configurator


def main(global_config, **settings):
    """
    """
    config = Configurator()

    config.add_route('about', '/about')
    config.add_route('contact', '/contact')
    config.add_route('projects', '/projects')
    config.add_route('root', '/')

    config.add_static_view(
        'static', 'aclarknet:static', cache_max_age=3600)

    # XXX Consider using view decorator instead
    config.add_view(
        'aclarknet.views.about',
        renderer='aclarknet:templates/about.mak',
        route_name='about')
    config.add_view(
        'aclarknet.views.contact',
        renderer='aclarknet:templates/contact.mak',
        route_name='contact')
    config.add_view(
        'aclarknet.views.projects',
        renderer='aclarknet:templates/projects.mak',
        route_name='projects')
    config.add_view(
        'aclarknet.views.root',
        renderer='aclarknet:templates/root.mak',
        route_name='root')

    return config.make_wsgi_app()
