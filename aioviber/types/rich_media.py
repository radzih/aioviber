from . import base
from . import fields
from .button import Button


class RichMedia(base.ViberObject):
    type: str = fields.Field(default='rich_media', alias='Type')
    button_group_columns: int = fields.Field(alias='ButtonsGroupColumns')
    button_group_rows: int = fields.Field(alias='ButtonsGroupRows')
    bg_color: str = fields.Field(alias='BgColor')
    buttons: list[Button] = fields.ListField(base='Button', alias='Buttons')

    def __init__(
        self,
        button_group_columns: int = None,
        button_group_rows: int = None,
        bg_color: str = None,
        buttons: list[Button] = None,
    ):
        super().__init__(
            button_group_columns=button_group_columns,
            button_group_rows=button_group_rows,
            bg_color=bg_color,
            buttons=buttons,
        )
        buttons: list[Button] = None,
