from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .credit_document_metadata import CreditDocumentMetadata
from .credit_pay_stub_employer import CreditPayStubEmployer
from .credit_pay_stub_employee import CreditPayStubEmployee
from .w_2_box_12 import W2Box12
from .w_2_state_and_local_wages import W2StateAndLocalWages


class CreditW2(BaseModel):
    document_metadata: CreditDocumentMetadata
    document_id: str
    employer: CreditPayStubEmployer
    employee: CreditPayStubEmployee
    tax_year: str = None
    employer_id_number: str = None
    wages_tips_other_comp: str = None
    federal_income_tax_withheld: str = None
    social_security_wages: str = None
    social_security_tax_withheld: str = None
    medicare_wages_and_tips: str = None
    medicare_tax_withheld: str = None
    social_security_tips: str = None
    allocated_tips: str = None
    box_9: str = None
    dependent_care_benefits: str = None
    nonqualified_plans: str = None
    box_12: List[W2Box12]
    statutory_employee: str = None
    retirement_plan: str = None
    third_party_sick_pay: str = None
    other: str = None
    state_and_local_wages: List[W2StateAndLocalWages]

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
