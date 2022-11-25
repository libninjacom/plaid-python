import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.asset_report_filter(asset_report_token, account_ids_to_exclude)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.asset_report_filter(
        asset_report_token, account_ids_to_exclude
    )
    print(f"{response!r}")


asset_report_token = "your asset report token"
account_ids_to_exclude = ["your account ids to exclude"]

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
