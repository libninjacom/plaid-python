from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class Security(BaseModel):
    security_id: str
    isin: Optional[str] = None
    cusip: Optional[str] = None
    sedol: Optional[str] = None
    institution_security_id: Optional[str] = None
    institution_id: Optional[str] = None
    proxy_security_id: Optional[str] = None
    name: Optional[str] = None
    ticker_symbol: Optional[str] = None
    is_cash_equivalent: Optional[bool] = None
    type: Optional[str] = None
    close_price: Optional[float] = None
    close_price_as_of: Optional[str] = None
    update_datetime: Optional[str] = None
    iso_currency_code: Optional[str] = None
    unofficial_currency_code: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Security":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Security":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
