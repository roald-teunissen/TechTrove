from wtforms import Form
from wtforms_alchemy import model_form_factory
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired

from apps.models import *

ModelForm = model_form_factory(Form)


class BookForm(ModelForm):
    class Meta:
        model = Book

class ManufacturerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])

class ProductCategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])

class VendorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    website = StringField('Website')

class ProductForm(FlaskForm):
    model = StringField('Model', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    price_when_bought = IntegerField('Price when bought', validators=[DataRequired()])
    description = TextAreaField('Description')
    EAN = StringField('EAN')
    manufacturer = StringField('Manufacturer', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    vendor = StringField('Vendor', validators=[DataRequired()])

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])

class BorrowForm(FlaskForm):
    product_id = IntegerField('Product ID', validators=[DataRequired()])
    user_id = IntegerField('User ID', validators=[DataRequired()])
    quantity = IntegerField('Quantity', default=1, validators=[DataRequired()])
    returned = IntegerField('Returned', default=0, validators=[DataRequired()])
    estimated_return_date = IntegerField('Estimated return date', default=0, validators=[DataRequired()])
    borrowed_at = IntegerField('Borrowed at', validators=[DataRequired()])

class OrderedForm(FlaskForm):
    product_id = IntegerField('Product ID', validators=[DataRequired()])
    vendor_id = IntegerField('Vendor ID', validators=[DataRequired()])
    ordered = IntegerField('Ordered', default=0, validators=[DataRequired()])
    delivered = IntegerField('Delivered', default=0, validators=[DataRequired()])
    ordered_at = IntegerField('Ordered at', validators=[DataRequired()])

