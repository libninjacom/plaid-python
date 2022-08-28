from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class DepositSwitchGetResponse(BaseModel):
    deposit_switch_id: str
    target_account_id: str = None
    target_item_id: str = None
    state: str
    switch_method: str = None
    account_has_multiple_allocations: bool = None
    is_allocated_remainder: bool = None
    percent_allocated: float = None
    amount_allocated: float = None
    employer_name: str = None
    employer_id: str = None
    institution_name: str = None
    institution_id: str = None
    date_created: str
    date_completed: str = None
    request_id: str

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
