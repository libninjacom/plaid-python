from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class SignalEvaluateCoreAttributes(BaseModel):
    unauthorized_transactions_count_7_d: int = None
    unauthorized_transactions_count_30_d: int = None
    unauthorized_transactions_count_60_d: int = None
    unauthorized_transactions_count_90_d: int = None
    nsf_overdraft_transactions_count_7_d: int = None
    nsf_overdraft_transactions_count_30_d: int = None
    nsf_overdraft_transactions_count_60_d: int = None
    nsf_overdraft_transactions_count_90_d: int = None
    days_since_first_plaid_connection: int = None
    plaid_connections_count_7_d: int = None
    plaid_connections_count_30_d: int = None
    total_plaid_connections_count: int = None
    is_savings_or_money_market_account: bool
    total_credit_transactions_amount_10_d: float = None
    total_debit_transactions_amount_10_d: float = None
    p_50_credit_transactions_amount_28_d: float = None
    p_50_debit_transactions_amount_28_d: float = None
    p_95_credit_transactions_amount_28_d: float = None
    p_95_debit_transactions_amount_28_d: float = None
    days_with_negative_balance_count_90_d: int = None
    p_90_eod_balance_30_d: float = None
    p_90_eod_balance_60_d: float = None
    p_90_eod_balance_90_d: float = None
    p_10_eod_balance_30_d: float = None
    p_10_eod_balance_60_d: float = None
    p_10_eod_balance_90_d: float = None
    available_balance: float = None
    current_balance: float = None
    balance_last_updated: str = None
    phone_change_count_28_d: int = None
    phone_change_count_90_d: int = None
    email_change_count_28_d: int = None
    email_change_count_90_d: int = None
    address_change_count_28_d: int = None
    address_change_count_90_d: int = None
    plaid_non_oauth_authentication_attempts_count_3_d: int = None
    plaid_non_oauth_authentication_attempts_count_7_d: int = None
    plaid_non_oauth_authentication_attempts_count_30_d: int = None
    failed_plaid_non_oauth_authentication_attempts_count_3_d: int = None
    failed_plaid_non_oauth_authentication_attempts_count_7_d: int = None
    failed_plaid_non_oauth_authentication_attempts_count_30_d: int = None
    debit_transactions_count_10_d: int = None
    credit_transactions_count_10_d: int = None
    debit_transactions_count_30_d: int = None
    credit_transactions_count_30_d: int = None
    debit_transactions_count_60_d: int = None
    credit_transactions_count_60_d: int = None
    debit_transactions_count_90_d: int = None
    credit_transactions_count_90_d: int = None
    total_debit_transactions_amount_30_d: float = None
    total_credit_transactions_amount_30_d: float = None
    total_debit_transactions_amount_60_d: float = None
    total_credit_transactions_amount_60_d: float = None
    total_debit_transactions_amount_90_d: float = None
    total_credit_transactions_amount_90_d: float = None
    p_50_eod_balance_30_d: float = None
    p_50_eod_balance_60_d: float = None
    p_50_eod_balance_90_d: float = None
    p_50_eod_balance_31_d_to_60_d: float = None
    p_50_eod_balance_61_d_to_90_d: float = None
    p_90_eod_balance_31_d_to_60_d: float = None
    p_90_eod_balance_61_d_to_90_d: float = None
    p_10_eod_balance_31_d_to_60_d: float = None
    p_10_eod_balance_61_d_to_90_d: float = None

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
