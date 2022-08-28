from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class TransactionsGetRequestOptions(BaseModel):
    account_ids: Optional[List[str]] = None
    count: Optional[int] = None
    offset: Optional[int] = None
    include_original_description: Optional[bool] = None
    include_personal_finance_category_beta: Optional[bool] = None
    include_personal_finance_category: Optional[bool] = None

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
