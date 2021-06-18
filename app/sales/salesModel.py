from app import db
from sqlalchemy.sql import func


class SalesModel(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())  # SELECT NOW()
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    #
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    ##
    product = db.relationship(
        'ProductsModel', uselist=False, back_populates='sales')
    user = db.relationship('UserModel', uselist=False,
                           back_populates='sales')  # [{}] -> {}

    def __repr__(self):
        return f'Product: {self.name}'
