from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .credit_pay_stub_deductions import CreditPayStubDeductions
from .credit_document_metadata import CreditDocumentMetadata
from .credit_pay_stub_earnings import CreditPayStubEarnings
from .credit_pay_stub_employee import CreditPayStubEmployee
from .credit_pay_stub_employer import CreditPayStubEmployer
from .credit_pay_stub_net_pay import CreditPayStubNetPay
from .pay_stub_pay_period_details import PayStubPayPeriodDetails
from .credit_pay_stub_verification import CreditPayStubVerification


class CreditPayStub(BaseModel):
    deductions: CreditPayStubDeductions
    document_id: Optional[str] = None
    document_metadata: CreditDocumentMetadata
    earnings: CreditPayStubEarnings
    employee: CreditPayStubEmployee
    employer: CreditPayStubEmployer
    net_pay: CreditPayStubNetPay
    pay_period_details: PayStubPayPeriodDetails
    verification: Optional[CreditPayStubVerification] = None

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
