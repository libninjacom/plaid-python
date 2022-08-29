from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .auth_metadata import AuthMetadata
from .institution_status import InstitutionStatus
from .payment_initiation_metadata import PaymentInitiationMetadata


class Institution(BaseModel):
    institution_id: str
    name: str
    products: List[str]
    country_codes: List[str]
    url: Optional[str] = None
    primary_color: Optional[str] = None
    logo: Optional[str] = None
    routing_numbers: List[str]
    oauth: bool
    status: Optional[InstitutionStatus] = None
    payment_initiation_metadata: Optional[PaymentInitiationMetadata] = None
    auth_metadata: Optional[AuthMetadata] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Institution":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Institution":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
