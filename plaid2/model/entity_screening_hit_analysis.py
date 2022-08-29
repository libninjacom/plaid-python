from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class EntityScreeningHitAnalysis(BaseModel):
    documents: Optional[str] = None
    email_addresses: Optional[str] = None
    locations: Optional[str] = None
    names: Optional[str] = None
    phone_numbers: Optional[str] = None
    urls: Optional[str] = None
    search_terms_version: float

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "EntityScreeningHitAnalysis":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "EntityScreeningHitAnalysis":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
