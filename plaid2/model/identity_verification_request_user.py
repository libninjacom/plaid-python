from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .user_address import UserAddress
from .user_id_number import UserIdNumber
from .user_name import UserName


class IdentityVerificationRequestUser(BaseModel):
    client_user_id: str
    email_address: Optional[Any] = None
    phone_number: Optional[str] = None
    date_of_birth: Optional[str] = None
    name: Optional[UserName] = None
    address: Optional[UserAddress] = None
    id_number: Optional[UserIdNumber] = None

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
