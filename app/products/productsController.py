from app import db
from flask import redirect, url_for, flash
from flask_login import current_user
from app.products.productsModel import ProductsModel
from app.sales.salesModel import SalesModel


class ProductsController:
    def records(self, page):
        return ProductsModel.query.order_by(ProductsModel.id).paginate(
            page=page, per_page=5
        )

    def create(self, form):
        try:
            name_product = form.name.data
            stock_product = form.stock.data
            price_product = form.price.data
            product = ProductsModel(
                name=name_product, stock=stock_product, price=price_product)
            db.session.add(product)
            db.session.commit()
            flash(
                f'Se creo el producto {name_product} con exito !', 'success')
            return redirect(url_for('products'))
        except Exception as e:
            db.session.rollback()
            if 'Unique' in str(e):
                flash(f'Ese producto ya existe!', 'danger')
            else:
                flash(f'Ocurrio un error -> {str(e)}', 'danger')
            return redirect(url_for('products_create'))

    def update(self, form, product_id):
        if current_user.rol.name != "admin":
            return redirect(url_for('products'))
        try:
            name_product = form.name.data
            stock_product = form.stock.data
            price_product = form.price.data
            product = ProductsModel.query.filter_by(id=product_id).first()
            product.name = name_product
            product.stock = stock_product
            product.price = price_product
            db.session.commit()
            flash('Se actualizo el producto con exito !', 'success')
            return redirect(url_for('products'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', 'danger')
            return redirect(url_for('products_update', id=product_id))

    def delete(self, product_id):
        try:
            product = ProductsModel.query.filter_by(id=product_id).first()
            db.session.delete(product)
            # status = 0 if product.status == 1 else 1
            # product.status = status
            db.session.commit()
            flash('Se cambio el estado con exito !', 'success')
            return redirect(url_for('products'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', 'danger')
            return redirect(url_for('products'))

    def buy(self, form, id):
        try:
            product = ProductsModel.query.filter_by(id=id).first()
            product_amount = form.quantity.data
            if product_amount > 0 or product_amount > product.stock:
                sale = SalesModel(quantity=product_amount,
                                  user_id=current_user.id, product_id=product.id)
                product.stock -= product_amount
                db.session.add(sale)
                db.session.commit()
                flash(
                    f'Se agregó {product_amount} de {product.name} al carrito !', 'success')
                return redirect(url_for('products'))
            elif product_amount < product.stock:
                flash(
                    f'No hay suficiente stock de {product.name}', 'success')
                return redirect(url_for('products'))
            else:
                flash(
                    f'Hiceste algo indebido, muy mal!', 'success')
                return redirect(url_for('products'))
        except Exception as e:
            db.session.rollback()
            if 'Unique' in str(e):
                flash(f'Ese producto ya existe!', 'danger')
            else:
                flash(f'Ocurrio un error -> {str(e)}', 'danger')
            return redirect(url_for('products_create'))
