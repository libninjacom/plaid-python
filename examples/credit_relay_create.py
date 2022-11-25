import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.credit_relay_create(report_tokens, secondary_client_id)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.credit_relay_create(report_tokens, secondary_client_id)
    print(f"{response!r}")


report_tokens = [
    ReportToken(
        report_type="your report type",
        token="your token",
    )
]
secondary_client_id = "your secondary client id"

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
