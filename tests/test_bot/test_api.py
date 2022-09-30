import pytest

from aioviber.bot.api import check_token
from aioviber.utils.exceptions import ValidationError


VALID_TOKEN = '4fdf67ce1167de1f-c5c596d664899a65-90ec00c8f4c8cbce'

INVALID_TOKENS = [
    '4fdf67ce1167de1f-c5c596d664899a65-90ec00c8f7c8cbce ', # space at the end
    '4fdf67ce1167de1f-c5c596d664899a65-90ec00c8f7c8cbc', # 48 characters
    '4fdf67ce1167de1f-c5c596d664899a65-90ec00c8f7c8cbcep', # 51 characters
    '4fdf67ce1167de1fc5c596d664899a6590ec00c8f4c8cbce', # miss dash
    None, # is None
    123456789, # is int
    {}, # is dict
    [], # is list
    object, # is object
]


@pytest.fixture(params=INVALID_TOKENS, name='invalid_token')
def invalid_token_fixture(request):
    return request.param

class TestCheckToken:

    def test_valid(self):
        assert check_token(VALID_TOKEN) is True

    def test_invalid_token(self, invalid_token):
        with pytest.raises(ValidationError):
            check_token(invalid_token)
