from flask import Flask, redirect
from flask_restful import Api
from security import *
from flask_jwt import JWT
from resources.item import *
from resources.user import *


app = Flask(__name__)
app.config['SECRET_KEY'] = '91939'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api = Api(app)
jwt = JWT(app, authenticate, identity)

api.add_resource(ItemList, "/items")
api.add_resource(Item, "/items/<int:product_id>")
api.add_resource(RegisterUser, "/registration")

@app.route("/")
def home():
    return redirect("https://github.com/RegiusPythonidae/unilab_internship_project/tree/main"), 302

if __name__ == '__main__':
    app.run()
