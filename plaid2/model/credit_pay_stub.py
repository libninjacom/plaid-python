from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .credit_document_metadata import CreditDocumentMetadata
from .credit_pay_stub_deductions import CreditPayStubDeductions
from .credit_pay_stub_earnings import CreditPayStubEarnings
from .credit_pay_stub_employee import CreditPayStubEmployee
from .credit_pay_stub_employer import CreditPayStubEmployer
from .credit_pay_stub_net_pay import CreditPayStubNetPay
from .credit_pay_stub_verification import CreditPayStubVerification
from .pay_stub_pay_period_details import PayStubPayPeriodDetails


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

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditPayStub":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditPayStub":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
