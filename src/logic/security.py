# ######################################################################################################################
# Backend security logic.
# ######################################################################################################################

def user_attempt_login(username, password):
    """
    Determine if the provided information constitutes a valid login.
    :param username: The username with which to attempt a login.
    :param password: The password with which to attempt a login.
    :return: True if the user should be granted access to the application. False otherwise.
    """
    if username is None or password is None:
        return False

    if len(username) == 0 or len(password) == 0:
        return False

    if username == "fail":
        return False

    #TODO: Actually validate.
    return True
