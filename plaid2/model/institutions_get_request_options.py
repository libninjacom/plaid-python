from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class InstitutionsGetRequestOptions(BaseModel):
    products: Optional[List[str]] = None
    routing_numbers: Optional[List[str]] = None
    oauth: Optional[bool] = None
    include_optional_metadata: Optional[bool] = None
    include_auth_metadata: Optional[bool] = None
    include_payment_initiation_metadata: Optional[bool] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "InstitutionsGetRequestOptions":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "InstitutionsGetRequestOptions":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
