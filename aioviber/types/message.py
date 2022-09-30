import functools

from . import base
from . import fields
from .user import User
from .account import Account
from .location import Location
from .contact import Contact
from .location import Location
from .sticker import Sticker
from .picture import Picture
from .file import File
from .video import Video
from ..utils import helper


class Message(base.ViberObject):
    token: int = fields.Field(alias='message_token')
    sender: User = fields.Field(base=User)
    text: str = fields.Field()
    media: str = fields.Field()
    tracking_data: str = fields.Field()
    file: File = fields.Field(base=File)
    video: Video = fields.Field(base=Video)
    contact: Contact = fields.Field(base=Contact)
    picture: Picture = fields.Field(base=Picture)
    location: Location = fields.Field(base=Location)
    content_type: 'ContentType' = fields.Field(alias='type')
    sticker: Sticker = fields.Field(base=Sticker, alias='sticker_id')
    

class ContentType(helper.Helper):
    
    mode = helper.HelperMode.snake_case
    
    TEXT = helper.Item()
    PICTURE = helper.Item()
    VIDEO = helper.Item()
    FILE = helper.Item()
    CONTACT = helper.Item()
    LOCATION = helper.Item()
    STICKER = helper.Item()
    URL = helper.Item()
    CAROUSEL_CONTENT = helper.Item()