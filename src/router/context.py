from flask import g, session, request

def is_request_post():
    return request.method == "POST"

def get_request_session():
    """
    Pulls the session variable out of the web platform (currently Flask) for us to use for business logic. Don't really
    want to mingle the web framework with the core logic so we pull out the important piece here and pass it down when
    relevant.
    :return: The session object with the context of the current request. The session object contains things like cookie
             data and per-user variables.
    """
    return session

def get_request_context():
    """
    Pulls the context variable out of the web platform (currently Flask) for us to use for business logic. Don't really
    want to mingle the web framework with the core logic so we pull out the important piece here and pass it down when
    relevant.
    :return: The "global" object with the context of the current request. The global object contains singletons or other
             persistent references.
    """
    return g

def get_request_request():
    """
    Pulls the request variable out of the web platform (currently Flask) for us to use for business logic. Don't really
    want to mingle the web framework with the core logic so we pull out the important piece here and pass it down when
    relevant.
    :return: The request object with the context of the current request. The request object contains things like POST
             data and URL parameters.
    """
    return request
