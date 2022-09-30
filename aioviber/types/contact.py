from . import base
from . import fields


class Contact(base.ViberObject):
    name: str = fields.Field()
    phone_number: str = fields.Field()

    def __init__(
        self,
        name: str = None,
        phone_number: str = None,
    ):
        super().__init__(name=name, phone_number=phone_number)