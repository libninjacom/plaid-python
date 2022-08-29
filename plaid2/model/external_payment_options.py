from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .payment_initiation_optional_restriction_bacs import (
    PaymentInitiationOptionalRestrictionBacs,
)


class ExternalPaymentOptions(BaseModel):
    request_refund_details: Optional[bool] = None
    iban: Optional[str] = None
    bacs: Optional[PaymentInitiationOptionalRestrictionBacs] = None
    wallet_id: Optional[str] = None
    scheme: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ExternalPaymentOptions":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "ExternalPaymentOptions":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
