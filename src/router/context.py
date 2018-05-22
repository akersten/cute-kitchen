from flask import g, session


def get_request_session():
    """
    Pulls the session variable out of the web platform (currently Flask) for us to use for business logic. Don't really
    want to mingle the web framework with the core logic so we pull out the important piece here and pass it down when
    relevant.
    :return: The session object with the context of the current request.
    """
    return session

def get_request_context():
    """
    Pulls the context variable out of the web platform (currently Flask) for us to use for business logic. Don't really
    want to mingle the web framework with the core logic so we pull out the important piece here and pass it down when
    relevant.
    :return: The "global" object with the context of the current request.
    """
    return g
