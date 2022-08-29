from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .pslf_status import PslfStatus
from .servicer_address_data import ServicerAddressData
from .student_loan_status import StudentLoanStatus
from .student_repayment_plan import StudentRepaymentPlan


class StudentLoan(BaseModel):
    account_id: Optional[str] = None
    account_number: Optional[str] = None
    disbursement_dates: Optional[List[str]] = None
    expected_payoff_date: Optional[str] = None
    guarantor: Optional[str] = None
    interest_rate_percentage: float
    is_overdue: Optional[bool] = None
    last_payment_amount: Optional[float] = None
    last_payment_date: Optional[str] = None
    last_statement_issue_date: Optional[str] = None
    loan_name: Optional[str] = None
    loan_status: StudentLoanStatus
    minimum_payment_amount: Optional[float] = None
    next_payment_due_date: Optional[str] = None
    origination_date: Optional[str] = None
    origination_principal_amount: Optional[float] = None
    outstanding_interest_amount: Optional[float] = None
    payment_reference_number: Optional[str] = None
    pslf_status: PslfStatus
    repayment_plan: StudentRepaymentPlan
    sequence_number: Optional[str] = None
    servicer_address: ServicerAddressData
    ytd_interest_paid: Optional[float] = None
    ytd_principal_paid: Optional[float] = None

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
