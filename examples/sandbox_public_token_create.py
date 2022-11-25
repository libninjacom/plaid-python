import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.sandbox_public_token_create(institution_id, initial_products)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.sandbox_public_token_create(
        institution_id, initial_products
    )
    print(f"{response!r}")


institution_id = "your institution id"
initial_products = ["your initial products"]

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
