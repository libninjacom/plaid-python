import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.signal_decision_report(client_transaction_id, initiated)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.signal_decision_report(client_transaction_id, initiated)
    print(f"{response!r}")


client_transaction_id = "your client transaction id"
initiated = True

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
