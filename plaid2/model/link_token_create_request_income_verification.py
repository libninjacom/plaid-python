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
    income_verification_id: Optional[str] = None
    asset_report_id: Optional[str] = None
    precheck_id: Optional[str] = None
    access_tokens: Optional[List[str]] = None
    income_source_types: Optional[List[str]] = None
    bank_income: Optional[LinkTokenCreateRequestIncomeVerificationBankIncome] = None
    payroll_income: Optional[
        LinkTokenCreateRequestIncomeVerificationPayrollIncome
    ] = None
    stated_income_sources: Optional[
        List[LinkTokenCreateRequestUserStatedIncomeSource]
    ] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LinkTokenCreateRequestIncomeVerification":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "LinkTokenCreateRequestIncomeVerification":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
