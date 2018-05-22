from ..router.annotations import is_route_login_required

def run_endpoint_checks(session, g, function):
    """
    Given an endpoint function, check for security dictated by its decorators. This includes things like whether we're
    logged in, or whether we have the correct security.
    :param session: The application session.
    :param g: The application context.
    :param function: The endpoint function to inspect for security requirements.
    :return: True if the user in the application context should be allowed to access this endpoint. False otherwise.
    """
    if is_route_login_required(function):
        if 'username' not in session:
            return False

    return True