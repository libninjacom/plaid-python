import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.sandbox_item_set_verification_status(
        access_token, account_id, verification_status
    )
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.sandbox_item_set_verification_status(
        access_token, account_id, verification_status
    )
    print(f"{response!r}")


access_token = "your access token"
account_id = "your account id"
verification_status = "your verification status"

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
