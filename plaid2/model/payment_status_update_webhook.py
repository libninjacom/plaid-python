from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .plaid_error import PlaidError


class PaymentStatusUpdateWebhook(BaseModel):
    webhook_type: str
    webhook_code: str
    payment_id: str
    new_payment_status: str
    old_payment_status: str
    original_reference: Optional[str] = None
    adjusted_reference: Optional[str] = None
    original_start_date: Optional[str] = None
    adjusted_start_date: Optional[str] = None
    timestamp: str
    error: Optional[PlaidError] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentStatusUpdateWebhook":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "PaymentStatusUpdateWebhook":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
