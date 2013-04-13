from pyramid.httpexceptions import HTTPMovedPermanently


REDIR_TO = 'http://blog.aclark.net'


def blog(request):
    """
    Redir: aclark.net/blog -> blog.aclark.net
    """
    return HTTPMovedPermanently(location=REDIR_TO)


def blog_entry(request):
    """
    Redir: aclark.net/blog/{entry} -> blog.aclark.net/entry
    """
    entry = request.matchdict['entry']
    return HTTPMovedPermanently(location="%s/%s" % (REDIR_TO, entry))


def blog_slash(request):
    """
    Redir: aclark.net/blog/ -> blog.aclark.net
    """
    return HTTPMovedPermanently(location=REDIR_TO)
