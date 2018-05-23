from ..router.annotations import is_route_login_required


def user_is_logged_in(session, g, request):
    return 'username' in session


def run_endpoint_checks(session, g, request, function):
    """
    Given an endpoint function, check for security dictated by its decorators. This includes things like whether we're
    logged in, or whether we have the correct security.
    :param session: The application session.
    :param g: The application context.
    :param request: The application request.
    :param function: The endpoint function to inspect for security requirements.
    :return: True if the user in the application context should be allowed to access this endpoint. False otherwise.
    """
    if is_route_login_required(function):
        if not user_is_logged_in(session, g, request):
            return False

    #TODO: Check security level.

    return True
