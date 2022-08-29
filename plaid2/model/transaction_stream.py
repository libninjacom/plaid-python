from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .personal_finance_category import PersonalFinanceCategory
from .transaction_stream_amount import TransactionStreamAmount


class TransactionStream(BaseModel):
    account_id: str
    stream_id: str
    category_id: str
    category: List[str]
    description: str
    merchant_name: Optional[str] = None
    first_date: str
    last_date: str
    frequency: str
    transaction_ids: List[str]
    average_amount: TransactionStreamAmount
    last_amount: TransactionStreamAmount
    is_active: bool
    status: str
    personal_finance_category: Optional[PersonalFinanceCategory] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransactionStream":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransactionStream":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
