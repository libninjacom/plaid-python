from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .link_token_create_request_user import LinkTokenCreateRequestUser
from .link_token_create_institution_data import LinkTokenCreateInstitutionData
from .link_token_account_filters import LinkTokenAccountFilters
from .link_token_eu_config import LinkTokenEuConfig
from .link_token_create_request_payment_initiation import (
    LinkTokenCreateRequestPaymentInitiation,
)
from .link_token_create_request_deposit_switch import (
    LinkTokenCreateRequestDepositSwitch,
)
from .link_token_create_request_income_verification import (
    LinkTokenCreateRequestIncomeVerification,
)
from .link_token_create_request_auth import LinkTokenCreateRequestAuth
from .link_token_create_request_transfer import LinkTokenCreateRequestTransfer
from .link_token_create_request_update import LinkTokenCreateRequestUpdate
from .link_token_create_request_identity_verification import (
    LinkTokenCreateRequestIdentityVerification,
)


class LinkTokenCreateRequest(BaseModel):
    client_name: str
    language: str
    country_codes: List[str]
    user: LinkTokenCreateRequestUser
    products: List[str]
    additional_consented_products: List[str]
    webhook: str
    access_token: str
    link_customization_name: str
    redirect_uri: str
    android_package_name: str
    institution_data: LinkTokenCreateInstitutionData
    account_filters: LinkTokenAccountFilters
    eu_config: LinkTokenEuConfig
    institution_id: str
    payment_initiation: LinkTokenCreateRequestPaymentInitiation
    deposit_switch: LinkTokenCreateRequestDepositSwitch
    income_verification: LinkTokenCreateRequestIncomeVerification
    auth: LinkTokenCreateRequestAuth
    transfer: LinkTokenCreateRequestTransfer
    update: LinkTokenCreateRequestUpdate
    identity_verification: LinkTokenCreateRequestIdentityVerification
    user_token: str

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
