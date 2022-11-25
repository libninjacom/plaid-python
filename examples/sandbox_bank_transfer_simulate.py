import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.sandbox_bank_transfer_simulate(bank_transfer_id, event_type)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.sandbox_bank_transfer_simulate(bank_transfer_id, event_type)
    print(f"{response!r}")


bank_transfer_id = "your bank transfer id"
event_type = "your event type"

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
