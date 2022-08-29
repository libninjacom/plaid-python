from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .deductions import Deductions
from .earnings import Earnings
from .employee import Employee
from .employment_details import EmploymentDetails
from .income_breakdown import IncomeBreakdown
from .net_pay import NetPay
from .pay_period_details import PayPeriodDetails
from .paystub_details import PaystubDetails
from .paystub_employer import PaystubEmployer
from .paystub_verification import PaystubVerification
from .paystub_ytd_details import PaystubYtdDetails


class Paystub(BaseModel):
    deductions: Deductions
    doc_id: str
    earnings: Earnings
    employee: Employee
    employer: PaystubEmployer
    employment_details: Optional[EmploymentDetails] = None
    net_pay: NetPay
    pay_period_details: PayPeriodDetails
    paystub_details: Optional[PaystubDetails] = None
    income_breakdown: Optional[List[IncomeBreakdown]] = None
    ytd_earnings: Optional[PaystubYtdDetails] = None
    verification: Optional[PaystubVerification] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Paystub":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Paystub":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
