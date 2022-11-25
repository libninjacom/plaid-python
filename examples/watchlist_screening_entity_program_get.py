import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.watchlist_screening_entity_program_get(
        entity_watchlist_program_id
    )
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.watchlist_screening_entity_program_get(
        entity_watchlist_program_id
    )
    print(f"{response!r}")


entity_watchlist_program_id = "your entity watchlist program id"

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
