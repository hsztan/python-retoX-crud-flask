from app import app
from flask_login import current_user, login_required
from flask import request, render_template
from app.sales.salesController import SalesController
from app.products.productsModel import ProductsModel
from app.products.productsController import ProductsController


@app.route('/sales/create/<int:product_id>', methods=['GET', 'POST'])
@login_required
def sales_create(product_id):
    product = ProductsModel.query.get_or_404(product_id)
# if form.validate_on_submit():
#     controller = SalesController()
#     return controller.create(form, id)
# # AQUÍ ABAJO ESTA EL PROBLEM
# print(product.id)
# return render_template('views/products/forms/update.html',
#                        title='Categorias - Actualizar', form=form, product_id=product.id)
