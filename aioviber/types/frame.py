from . import base
from . import fields 


class Frame(base.ViberObject):
    
    border_width: int = fields.Field(alias='BorderWidth')
    border_color: str = fields.Field(alias='BorderColor')
    corner_radius: int = fields.Field(alias='CornerRadius')

    def __init__(
        self,
        border_width: int = None,
        border_color: str = None,
        corner_radius: int = None,
    ):
        super().__init__(
            border_width=border_width,
            border_color=border_color,
            corner_radius=corner_radius,
        )
