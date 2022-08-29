from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class DepositSwitchGetResponse(BaseModel):
    deposit_switch_id: str
    target_account_id: Optional[str] = None
    target_item_id: Optional[str] = None
    state: str
    switch_method: Optional[str] = None
    account_has_multiple_allocations: Optional[bool] = None
    is_allocated_remainder: Optional[bool] = None
    percent_allocated: Optional[float] = None
    amount_allocated: Optional[float] = None
    employer_name: Optional[str] = None
    employer_id: Optional[str] = None
    institution_name: Optional[str] = None
    institution_id: Optional[str] = None
    date_created: str
    date_completed: Optional[str] = None
    request_id: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "DepositSwitchGetResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "DepositSwitchGetResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
