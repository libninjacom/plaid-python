from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .document_risk_signal_institution_metadata import (
    DocumentRiskSignalInstitutionMetadata,
)


class DocumentRiskSignal(BaseModel):
    type: Optional[str] = None
    field: Optional[str] = None
    has_fraud_risk: Optional[bool] = None
    institution_metadata: Optional[DocumentRiskSignalInstitutionMetadata] = None
    expected_value: Optional[str] = None
    actual_value: Optional[str] = None
    signal_description: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "DocumentRiskSignal":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "DocumentRiskSignal":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
