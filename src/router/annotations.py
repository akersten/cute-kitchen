

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


def route_security_required():
    pass

def get_route_security_required():
    pass

def route_business_logic(logicFn):
    """
    Decorates a function to indicate the business logic that should be executed after security checks pass.
    :param logicFn: The business logic function to assign.
    :return: The decorated function.
    """
    def decorator(fn):
        fn.route_business_logic = logicFn
        return fn
    return decorator

def get_route_business_logic(fn):
    """
    Returns the business logic function associated with an endpoint.
    :param fn: The endpoint whose logic to return.
    :return: A function pointer to the business logic for an endpoint, or None if no such logic exists.
    """
    if not hasattr(fn, "route_business_logic"):
        return None
    return fn.route_business_logic
