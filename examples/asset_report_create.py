import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.asset_report_create(access_tokens, days_requested)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.asset_report_create(access_tokens, days_requested)
    print(f"{response!r}")


access_tokens = ["your access tokens"]
days_requested = 1

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
