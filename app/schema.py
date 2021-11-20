from marshmallow import fields, Schema


class GetPhoneNumberRequestSchema(Schema):
    address = fields.String(required=True, allow_none=False, validate=fields.validate.Length(min=1))


class GetPhoneNumberResponseSchema(Schema):
    formatted_phone_number = fields.String()
