import hmac
import hashlib
from typing import Any




class HmacSigner:
"""Firma HMAC-SHA256 de Crypto.com Exchange v1.


Firma sobre: method + id + api_key + parameter_string + nonce
Donde parameter_string concatena pares key+value (keys ordenadas asc.).
"""