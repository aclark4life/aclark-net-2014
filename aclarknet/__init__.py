from pyramid.config import Configurator


def root(request):
    """
    """
    return {}


def main(global_config, **settings):
    """
    """
    config = Configurator()

    config.add_route('root', '/')
    config.add_view(
        root, route_name='root',
        renderer='aclarknet:templates/root.mak')

    config.add_route('about', '/about')
    config.add_view(
        'aclarknet.views.about',
        route_name='about',
        renderer='aclarknet:templates/about.mak')

    config.add_route('contact', '/contact')
    config.add_view(
        'aclarknet.views.contact',
        route_name='contact',
        renderer='aclarknet:templates/contact.mak')

    config.add_route('projects', '/projects')
    config.add_view(
        'aclarknet.views.projects',
        route_name='projects',
        renderer='aclarknet:templates/projects.mak')

    config.add_static_view(
        'static', 'aclarknet:static', cache_max_age=3600)

    return config.make_wsgi_app()
