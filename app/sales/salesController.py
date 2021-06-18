from app import db
from app.sales.salesModel import SalesModel
from app.products.productsModel import ProductsModel


class SalesController:
    def records(self, page):
        return SalesModel.query.order_by(SalesModel.id).paginate(
            page=page, per_page=5
        )
