import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.item_import(products, user_auth)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.item_import(products, user_auth)
    print(f"{response!r}")


products = ["your products"]
user_auth = ItemImportRequestUserAuth(
    user_id="your user id",
    auth_token="your auth token",
)

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
