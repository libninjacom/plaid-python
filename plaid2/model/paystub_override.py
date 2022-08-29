from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .income_breakdown import IncomeBreakdown
from .pay_period_details import PayPeriodDetails
from .paystub_override_employee import PaystubOverrideEmployee
from .paystub_override_employer import PaystubOverrideEmployer


class PaystubOverride(BaseModel):
    employer: Optional[PaystubOverrideEmployer] = None
    employee: Optional[PaystubOverrideEmployee] = None
    income_breakdown: Optional[List[IncomeBreakdown]] = None
    pay_period_details: Optional[PayPeriodDetails] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaystubOverride":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PaystubOverride":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
