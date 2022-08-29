from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .bank_transfer_failure import BankTransferFailure


class BankTransferEvent(BaseModel):
    event_id: int
    timestamp: str
    event_type: str
    account_id: str
    bank_transfer_id: str
    origination_account_id: Optional[str] = None
    bank_transfer_type: str
    bank_transfer_amount: str
    bank_transfer_iso_currency_code: str
    failure_reason: Optional[BankTransferFailure] = None
    direction: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "BankTransferEvent":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "BankTransferEvent":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
