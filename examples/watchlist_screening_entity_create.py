import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.watchlist_screening_entity_create(search_terms)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.watchlist_screening_entity_create(search_terms)
    print(f"{response!r}")


search_terms = EntityWatchlistSearchTerms(
    phone_number="your phone number",
    email_address="your email address",
    url="your url",
    entity_watchlist_program_id="your entity watchlist program id",
    document_number="your document number",
    legal_name="your legal name",
    country="your country",
)

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
