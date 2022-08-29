from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .pay import Pay


class DistributionBreakdown(BaseModel):
    account_name: Optional[str] = None
    bank_name: Optional[str] = None
    current_amount: Optional[float] = None
    iso_currency_code: Optional[str] = None
    mask: Optional[str] = None
    type: Optional[str] = None
    unofficial_currency_code: Optional[str] = None
    current_pay: Optional[Pay] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "DistributionBreakdown":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "DistributionBreakdown":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
