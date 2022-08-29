from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field
from .employee_income_summary_field_string import EmployeeIncomeSummaryFieldString
from .employer_income_summary_field_string import EmployerIncomeSummaryFieldString
from .pay_frequency import PayFrequency
from .projected_income_summary_field_number import ProjectedIncomeSummaryFieldNumber
from .transaction_data import TransactionData
from .ytd_gross_income_summary_field_number import YtdGrossIncomeSummaryFieldNumber
from .ytd_net_income_summary_field_number import YtdNetIncomeSummaryFieldNumber


class IncomeSummary(BaseModel):
    employer_name: EmployerIncomeSummaryFieldString
    employee_name: EmployeeIncomeSummaryFieldString
    ytd_gross_income: YtdGrossIncomeSummaryFieldNumber
    ytd_net_income: YtdNetIncomeSummaryFieldNumber
    pay_frequency: Optional[PayFrequency] = None
    projected_wage: ProjectedIncomeSummaryFieldNumber
    verified_transaction: Optional[TransactionData] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        return super().json(by_alias=True, **kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        return super().dict(by_alias=True, **kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IncomeSummary":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IncomeSummary":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
