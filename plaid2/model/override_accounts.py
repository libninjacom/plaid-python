from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .holdings_override import HoldingsOverride
from .income_override import IncomeOverride
from .inflow_model import InflowModel
from .investments_transactions_override import InvestmentsTransactionsOverride
from .liability_override import LiabilityOverride
from .meta import Meta
from .numbers import Numbers
from .owner_override import OwnerOverride
from .transaction_override import TransactionOverride


class OverrideAccounts(BaseModel):
    type: str
    subtype: Optional[str] = None
    starting_balance: float
    force_available_balance: float
    currency: str
    meta: Meta
    numbers: Numbers
    transactions: List[TransactionOverride]
    holdings: Optional[HoldingsOverride] = None
    investment_transactions: Optional[InvestmentsTransactionsOverride] = None
    identity: OwnerOverride
    liability: LiabilityOverride
    inflow_model: InflowModel
    income: Optional[IncomeOverride] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "OverrideAccounts":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "OverrideAccounts":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
