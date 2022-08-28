from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .update_entity_screening_request_search_terms import (
    UpdateEntityScreeningRequestSearchTerms,
)


class UpdateEntityScreeningRequest(BaseModel):
    entity_watchlist_screening_id: str
    search_terms: UpdateEntityScreeningRequestSearchTerms = None
    assignee: Any = None
    status: Any = None
    client_user_id: Any = None
    reset_fields: List[str] = None

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
