from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .user_name import UserName
from .identity_verification_user_address import IdentityVerificationUserAddress
from .user_id_number import UserIdNumber


class IdentityVerificationUserData(BaseModel):
    phone_number: str = None
    date_of_birth: str = None
    ip_address: str = None
    email_address: Any = None
    name: UserName = None
    address: IdentityVerificationUserAddress = None
    id_number: UserIdNumber = None

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
