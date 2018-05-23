# ######################################################################################################################
# Authentication routes handle login, logout, registration, password recovery, etc. Typically we don't have an existing
# user session yet.
# ######################################################################################################################

from flask import redirect, url_for

from ..generic import generic_path_render, generic_logic_render
from ..annotations import route_business_logic
from ..context import is_request_post, get_request_request, get_request_context, get_request_session
from ...controller.security import user_is_logged_in
from ...controller.authentication import authentication

@route_business_logic(authentication.login)
def login():
    if is_request_post():
        return generic_logic_render("authentication/login/login.html", login, "home", "login")

    if user_is_logged_in(get_request_session(), get_request_context(), get_request_request()):
        return redirect(url_for("home"))

    return generic_path_render("authentication/login/login.html")


def register():
    return generic_path_render("authentication/register/register.html")


@route_business_logic(authentication.logout)
def logout():
    return generic_logic_render("outside/splash/splash.html", logout)
