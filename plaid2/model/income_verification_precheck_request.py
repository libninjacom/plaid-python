from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .income_verification_precheck_user import IncomeVerificationPrecheckUser
from .income_verification_precheck_employer import IncomeVerificationPrecheckEmployer
from .income_verification_precheck_military_info import (
    IncomeVerificationPrecheckMilitaryInfo,
)


class IncomeVerificationPrecheckRequest(BaseModel):
    user: Optional[IncomeVerificationPrecheckUser] = None
    employer: Optional[IncomeVerificationPrecheckEmployer] = None
    transactions_access_token: Optional[Any] = None
    transactions_access_tokens: Optional[List[str]] = None
    us_military_info: Optional[IncomeVerificationPrecheckMilitaryInfo] = None

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
