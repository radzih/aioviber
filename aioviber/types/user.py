from . import base
from . import fields

class User(base.ViberObject):
    id: str = fields.Field()
    name: str = fields.Field()
    avatar: str = fields.Field()
    country: str = fields.Field()
    language: str = fields.Field()
    primary_device_os: str = fields.Field()
    api_version: int = fields.Field()
    viber_version: str = fields.Field()
    mobile_country_code: str = fields.Field(alias='mcc')
    mobile_network_code: str = fields.Field(alias='mnc')
    device_type: str = fields.Field()