from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .generic_screening_hit_location_items import GenericScreeningHitLocationItems
from .screening_hit_date_of_birth_item import ScreeningHitDateOfBirthItem
from .screening_hit_documents_items import ScreeningHitDocumentsItems
from .screening_hit_names_items import ScreeningHitNamesItems


class ScreeningHitData(BaseModel):
    dates_of_birth: Optional[List[ScreeningHitDateOfBirthItem]] = None
    documents: Optional[List[ScreeningHitDocumentsItems]] = None
    locations: Optional[List[GenericScreeningHitLocationItems]] = None
    names: Optional[List[ScreeningHitNamesItems]] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ScreeningHitData":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "ScreeningHitData":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
