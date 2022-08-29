from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class Holding(BaseModel):
    account_id: str
    security_id: str
    institution_price: float
    institution_price_as_of: Optional[str] = None
    institution_price_datetime: Optional[str] = None
    institution_value: float
    cost_basis: Optional[float] = None
    quantity: float
    iso_currency_code: Optional[str] = None
    unofficial_currency_code: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Holding":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Holding":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
