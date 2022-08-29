from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .entity_watchlist_screening_search_terms import EntityWatchlistScreeningSearchTerms
from .watchlist_screening_audit_trail import WatchlistScreeningAuditTrail


class EntityWatchlistScreening(BaseModel):
    id: str
    search_terms: EntityWatchlistScreeningSearchTerms
    assignee: Optional[Any] = None
    status: str
    client_user_id: Optional[Any] = None
    audit_trail: WatchlistScreeningAuditTrail

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "EntityWatchlistScreening":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "EntityWatchlistScreening":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
