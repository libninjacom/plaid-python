from plaid2 import PlaidClient, AsyncPlaidClient, enable_debug_logging
from plaid2.model import LinkTokenCreateRequestUser


def main():
    client = PlaidClient.from_env()
    enable_debug_logging()
    res = client.link_token_create(
        "plaid-test",
        "en",
        ["US"],
        user=LinkTokenCreateRequestUser(client_user_id="user-id"),
        products=["auth", "transactions"],
    )
    print(f"{res!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    enable_debug_logging()
    res = await client.link_token_create(
        "plaid-test",
        "en",
        ["US"],
        user=LinkTokenCreateRequestUser(client_user_id="user-id"),
        products=["auth", "transactions"],
    )
    print(f"{res!r}")


if __name__ == "__main__":
    main()
    # import asyncio
    # asyncio.run(async_main())
