from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .credit_bank_income_historical_summary import CreditBankIncomeHistoricalSummary


class CreditBankIncomeSummary(BaseModel):
    total_amount: Optional[float] = None
    iso_currency_code: Optional[str] = None
    unofficial_currency_code: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    income_sources_count: Optional[int] = None
    income_categories_count: Optional[int] = None
    income_transactions_count: Optional[int] = None
    historical_summary: Optional[List[CreditBankIncomeHistoricalSummary]] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditBankIncomeSummary":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "CreditBankIncomeSummary":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
