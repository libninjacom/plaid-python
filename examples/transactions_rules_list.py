import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.transactions_rules_list(client_id, access_token, secret)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.transactions_rules_list(client_id, access_token, secret)
    print(f"{response!r}")


client_id = "your client id"
access_token = "your access token"
secret = "your secret"

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
