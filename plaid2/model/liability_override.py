from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .student_loan_repayment_model import StudentLoanRepaymentModel
from .student_loan_status import StudentLoanStatus
from .pslf_status import PslfStatus
from .address import Address


class LiabilityOverride(BaseModel):
    type: str
    purchase_apr: float
    cash_apr: float
    balance_transfer_apr: float
    special_apr: float
    last_payment_amount: float
    minimum_payment_amount: float
    is_overdue: bool
    origination_date: str
    principal: float
    nominal_apr: float
    interest_capitalization_grace_period_months: float
    repayment_model: StudentLoanRepaymentModel
    expected_payoff_date: str
    guarantor: str
    is_federal: bool
    loan_name: str
    loan_status: StudentLoanStatus
    payment_reference_number: str
    pslf_status: PslfStatus
    repayment_plan_description: str
    repayment_plan_type: str
    sequence_number: str
    servicer_address: Address

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
