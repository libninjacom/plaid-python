from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .plaid_error import PlaidError


class Item(BaseModel):
    item_id: str
    institution_id: Optional[str] = None
    webhook: Optional[str] = None
    error: Optional[PlaidError] = None
    available_products: List[str]
    billed_products: List[str]
    products: Optional[List[str]] = None
    consented_products: Optional[List[str]] = None
    consent_expiration_time: Optional[str] = None
    update_type: str

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
