from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .account_filters_response import AccountFiltersResponse
from .link_token_create_institution_data import LinkTokenCreateInstitutionData


class LinkTokenGetMetadataResponse(BaseModel):
    initial_products: List[str]
    webhook: Optional[str] = None
    country_codes: List[str]
    language: Optional[str] = None
    institution_data: Optional[LinkTokenCreateInstitutionData] = None
    account_filters: Optional[AccountFiltersResponse] = None
    redirect_uri: Optional[str] = None
    client_name: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LinkTokenGetMetadataResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "LinkTokenGetMetadataResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
