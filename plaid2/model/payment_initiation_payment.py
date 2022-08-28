from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .payment_amount import PaymentAmount
from .external_payment_schedule_get import ExternalPaymentScheduleGet
from .external_payment_refund_details import ExternalPaymentRefundDetails
from .sender_bacs_nullable import SenderBacsNullable


class PaymentInitiationPayment(BaseModel):
    payment_id: str
    amount: PaymentAmount
    status: str
    recipient_id: str
    reference: str
    adjusted_reference: str = None
    last_status_update: str
    schedule: ExternalPaymentScheduleGet = None
    refund_details: ExternalPaymentRefundDetails = None
    bacs: SenderBacsNullable = None
    iban: str = None
    refund_ids: List[str]
    wallet_id: str = None
    scheme: str = None
    adjusted_scheme: str = None
    consent_id: str = None

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
