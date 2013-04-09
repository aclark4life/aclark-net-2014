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
        renderer='pythonpackages:templates/root.mak')

    config.add_route('about', '/about')
    config.add_view(
        'pythonpackages.views.about',
        route_name='about',
        renderer='pythonpackages:templates/about.mak')

    config.add_route('contact', '/contact')
    config.add_view(
        'pythonpackages.views.contact',
        route_name='contact',
        renderer='pythonpackages:templates/contact.mak')

    config.add_static_view(
        'static', 'pythonpackages:static', cache_max_age=3600)

    return config.make_wsgi_app()
