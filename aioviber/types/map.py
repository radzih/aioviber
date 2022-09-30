from . import base
from . import fields 


class Map(base.ViberObject):
    latitude: float = fields.Field(alias='Latitude')
    longitude: float = fields.Field(alias='Longitude')

    def __init__(
        self,
        latitude: float = None,
        longitude: float = None,
    ):
        super().__init__(
            latitude=latitude,
            longitude=longitude,
        )