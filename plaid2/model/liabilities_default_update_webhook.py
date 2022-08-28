from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .plaid_error import PlaidError
from .liabilities_account_ids_with_updated_liabilities import (
    LiabilitiesAccountIdsWithUpdatedLiabilities,
)


class LiabilitiesDefaultUpdateWebhook(BaseModel):
    webhook_type: str
    webhook_code: str
    item_id: str
    error: PlaidError = None
    account_ids_with_new_liabilities: List[str]
    account_ids_with_updated_liabilities: LiabilitiesAccountIdsWithUpdatedLiabilities

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