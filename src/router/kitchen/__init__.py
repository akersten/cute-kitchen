from flask import Flask

from . import kitchen

def init_routes(flask_app: Flask):
    flask_app.add_url_rule("/home", "home", methods=["GET", "POST"], view_func=kitchen.home)
    flask_app.add_url_rule("/inventory", "inventory", methods=["GET", "POST"], view_func=kitchen.inventory)
    flask_app.add_url_rule("/shopping", "shopping", methods=["GET"], view_func=kitchen.shopping)
