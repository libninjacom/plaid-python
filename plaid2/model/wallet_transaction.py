from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .wallet_transaction_amount import WalletTransactionAmount
from .wallet_transaction_counterparty import WalletTransactionCounterparty


class WalletTransaction(BaseModel):
    transaction_id: str
    reference: str
    type: str
    amount: WalletTransactionAmount
    counterparty: WalletTransactionCounterparty
    status: str
    created_at: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "WalletTransaction":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "WalletTransaction":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
