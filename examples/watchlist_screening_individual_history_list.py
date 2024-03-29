import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.watchlist_screening_individual_history_list(
        watchlist_screening_id
    )
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.watchlist_screening_individual_history_list(
        watchlist_screening_id
    )
    print(f"{response!r}")


watchlist_screening_id = "your watchlist screening id"

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
