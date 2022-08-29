from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .health_incident import HealthIncident
from .product_status import ProductStatus


class InstitutionStatus(BaseModel):
    item_logins: Optional[ProductStatus] = None
    transactions_updates: Optional[ProductStatus] = None
    auth: Optional[ProductStatus] = None
    identity: Optional[ProductStatus] = None
    investments_updates: Optional[ProductStatus] = None
    liabilities_updates: Optional[ProductStatus] = None
    liabilities: Optional[ProductStatus] = None
    investments: Optional[ProductStatus] = None
    health_incidents: Optional[List[HealthIncident]] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "InstitutionStatus":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "InstitutionStatus":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
