from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .identity_verification_template_reference import (
    IdentityVerificationTemplateReference,
)
from .identity_verification_user_data import IdentityVerificationUserData
from .identity_verification_step_summary import IdentityVerificationStepSummary
from .documentary_verification import DocumentaryVerification
from .kyc_check_details import KycCheckDetails


class IdentityVerificationResponse(BaseModel):
    id: str
    client_user_id: str
    created_at: str
    completed_at: str = None
    previous_attempt_id: str = None
    shareable_url: str = None
    template: IdentityVerificationTemplateReference
    user: IdentityVerificationUserData
    status: str
    steps: IdentityVerificationStepSummary
    documentary_verification: DocumentaryVerification = None
    kyc_check: KycCheckDetails = None
    watchlist_screening_id: Any = None
    request_id: str

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
