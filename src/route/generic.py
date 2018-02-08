# ######################################################################################################################
# Generic top-level routes like the splash screen.
# ######################################################################################################################

from flask import render_template


def splash():
    """
    The splash screen for the CuteKitchen homepage.
    :return: The rendered template.
    """
    return generic_path_render("splash/splash.html")


def app():
    """
    The main application path for CuteKitchen.
    :return: The rendered template.
    """
    return generic_path_render("cutekitchen-app/cutekitchen-app.html")


def generic_path_render(file):
    """
    A generic renderer for a static page.
    :param file: The filename to render.
    :return: The rendered template for a static page.
    """
    return render_template(file)
