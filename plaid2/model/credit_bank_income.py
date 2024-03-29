from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .credit_bank_income_item import CreditBankIncomeItem
from .credit_bank_income_summary import CreditBankIncomeSummary
from .credit_bank_income_warning import CreditBankIncomeWarning


class CreditBankIncome(BaseModel):
    bank_income_id: Optional[str] = None
    generated_time: Optional[str] = None
    days_requested: Optional[int] = None
    items: Optional[List[CreditBankIncomeItem]] = None
    bank_income_summary: Optional[CreditBankIncomeSummary] = None
    warnings: Optional[List[CreditBankIncomeWarning]] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditBankIncome":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditBankIncome":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
