import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.watchlist_screening_entity_review_create(
        confirmed_hits, dismissed_hits, entity_watchlist_screening_id
    )
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.watchlist_screening_entity_review_create(
        confirmed_hits, dismissed_hits, entity_watchlist_screening_id
    )
    print(f"{response!r}")


confirmed_hits = ["your confirmed hits"]
dismissed_hits = ["your dismissed hits"]
entity_watchlist_screening_id = "your entity watchlist screening id"

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
