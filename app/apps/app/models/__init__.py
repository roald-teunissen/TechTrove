from flask import Blueprint
from .product import Product
from .product_category import ProductCategory
from .manufacturer import Manufacturer
from .vendor import Vendor

blueprint = Blueprint(
    'models_blueprint',
    __name__,
    url_prefix=''
)
