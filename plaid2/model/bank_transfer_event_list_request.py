from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class BankTransferEventListRequest(BaseModel):
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    bank_transfer_id: Optional[str] = None
    account_id: Optional[str] = None
    bank_transfer_type: Optional[str] = None
    event_types: Optional[List[str]] = None
    count: Optional[int] = None
    offset: Optional[int] = None
    origination_account_id: Optional[str] = None
    direction: Optional[str] = None

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
