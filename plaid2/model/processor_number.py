from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .numbers_ach_nullable import NumbersAchNullable
from .numbers_bacs_nullable import NumbersBacsNullable
from .numbers_eft_nullable import NumbersEftNullable
from .numbers_international_nullable import NumbersInternationalNullable


class ProcessorNumber(BaseModel):
    ach: Optional[NumbersAchNullable] = None
    eft: Optional[NumbersEftNullable] = None
    international: Optional[NumbersInternationalNullable] = None
    bacs: Optional[NumbersBacsNullable] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ProcessorNumber":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "ProcessorNumber":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
