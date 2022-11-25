import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.payment_initiation_consent_create(
        recipient_id="your recipient id",
        reference="your reference",
        scopes=["your scopes"],
        constraints=PaymentInitiationConsentConstraints(
            valid_date_time=PaymentConsentValidDateTime(
                from_="your from",
                to="your to",
            ),
            periodic_amounts=[
                PaymentConsentPeriodicAmount(
                    interval="your interval",
                    amount=PaymentConsentPeriodicAmountAmount(
                        PaymentAmount(
                            currency="your currency",
                            value=1.0,
                        )
                    ),
                    alignment="your alignment",
                )
            ],
            max_payment_amount=PaymentConsentMaxPaymentAmount(
                PaymentAmount(
                    currency="your currency",
                    value=1.0,
                )
            ),
        ),
    )
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.payment_initiation_consent_create(
        recipient_id="your recipient id",
        reference="your reference",
        scopes=["your scopes"],
        constraints=PaymentInitiationConsentConstraints(
            valid_date_time=PaymentConsentValidDateTime(
                from_="your from",
                to="your to",
            ),
            periodic_amounts=[
                PaymentConsentPeriodicAmount(
                    interval="your interval",
                    amount=PaymentConsentPeriodicAmountAmount(
                        PaymentAmount(
                            currency="your currency",
                            value=1.0,
                        )
                    ),
                    alignment="your alignment",
                )
            ],
            max_payment_amount=PaymentConsentMaxPaymentAmount(
                PaymentAmount(
                    currency="your currency",
                    value=1.0,
                )
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
