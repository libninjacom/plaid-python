from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .credit_1099_filer import Credit1099Filer
from .credit_1099_payer import Credit1099Payer
from .credit_1099_recipient import Credit1099Recipient
from .credit_document_metadata import CreditDocumentMetadata


class Credit1099(BaseModel):
    document_id: Optional[str] = None
    document_metadata: Optional[CreditDocumentMetadata] = None
    form_1099_type: Optional[str] = None
    recipient: Optional[Credit1099Recipient] = None
    payer: Optional[Credit1099Payer] = None
    filer: Optional[Credit1099Filer] = None
    tax_year: Optional[str] = None
    rents: Optional[float] = None
    royalties: Optional[float] = None
    other_income: Optional[float] = None
    federal_income_tax_withheld: Optional[float] = None
    fishing_boat_proceeds: Optional[float] = None
    medical_and_healthcare_payments: Optional[float] = None
    nonemployee_compensation: Optional[float] = None
    substitute_payments_in_lieu_of_dividends_or_interest: Optional[float] = None
    payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer: Optional[
        str
    ] = None
    crop_insurance_proceeds: Optional[float] = None
    excess_golden_parachute_payments: Optional[float] = None
    gross_proceeds_paid_to_an_attorney: Optional[float] = None
    section_409_a_deferrals: Optional[float] = None
    section_409_a_income: Optional[float] = None
    state_tax_withheld: Optional[float] = None
    state_tax_withheld_lower: Optional[float] = None
    payer_state_number: Optional[str] = None
    payer_state_number_lower: Optional[str] = None
    state_income: Optional[float] = None
    state_income_lower: Optional[float] = None
    transactions_reported: Optional[str] = None
    pse_name: Optional[str] = None
    pse_telephone_number: Optional[str] = None
    gross_amount: Optional[float] = None
    card_not_present_transaction: Optional[float] = None
    merchant_category_code: Optional[str] = None
    number_of_payment_transactions: Optional[str] = None
    january_amount: Optional[float] = None
    february_amount: Optional[float] = None
    march_amount: Optional[float] = None
    april_amount: Optional[float] = None
    may_amount: Optional[float] = None
    june_amount: Optional[float] = None
    july_amount: Optional[float] = None
    august_amount: Optional[float] = None
    september_amount: Optional[float] = None
    october_amount: Optional[float] = None
    november_amount: Optional[float] = None
    december_amount: Optional[float] = None
    primary_state: Optional[str] = None
    secondary_state: Optional[str] = None
    primary_state_id: Optional[str] = None
    secondary_state_id: Optional[str] = None
    primary_state_income_tax: Optional[float] = None
    secondary_state_income_tax: Optional[float] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Credit1099":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Credit1099":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
