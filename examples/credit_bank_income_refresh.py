import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.credit_bank_income_refresh(client_id, secret, user_token)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.credit_bank_income_refresh(client_id, secret, user_token)
    print(f"{response!r}")


client_id = "your client id"
secret = "your secret"
user_token = "your user token"

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
