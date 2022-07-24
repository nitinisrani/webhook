from flask import Flask

from .webhook.routes import webhook
from .main import main
from .extensions import mongo


# Creating our flask app
def create_app():

    app = Flask(__name__)
    
    # app.config["MONGO_URI"] = 

    mongo.init_app(app, uri = "mongodb://localhost:27017/gitdb")
    
    # registering all the blueprints
    app.register_blueprint(main)
    app.register_blueprint(webhook)
    
    return app
