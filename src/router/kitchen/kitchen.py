# ######################################################################################################################
# The kitchen routes cover the main functionality of the application.
# ######################################################################################################################

from ..generic import generic_path_render


def home():
    return generic_path_render("kitchen/home/home.html")


def inventory():
    return generic_path_render("kitchen/inventory/inventory.html")


def shopping():
    return generic_path_render("kitchen/shopping/shopping.html")
