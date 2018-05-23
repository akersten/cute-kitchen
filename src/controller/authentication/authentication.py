from ..security import user_is_logged_in
from ...logic.security import user_attempt_login


def login(session, g, request):
    if user_is_logged_in(session, g, request):
        # Should not be POSTing to login if you're already logged in.
        return False

    username = request.form.get("input-username")
    password = request.form.get("input-password")

    if not user_attempt_login(username, password):
        return False

    session["username"] = username

    return True


def logout(session, g, request):
    session.pop("username", None)
    return True