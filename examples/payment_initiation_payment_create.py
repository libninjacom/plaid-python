import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.payment_initiation_payment_create(recipient_id, reference, amount)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.payment_initiation_payment_create(
        recipient_id, reference, amount
    )
    print(f"{response!r}")


recipient_id = "your recipient id"
reference = "your reference"
amount = PaymentAmount(
    currency="your currency",
    value=1.0,
)

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
