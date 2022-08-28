from typing import List
from pydantic import BaseModel, Field


class Account(BaseModel):
    id: str
    name: str


class Item(BaseModel):
    access_token: str = Field(alias="accessToken")
    item_id: str
    institution_id: str
    webhook: str
    accounts: List[Account]


def main():
    json = {
        "accessToken": "access_token",
        "item_id": "item_id",
        "institution_id": "institution_id",
        "webhook": "webhook",
        "accounts": [{"id": "id", "name": "name"}],
    }
    item = Item.parse_obj(json)
    print(repr(item))
    json = item.json(by_alias=True)
    print(json)


if __name__ == "__main__":
    main()
    # import asyncio
    # asyncio.run(async_main())
