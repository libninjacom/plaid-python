import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.transfer_intent_create(
        mode="your mode",
        amount="your amount",
        description="your description",
        ach_class="your ach class",
        user=TransferUserInRequest(
            legal_name="your legal name",
            email_address="your email address",
            phone_number="your phone number",
            address=TransferUserAddressInRequest(
                region="your region",
                country="your country",
                postal_code="your postal code",
                city="your city",
                street="your street",
            ),
        ),
    )
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.transfer_intent_create(
        mode="your mode",
        amount="your amount",
        description="your description",
        ach_class="your ach class",
        user=TransferUserInRequest(
            legal_name="your legal name",
            email_address="your email address",
            phone_number="your phone number",
            address=TransferUserAddressInRequest(
                region="your region",
                country="your country",
                postal_code="your postal code",
                city="your city",
                street="your street",
            ),
        ),
    )
    print(f"{response!r}")


if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
