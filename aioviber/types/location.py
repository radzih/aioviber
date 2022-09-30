from . import base
from . import fields

class Location(base.ViberObject):
    latitude: float = fields.Field(base=float,alias='lat')
    longitude: float = fields.Field(base=float,alias='lon')

    def __init__(
        self,
        latitude: float = None,
        longitude: float = None,
        **kwargs,
    ):
        super(Location, self).__init__(
            latitude=latitude,
            longitude=longitude,
            **kwargs
        )