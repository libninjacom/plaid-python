import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.identity_verification_create(
        is_shareable=True,
        template_id="your template id",
        gave_consent=True,
        user=IdentityVerificationRequestUser(
            date_of_birth="your date of birth",
            phone_number="your phone number",
            id_number=UserIdNumber(
                type="your type",
                value="your value",
            ),
            email_address="your email address",
            name=UserName(
                family_name="your family name",
                given_name="your given name",
            ),
            client_user_id="your client user id",
            address=UserAddress(
                street_2="your street 2",
                street="your street",
                city="your city",
                region="your region",
                postal_code="your postal code",
                country="your country",
            ),
        ),
    )
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.identity_verification_create(
        is_shareable=True,
        template_id="your template id",
        gave_consent=True,
        user=IdentityVerificationRequestUser(
            date_of_birth="your date of birth",
            phone_number="your phone number",
            id_number=UserIdNumber(
                type="your type",
                value="your value",
            ),
            email_address="your email address",
            name=UserName(
                family_name="your family name",
                given_name="your given name",
            ),
            client_user_id="your client user id",
            address=UserAddress(
                street_2="your street 2",
                street="your street",
                city="your city",
                region="your region",
                postal_code="your postal code",
                country="your country",
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
