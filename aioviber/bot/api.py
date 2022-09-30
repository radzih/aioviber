from email import header
import json
import os
import logging
from dataclasses import dataclass
from re import L, T
from wsgiref import headers
from http import HTTPStatus

import aiohttp


from ..utils import exceptions
from ..utils.helper import Helper, Item, ItemsList, ListItem, HelperMode


# Main logger
logger = logging.getLogger('aioviber')

@dataclass(frozen=True)
class ViberAPIServer:
    base: str
    # file: str
    
    def api_url(self, method: str) -> str:
        return self.base.format(method=method)

    # def file_url(self, token: str, method: str) -> str:
    #     return self.file.format(token=token, method=method)
    
    @classmethod
    def from_base(cls, base: str) -> 'ViberAPIServer':
        base = base.rstrip('/')
        return cls(
            base=f'{base}/{{method}}',
            # file=f'{base}/file/{{token}}/{{method}}',
        )


VIBER_PRODUCTION = ViberAPIServer.from_base('https://chatapi.viber.com/pa')


def check_token(token: str) -> None:

    if token == 'test_token':
        return True

    if not isinstance(token, str):
        raise exceptions.ValidationError(
            message='Token must be a string instead of %s type' % type(token)
        )

    if any(char.isspace() for char in token):
        raise exceptions.ValidationError(
            message='Token must not contain whitespace characters'
        )
        
    left, sep, right = token.partition('-')

    if (not sep) or (not left) or (not right):
        raise exceptions.ValidationError(
            message='Token must be in format "left-sep-right"'
        )
    
    if len(token) != 50:
        raise exceptions.ValidationError(
            message='Token must be 50 characters long'
        )
        
    return True

async def make_request(
    session: aiohttp.ClientSession,
    server: ViberAPIServer,
    method: str,
    data=None,
    files=None,
    **kwargs
    ) -> dict:
    logger.debug(
        'Making request: "%s" with data "%s" and files "%r"',
        method, data, files
        )

    url = server.api_url(method)
    
    req = compose_data(data)

    try: 
        async with session.post(url=url, json=data, **kwargs) as response:
            return await check_result(
                method_name=method,
                content_type=response.content_type,
                status_code=response.status,
                body=await response.text(),
            )
    except aiohttp.ClientError as e:
        raise exceptions.NetworkError(
            message='Aiohttp client error: %s' % e
            )

def compose_data(params=None):
    """
    Prepare request data

    :param params:
    :param files:
    :return:
    """
    data = aiohttp.formdata.FormData(quote_fields=False)

    if params:
        for key, value in params.items():
            data.add_field(key, str(value))

    # if files:
    #     for key, f in files.items():
    #         if isinstance(f, tuple):
    #             if len(f) == 2:
    #                 filename, fileobj = f
    #             else:
    #                 raise ValueError('Tuple must have exactly 2 elements: filename, fileobj')
    #         elif isinstance(f, types.InputFile):
    #             filename, fileobj = f.filename, f.file
    #         else:
    #             filename, fileobj = guess_filename(f) or key, f

    #         data.add_field(key, fileobj, filename=filename)

    return data

async def check_result(
    method_name: str,
    content_type: str,
    status_code: int, 
    body: str
    ) -> None:
    
    logger.debug('Response for %s: [%d] "%r"', method_name, status_code, body)
    
    if content_type != 'application/json':
        raise exceptions.NetworkError(
            message='Invalid content type: %s' % content_type
        )
    
    try:
        result_json = json.loads(body)
    except ValueError:
        result_json = {}
    return result_json
    description = result_json.get('description') or body
    # parameters = types.ResponseParameters(**result_json.get('parameters', {}) or {})

    if HTTPStatus.OK <= status_code <= HTTPStatus.IM_USED:
        return result_json.get('result')

class Methods(Helper):
    
    mode = HelperMode.snake_case
    
    #Webhooks
    SET_WEBHOOK = Item()
    
    #Message
    SEND_MESSAGE = Item()
    BROADCAST_MESSAGE = Item()
    
    #ACCOUNTS
    GET_ACCOUNT_INFO = Item()
    GET_USER_DETAILS = Item()
    GET_ONLINE = Item()