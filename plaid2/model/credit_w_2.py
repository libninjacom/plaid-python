from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .credit_document_metadata import CreditDocumentMetadata
from .credit_pay_stub_employee import CreditPayStubEmployee
from .credit_pay_stub_employer import CreditPayStubEmployer
from .w_2_box_12 import W2Box12
from .w_2_state_and_local_wages import W2StateAndLocalWages


class CreditW2(BaseModel):
    document_metadata: CreditDocumentMetadata
    document_id: str
    employer: CreditPayStubEmployer
    employee: CreditPayStubEmployee
    tax_year: Optional[str] = None
    employer_id_number: Optional[str] = None
    wages_tips_other_comp: Optional[str] = None
    federal_income_tax_withheld: Optional[str] = None
    social_security_wages: Optional[str] = None
    social_security_tax_withheld: Optional[str] = None
    medicare_wages_and_tips: Optional[str] = None
    medicare_tax_withheld: Optional[str] = None
    social_security_tips: Optional[str] = None
    allocated_tips: Optional[str] = None
    box_9: Optional[str] = None
    dependent_care_benefits: Optional[str] = None
    nonqualified_plans: Optional[str] = None
    box_12: List[W2Box12]
    statutory_employee: Optional[str] = None
    retirement_plan: Optional[str] = None
    third_party_sick_pay: Optional[str] = None
    other: Optional[str] = None
    state_and_local_wages: List[W2StateAndLocalWages]

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditW2":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditW2":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
