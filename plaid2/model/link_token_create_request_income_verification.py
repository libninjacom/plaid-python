from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .link_token_create_request_income_verification_bank_income import (
    LinkTokenCreateRequestIncomeVerificationBankIncome,
)
from .link_token_create_request_income_verification_payroll_income import (
    LinkTokenCreateRequestIncomeVerificationPayrollIncome,
)
from .link_token_create_request_user_stated_income_source import (
    LinkTokenCreateRequestUserStatedIncomeSource,
)


class LinkTokenCreateRequestIncomeVerification(BaseModel):
    income_verification_id: str
    asset_report_id: str
    precheck_id: str
    access_tokens: List[str]
    income_source_types: List[str]
    bank_income: LinkTokenCreateRequestIncomeVerificationBankIncome
    payroll_income: LinkTokenCreateRequestIncomeVerificationPayrollIncome
    stated_income_sources: List[LinkTokenCreateRequestUserStatedIncomeSource]

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
