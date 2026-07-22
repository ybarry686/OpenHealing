import os

from flask import Flask

from backend.config import Config
from backend.db.connection import engine, Base
from backend.db import models
from backend.routes.main_routes import main_bp
from backend.routes.auth_routes import auth_bp
from backend.routes.findhelp_routes import findhelp_bp
from backend.routes.resource_routes import resources_bp
from backend.routes.article_routes import article_routes
from backend.routes.forum_routes import forum_bp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(BASE_DIR)

app = Flask(
    __name__,
    template_folder=os.path.join(REPO_ROOT, "frontend", "templates"),
    static_folder=os.path.join(REPO_ROOT, "frontend", "static"),
    static_url_path="/static",
)

class PrefixMiddleware:
    def __init__(self, wsgi_app, prefix):
        self.wsgi_app = wsgi_app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        if self.prefix:
            environ["SCRIPT_NAME"] = self.prefix
            path_info = environ.get("PATH_INFO", "")
            if path_info.startswith(self.prefix):
                environ["PATH_INFO"] = path_info[len(self.prefix):]
        return self.wsgi_app(environ, start_response)


app.wsgi_app = PrefixMiddleware(app.wsgi_app, os.environ.get("SCRIPT_NAME", "/proxy/5001"))

app.secret_key = Config.SECRET_KEY

Base.metadata.create_all(engine)

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(findhelp_bp)
app.register_blueprint(resources_bp)
app.register_blueprint(article_routes)
app.register_blueprint(forum_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5001)