from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .meta import Meta
from .numbers import Numbers
from .transaction_override import TransactionOverride
from .holdings_override import HoldingsOverride
from .investments_transactions_override import InvestmentsTransactionsOverride
from .owner_override import OwnerOverride
from .liability_override import LiabilityOverride
from .inflow_model import InflowModel
from .income_override import IncomeOverride


class OverrideAccounts(BaseModel):
    type: str
    subtype: str = None
    starting_balance: float
    force_available_balance: float
    currency: str
    meta: Meta
    numbers: Numbers
    transactions: List[TransactionOverride]
    holdings: HoldingsOverride
    investment_transactions: InvestmentsTransactionsOverride
    identity: OwnerOverride
    liability: LiabilityOverride
    inflow_model: InflowModel
    income: IncomeOverride

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
