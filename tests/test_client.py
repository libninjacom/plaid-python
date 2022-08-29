import plaid2
import plaid2.authenticator


def test_client():
    auth = plaid2.authenticator.PlaidAuthenticator("client_id", "secret", "version")
    plaid2.client.PlaidClient(base_url="https://sandbox.plaid.com", authenticator=auth)
