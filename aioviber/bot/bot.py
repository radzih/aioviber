from typing import Optional

from . import api
from .base import BaseBot
from ..types.keyboard import Keyboard
from .. import types
from ..utils.mixins import DataMixin, ContextInstanceMixin
from ..utils.payload import generate_payload, prepare_arg

class Bot(BaseBot, DataMixin, ContextInstanceMixin):
    
    async def get_account_info(self) -> types.Account:

        payload = generate_payload(**locals())

        result = await self.request(
            api.Methods.GET_ACCOUNT_INFO,
            data=payload,
        )

        return types.Account(**result)

    async def get_online(self):

        payload = generate_payload()

        result = await self.request(
            method=api.Methods.GET_ONLINE,
            data=payload,
        )
        return [types.BroadcastUser(**user) for user in result['users']]

    async def get_user_details(self, id: str) -> types.User:
        '''
        :param id: User ID
        '''

        payload = generate_payload(**locals())

        result = await self.request(
            api.Methods.GET_USER_DETAILS,
            data=payload,
        )
        return types.User(**result['user'])

    async def send_message(
        self,
        receiver: str,
        text: str,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        keyboard: Keyboard = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version
            
        keyboard = prepare_arg(keyboard)
        
        payload = generate_payload(
            **locals(),
            type = 'text',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.SEND_MESSAGE,
            data=payload,
        )

        return types.Message(
            **result,
            **payload,
            )
    
    async def send_picture(
        self,
        receiver: str,
        media: str,
        text: Optional[str] = None,
        thumbnail: Optional[str] = None,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        keyboard: Optional[Keyboard] = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version

        keyboard = prepare_arg(keyboard)
        
        payload = generate_payload(
            **locals(),
            type = 'picture',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.SEND_MESSAGE,
            data=payload,
        )
    
    async def send_video(
        self,
        receiver: str,
        size: int,
        media: str,
        text: Optional[str] = None,
        duration: Optional[int] = None,
        thumbnail: Optional[str] = None,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        keyboard: Optional[Keyboard] = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version

        keyboard = prepare_arg(keyboard)

        payload = generate_payload(
            **locals(),
            type='video',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.SEND_MESSAGE,
            data=payload,
        )

    async def send_location(
        self,
        receiver: str,
        location: types.Location,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        keyboard: Optional[Keyboard] = None,
    ) -> types.Message:

        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version
        
        keyboard = prepare_arg(keyboard)
        location = prepare_arg(location)

        payload = generate_payload(
            **locals(),
            type='location',
            sender={'name': sender_name, 'avatar': sender_avatar},
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.SEND_MESSAGE,
            data=payload,
        )
        
        return types.Message(**result, **payload)
    
    async def send_url(
        self,
        receiver: str,
        media: str,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        keyboard: Optional[Keyboard] = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version

        keyboard = prepare_arg(keyboard)

        payload = generate_payload(
            **locals(),
            type='url',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.SEND_MESSAGE,
            data=payload,
        )
    
    async def send_sticker(
        self, 
        receiver: str,
        sticker_id: int,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        keyboard: Optional[Keyboard] = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version

        keyboard = prepare_arg(keyboard)

        payload = generate_payload(
            **locals(),
            type='sticker',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.SEND_MESSAGE,
            data=payload,
        )
        
    async def send_rich_media(
        self,
        receiver: str,
        rich_media: types.RichMedia,
        alt_text: Optional[str] = None,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version

        rich_media = prepare_arg(rich_media)

        payload = generate_payload(
            **locals(),
            type='rich_media',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.SEND_MESSAGE,
            data=payload,
        )
    
    async def send_contact(
        self, 
        receiver: str,
        contact: types.Contact,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        keyboard: Optional[Keyboard] = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version

        keyboard = prepare_arg(keyboard)
        contact = prepare_arg(contact)

        payload = generate_payload(
            **locals(),
            type='contact',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.SEND_MESSAGE,
            data=payload,
        )

    async def broadcast_message(
        self,
        broadcast_list: list[str],
        text: str,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version

        keyboard = prepare_arg(keyboard)

        payload = generate_payload(
            **locals(),
            type='text',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.BROADCAST_MESSAGE,
            data=payload,
        )
        

    async def broadcast_picture(
        self,
        broadcast_list: list[str],
        media: str,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version

        keyboard = prepare_arg(keyboard)

        payload = generate_payload(
            **locals(),
            type='picture',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.BROADCAST_MESSAGE,
            data=payload,
        )
    
    async def broadcast_video(
        self,
        broadcast_list: list[str],
        media: str,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version

        keyboard = prepare_arg(keyboard)

        payload = generate_payload(
            **locals(),
            type='video',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.BROADCAST_MESSAGE,
            data=payload,
        )

    async def broadcast_file(
        self,
        broadcast_list: list[str],
        media: str,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version

        keyboard = prepare_arg(keyboard)

        payload = generate_payload(
            **locals(),
            type='file',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.BROADCAST_MESSAGE,
            data=payload,
        )

    async def broadcast_url(
        self,
        broadcast_list: list[str],
        media: str,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version

        keyboard = prepare_arg(keyboard)

        payload = generate_payload(
            **locals(),
            type='url',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.BROADCAST_MESSAGE,
            data=payload,
        )
    
    async def broadcast_contact(
        self,
        broadcast_list: list[str],
        contact: types.Contact,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version

        keyboard = prepare_arg(keyboard)
        contact = prepare_arg(contact)

        payload = generate_payload(
            **locals(),
            type='contact',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.BROADCAST_MESSAGE,
            data=payload,
        )

    async def broadcast_location(
        self,
        broadcast_list: list[str],
        location: types.Location,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version

        keyboard = prepare_arg(keyboard)
        location = prepare_arg(location)

        payload = generate_payload(
            **locals(),
            type='location',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.BROADCAST_MESSAGE,
            data=payload,
        )

    async def broadcast_sticker(
        self,
        broadcast_list: list[str],
        sticker: types.Sticker,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version

        keyboard = prepare_arg(keyboard)
        sticker = prepare_arg(sticker)

        payload = generate_payload(
            **locals(),
            type='sticker',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.BROADCAST_MESSAGE,
            data=payload,
        )

    async def broadcast_rich_media(
        self,
        broadcast_list: list[str],
        rich_media: types.RichMedia,
        tracking_data: Optional[bool] = None,
        min_api_version: Optional[int] = None,
        sender_name: Optional[str] = None,
        sender_avatar: Optional[str] = None,
        keyboard: Optional[Keyboard] = None,
    ):
        if sender_name is None:
            sender_name = self._name
        if sender_avatar is None:
            sender_avatar = self._avatar
        if min_api_version is None:
            min_api_version = self._min_api_version

        keyboard = prepare_arg(keyboard)
        rich_media = prepare_arg(rich_media)

        payload = generate_payload(
            **locals(),
            type='rich_media',
            sender={'name': sender_name, 'avatar': sender_avatar}, 
            exclude=['sender_name', 'sender_avatar'],
            )
        
        result = await self.request(
            method=api.Methods.BROADCAST_MESSAGE,
            data=payload,
        )
