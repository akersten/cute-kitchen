# ######################################################################################################################
# Generic top-level routes like the splash screen.
# ######################################################################################################################

from flask import render_template, abort, redirect, url_for

from .annotations import get_route_business_logic, get_route_vm_logic
from .context import get_request_context, get_request_session, get_request_request
from ..controller.security import run_endpoint_checks


# #########
# region Status code pages
# #########

def status_403():
    return generic_path_render("error/403.html"), 403


def status_404():
    return generic_path_render("error/404.html"), 404


def status_500():
    return generic_path_render("error/500.html"), 500


# #########
# endregion
# #########

# #########
# region Unauthenticated routes
###########

def splash():
    """
    The splash screen for the CuteKitchen homepage.
    :return: The rendered template.
    """
    return generic_path_render("outside/splash/splash.html")


def privacy():
    """
    The privacy policy for CuteKitchen.
    :return: The rendered template.
    """
    return generic_path_render("outside/privacy/privacy.html")


def terms():
    """
    The terms of use for CuteKitchen.
    :return: The rendered template.
    """
    return generic_path_render("outside/terms/terms.html")


def license():
    """
    The license for CuteKitchen.
    :return: The rendered template.
    """
    return generic_path_render("outside/license/license.html")


# #########
# endregion
# #########

# #########
# region Router functions
# #########

def generic_path_render(file):
    """
    A generic renderer for a static page.
    :param file: The filename to render.
    :return: The rendered template for a static page.
    """
    return render_template(file)


def generic_logic_render(file, fn, pathOnSuccess=None, pathOnFail=None):
    """
    Renders the given template in the context of the calling function. The calling function should be an endpoint
    decorated with annotations from the annotations file.
    :param file: The filename to render.
    :param fn: The endpoint we're rendering from.
    :param pathOnSuccess: The path to redirect to if the endpoint's logic returns True.
    :param fileOnFail: The path to redirect to if the endpoint's logic returns False.
    :return: The rendered template for a page.
    """
    if not run_endpoint_checks(get_request_session(), get_request_context(), get_request_request(), fn):
        abort(403)

    logic = get_route_business_logic(fn)
    if logic is not None:
        if not logic(get_request_session(), get_request_context(), get_request_request()):
            if pathOnFail is not None:
                return redirect(url_for(pathOnFail))

            abort(500)

        if pathOnSuccess is not None:
            return redirect(url_for(pathOnSuccess))

    vmFn = get_route_vm_logic(fn)
    vm = None
    if vmFn is not None:
        vm = vmFn(get_request_session(), get_request_context(), get_request_request())

    return render_template(file, vm=vm)

# #########
# endregion
# #########
