from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .earnings_breakdown import EarningsBreakdown
from .earnings_total import EarningsTotal


class Earnings(BaseModel):
    subtotals: Optional[List[EarningsTotal]] = None
    totals: Optional[List[EarningsTotal]] = None
    breakdown: Optional[List[EarningsBreakdown]] = None
    total: Optional[EarningsTotal] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Earnings":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Earnings":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
