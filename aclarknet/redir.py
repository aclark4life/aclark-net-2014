from pyramid.httpexceptions import HTTPMovedPermanently


BLOG_URL = "http://blog.aclark.net"


def blog(request):
    """
    Handle blog move from aclark.net/blog to blog.aclark.net
    """
    return HTTPMovedPermanently(location=BLOG_URL)


def blog_entry(request):
    """
    Handle blog move from aclark.net/blog/{entry} to blog.aclark.net/entry
    """
    entry = request.matchdict['entry']
    return HTTPMovedPermanently(
        location="%s/%s" % (BLOG_URL, entry))


def blog_slash(request):
    """
    Handle blog move from aclark.net/blog/ to blog.aclark.net
    """
    return HTTPMovedPermanently(location=BLOG_URL)
