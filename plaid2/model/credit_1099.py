from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .credit_document_metadata import CreditDocumentMetadata
from .credit_1099_recipient import Credit1099Recipient
from .credit_1099_payer import Credit1099Payer
from .credit_1099_filer import Credit1099Filer


class Credit1099(BaseModel):
    document_id: str = None
    document_metadata: CreditDocumentMetadata
    form_1099_type: str
    recipient: Credit1099Recipient
    payer: Credit1099Payer
    filer: Credit1099Filer
    tax_year: str = None
    rents: float = None
    royalties: float = None
    other_income: float = None
    federal_income_tax_withheld: float = None
    fishing_boat_proceeds: float = None
    medical_and_healthcare_payments: float = None
    nonemployee_compensation: float = None
    substitute_payments_in_lieu_of_dividends_or_interest: float = None
    payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer: str = None
    crop_insurance_proceeds: float = None
    excess_golden_parachute_payments: float = None
    gross_proceeds_paid_to_an_attorney: float = None
    section_409_a_deferrals: float = None
    section_409_a_income: float = None
    state_tax_withheld: float = None
    state_tax_withheld_lower: float = None
    payer_state_number: str = None
    payer_state_number_lower: str = None
    state_income: float = None
    state_income_lower: float = None
    transactions_reported: str = None
    pse_name: str = None
    pse_telephone_number: str = None
    gross_amount: float = None
    card_not_present_transaction: float = None
    merchant_category_code: str = None
    number_of_payment_transactions: str = None
    january_amount: float = None
    february_amount: float = None
    march_amount: float = None
    april_amount: float = None
    may_amount: float = None
    june_amount: float = None
    july_amount: float = None
    august_amount: float = None
    september_amount: float = None
    october_amount: float = None
    november_amount: float = None
    december_amount: float = None
    primary_state: str = None
    secondary_state: str = None
    primary_state_id: str = None
    secondary_state_id: str = None
    primary_state_income_tax: float = None
    secondary_state_income_tax: float = None

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
