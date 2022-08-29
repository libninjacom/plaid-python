from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .transfer_authorization_guarantee_decision_rationale import (
    TransferAuthorizationGuaranteeDecisionRationale,
)
from .transfer_failure import TransferFailure
from .transfer_metadata import TransferMetadata
from .transfer_user_in_response import TransferUserInResponse


class Transfer(BaseModel):
    id: str
    ach_class: str
    account_id: str
    type: str
    user: TransferUserInResponse
    amount: str
    description: str
    created: str
    status: str
    sweep_status: Optional[str] = None
    network: str
    cancellable: bool
    failure_reason: Optional[TransferFailure] = None
    metadata: Optional[TransferMetadata] = None
    origination_account_id: str
    guarantee_decision: Optional[str] = None
    guarantee_decision_rationale: Optional[
        TransferAuthorizationGuaranteeDecisionRationale
    ] = None
    iso_currency_code: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Transfer":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Transfer":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
