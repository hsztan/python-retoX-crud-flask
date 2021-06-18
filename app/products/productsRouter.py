from app import app
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.products.productsController import ProductsController
from app.products.productsForm import ProductsForm
from app.sales.salesForm import SalesForm
from app.products.productsModel import ProductsModel


@app.route('/products')
@login_required
def products():
    page = request.args.get('page', type=int, default=1)
    controller = ProductsController()
    products = controller.records(page)
    ##########
    form = SalesForm()
    return render_template('views/products/index.html', title='Products', data=products, form=form)


@app.route('/products/create', methods=['GET', 'POST'])
@login_required
def products_create():
    if current_user.rol.name != "admin":
        return redirect(url_for('products'))
    form = ProductsForm()
    if form.validate_on_submit():
        controller = ProductsController()
        return controller.create(form)
    return render_template('views/products/forms/create.html', title='Productos - Crear', form=form)


@app.route('/products/update/<int:id>', methods=['GET', 'POST'])
@login_required
def products_update(id):
    if current_user.rol.name != "admin":
        return redirect(url_for('products'))
    product = ProductsModel.query.get_or_404(id)
    form = ProductsForm(obj=product)
    if form.validate_on_submit():
        controller = ProductsController()
        return controller.update(form, id)
    print(product.id)
    return render_template('views/products/forms/update.html',
                           title='Categorias - Actualizar', form=form, product_id=product.id)


@app.route('/products/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def products_delete(id):
    if current_user.rol.name != "admin":
        return redirect(url_for('products'))
    controller = ProductsController()
    return controller.delete(id)


@app.route('/products/buy/<int:id>', methods=['GET', 'POST'])
@login_required
def products_buy(id):
    product = ProductsModel.query.get_or_404(id)
    form = SalesForm(obj=product)
    if form.validate_on_submit():
        controller = ProductsController()
        return controller.buy(form, id)
