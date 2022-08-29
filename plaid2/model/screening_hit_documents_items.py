from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .match_summary import MatchSummary
from .watchlist_screening_document import WatchlistScreeningDocument


class ScreeningHitDocumentsItems(BaseModel):
    analysis: Optional[MatchSummary] = None
    data: Optional[WatchlistScreeningDocument] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ScreeningHitDocumentsItems":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "ScreeningHitDocumentsItems":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
