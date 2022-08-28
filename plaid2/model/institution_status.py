from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .product_status import ProductStatus
from .product_status import ProductStatus
from .product_status import ProductStatus
from .product_status import ProductStatus
from .product_status import ProductStatus
from .product_status import ProductStatus
from .product_status import ProductStatus
from .product_status import ProductStatus
from .health_incident import HealthIncident


class InstitutionStatus(BaseModel):
    item_logins: ProductStatus
    transactions_updates: ProductStatus
    auth: ProductStatus
    identity: ProductStatus
    investments_updates: ProductStatus
    liabilities_updates: ProductStatus
    liabilities: ProductStatus
    investments: ProductStatus
    health_incidents: List[HealthIncident] = None

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
