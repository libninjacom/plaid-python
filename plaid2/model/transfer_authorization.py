from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .transfer_authorization_decision_rationale import (
    TransferAuthorizationDecisionRationale,
)
from .transfer_authorization_guarantee_decision_rationale import (
    TransferAuthorizationGuaranteeDecisionRationale,
)
from .transfer_authorization_proposed_transfer import (
    TransferAuthorizationProposedTransfer,
)


class TransferAuthorization(BaseModel):
    id: str
    created: str
    decision: str
    decision_rationale: Optional[TransferAuthorizationDecisionRationale] = None
    guarantee_decision: Optional[str] = None
    guarantee_decision_rationale: Optional[
        TransferAuthorizationGuaranteeDecisionRationale
    ] = None
    proposed_transfer: TransferAuthorizationProposedTransfer

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferAuthorization":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransferAuthorization":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
