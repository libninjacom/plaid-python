from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .link_token_account_filters import LinkTokenAccountFilters
from .link_token_create_institution_data import LinkTokenCreateInstitutionData
from .link_token_create_request_auth import LinkTokenCreateRequestAuth
from .link_token_create_request_deposit_switch import (
    LinkTokenCreateRequestDepositSwitch,
)
from .link_token_create_request_identity_verification import (
    LinkTokenCreateRequestIdentityVerification,
)
from .link_token_create_request_income_verification import (
    LinkTokenCreateRequestIncomeVerification,
)
from .link_token_create_request_payment_initiation import (
    LinkTokenCreateRequestPaymentInitiation,
)
from .link_token_create_request_transfer import LinkTokenCreateRequestTransfer
from .link_token_create_request_update import LinkTokenCreateRequestUpdate
from .link_token_create_request_user import LinkTokenCreateRequestUser
from .link_token_eu_config import LinkTokenEuConfig


class LinkTokenCreateRequest(BaseModel):
    client_name: str
    language: str
    country_codes: List[str]
    user: LinkTokenCreateRequestUser
    products: Optional[List[str]] = None
    additional_consented_products: Optional[List[str]] = None
    webhook: Optional[str] = None
    access_token: Optional[str] = None
    link_customization_name: Optional[str] = None
    redirect_uri: Optional[str] = None
    android_package_name: Optional[str] = None
    institution_data: Optional[LinkTokenCreateInstitutionData] = None
    account_filters: Optional[LinkTokenAccountFilters] = None
    eu_config: Optional[LinkTokenEuConfig] = None
    institution_id: Optional[str] = None
    payment_initiation: Optional[LinkTokenCreateRequestPaymentInitiation] = None
    deposit_switch: Optional[LinkTokenCreateRequestDepositSwitch] = None
    income_verification: Optional[LinkTokenCreateRequestIncomeVerification] = None
    auth: Optional[LinkTokenCreateRequestAuth] = None
    transfer: Optional[LinkTokenCreateRequestTransfer] = None
    update: Optional[LinkTokenCreateRequestUpdate] = None
    identity_verification: Optional[LinkTokenCreateRequestIdentityVerification] = None
    user_token: Optional[str] = None

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
