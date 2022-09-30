from . import base
from . import fields
from ..utils import helper
from .button import Button
from typing import List, Literal, Union, NewType, TypeVar


class InputFieldState(helper.Helper):
    
    mode = helper.HelperMode.lowercase
    
    REGULAR = helper.Item()
    MINIMIZED = helper.Item()
    HIDDEN = helper.Item()


class Keyboard(base.ViberObject):

    buttons: List[Button] = fields.ListField(base='KeyboardButton', alias='Buttons')
    type: str = fields.Field(alias='Type', default='keyboard')
    default_height: bool = fields.Field(alias='DefaultHeight')
    background_color: str = fields.Field(alias='BgColor')
    custom_default_height: int = fields.Field(alias='CustomDefaultHeight')
    height_scale: int = fields.Field(alias='HeightScale')
    button_group_collumns: int = fields.Field(alias='ButtonGroupColumns')
    button_group_rows: int = fields.Field(alias='ButtonGroupRows')
    input_field_state: str  = fields.Field(alias='InputFieldState')
    favorites_metadata: str = fields.Field(alias='FavoritesMetadata')


    def __init__(
        self,
        buttons: list[Button] ,
        type: str = None,
        default_height: bool = False,
        background_color: str = None,
        custom_default_height: int = None,
        height_scale: int = None,
        button_group_collumns: int = None,
        button_group_rows: int = None,
        input_field_state: Literal['regular', 'minimized', 'hidden'] = None,
        favorites_metadata: str = None,
    ):
        super().__init__(
            buttons=buttons,
            type=type,
            default_height=default_height,
            background_color=background_color,
            custom_default_height=custom_default_height,
            height_scale=height_scale,
            button_group_collumns=button_group_collumns,
            button_group_rows=button_group_rows,
            input_field_state=input_field_state,
            favorites_metadata=favorites_metadata,
        )
