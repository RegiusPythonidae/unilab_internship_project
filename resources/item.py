from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from modules.item import ItemModel


class ItemList(Resource):

    def get(self):
        product_list = ItemModel.get_all_items()
        return product_list, 200

    @jwt_required()
    def delete(self):
        ItemModel.delete_all_items()
        return "Product list purged", 200


class Item(Resource):

    product_parser = reqparse.RequestParser()
    product_parser.add_argument('product_name', type=str, required=True, help="Name can not be blank")
    product_parser.add_argument('product_price', type=float, required=True, help="Price can not be blank")

    def get(self, product_id):
        product = ItemModel.find_by_id(product_id)
        if product is not None:
            return product.json(), 200
        else:
            return "Product not found", 404

    @jwt_required()
    def post(self, product_id):
        product = ItemModel.find_by_id(product_id)

        if product:
            return "A product by such ID already exists", 400

        product_details = Item.product_parser.parse_args()
        new_product = ItemModel(product_id, product_details['product_name'], product_details['product_price'])
        new_product.save_to_db()
        return "The product has been added to the list", 200

    @jwt_required()
    def put(self, product_id):
        product = ItemModel.find_by_id(product_id)
        product_details = Item.product_parser.parse_args()

        if product is None:
            product = ItemModel(product_id, **product_details)
            product.save_to_db()
            return "Product created", 200
        else:
            product.product_name = product_details['product_name']
            product.product_price = product_details['product_price']
            product.save_to_db()
            return "Product updated", 200

    @jwt_required()
    def delete(self, product_id):
        product = ItemModel.find_by_id(product_id)

        if product is not None:
            product.remove_from_db()
            return "Product removed", 200
        else:
            return "Product not found", 404