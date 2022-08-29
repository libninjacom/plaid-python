from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .entity_screening_hit_documents_items import EntityScreeningHitDocumentsItems
from .entity_screening_hit_emails_items import EntityScreeningHitEmailsItems
from .entity_screening_hit_names_items import EntityScreeningHitNamesItems
from .entity_screening_hit_urls_items import EntityScreeningHitUrlsItems
from .entity_screening_hits_phone_number_items import (
    EntityScreeningHitsPhoneNumberItems,
)
from .generic_screening_hit_location_items import GenericScreeningHitLocationItems


class EntityScreeningHitData(BaseModel):
    documents: Optional[List[EntityScreeningHitDocumentsItems]] = None
    email_addresses: Optional[List[EntityScreeningHitEmailsItems]] = None
    locations: Optional[List[GenericScreeningHitLocationItems]] = None
    names: Optional[List[EntityScreeningHitNamesItems]] = None
    phone_numbers: Optional[List[EntityScreeningHitsPhoneNumberItems]] = None
    urls: Optional[List[EntityScreeningHitUrlsItems]] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "EntityScreeningHitData":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "EntityScreeningHitData":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
