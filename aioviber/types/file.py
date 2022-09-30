from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from . import base
from . import fields


class File(base.ViberObject):
    url: str = fields.Field(alias='media')
    size: bytes = fields.Field(base=bytes)
    file_name: str = fields.Field()
    