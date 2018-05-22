# ######################################################################################################################
# The kitchen routes cover the main functionality of the application.
# ######################################################################################################################

from ..generic import generic_logic_render
from ..annotations import route_login_required, route_business_logic
from ...business.kitchen import kitchen

@route_login_required()
@route_business_logic(kitchen.home)
def home():
    return generic_logic_render("kitchen/home/home.html", home)


@route_login_required()
@route_business_logic(kitchen.inventory)
def inventory():
    return generic_logic_render("kitchen/inventory/inventory.html", inventory)


@route_login_required()
@route_business_logic(kitchen.shopping)
def shopping():
    return generic_logic_render("kitchen/shopping/shopping.html", shopping)
