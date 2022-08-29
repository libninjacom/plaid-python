from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .transfer_authorization_device import TransferAuthorizationDevice
from .transfer_authorization_user_in_request import TransferAuthorizationUserInRequest


class TransferAuthorizationCreateRequest(BaseModel):
    access_token: Optional[str] = None
    account_id: Optional[str] = None
    type: str
    network: str
    amount: str
    ach_class: str
    user: TransferAuthorizationUserInRequest
    device: Optional[TransferAuthorizationDevice] = None
    origination_account_id: Optional[str] = None
    iso_currency_code: Optional[str] = None
    user_present: Optional[bool] = None
    payment_profile_id: Optional[str] = None

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
