from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .institutions_search_payment_initiation_options import (
    InstitutionsSearchPaymentInitiationOptions,
)


class InstitutionsSearchRequestOptions(BaseModel):
    oauth: Optional[bool] = None
    include_optional_metadata: Optional[bool] = None
    include_auth_metadata: Optional[bool] = None
    include_payment_initiation_metadata: Optional[bool] = None
    payment_initiation: Optional[InstitutionsSearchPaymentInitiationOptions] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "InstitutionsSearchRequestOptions":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "InstitutionsSearchRequestOptions":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
