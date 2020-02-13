from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)

    #Initializing flask extension
    db.init_app(app)