from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .liabilities_account_ids_with_updated_liabilities import (
    LiabilitiesAccountIdsWithUpdatedLiabilities,
)
from .plaid_error import PlaidError


class LiabilitiesDefaultUpdateWebhook(BaseModel):
    webhook_type: str
    webhook_code: str
    item_id: str
    error: Optional[PlaidError] = None
    account_ids_with_new_liabilities: List[str]
    account_ids_with_updated_liabilities: LiabilitiesAccountIdsWithUpdatedLiabilities

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LiabilitiesDefaultUpdateWebhook":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "LiabilitiesDefaultUpdateWebhook":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
