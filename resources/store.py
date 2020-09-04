from flask_restful import Resource
from flask_restful import reqparse
from code.models.store import StoreModel


class Store(Resource):
    @staticmethod
    def get(name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {'message': 'Store not found'}, 404

    @staticmethod
    def post(name):
        if StoreModel.find_by_name(name):
            return {'message': f'A store with name {name} already exists'}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred while creating the store'}, 500
        return store.json(), 201

    @staticmethod
    def delete(name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': 'Store deleted'}


class StoreList(Resource):
    @staticmethod
    def get():
        return {'stores': [store.json() for store in StoreModel.query.all()]}
