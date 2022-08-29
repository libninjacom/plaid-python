from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .transfer_metadata import TransferMetadata
from .transfer_user_in_request import TransferUserInRequest


class TransferIntentCreateRequest(BaseModel):
    account_id: Optional[str] = None
    mode: str
    amount: str
    description: str
    ach_class: str
    origination_account_id: Optional[str] = None
    user: TransferUserInRequest
    metadata: Optional[TransferMetadata] = None
    iso_currency_code: Optional[str] = None
    require_guarantee: Optional[bool] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferIntentCreateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "TransferIntentCreateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
