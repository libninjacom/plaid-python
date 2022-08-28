from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .payment_initiation_maximum_payment_amount import (
    PaymentInitiationMaximumPaymentAmount,
)
from .payment_initiation_standing_order_metadata import (
    PaymentInitiationStandingOrderMetadata,
)


class PaymentInitiationMetadata(BaseModel):
    supports_international_payments: bool
    supports_sepa_instant: bool
    maximum_payment_amount: PaymentInitiationMaximumPaymentAmount
    supports_refund_details: bool
    standing_order_metadata: PaymentInitiationStandingOrderMetadata = None

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
