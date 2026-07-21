from flask import Flask

from db.connection import engine, Base
from db import models
from routes.article_routes import article_routes

app = Flask(__name__)

Base.metadata.create_all(engine)

app.register_blueprint(article_routes)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
