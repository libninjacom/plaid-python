from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .multi_document_risk_signal import MultiDocumentRiskSignal
from .single_document_risk_signal import SingleDocumentRiskSignal


class DocumentRiskSignalsObject(BaseModel):
    account_id: Optional[str] = None
    single_document_risk_signals: List[SingleDocumentRiskSignal]
    multi_document_risk_signals: List[MultiDocumentRiskSignal]

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "DocumentRiskSignalsObject":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "DocumentRiskSignalsObject":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
