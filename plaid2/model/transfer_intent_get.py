from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .transfer_authorization_decision_rationale import (
    TransferAuthorizationDecisionRationale,
)
from .transfer_authorization_guarantee_decision_rationale import (
    TransferAuthorizationGuaranteeDecisionRationale,
)
from .transfer_intent_get_failure_reason import TransferIntentGetFailureReason
from .transfer_metadata import TransferMetadata
from .transfer_user_in_response import TransferUserInResponse


class TransferIntentGet(BaseModel):
    id: str
    created: str
    status: str
    transfer_id: Optional[str] = None
    failure_reason: Optional[TransferIntentGetFailureReason] = None
    authorization_decision: Optional[str] = None
    authorization_decision_rationale: Optional[
        TransferAuthorizationDecisionRationale
    ] = None
    account_id: Optional[str] = None
    origination_account_id: str
    amount: str
    mode: str
    ach_class: str
    user: TransferUserInResponse
    description: str
    metadata: Optional[TransferMetadata] = None
    iso_currency_code: str
    require_guarantee: Optional[bool] = None
    guarantee_decision: Optional[str] = None
    guarantee_decision_rationale: Optional[
        TransferAuthorizationGuaranteeDecisionRationale
    ] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferIntentGet":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransferIntentGet":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
