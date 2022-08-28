from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .screening_hit_analysis import ScreeningHitAnalysis
from .screening_hit_data import ScreeningHitData


class WatchlistScreeningHit(BaseModel):
    id: str
    review_status: str
    first_active: str
    inactive_since: Optional[str] = None
    historical_since: Optional[str] = None
    list_code: str
    plaid_uid: str
    source_uid: Optional[str] = None
    analysis: Optional[ScreeningHitAnalysis] = None
    data: Optional[ScreeningHitData] = None

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
