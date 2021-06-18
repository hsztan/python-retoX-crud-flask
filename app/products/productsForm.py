from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired, EqualTo


class ProductsForm(FlaskForm):
    name = StringField('Producto', validators=[
        DataRequired('Este campo es requerido')])
    stock = IntegerField('Stock', validators=[
        DataRequired('Este campo es requerido')])
    price = FloatField('Precio', validators=[
        DataRequired('Este campo es requerido')])
    submit = SubmitField('Ingresar')
