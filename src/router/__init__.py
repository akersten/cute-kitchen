# ######################################################################################################################
# Everything in the router directory should be a  straightforward mapping from endpoint to logic. Anything that is
# more complex than one line (e.g. anything that needs logic beyond "render this template") should call out to the
# router-logic package.
# ######################################################################################################################

from flask import Flask

from . import generic


def init_routes(flask_app: Flask):
    flask_app.add_url_rule("/", "splash", methods=["GET"], view_func=generic.splash)
    flask_app.add_url_rule("/privacy", "privacy", methods=["GET"], view_func=generic.privacy)
    flask_app.add_url_rule("/license", "license", methods=["GET"], view_func=generic.license)
    flask_app.add_url_rule("/terms", "terms", methods=["GET"], view_func=generic.terms)
