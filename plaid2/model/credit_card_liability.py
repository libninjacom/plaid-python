from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .apr import Apr


class CreditCardLiability(BaseModel):
    account_id: Optional[str] = None
    aprs: List[Apr]
    is_overdue: Optional[bool] = None
    last_payment_amount: Optional[float] = None
    last_payment_date: Optional[str] = None
    last_statement_issue_date: Optional[str] = None
    last_statement_balance: Optional[float] = None
    minimum_payment_amount: Optional[float] = None
    next_payment_due_date: Optional[str] = None

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
