from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .location import Location
from .payment_meta import PaymentMeta


class TransactionBase(BaseModel):
    transaction_type: str
    pending_transaction_id: str = None
    category_id: str = None
    category: List[str] = None
    location: Location
    payment_meta: PaymentMeta
    account_owner: str = None
    name: str
    original_description: str = None
    account_id: str
    amount: float
    iso_currency_code: str = None
    unofficial_currency_code: str = None
    date: str
    pending: bool
    transaction_id: str
    merchant_name: str = None
    check_number: str = None

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
