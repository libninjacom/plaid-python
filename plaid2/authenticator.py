import os
from typing import Dict, Any


class PlaidAuthenticator:
    def __init__(self, client_id: str, secret: str, plaid_version: str):
        self.client_id = client_id
        self.secret = secret
        self.plaid_version = plaid_version

    def authenticate(
        self, headers: Dict[str, str], params: Dict[str, str], data: Dict[str, Any]
    ) -> None:
        headers["PLAID-CLIENT-ID"] = self.client_id
        headers["PLAID-SECRET"] = self.secret
        headers["Plaid-Version"] = self.plaid_version

    @classmethod
    def from_env(cls) -> "PlaidAuthenticator":
        client_id = os.environ["PLAID_CLIENT_ID"]
        secret = os.environ["PLAID_SECRET"]
        plaid_version = os.environ["PLAID_VERSION"]
        return cls(client_id=client_id, secret=secret, plaid_version=plaid_version)
