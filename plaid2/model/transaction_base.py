from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .location import Location
from .payment_meta import PaymentMeta


class TransactionBase(BaseModel):
    transaction_type: Optional[str] = None
    pending_transaction_id: Optional[str] = None
    category_id: Optional[str] = None
    category: Optional[List[str]] = None
    location: Optional[Location] = None
    payment_meta: Optional[PaymentMeta] = None
    account_owner: Optional[str] = None
    name: Optional[str] = None
    original_description: Optional[str] = None
    account_id: str
    amount: float
    iso_currency_code: Optional[str] = None
    unofficial_currency_code: Optional[str] = None
    date: str
    pending: bool
    transaction_id: str
    merchant_name: Optional[str] = None
    check_number: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransactionBase":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransactionBase":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
