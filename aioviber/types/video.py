from . import base
from . import fields


class Video(base.ViberObject):
    
    url: str = fields.Field(alias='media')
    size: bytes = fields.Field(base=bytes)
    duration: int = fields.Field()
    thumbnail: str = fields.Field()