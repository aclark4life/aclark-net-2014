# XXX Why am I putting code in __init__.py?
from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPMovedPermanently


# XXX Some day, do something useful here. E.g. enable some CRUD functionality
# for the website content just like a CMS! ;-)
def clients(request):
    """
    """
    return {}


def blog(request):
    """
    Handle blog move from aclark.net/blog to blog.aclark.net
    """
    return HTTPMovedPermanently(location="http://%s%s" % (
        'blog.aclark.net', request.path_qs.replace('/blog', '')))


def blog_entry(request):
    """
    Handle blog move from aclark.net/blog to blog.aclark.net
    """
    entry = request.matchdict['entry']
    return HTTPMovedPermanently(location="http://%s%s" % (
        'blog.aclark.net', request.path_qs.replace('/blog', '') + entry))


def contact(request):
    """
    """
    return {}


def projects(request):
    """
    """
    return {}


def root(request):
    """
    """
    return {}


def services(request):
    """
    """
    return {}


def testimonials(request):
    """
    """
    return {}


def team(request):
    """
    """
    return {}


def main(global_config, **settings):
    """
    """
    config = Configurator()

    # Redirs
    config.add_route('blog_entry', '/blog/{entry}')
    config.add_route('blog', '/blog')

    # Everything else
    config.add_route('contact', '/contact')
    config.add_route('clients', '/clients')
    config.add_route('projects', '/projects')
    config.add_route('services', '/services')
    config.add_route('team', '/team')
    config.add_route('testimonials', '/testimonials')
    config.add_route('root', '/')

    config.add_static_view(
        'static', 'aclarknet:static', cache_max_age=3600)

    # XXX Consider using view decorator instead
    config.add_view(
        blog,
        route_name='blog')
    config.add_view(
        blog_entry,
        route_name='blog_entry')
    config.add_view(
        clients,
        renderer='aclarknet:templates/clients.mak',
        route_name='clients')
    config.add_view(
        contact,
        renderer='aclarknet:templates/contact.mak',
        route_name='contact')
    config.add_view(
        projects,
        renderer='aclarknet:templates/projects.mak',
        route_name='projects')
    config.add_view(
        root,
        renderer='aclarknet:templates/root.mak',
        route_name='root')
    config.add_view(
        services,
        renderer='aclarknet:templates/services.mak',
        route_name='services')
    config.add_view(
        testimonials,
        renderer='aclarknet:templates/testimonials.mak',
        route_name='testimonials')
    config.add_view(
        team,
        renderer='aclarknet:templates/team.mak',
        route_name='team')

    return config.make_wsgi_app()
