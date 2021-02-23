from flask import Flask
from flask_restful import Api
from security import *
from flask_jwt import JWT
from resources.item import *
from resources.user import *
from db import db

app = Flask(__name__)
app.config['SECRET_KEY'] = '91939'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


api = Api(app)
jwt = JWT(app, authenticate, identity)
db.init_app(app)

@app.before_first_request
def initialize_tables():
    db.create_all()


api.add_resource(ItemList, "/items")
api.add_resource(Item, "/items/<int:product_id>")
api.add_resource(RegisterUser, "/registration")


if __name__ == '__main__':

    app.run()
