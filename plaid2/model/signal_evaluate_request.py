from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .signal_user import SignalUser
from .signal_device import SignalDevice


class SignalEvaluateRequest(BaseModel):
    access_token: str
    account_id: str
    client_transaction_id: str
    amount: float
    user_present: bool = None
    client_user_id: str
    user: SignalUser
    device: SignalDevice

    def json(self, **kwargs) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any):
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, data: str, **kwargs):
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(data, **kwargs)