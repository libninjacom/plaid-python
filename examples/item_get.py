from plaid2 import PlaidClient, AsyncPlaidClient
import logging

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


def main():
    client = PlaidClient.from_env()
    res = client.item_get("access-sandbox-b4957595-eae2-4130-9da7-114d14726a62")
    print(res)


async def async_main():
    client = AsyncPlaidClient.from_env()
    res = await client.item_get("access-sandbox-b4957595-eae2-4130-9da7-114d14726a62")
    print(res)


if __name__ == "__main__":
    main()
    # import asyncio
    # asyncio.run(async_main())
