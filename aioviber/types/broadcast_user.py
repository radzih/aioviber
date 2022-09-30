from datetime import datetime
from . import base
from . import fields


class BroadcastUser(base.ViberObject):
    
    id: str = fields.Field()
    online_status: int = fields.Field()
    online_status_message: str = fields.Field()
    last_online: datetime = fields.DateTimeField()