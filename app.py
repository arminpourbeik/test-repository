# import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from code.security import authenticate, identity
from code.resources.user import UserRegister
from code.resources.item import Item, ItemList
from code.resources.store import Store, StoreList
from code.db import db

app = Flask(__name__)
app.secret_key = 'armin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
