from flask import Flask, render_template
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from app.utils import config

# -----------------------------------
# Flask app cofig
app = Flask(
    __name__,
    static_folder=config.get('server', 'static_folder'),
    template_folder=config.get('server', 'template_folder'),
    static_url_path='/static'
)

# -----------------------------------
# CORS
CORS(app)

# -----------------------------------
# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('database', 'url')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def create_tables(app):
    with app.app_context():
        import app.models
        db.create_all()

create_tables(app)

# -----------------------------------
# JWT
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# -----------------------------------
# Serve Vue app
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")

# -----------------------------------
# API
from app.api.routes import api
app.register_blueprint(api)