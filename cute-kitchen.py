from flask import Flask

from src.router.routes import init_all_routes
from src.router.generic import status_403, status_404, status_500

app = Flask(__name__)

init_all_routes(app)


@app.errorhandler(403)
def e403(e):
    return status_403()

@app.errorhandler(404)
def e404(e):
    return status_404()

app.secret_key = "DEBUG SECRET KEY, CHANGE BEFORE DEPLOYMENT"

if __name__ == '__main__':
    app.run()
