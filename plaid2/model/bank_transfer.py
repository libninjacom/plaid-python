from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .bank_transfer_user import BankTransferUser
from .bank_transfer_failure import BankTransferFailure
from .bank_transfer_metadata import BankTransferMetadata


class BankTransfer(BaseModel):
    id: str
    ach_class: str
    account_id: str
    type: str
    user: BankTransferUser
    amount: str
    iso_currency_code: str
    description: str
    created: str
    status: str
    network: str
    cancellable: bool
    failure_reason: BankTransferFailure = None
    custom_tag: str = None
    metadata: BankTransferMetadata = None
    origination_account_id: str
    direction: str = None

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
