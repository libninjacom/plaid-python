from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .kyc_check_address_summary import KycCheckAddressSummary
from .kyc_check_date_of_birth_summary import KycCheckDateOfBirthSummary
from .kyc_check_id_number_summary import KycCheckIdNumberSummary
from .kyc_check_name_summary import KycCheckNameSummary
from .kyc_check_phone_summary import KycCheckPhoneSummary


class KycCheckDetails(BaseModel):
    status: str
    address: KycCheckAddressSummary
    name: KycCheckNameSummary
    date_of_birth: KycCheckDateOfBirthSummary
    id_number: KycCheckIdNumberSummary
    phone_number: KycCheckPhoneSummary

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
