from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .deductions import Deductions
from .earnings import Earnings
from .employee import Employee
from .paystub_employer import PaystubEmployer
from .employment_details import EmploymentDetails
from .net_pay import NetPay
from .pay_period_details import PayPeriodDetails
from .paystub_details import PaystubDetails
from .income_breakdown import IncomeBreakdown
from .paystub_ytd_details import PaystubYtdDetails
from .paystub_verification import PaystubVerification


class Paystub(BaseModel):
    deductions: Deductions
    doc_id: str
    earnings: Earnings
    employee: Employee
    employer: PaystubEmployer
    employment_details: EmploymentDetails
    net_pay: NetPay
    pay_period_details: PayPeriodDetails
    paystub_details: PaystubDetails
    income_breakdown: List[IncomeBreakdown]
    ytd_earnings: PaystubYtdDetails
    verification: PaystubVerification = None

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
