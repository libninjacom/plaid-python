from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class Security(BaseModel):
    security_id: str
    isin: str = None
    cusip: str = None
    sedol: str = None
    institution_security_id: str = None
    institution_id: str = None
    proxy_security_id: str = None
    name: str = None
    ticker_symbol: str = None
    is_cash_equivalent: bool = None
    type: str = None
    close_price: float = None
    close_price_as_of: str = None
    update_datetime: str = None
    iso_currency_code: str = None
    unofficial_currency_code: str = None

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
