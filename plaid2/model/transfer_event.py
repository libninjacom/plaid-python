from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .transfer_failure import TransferFailure


class TransferEvent(BaseModel):
    event_id: int
    timestamp: str
    event_type: str
    account_id: str
    transfer_id: str
    origination_account_id: str = None
    transfer_type: str
    transfer_amount: str
    failure_reason: TransferFailure = None
    sweep_id: str = None
    sweep_amount: str = None

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
