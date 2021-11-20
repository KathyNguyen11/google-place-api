# app/__init__.py
from http import HTTPStatus

from flask import request, make_response
from flask_api import FlaskAPI
# local import
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError

from app.schema import GetPhoneNumberRequestSchema, GetPhoneNumberResponseSchema
from app.service import GooglePlaceService


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    ma = Marshmallow(app)
    cors = CORS(app)

    @app.route('/getphonenumber/', methods=['GET'])
    def getphonenumber():
        try:
            input_data = GetPhoneNumberRequestSchema().load(data=request.args)
            address = input_data.get('address')
            is_success, response = GooglePlaceService.get_formatted_phone_number(address)

            if is_success:
                return make_response(GetPhoneNumberResponseSchema().dump(response)), HTTPStatus.OK
            return make_response({'message': response}), HTTPStatus.NOT_FOUND
        except ValidationError as err:
            return make_response(err.messages), HTTPStatus.BAD_REQUEST

    return app
