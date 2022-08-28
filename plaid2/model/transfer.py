from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .transfer_user_in_response import TransferUserInResponse
from .transfer_failure import TransferFailure
from .transfer_metadata import TransferMetadata
from .transfer_authorization_guarantee_decision_rationale import (
    TransferAuthorizationGuaranteeDecisionRationale,
)


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
    sweep_status: str = None
    network: str
    cancellable: bool
    failure_reason: TransferFailure = None
    metadata: TransferMetadata = None
    origination_account_id: str
    guarantee_decision: str = None
    guarantee_decision_rationale: TransferAuthorizationGuaranteeDecisionRationale = None
    iso_currency_code: str

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
