from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class PayStubDeductionsBreakdown(BaseModel):
    current_amount: Optional[float] = None
    description: Optional[str] = None
    iso_currency_code: Optional[str] = None
    unofficial_currency_code: Optional[str] = None
    ytd_amount: Optional[float] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PayStubDeductionsBreakdown":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "PayStubDeductionsBreakdown":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
