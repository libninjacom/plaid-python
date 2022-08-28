from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .mortgage_interest_rate import MortgageInterestRate
from .mortgage_property_address import MortgagePropertyAddress


class MortgageLiability(BaseModel):
    account_id: str
    account_number: str
    current_late_fee: Optional[float] = None
    escrow_balance: Optional[float] = None
    has_pmi: Optional[bool] = None
    has_prepayment_penalty: Optional[bool] = None
    interest_rate: MortgageInterestRate
    last_payment_amount: Optional[float] = None
    last_payment_date: Optional[str] = None
    loan_type_description: Optional[str] = None
    loan_term: Optional[str] = None
    maturity_date: Optional[str] = None
    next_monthly_payment: Optional[float] = None
    next_payment_due_date: Optional[str] = None
    origination_date: Optional[str] = None
    origination_principal_amount: Optional[float] = None
    past_due_amount: Optional[float] = None
    property_address: MortgagePropertyAddress
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
