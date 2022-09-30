from . import base
from . import fields

class Sticker(base.ViberObject):
    id = fields.Field(alias='sticker_id')