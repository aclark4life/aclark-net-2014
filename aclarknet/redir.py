from pyramid.httpexceptions import HTTPMovedPermanently


REDIR_TARGET_BASE = 'http://blog.aclark.net'


def blog(request):
    """
    Redirect http://aclark.net/blog to http//blog.aclark.net
    """
    return HTTPMovedPermanently(location=REDIR_TARGET_BASE)


def blog_entry(request):
    """
    Redirect http://aclark.net/blog/{entry} to http://blog.aclark.net/{entry}
    """
    entry = request.matchdict['entry']
    return HTTPMovedPermanently(location="%s/%s" % (REDIR_TARGET_BASE, entry))


def blog_slash(request):
    """
    Redirect http://aclark.net/blog/ to http://blog.aclark.net
    """
    return HTTPMovedPermanently(location=REDIR_TARGET_BASE)
