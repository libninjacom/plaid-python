import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.item_application_scopes_update(
        access_token="your access token",
        application_id="your application id",
        scopes=Scopes(
            product_access=ProductAccess(
                statements=True,
                accounts_routing_number=True,
                accounts_statements=True,
                auth=True,
                accounts_details_transactions=True,
                customers_profiles=True,
                transactions=True,
                identity=True,
                accounts_tax_statements=True,
            ),
            accounts=[
                AccountAccess(
                    unique_id="your unique id",
                    account_product_access=AccountProductAccessNullable(
                        AccountProductAccess(
                            account_data=True,
                            tax_documents=True,
                            statements=True,
                        ),
                        {},
                    ),
                    authorized=True,
                )
            ],
            new_accounts=True,
        ),
        context="your context",
    )
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.item_application_scopes_update(
        access_token="your access token",
        application_id="your application id",
        scopes=Scopes(
            product_access=ProductAccess(
                statements=True,
                accounts_routing_number=True,
                accounts_statements=True,
                auth=True,
                accounts_details_transactions=True,
                customers_profiles=True,
                transactions=True,
                identity=True,
                accounts_tax_statements=True,
            ),
            accounts=[
                AccountAccess(
                    unique_id="your unique id",
                    account_product_access=AccountProductAccessNullable(
                        AccountProductAccess(
                            account_data=True,
                            tax_documents=True,
                            statements=True,
                        ),
                        {},
                    ),
                    authorized=True,
                )
            ],
            new_accounts=True,
        ),
        context="your context",
    )
    print(f"{response!r}")


if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
