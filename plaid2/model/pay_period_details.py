from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .distribution_breakdown import DistributionBreakdown


class PayPeriodDetails(BaseModel):
    check_amount: Optional[float] = None
    distribution_breakdown: Optional[List[DistributionBreakdown]] = None
    end_date: Optional[str] = None
    gross_earnings: Optional[float] = None
    pay_date: Optional[str] = None
    pay_frequency: Optional[str] = None
    pay_day: Optional[str] = None
    start_date: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PayPeriodDetails":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PayPeriodDetails":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
