from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .bank_transfer_metadata import BankTransferMetadata
from .bank_transfer_user import BankTransferUser


class ProcessorBankTransferCreateRequest(BaseModel):
    idempotency_key: str
    processor_token: str
    type: str
    network: str
    amount: str
    iso_currency_code: str
    description: str
    ach_class: Optional[str] = None
    user: BankTransferUser
    custom_tag: Optional[str] = None
    metadata: Optional[BankTransferMetadata] = None
    origination_account_id: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ProcessorBankTransferCreateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "ProcessorBankTransferCreateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
