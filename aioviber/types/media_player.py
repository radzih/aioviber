from . import base
from . import fields


class MediaPlayer(base.ViberObject):

    title: str = fields.Field(alias='Title')
    subtitle: str = fields.Field(alias='Subtitle')
    thubnail: str = fields.Field(alias='ThumbnailURL')
    loop: bool = fields.Field(alias='Loop')
    
    
    def __init__(
        self,
        title: str = None,
        subtitle: str = None,
        thubnail: str = None,
        loop: bool = None,
    ):
        super().__init__(
            title=title,
            subtitle=subtitle,
            thubnail=thubnail,
            loop=loop,
        )