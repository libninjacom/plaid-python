import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.identity_verification_get(identity_verification_id)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.identity_verification_get(identity_verification_id)
    print(f"{response!r}")


identity_verification_id = "your identity verification id"

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
