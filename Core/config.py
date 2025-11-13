from dataclasses import dataclass
import os

@dataclass(frozen=True)
class ApiCredentials:
api_key: str
api_secret: str


@staticmethod
def from_env(prefix: str = "CRYPTOCOM_") -> "ApiCredentials":
key = os.environ.get(prefix + "API_KEY")
secret = os.environ.get(prefix + "API_SECRET")
if not key or not secret:
raise RuntimeError(
"Faltan variables de entorno: {}API_KEY y {}API_SECRET".format(prefix, prefix)
)
return ApiCredentials(api_key=key, api_secret=secret)