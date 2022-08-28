from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .transfer_user_in_request import TransferUserInRequest
from .transfer_metadata import TransferMetadata


class TransferIntentCreateRequest(BaseModel):
    account_id: str = None
    mode: str
    amount: str
    description: str
    ach_class: str
    origination_account_id: str = None
    user: TransferUserInRequest
    metadata: TransferMetadata = None
    iso_currency_code: str
    require_guarantee: bool = None

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
