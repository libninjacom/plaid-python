from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .location import Location
from .personal_finance_category import PersonalFinanceCategory


class Enhancements(BaseModel):
    merchant_name: Optional[str] = None
    website: Optional[str] = None
    logo_url: Optional[str] = None
    check_number: Optional[str] = None
    payment_channel: str
    category_id: Optional[str] = None
    category: List[str]
    location: Location
    personal_finance_category: Optional[PersonalFinanceCategory] = None
    personal_finance_category_icon_url: Optional[str] = None

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
