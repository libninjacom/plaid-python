from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .screening_hit_date_of_birth_item import ScreeningHitDateOfBirthItem
from .screening_hit_documents_items import ScreeningHitDocumentsItems
from .generic_screening_hit_location_items import GenericScreeningHitLocationItems
from .screening_hit_names_items import ScreeningHitNamesItems


class ScreeningHitData(BaseModel):
    dates_of_birth: List[ScreeningHitDateOfBirthItem]
    documents: List[ScreeningHitDocumentsItems]
    locations: List[GenericScreeningHitLocationItems]
    names: List[ScreeningHitNamesItems]

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
