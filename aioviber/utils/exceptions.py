

_PREFIXES = ['error: ', '[error]: ', 'bad request: ', 'conflict: ', 'not found: ']


def _clean_message(text: str) -> str:
    for prefix in _PREFIXES:
        if text.startswith(prefix):
            text = text[len(prefix):]
    return (text[0].upper() + text[1:]).strip()

class ViberAPIError(Exception):
    def __init__(self, message=None):
        super(ViberAPIError, self).__init__(_clean_message(message))
        
class ValidationError(ViberAPIError):
    pass

class NetworkError(ViberAPIError):
    pass