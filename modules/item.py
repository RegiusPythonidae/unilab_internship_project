from db import db

class ItemModel(db.Model):

    __tablename__ = "Products"

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String, nullable=False)
    product_price = db.Column(db.String, nullable=False)
    product_qty = db.Column(db.String, nullable=False)

    def __init__(self, product_id, product_name, product_price, product_qty):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_qty = product_qty

    def json(self):
        if self is not None:
            return {"id": self.product_id, "name": self.product_name, "price": self.product_price, "qty": self.product_qty}

    @classmethod
    def get_all_items(cls):
        product_list = list(map(cls.json, ItemModel.query.all()))
        return product_list

    @classmethod
    def delete_all_items(cls):
        ItemModel.query.delete()
        db.session.commit()

    @classmethod
    def find_by_id(cls, product_id):
        found_product = ItemModel.query.filter_by(product_id=product_id).first()
        return found_product

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()
