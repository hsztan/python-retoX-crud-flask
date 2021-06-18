from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired


class SalesForm(FlaskForm):
    quantity = IntegerField(label="Cantidad", validators=[
        DataRequired('Este campo es requerido')])
    submit = SubmitField('Comprar')
