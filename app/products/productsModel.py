from app import db
from sqlalchemy.sql import func


class ProductsModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True, unique=True)
    stock = db.Column(db.Integer)
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())  # SELECT NOW()
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    #
    sales = db.relationship('SalesModel', back_populates='product')

    def __repr__(self):
        return f'Product: {self.name}'
