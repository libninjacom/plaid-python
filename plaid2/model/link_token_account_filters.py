from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .depository_filter import DepositoryFilter
from .credit_filter import CreditFilter
from .loan_filter import LoanFilter
from .investment_filter import InvestmentFilter


class LinkTokenAccountFilters(BaseModel):
    depository: DepositoryFilter
    credit: CreditFilter
    loan: LoanFilter
    investment: InvestmentFilter

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
