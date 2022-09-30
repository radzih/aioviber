from typing import Literal
from . import base
from . import fields


class InternalBrowser(base.ViberObject):
    
    action_button: str = fields.Field(alias='ActionButton')
    action_predefined_url: str = fields.Field(alias='ActionPredefinedURL')
    title_type: str = fields.Field(alias='TitleType')
    custom_title: str = fields.Field(alias='CustomTitle')
    mode: str = fields.Field(alias='Mode')
    footer_type: str = fields.Field(alias='FooterType')
    action_reply_data: str = fields.Field(alias='ActionReplyData')

    def __init__(
        self,
        action_button: Literal[
            'forward', 'send',
            'open-externaly', 'send-to-bot', ''
            ] = None,
        action_predefined_url: str = None,
        title_type: Literal['domain', 'default'] = None,
        custom_title: str = None,
        mode: Literal[
            'fullscreen', 'fullscreen-portrait', 
            'fullscreen-landscape', 'partial-size'
            ] = None,
        footer_type: Literal['default', 'hidden'] = None,
        action_reply_data: str = None,
    ):
        super().__init__(
            action_button=action_button,
            action_predefined_url=action_predefined_url,
            title_type=title_type,
            custom_title=custom_title,
            mode=mode,
            footer_type=footer_type,
            action_reply_data=action_reply_data,
        )
