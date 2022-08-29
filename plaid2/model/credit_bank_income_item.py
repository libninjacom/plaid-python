from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .credit_bank_income_account import CreditBankIncomeAccount
from .credit_bank_income_source import CreditBankIncomeSource


class CreditBankIncomeItem(BaseModel):
    bank_income_accounts: Optional[List[CreditBankIncomeAccount]] = None
    bank_income_sources: Optional[List[CreditBankIncomeSource]] = None
    last_updated_time: Optional[str] = None
    institution_id: Optional[str] = None
    institution_name: Optional[str] = None
    item_id: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditBankIncomeItem":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditBankIncomeItem":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
