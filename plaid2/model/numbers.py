from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class Numbers(BaseModel):
    account: Optional[str] = None
    ach_routing: Optional[str] = None
    ach_wire_routing: Optional[str] = None
    eft_institution: Optional[str] = None
    eft_branch: Optional[str] = None
    international_bic: Optional[str] = None
    international_iban: Optional[str] = None
    bacs_sort_code: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Numbers":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Numbers":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
