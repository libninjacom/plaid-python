from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .documentary_verification import DocumentaryVerification
from .identity_verification_step_summary import IdentityVerificationStepSummary
from .identity_verification_template_reference import (
    IdentityVerificationTemplateReference,
)
from .identity_verification_user_data import IdentityVerificationUserData
from .kyc_check_details import KycCheckDetails


class IdentityVerification(BaseModel):
    id: str
    client_user_id: str
    created_at: str
    completed_at: Optional[str] = None
    previous_attempt_id: Optional[str] = None
    shareable_url: Optional[str] = None
    template: IdentityVerificationTemplateReference
    user: IdentityVerificationUserData
    status: str
    steps: IdentityVerificationStepSummary
    documentary_verification: Optional[DocumentaryVerification] = None
    kyc_check: Optional[KycCheckDetails] = None
    watchlist_screening_id: Optional[Any] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IdentityVerification":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IdentityVerification":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
