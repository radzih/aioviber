from . import base
from . import fields
from .location import Location

class Account(base.ViberObject):
    id: str = fields.Field()
    name: str = fields.Field()
    uri: str = fields.Field()
    icon: str = fields.Field()
    background: str = fields.Field()
    category: str = fields.Field()
    subcategory: str = fields.Field()
    location: Location = fields.Field()
    country: str = fields.Field()
    webhook: str = fields.Field()
    event_types: list = fields.Field()
    subscribers_count: int = fields.Field()
    members: list = fields.Field()
    