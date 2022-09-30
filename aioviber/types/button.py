from typing import Literal
import typing
from . import base
from .map import Map
from . import fields
from .frame import Frame
from .media_player import MediaPlayer
from .internal_browser import InternalBrowser

from babel.support import LazyProxy

class Button(base.ViberObject):

    columns: int = fields.Field(alias='Columns')
    rows: int = fields.Field(alias='Rows')
    text: str = fields.Field(alias='Text')
    text_config: 'ButtonTextConfig' = fields.Field(base='ButtonTextConfig')
    background_config: 'ButtonBackgroundConfig' = fields.Field(base='ButtonBackgroundConfig')
    siltent: bool = fields.Field(alias='Silent')
    action_type: str = fields.Field(alias='ActionType')
    action_body: str = fields.Field(alias='ActionBody')
    image_scale_type: str = fields.Field(alias='ImageScaleType')
    image: str = fields.Field(alias='Image')
    open_url_type: str = fields.Field(alias='OpenURLType')
    open_url_media_type: str = fields.Field(alias='OpenURLMediaType')
    internal_browser: InternalBrowser = fields.Field(base=InternalBrowser, alias='InternalBrowser')
    map: Map = fields.Field(base=Map, alias='Map')
    frame: Frame = fields.Field(base=Frame, alias='Frame')
    media_player: MediaPlayer = fields.Field(base=MediaPlayer, alias='MediaPlayer')

    def __init__(
        self,
        text: str = None,
        text_config: 'ButtonTextConfig' = None,
        background_config: 'ButtonBackgroundConfig' = None,
        columns:Literal[1,2,3,4,5,6,7] = None,
        rows: Literal[1,2] = None,
        siltent: bool = None,
        action_type: Literal[
            'reply', 'open-url', 'location-picker', 'share_phone', None
            ] = None,
        action_body: str = None,
        image_scale_type: Literal['crop', 'fill', 'fit'] = None,
        image: str = None,
        open_url_type: Literal['internal', 'external'] = None,
        open_url_media_type: Literal['not-media', 'video', 'gif', 'picture'] = None,
        internal_browser: InternalBrowser = None,
        map: Map = None,
        frame: Frame = None,
        media_player: MediaPlayer = None,
    ):
        super().__init__(
            columns=columns,
            text=text,
            text_config=text_config,
            background_config=background_config,
            rows=rows,
            siltent=siltent,
            action_type=action_type,
            action_body=action_body,
            image_scale_type=image_scale_type,
            image=image,
            open_url_type=open_url_type,
            open_url_media_type=open_url_media_type,
            internal_browser=internal_browser,
            map=map,
            frame=frame,
            media_player=media_player,
        )

    def to_python(self) -> typing.Dict[str, typing.Any]:
        """
        Get object as JSON serializable

        :return:
        """
        result = {}
        for name, value in self.values.items():
            if value is None:
                continue
            if isinstance(value, ButtonTextConfig):
                result.update(value.to_python())
                continue
            if name in self.props:
                value = self.props[name].export(self)
            if isinstance(value, base.ViberObject):
                value = value.to_python()
            if isinstance(value, LazyProxy):
                value = str(value)
            result[self.props_aliases.get(name, name)] = value
        return result
        


class ButtonTextConfig(base.ViberObject):
    
    v_align: str = fields.Field(alias='TextVAlign')
    h_align: str = fields.Field(alias='TextHAlign')
    paddings: list[int,int,int,int] = fields.Field(alias='TextPaddings')
    opacity: int = fields.Field(alias='TextOpacity')
    bg_gradient_color: str = fields.Field(alias='TextBgGradientColor')
    should_fit: bool = fields.Field(alias='TextShouldFit')
    size: str = fields.Field(alias='TextSize')

    def __init__(

        self,
        h_align: Literal['left', 'center', 'right'] = None,
        v_align: Literal['top', 'middle', 'bottom'] = None,
        paddings: list[int,int,int,int] = None,
        opacity: int = None,
        bg_gradient_color: str = None,
        should_fit: bool = None,
        size: Literal['small', 'regular', 'large'] = None,
    ):
        super().__init__(
            h_align=h_align,
            v_align=v_align,
            paddings=paddings,
            opacity=opacity,
            bg_gradient_color=bg_gradient_color,
            should_fit=should_fit,
            size=size,
        )


class ButtonBackgroundConfig(base.ViberObject):
    
    color: str = fields.Field(alias='BgColor')
    media: str = fields.Field(alias='BgMedia')
    media_type: str = fields.Field(alias='BgMediaType')
    media_scale_type: str = fields.Field(alias='BgMediaScaleType')
    loop: bool = fields.Field(alias='BgLoop')

    def __init__(
        self,
        color: str = None,
        media: str = None,
        media_type: Literal['picture', 'gif'] = None,
        media_scale_type: Literal['crop', 'fill', 'fit'] = None,
        loop: bool = None,
    ):
        super().__init__(
            color=color,
            media=media,
            media_type=media_type,
            media_scale_type=media_scale_type,
            loop=loop,
        )