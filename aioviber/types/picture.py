from . import base
from . import fields


class Picture(base.ViberObject):
    url: str = fields.Field(alias='media')
    thumbnail: str = fields.Field()