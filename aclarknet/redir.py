from pyramid.httpexceptions import HTTPMovedPermanently


BLOG_URL = 'http://blog.aclark.net'


def blog(request):
    """
    Redirect http://aclark.net/blog to http//blog.aclark.net
    """
    return HTTPMovedPermanently(location=BLOG_URL)


def blog_entry(request):
    """
    Redirect http://aclark.net/blog/{entry} to http://blog.aclark.net/{entry}
    """
    entry = request.matchdict['entry']
    return HTTPMovedPermanently(location="%s/%s" % (BLOG_URL, entry))


def blog_slash(request):
    """
    Redirect http://aclark.net/blog/ to http://blog.aclark.net
    """
    return HTTPMovedPermanently(location=BLOG_URL)


def book(request):
    """
    Redirect http://aclark.net/book to http://www.packtpub.com/plone-33-site-administration/book
    """
    return HTTPMovedPermanently(location='http://www.packtpub.com/plone-33-site-administration/book')
