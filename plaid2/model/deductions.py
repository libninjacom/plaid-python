from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .deductions_breakdown import DeductionsBreakdown
from .deductions_total import DeductionsTotal
from .total import Total


class Deductions(BaseModel):
    subtotals: Optional[List[Total]] = None
    breakdown: List[DeductionsBreakdown]
    totals: Optional[List[Total]] = None
    total: DeductionsTotal

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Deductions":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Deductions":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
