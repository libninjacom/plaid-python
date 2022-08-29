from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .payroll_income_account_data import PayrollIncomeAccountData
from .payroll_income_object import PayrollIncomeObject
from .payroll_item_status import PayrollItemStatus


class PayrollItem(BaseModel):
    item_id: str
    accounts: List[PayrollIncomeAccountData]
    payroll_income: List[PayrollIncomeObject]
    status: Optional[PayrollItemStatus] = None
    pull_id: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PayrollItem":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PayrollItem":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
