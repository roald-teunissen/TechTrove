from flask import Blueprint
from models import *

blueprint = Blueprint(
    'models_blueprint',
    __name__,
    url_prefix=''
)
