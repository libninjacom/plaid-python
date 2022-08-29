from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .watchlist_screening_audit_trail import WatchlistScreeningAuditTrail
from .watchlist_screening_search_terms import WatchlistScreeningSearchTerms


class WatchlistScreeningIndividualResponse(BaseModel):
    id: str
    search_terms: WatchlistScreeningSearchTerms
    assignee: Optional[Any] = None
    status: str
    client_user_id: Optional[Any] = None
    audit_trail: WatchlistScreeningAuditTrail
    request_id: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "WatchlistScreeningIndividualResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "WatchlistScreeningIndividualResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
