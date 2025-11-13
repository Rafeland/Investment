# core/config.py
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class ApiCredentials:
    api_key: str
    api_secret: str

    @staticmethod
    def from_env():
        return ApiCredentials(
            api_key=os.environ["CRYPTOCOM_API_KEY"],
            api_secret=os.environ["CRYPTOCOM_API_SECRET"],
        )
