import json
import os
import io
import ssl
from tempfile import gettempprefix
import typing
import pathlib
import asyncio
import warnings
import contextlib
from contextvars import ContextVar
from typing import Dict, List, Optional, Type, Union

import aiohttp
import certifi
from aiohttp.helpers import sentinel

from . import api
from .api import ViberAPIServer, VIBER_PRODUCTION


class BaseBot:
    
    _ctx_token = ContextVar('BotDifferentToken')
    
    def __init__(
        self,
        token: str,
        name: str ,
        avatar: Optional[str] = None,
        min_api_version: int = 5,
        loop: Optional[Union[asyncio.BaseEventLoop, asyncio.AbstractEventLoop]] = None,
        connections_limit: Optional[int] = None,
        proxy: Optional[str] = None,
        proxy_auth: Optional[aiohttp.BasicAuth] = None,
        validate_token: Optional[bool] = True,
        timeout: Optional[Union[int, float, aiohttp.ClientTimeout]] = None,
        server: Optional[ViberAPIServer] = VIBER_PRODUCTION,
        ) -> None:
        
        self._main_loop = loop
        if validate_token:
            api.check_token(token)
        self._token = None
        self.__token = token
        self._name = name
        self._avatar = avatar
        self._min_api_version = min_api_version
        self.server = server
        
        self.proxy = proxy
        self.proxy_auth = proxy_auth

        
        ssl_context = ssl.create_default_context(cafile=certifi.where())

        self._session: Optional[aiohttp.ClientSession] = None
        self._connector_class: Type[aiohttp.BaseConnector] = aiohttp.TCPConnector
        self._connector_init =  dict(limit=connections_limit, ssl=ssl_context)

        
        self._timeout = timeout
        
    async def request(
        self,
        method: str,
        data: Optional[dict] = None,
        **kwargs,
    ) -> Union[list, dict, bool]:
        data['auth_token'] = self._token
        return await api.make_request(
            session=await self.get_session(),
            server=self.server,
            method=method,
            data=data,
            timeout=self._timeout,
            **kwargs,
        )
        
    @property
    def session(self) -> Optional[aiohttp.ClientSession]:
        return self._session
    
    async def get_session(self) -> Optional[aiohttp.ClientSession]:
        if self._session is None:
            self._session = await self.get_new_session()
        
        if not self._session._loop.is_running():
            await self._session.close()
            self._session = await self.get_new_session()

        return self._session
            
    async def get_new_session(self) -> aiohttp.ClientSession:
        return aiohttp.ClientSession(
            headers=[
                ("User-Agent", "ViberBot-Python/1.0.12"),
                ],
            connector=self._connector_class(**self._connector_init),
            json_serialize=json.dumps,
            )

    async def close(self):
        if self._session:
            await self._session.close() 
        self._session = None
        
    @property
    def loop(self) -> Optional[asyncio.AbstractEventLoop]:
        return self._main_loop
    
    @property
    def __token(self):
        return self._ctx_token.get(self._token) 

    @__token.setter
    def __token(self, value):
        self._token = value
    
    