import json

from flask import request
from flask_restx import Api, Resource
from werkzeug.datastructures import MultiDict

from apps.api import blueprint
from apps.authentication.decorators import token_required
from apps.authentication.models import Users

from apps.api.forms import *
from apps.models    import *

api = Api(blueprint)

# TODO: DELETE and PUT have to be implemented
# TODO: Implement a user permission system to not allow everyone to access user info
@api.route('/users/', methods=['GET']) 
class UsersRoute(Resource):
    def get(self):
        all_objects = Users.query.all()
        output = [{'id': obj.id, **UsersForm(obj=obj).data} for obj in all_objects]
        return {
                'data': output,
                'success': True
            }, 200
            