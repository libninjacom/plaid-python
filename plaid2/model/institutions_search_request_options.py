from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .institutions_search_payment_initiation_options import (
    InstitutionsSearchPaymentInitiationOptions,
)


class InstitutionsSearchRequestOptions(BaseModel):
    oauth: bool = None
    include_optional_metadata: bool
    include_auth_metadata: bool = None
    include_payment_initiation_metadata: bool = None
    payment_initiation: InstitutionsSearchPaymentInitiationOptions = None

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
