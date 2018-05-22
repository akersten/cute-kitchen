

def route_login_required():
    """
    Decorates a function to indicate the requirement for a logged-in session.
    :return: The decorated function.
    """
    def decorator(fn):
        fn.route_login_required = True
        return fn
    return decorator


def is_route_login_required(fn):
    """
    Determine if a function is decorated to require a logged-in session.
    :param fn: The function to check.
    :return: True if this function requires a logged-in session, False otherwise.
    """
    return hasattr(fn, "route_login_required") and fn.route_login_required
