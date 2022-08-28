
import aiohttp
import requests
import os
import plaid2.model as model
from typing import Optional


class AsyncPlaidClient:
    
    def __init__(self, base_url: str) :
        
        self.authenticator = None
        self.base_url = base_url
    def _raise_for_status(self, response: aiohttp.ClientResponse) -> None:
        
        if response.status < 400:
            return
        raise requests.exceptions.HTTPError(response.status, response.reason, response.content)
    async def item_application_list(self, access_token: Optional[Optional[model.AccessTokenNullable]] = None) -> model.model.ItemApplicationListResponse:
        """List a user’s connected applications
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/item/application/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ItemApplicationListResponse.from_json(data)
    async def item_application_scopes_update(self, access_token: model.AccessToken, application_id: model.ApplicationId, scopes: model.Scopes, state: Optional[model.ScopesState] = None, context: model.ScopesContext) -> model.model.ItemApplicationScopesUpdateResponse:
        """Update the scopes of access for a particular application
        
        Enable consumers to update product access on selected accounts for an application.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "application_id": application_id,
            "scopes": scopes,
            "state": state,
            "context": context,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/item/application/scopes/update", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ItemApplicationScopesUpdateResponse.from_json(data)
    async def application_get(self, application_id: model.ApplicationId) -> model.model.ApplicationGetResponse:
        """Retrieve information about a Plaid application
        
        Allows financial institutions to retrieve information about Plaid clients for the purpose of building control-tower experiences
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "application_id": application_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/application/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ApplicationGetResponse.from_json(data)
    async def item_get(self, access_token: model.AccessToken) -> model.model.ItemGetResponse:
        """Retrieve an Item
        
        Returns information about the status of an Item.
        
        See endpoint docs at <https://plaid.com/docs/api/items/#itemget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/item/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ItemGetResponse.from_json(data)
    async def auth_get(self, access_token: model.AccessToken, options: Optional[model.AuthGetRequestOptions] = None) -> model.model.AuthGetResponse:
        """Retrieve auth data
        
        The `/auth/get` endpoint returns the bank account and bank identification numbers (such as routing numbers, for US accounts) associated with an Item's checking and savings accounts, along with high-level account data and balances when available.
        
        Note: This request may take some time to complete if `auth` was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.
        
        Also note that `/auth/get` will not return data for any new accounts opened after the Item was created. To obtain data for new accounts, create a new Item.
        
        Versioning note: In API version 2017-03-08, the schema of the `numbers` object returned by this endpoint is substantially different. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2018-05-22).
        
        See endpoint docs at <https://plaid.com/docs/api/products/auth/#authget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/auth/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AuthGetResponse.from_json(data)
    async def transactions_get(self, options: Optional[model.TransactionsGetRequestOptions] = None, access_token: model.AccessToken, start_date: str, end_date: str) -> model.model.TransactionsGetResponse:
        """Get transaction data
        
        The `/transactions/get` endpoint allows developers to receive user-authorized transaction data for credit, depository, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). For transaction history from investments accounts, use the [Investments endpoint](https://plaid.com/docs/api/products/investments/) instead. Transaction data is standardized across financial institutions, and in many cases transactions are linked to a clean name, entity type, location, and category. Similarly, account data is standardized and returned with a clean name, number, balance, and other meta information where available.
        
        Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.  Transactions are not immutable and can also be removed altogether by the institution; a removed transaction will no longer appear in `/transactions/get`.  For more details, see [Pending and posted transactions](https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions).
        
        Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate the `count` and `offset` parameters in conjunction with the `total_transactions` response body field to fetch all available transactions.
        
        Data returned by `/transactions/get` will be the data available for the Item as of the most recent successful check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item's `status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, you can use the `/transactions/refresh` endpoint.
        
        Note that data may not be immediately available to `/transactions/get`. Plaid will begin to prepare transactions data upon Item link, if Link was initialized with `transactions`, or upon the first call to `/transactions/get`, if it wasn't. To be alerted when transaction data is ready to be fetched, listen for the [`INITIAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#initial_update) and [`HISTORICAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#historical_update) webhooks. If no transaction history is ready when `/transactions/get` is called, it will return a `PRODUCT_NOT_READY` error.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transactions/#transactionsget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "options": options,
            "access_token": access_token,
            "start_date": start_date,
            "end_date": end_date,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transactions/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransactionsGetResponse.from_json(data)
    async def transactions_refresh(self, access_token: model.AccessToken) -> model.model.TransactionsRefreshResponse:
        """Refresh transaction data
        
        `/transactions/refresh` is an optional endpoint for users of the Transactions product. It initiates an on-demand extraction to fetch the newest transactions for an Item. This on-demand extraction takes place in addition to the periodic extractions that automatically occur multiple times a day for any Transactions-enabled Item. If changes to transactions are discovered after calling `/transactions/refresh`, Plaid will fire a webhook: [`TRANSACTIONS_REMOVED`](https://plaid.com/docs/api/products/transactions/#transactions_removed) will be fired if any removed transactions are detected, and [`DEFAULT_UPDATE`](https://plaid.com/docs/api/products/transactions/#default_update) will be fired if any new transactions are detected. New transactions can be fetched by calling `/transactions/get`.
        
        Access to `/transactions/refresh` in Production is specific to certain pricing plans. If you cannot access `/transactions/refresh` in Production, [contact Sales](https://www.plaid.com/contact) for assistance.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transactions/#transactionsrefresh>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transactions/refresh", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransactionsRefreshResponse.from_json(data)
    async def transactions_recurring_get(self, access_token: model.AccessToken, options: Optional[model.TransactionsRecurringGetRequestOptions] = None, account_ids: List[str]) -> model.model.TransactionsRecurringGetResponse:
        """Fetch recurring transaction streams
        
        The `/transactions/recurring/get` endpoint allows developers to receive a summary of the recurring outflow and inflow streams (expenses and deposits) from a user’s checking, savings or credit card accounts. Additionally, Plaid provides key insights about each recurring stream including the category, merchant, last amount, and more. Developers can use these insights to build tools and experiences that help their users better manage cash flow, monitor subscriptions, reduce spend, and stay on track with bill payments.
        
        This endpoint is not included by default as part of Transactions. To request access to this endpoint and learn more about pricing, contact your Plaid account manager.
        
        Note that unlike `/transactions/get`, `/transactions/recurring/get` will not initialize an Item with Transactions. The Item must already have been initialized with Transactions (either during Link, by specifying it in `/link/token/create`, or after Link, by calling `/transactions/get`) before calling this endpoint. Data is available to `/transactions/recurring/get` approximately 5 seconds after the [`HISTORICAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#historical_update) webhook has fired (about 1-2 minutes after initialization).
        
        After the initial call, you can call `/transactions/recurring/get` endpoint at any point in the future to retrieve the latest summary of recurring streams. Since recurring streams do not change often, it will typically not be necessary to call this endpoint more than once per day.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transactions/#transactionsrecurringget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "options": options,
            "account_ids": account_ids,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transactions/recurring/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransactionsRecurringGetResponse.from_json(data)
    async def transactions_sync(self, access_token: model.AccessToken, cursor: Optional[str] = None, count: Optional[int] = None, options: Optional[model.TransactionsSyncRequestOptions] = None) -> model.model.TransactionsSyncResponse:
        """Get incremental transaction updates on an Item
        
        This endpoint replaces `/transactions/get` and its associated webhooks for most common use-cases.
        
        The `/transactions/sync` endpoint allows developers to subscribe to all transactions associated with an Item and get updates synchronously in a stream-like manner, using a cursor to track which updates have already been seen. `/transactions/sync` provides the same functionality as `/transactions/get` and can be used instead of `/transactions/get` to simplify the process of tracking transactions updates.
        
        This endpoint provides user-authorized transaction data for `credit`, `depository`, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). For transaction history from `investments` accounts, use `/investments/transactions/get` instead.
        
        Returned transactions data is grouped into three types of update, indicating whether the transaction was added, removed, or modified since the last call to the API.
        
        In the first call to `/transactions/sync` for an Item, the endpoint will return all historical transactions data associated with that Item up until the time of the API call (as "adds"), which then generates a `next_cursor` for that Item. In subsequent calls, send the `next_cursor` to receive only the changes that have occurred since the previous call.
        
        Due to the potentially large number of transactions associated with an Item, results are paginated. The `has_more` field specifies if additional calls are necessary to fetch all available transaction updates.
        
        Whenever new or updated transaction data becomes available, `/transactions/sync` will provide these updates. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item's `status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, use the `/transactions/refresh` endpoint.
        
        Note that for newly created Items, data may not be immediately available to `/transactions/sync`. Plaid begins preparing transactions data when the Item is created, but the process can take anywhere from a few seconds to several minutes to complete, depending on the number of transactions available.
        
        To be alerted when new data is available, listen for the [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#sync_updates_available) webhook.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transactions/#transactionssync>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "cursor": cursor,
            "count": count,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transactions/sync", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransactionsSyncResponse.from_json(data)
    async def institutions_get(self, count: int, offset: int, country_codes: List[model.CountryCode], options: Optional[model.InstitutionsGetRequestOptions] = None) -> model.model.InstitutionsGetResponse:
        """Get details of all supported institutions
        
        Returns a JSON response containing details on all financial institutions currently supported by Plaid. Because Plaid supports thousands of institutions, results are paginated.
        
        If there is no overlap between an institution’s enabled products and a client’s enabled products, then the institution will be filtered out from the response. As a result, the number of institutions returned may not match the count specified in the call.
        
        See endpoint docs at <https://plaid.com/docs/api/institutions/#institutionsget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "count": count,
            "offset": offset,
            "country_codes": country_codes,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/institutions/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.InstitutionsGetResponse.from_json(data)
    async def institutions_search(self, query: str, products: Optional[Optional[List[model.Products]]] = None, country_codes: List[model.CountryCode], options: Optional[model.InstitutionsSearchRequestOptions] = None) -> model.model.InstitutionsSearchResponse:
        """Search institutions
        
        Returns a JSON response containing details for institutions that match the query parameters, up to a maximum of ten institutions per query.
        
        Versioning note: API versions 2019-05-29 and earlier allow use of the `public_key` parameter instead of the `client_id` and `secret` parameters to authenticate to this endpoint. The `public_key` parameter has since been deprecated; all customers are encouraged to use `client_id` and `secret` instead.
        
        
        See endpoint docs at <https://plaid.com/docs/api/institutions/#institutionssearch>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "query": query,
            "products": products,
            "country_codes": country_codes,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/institutions/search", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.InstitutionsSearchResponse.from_json(data)
    async def institutions_get_by_id(self, institution_id: str, country_codes: List[model.CountryCode], options: Optional[model.InstitutionsGetByIdRequestOptions] = None) -> model.model.InstitutionsGetByIdResponse:
        """Get details of an institution
        
        Returns a JSON response containing details on a specified financial institution currently supported by Plaid.
        
        Versioning note: API versions 2019-05-29 and earlier allow use of the `public_key` parameter instead of the `client_id` and `secret` to authenticate to this endpoint. The `public_key` has been deprecated; all customers are encouraged to use `client_id` and `secret` instead.
        
        
        See endpoint docs at <https://plaid.com/docs/api/institutions/#institutionsget_by_id>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "institution_id": institution_id,
            "country_codes": country_codes,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/institutions/get_by_id", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.InstitutionsGetByIdResponse.from_json(data)
    async def item_remove(self, access_token: model.AccessToken) -> model.model.ItemRemoveResponse:
        """Remove an Item
        
        The `/item/remove` endpoint allows you to remove an Item. Once removed, the `access_token`, as well as any processor tokens or bank account tokens associated with the Item, is no longer valid and cannot be used to access any data that was associated with the Item.
        
        Note that in the Development environment, issuing an `/item/remove`  request will not decrement your live credential count. To increase your credential account in Development, contact Support.
        
        Also note that for certain OAuth-based institutions, an Item removed via `/item/remove` may still show as an active connection in the institution's OAuth permission manager.
        
        API versions 2019-05-29 and earlier return a `removed` boolean as part of the response.
        
        See endpoint docs at <https://plaid.com/docs/api/items/#itemremove>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/item/remove", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ItemRemoveResponse.from_json(data)
    async def accounts_get(self, access_token: model.AccessToken, options: Optional[model.AccountsGetRequestOptions] = None) -> model.model.AccountsGetResponse:
        """Retrieve accounts
        
        The `/accounts/get` endpoint can be used to retrieve a list of accounts associated with any linked Item. Plaid will only return active bank accounts — that is, accounts that are not closed and are capable of carrying a balance.
        For items that went through the updated account selection pane, this endpoint only returns accounts that were permissioned by the user when they initially created the Item. If a user creates a new account after the initial link, you can capture this event through the [`NEW_ACCOUNTS_AVAILABLE`](https://plaid.com/docs/api/items/#new_accounts_available) webhook and then use Link's [update mode](https://plaid.com/docs/link/update-mode/) to request that the user share this new account with you.
        
        This endpoint retrieves cached information, rather than extracting fresh information from the institution. As a result, balances returned may not be up-to-date; for realtime balance information, use `/accounts/balance/get` instead. Note that some information is nullable.
        
        See endpoint docs at <https://plaid.com/docs/api/accounts/#accountsget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/accounts/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AccountsGetResponse.from_json(data)
    async def categories_get(self) -> model.model.CategoriesGetResponse:
        """Get Categories
        
        Send a request to the `/categories/get` endpoint to get detailed information on categories returned by Plaid. This endpoint does not require authentication.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transactions/#categoriesget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/categories/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.CategoriesGetResponse.from_json(data)
    async def sandbox_processor_token_create(self, institution_id: str, options: Optional[model.SandboxProcessorTokenCreateRequestOptions] = None) -> model.model.SandboxProcessorTokenCreateResponse:
        """Create a test Item and processor token
        
        Use the `/sandbox/processor_token/create` endpoint to create a valid `processor_token` for an arbitrary institution ID and test credentials. The created `processor_token` corresponds to a new Sandbox Item. You can then use this `processor_token` with the `/processor/` API endpoints in Sandbox. You can also use `/sandbox/processor_token/create` with the [`user_custom` test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data.
        
        See endpoint docs at <https://plaid.com/docs/api/sandbox/#sandboxprocessor_tokencreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "institution_id": institution_id,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/sandbox/processor_token/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SandboxProcessorTokenCreateResponse.from_json(data)
    async def sandbox_public_token_create(self, institution_id: str, initial_products: List[model.Products], options: Optional[model.SandboxPublicTokenCreateRequestOptions] = None, user_token: Optional[model.UserToken] = None) -> model.model.SandboxPublicTokenCreateResponse:
        """Create a test Item
        
        Use the `/sandbox/public_token/create` endpoint to create a valid `public_token`  for an arbitrary institution ID, initial products, and test credentials. The created `public_token` maps to a new Sandbox Item. You can then call `/item/public_token/exchange` to exchange the `public_token` for an `access_token` and perform all API actions. `/sandbox/public_token/create` can also be used with the [`user_custom` test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data. `/sandbox/public_token/create` cannot be used with OAuth institutions.
        
        See endpoint docs at <https://plaid.com/docs/api/sandbox/#sandboxpublic_tokencreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "institution_id": institution_id,
            "initial_products": initial_products,
            "options": options,
            "user_token": user_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/sandbox/public_token/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SandboxPublicTokenCreateResponse.from_json(data)
    async def sandbox_item_fire_webhook(self, access_token: model.AccessToken, webhook_type: Optional[model.WebhookType] = None, webhook_code: str) -> model.model.SandboxItemFireWebhookResponse:
        """Fire a test webhook
        
        The `/sandbox/item/fire_webhook` endpoint is used to test that code correctly handles webhooks. This endpoint can trigger the following webhooks:
        
        `DEFAULT_UPDATE`: Transactions update webhook to be fired for a given Sandbox Item. If the Item does not support Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.
        
        `NEW_ACCOUNTS_AVAILABLE`: Webhook to be fired for a given Sandbox Item created with Account Select v2.
        
        `AUTH_DATA_UPDATE`: Webhook to be fired for a given Sandbox Item created with Auth as an enabled product.
        
        `RECURRING_TRANSACTIONS_UPDATE`: Recurring Transactions webhook to be fired for a given Sandbox Item. If the Item does not support Recurring Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.
        
        Note that this endpoint is provided for developer ease-of-use and is not required for testing webhooks; webhooks will also fire in Sandbox under the same conditions that they would in Production or Development.
        
        See endpoint docs at <https://plaid.com/docs/api/sandbox/#sandboxitemfire_webhook>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "webhook_type": webhook_type,
            "webhook_code": webhook_code,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/sandbox/item/fire_webhook", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SandboxItemFireWebhookResponse.from_json(data)
    async def accounts_balance_get(self, access_token: model.AccessToken, options: Optional[model.AccountsBalanceGetRequestOptions] = None) -> model.model.AccountsGetResponse:
        """Retrieve real-time balance data
        
        The `/accounts/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/accounts/balance/get` forces the available and current balance fields to be refreshed rather than cached. This endpoint can be used for existing Items that were added via any of Plaid’s other products. This endpoint can be used as long as Link has been initialized with any other product, `balance` itself is not a product that can be used to initialize Link.
        
        See endpoint docs at <https://plaid.com/docs/api/products/balance/#accountsbalanceget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/accounts/balance/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AccountsGetResponse.from_json(data)
    async def identity_get(self, access_token: model.AccessToken, options: Optional[model.IdentityGetRequestOptions] = None) -> model.model.IdentityGetResponse:
        """Retrieve identity data
        
        The `/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses. Only name data is guaranteed to be returned; other fields will be empty arrays if not provided by the institution.
        
        This request may take some time to complete if identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.
        
        Note: In API versions 2018-05-22 and earlier, the `owners` object is not returned, and instead identity information is returned in the top level `identity` object. For more details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2019-05-29).
        
        See endpoint docs at <https://plaid.com/docs/api/products/identity/#identityget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/identity/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.IdentityGetResponse.from_json(data)
    async def identity_match(self, access_token: model.AccessToken, user: Optional[model.IdentityMatchUser] = None, options: Optional[model.IdentityMatchRequestOptions] = None) -> model.model.IdentityMatchResponse:
        """Retrieve identity match score
        
        The `/identity/match` endpoint generates a match score, which indicates how well the provided identity data matches the identity information on file with the account holder's financial institution.
        
        This request may take some time to complete if Identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.
        
        See endpoint docs at <https://plaid.com/docs/api/products/identity/#identitymatch>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "user": user,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/identity/match", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.IdentityMatchResponse.from_json(data)
    async def dashobard_user_get(self, dashboard_user_id: model.DashboardUserId) -> model.model.DashboardUserResponse:
        """Retrieve a dashboard user
        
        Retrieve information about a dashboard user.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#dashboard_userget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "dashboard_user_id": dashboard_user_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/dashboard_user/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.DashboardUserResponse.from_json(data)
    async def dashboard_user_list(self, cursor: Optional[Optional[model.Cursor]] = None) -> model.model.PaginatedDashboardUserListResponse:
        """List dashboard users
        
        List all dashboard users associated with your account.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#dashboard_userlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "cursor": cursor,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/dashboard_user/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaginatedDashboardUserListResponse.from_json(data)
    async def identity_verification_create(self, is_shareable: bool, template_id: model.IdentityVerificationTemplateId, gave_consent: model.IdentityVerificationConsent, user: model.IdentityVerificationRequestUser, is_idempotent: Optional[Optional[model.IdempotencyFlag]] = None) -> model.model.IdentityVerificationResponse:
        """Create a new identity verification
        
        Create a new Identity Verification for the user specified by the `client_user_id` field. The requirements and behavior of the verification are determined by the `template_id` provided.
        If you don't know whether the associated user already has an active Identity Verification, you can specify `"is_idempotent": true` in the request body. With idempotency enabled, a new Identity Verification will only be created if one does not already exist for the associated `client_user_id` and `template_id`. If an Identity Verification is found, it will be returned unmodified with an `200 OK` HTTP status code.
        
        
        See endpoint docs at <https://plaid.com/docs/api/products/identity-verification/#identity_verificationcreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "is_shareable": is_shareable,
            "template_id": template_id,
            "gave_consent": gave_consent,
            "user": user,
            "is_idempotent": is_idempotent,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/identity_verification/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.IdentityVerificationResponse.from_json(data)
    async def identity_verification_get(self, identity_verification_id: model.IdentityVerificationId) -> model.model.IdentityVerificationResponse:
        """Retrieve Identity Verification
        
        Retrieve a previously created identity verification
        
        See endpoint docs at <https://plaid.com/docs/api/products/identity-verification/#identity_verificationget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "identity_verification_id": identity_verification_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/identity_verification/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.IdentityVerificationResponse.from_json(data)
    async def identity_verification_list(self, template_id: model.IdentityVerificationTemplateId, client_user_id: model.ClientUserId, cursor: Optional[Optional[model.Cursor]] = None) -> model.model.PaginatedIdentityVerificationListResponse:
        """List Identity Verifications
        
        Filter and list Identity Verifications created by your account
        
        See endpoint docs at <https://plaid.com/docs/api/products/identity-verification/#identity_verificationlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "template_id": template_id,
            "client_user_id": client_user_id,
            "cursor": cursor,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/identity_verification/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaginatedIdentityVerificationListResponse.from_json(data)
    async def identity_verification_retry(self, client_user_id: model.ClientUserId, template_id: model.IdentityVerificationTemplateId, strategy: model.Strategy, steps: Optional[Optional[model.IdentityVerificationRetryRequestStepsObject]] = None) -> model.model.IdentityVerificationResponse:
        """Retry an Identity Verification
        
        Allow a customer to retry their identity verification
        
        See endpoint docs at <https://plaid.com/docs/api/products/identity-verification/#identity_verificationretry>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "client_user_id": client_user_id,
            "template_id": template_id,
            "strategy": strategy,
            "steps": steps,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/identity_verification/retry", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.IdentityVerificationResponse.from_json(data)
    async def watchlist_screening_entity_create(self, search_terms: model.EntityWatchlistSearchTerms, client_user_id: Optional[Optional[Any]] = None) -> model.model.EntityWatchlistScreeningResponse:
        """Create a watchlist screening for an entity
        
        Create a new entity watchlist screening to check your customer against watchlists defined in the associated entity watchlist program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningentitycreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "search_terms": search_terms,
            "client_user_id": client_user_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/entity/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.EntityWatchlistScreeningResponse.from_json(data)
    async def watchlist_screening_entity_get(self, entity_watchlist_screening_id: model.EntityWatchlistScreeningId) -> model.model.EntityWatchlistScreeningResponse:
        """Get an entity screening
        
        Retrieve an entity watchlist screening.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningentityget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "entity_watchlist_screening_id": entity_watchlist_screening_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/entity/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.EntityWatchlistScreeningResponse.from_json(data)
    async def watchlist_screening_entity_history_list(self, entity_watchlist_screening_id: model.EntityWatchlistScreeningId, cursor: Optional[Optional[model.Cursor]] = None) -> model.model.PaginatedEntityWatchlistScreeningListResponse:
        """List history for entity watchlist screenings
        
        List all changes to the entity watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningentityhistorylist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "entity_watchlist_screening_id": entity_watchlist_screening_id,
            "cursor": cursor,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/entity/history/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaginatedEntityWatchlistScreeningListResponse.from_json(data)
    async def watchlist_screening_entity_hits_list(self, entity_watchlist_screening_id: model.EntityWatchlistScreeningId, cursor: Optional[Optional[model.Cursor]] = None) -> model.model.PaginatedEntityWatchlistScreeningHitListResponse:
        """List hits for entity watchlist screenings
        
        List all hits for the entity watchlist screening.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningentityhitlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "entity_watchlist_screening_id": entity_watchlist_screening_id,
            "cursor": cursor,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/entity/hit/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaginatedEntityWatchlistScreeningHitListResponse.from_json(data)
    async def watchlist_screening_entity_list(self, entity_watchlist_program_id: model.EntityWatchlistProgramId, client_user_id: Optional[Optional[Any]] = None, status: Optional[Optional[Any]] = None, assignee: Optional[Optional[Any]] = None, cursor: Optional[Optional[model.Cursor]] = None) -> model.model.PaginatedEntityWatchlistScreeningListResponse:
        """List entity watchlist screenings
        
        List all entity screenings.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningentitylist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "entity_watchlist_program_id": entity_watchlist_program_id,
            "client_user_id": client_user_id,
            "status": status,
            "assignee": assignee,
            "cursor": cursor,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/entity/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaginatedEntityWatchlistScreeningListResponse.from_json(data)
    async def watchlist_screening_entity_program_get(self, entity_watchlist_program_id: model.EntityWatchlistProgramId) -> model.model.EntityWatchlistProgramResponse:
        """Get entity watchlist screening program
        
        Get an entity watchlist screening program
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningentityprogramget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "entity_watchlist_program_id": entity_watchlist_program_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/entity/program/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.EntityWatchlistProgramResponse.from_json(data)
    async def watchlist_screening_entity_program_list(self, cursor: Optional[Optional[model.Cursor]] = None) -> model.model.PaginatedEntityWatchlistProgramListResponse:
        """List entity watchlist screening programs
        
        List all entity watchlist screening programs
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningentityprogramlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "cursor": cursor,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/entity/program/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaginatedEntityWatchlistProgramListResponse.from_json(data)
    async def watchlist_screening_entity_review_create(self, confirmed_hits: List[model.EntityWatchlistScreeningHitId], dismissed_hits: List[model.EntityWatchlistScreeningHitId], comment: Optional[Optional[model.ReviewComment]] = None, entity_watchlist_screening_id: model.EntityWatchlistScreeningId) -> model.model.EntityWatchlistScreeningReviewResponse:
        """Create a review for an entity watchlist screening
        
        Create a review for an entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningentityreviewcreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "confirmed_hits": confirmed_hits,
            "dismissed_hits": dismissed_hits,
            "comment": comment,
            "entity_watchlist_screening_id": entity_watchlist_screening_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/entity/review/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.EntityWatchlistScreeningReviewResponse.from_json(data)
    async def watchlist_screening_entity_review_list(self, entity_watchlist_screening_id: model.EntityWatchlistScreeningId, cursor: Optional[Optional[model.Cursor]] = None) -> model.model.PaginatedEntityWatchlistScreeningReviewListResponse:
        """List reviews for entity watchlist screenings
        
        List all reviews for a particular entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningentityreviewlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "entity_watchlist_screening_id": entity_watchlist_screening_id,
            "cursor": cursor,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/entity/review/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaginatedEntityWatchlistScreeningReviewListResponse.from_json(data)
    async def watchlist_screening_entity_update(self, entity_watchlist_screening_id: model.EntityWatchlistScreeningId, search_terms: Optional[Optional[model.UpdateEntityScreeningRequestSearchTerms]] = None, assignee: Optional[Optional[Any]] = None, status: Optional[Optional[Any]] = None, client_user_id: Optional[Optional[Any]] = None, reset_fields: Optional[Optional[model.UpdateEntityScreeningRequestResettableFieldList]] = None) -> model.model.EntityWatchlistScreeningResponse:
        """Update an entity screening
        
        Update an entity watchlist screening.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningentityupdate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "entity_watchlist_screening_id": entity_watchlist_screening_id,
            "search_terms": search_terms,
            "assignee": assignee,
            "status": status,
            "client_user_id": client_user_id,
            "reset_fields": reset_fields,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/entity/update", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.EntityWatchlistScreeningResponse.from_json(data)
    async def watchlist_screening_individual_create(self, search_terms: model.WatchlistScreeningRequestSearchTerms, client_user_id: Optional[Optional[Any]] = None) -> model.model.WatchlistScreeningIndividualResponse:
        """Create a watchlist screening for a person
        
        Create a new Watchlist Screening to check your customer against watchlists defined in the associated Watchlist Program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningindividualcreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "search_terms": search_terms,
            "client_user_id": client_user_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/individual/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.WatchlistScreeningIndividualResponse.from_json(data)
    async def watchlist_screening_individual_get(self, watchlist_screening_id: model.WatchlistScreeningIndividualId) -> model.model.WatchlistScreeningIndividualResponse:
        """Retrieve an individual watchlist screening
        
        Retrieve a previously created individual watchlist screening
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningindividualget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "watchlist_screening_id": watchlist_screening_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/individual/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.WatchlistScreeningIndividualResponse.from_json(data)
    async def watchlist_screening_individual_history_list(self, watchlist_screening_id: model.WatchlistScreeningIndividualId, cursor: Optional[Optional[model.Cursor]] = None) -> model.model.PaginatedIndividualWatchlistScreeningListResponse:
        """List history for individual watchlist screenings
        
        List all changes to the individual watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningindividualhistorylist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "watchlist_screening_id": watchlist_screening_id,
            "cursor": cursor,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/individual/history/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaginatedIndividualWatchlistScreeningListResponse.from_json(data)
    async def watchlist_screening_individual_hit_list(self, watchlist_screening_id: model.WatchlistScreeningIndividualId, cursor: Optional[Optional[model.Cursor]] = None) -> model.model.PaginatedIndividualWatchlistScreeningHitListResponse:
        """List hits for individual watchlist screening
        
        List all hits found by Plaid for a particular individual watchlist screening.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningindividualhitlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "watchlist_screening_id": watchlist_screening_id,
            "cursor": cursor,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/individual/hit/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaginatedIndividualWatchlistScreeningHitListResponse.from_json(data)
    async def watchlist_screening_individual_list(self, watchlist_program_id: model.WatchlistProgramId, client_user_id: Optional[Optional[Any]] = None, status: Optional[Optional[Any]] = None, assignee: Optional[Optional[Any]] = None, cursor: Optional[Optional[model.Cursor]] = None) -> model.model.PaginatedIndividualWatchlistScreeningListResponse:
        """List Individual Watchlist Screenings
        
        List previously created watchlist screenings for individuals
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningindividuallist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "watchlist_program_id": watchlist_program_id,
            "client_user_id": client_user_id,
            "status": status,
            "assignee": assignee,
            "cursor": cursor,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/individual/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaginatedIndividualWatchlistScreeningListResponse.from_json(data)
    async def watchlist_screening_individual_program_get(self, watchlist_program_id: model.WatchlistProgramId) -> model.model.IndividualWatchlistProgramResponse:
        """Get individual watchlist screening program
        
        Get an individual watchlist screening program
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningindividualprogramget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "watchlist_program_id": watchlist_program_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/individual/program/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.IndividualWatchlistProgramResponse.from_json(data)
    async def watchlist_screening_individual_program_list(self, cursor: Optional[Optional[model.Cursor]] = None) -> model.model.PaginatedIndividualWatchlistProgramListResponse:
        """List individual watchlist screening programs
        
        List all individual watchlist screening programs
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningindividualprogramlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "cursor": cursor,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/individual/program/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaginatedIndividualWatchlistProgramListResponse.from_json(data)
    async def watchlist_screening_individual_review_create(self, confirmed_hits: List[model.WatchlistScreeningHitId], dismissed_hits: List[model.WatchlistScreeningHitId], comment: Optional[Optional[model.ReviewComment]] = None, watchlist_screening_id: model.WatchlistScreeningIndividualId) -> model.model.WatchlistScreeningReviewResponse:
        """Create a review for an individual watchlist screening
        
        Create a review for the individual watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningindividualreviewcreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "confirmed_hits": confirmed_hits,
            "dismissed_hits": dismissed_hits,
            "comment": comment,
            "watchlist_screening_id": watchlist_screening_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/individual/review/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.WatchlistScreeningReviewResponse.from_json(data)
    async def watchlist_screening_individual_reviews_list(self, watchlist_screening_id: model.WatchlistScreeningIndividualId, cursor: Optional[Optional[model.Cursor]] = None) -> model.model.PaginatedIndividualWatchlistScreeningReviewListResponse:
        """List reviews for individual watchlist screenings
        
        List all reviews for the individual watchlist screening.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningindividualreviewlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "watchlist_screening_id": watchlist_screening_id,
            "cursor": cursor,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/individual/review/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaginatedIndividualWatchlistScreeningReviewListResponse.from_json(data)
    async def watchlist_screening_individual_update(self, watchlist_screening_id: model.WatchlistScreeningIndividualId, search_terms: Optional[Optional[model.UpdateIndividualScreeningRequestSearchTerms]] = None, assignee: Optional[Optional[Any]] = None, status: Optional[Optional[Any]] = None, client_user_id: Optional[Optional[Any]] = None, reset_fields: Optional[Optional[model.UpdateIndividualScreeningRequestResettableFieldList]] = None) -> model.model.WatchlistScreeningIndividualResponse:
        """Update individual watchlist screening
        
        Update a specific individual watchlist screening. This endpoint can be used to add additional customer information, correct outdated information, add a reference id, assign the individual to a reviewer, and update which program it is associated with. Please note that you may not update `search_terms` and `status` at the same time since editing `search_terms` may trigger an automatic `status` change.
        
        See endpoint docs at <https://plaid.com/docs/api/products/monitor/#watchlist_screeningindividualupdate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "watchlist_screening_id": watchlist_screening_id,
            "search_terms": search_terms,
            "assignee": assignee,
            "status": status,
            "client_user_id": client_user_id,
            "reset_fields": reset_fields,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/watchlist_screening/individual/update", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.WatchlistScreeningIndividualResponse.from_json(data)
    async def processor_auth_get(self, processor_token: model.ProcessorToken) -> model.model.ProcessorAuthGetResponse:
        """Retrieve Auth data
        
        The `/processor/auth/get` endpoint returns the bank account and bank identification number (such as the routing number, for US accounts), for a checking or savings account that''s associated with a given `processor_token`. The endpoint also returns high-level account data and balances when available.
        
        Versioning note: API versions 2019-05-29 and earlier use a different schema for the `numbers` object returned by this endpoint. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2020-09-14).
        
        
        See endpoint docs at <https://plaid.com/docs/api/processors/#processorauthget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "processor_token": processor_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/processor/auth/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ProcessorAuthGetResponse.from_json(data)
    async def processor_bank_transfer_create(self, idempotency_key: model.BankTransferIdempotencyKey, processor_token: model.ProcessorToken, type_: model.BankTransferType, network: model.BankTransferNetwork, amount: model.BankTransferAmount, iso_currency_code: str, description: str, ach_class: Optional[model.AchClass] = None, user: model.BankTransferUser, custom_tag: Optional[Optional[str]] = None, metadata: Optional[Optional[model.BankTransferMetadata]] = None, origination_account_id: Optional[Optional[str]] = None) -> model.model.ProcessorBankTransferCreateResponse:
        """Create a bank transfer as a processor
        
        Use the `/processor/bank_transfer/create` endpoint to initiate a new bank transfer as a processor
        
        See endpoint docs at <https://plaid.com/docs/api/processors/#bank_transfercreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "idempotency_key": idempotency_key,
            "processor_token": processor_token,
            "type": type,
            "network": network,
            "amount": amount,
            "iso_currency_code": iso_currency_code,
            "description": description,
            "ach_class": ach_class,
            "user": user,
            "custom_tag": custom_tag,
            "metadata": metadata,
            "origination_account_id": origination_account_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/processor/bank_transfer/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ProcessorBankTransferCreateResponse.from_json(data)
    async def processor_identity_get(self, processor_token: model.ProcessorToken) -> model.model.ProcessorIdentityGetResponse:
        """Retrieve Identity data
        
        The `/processor/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses.
        
        See endpoint docs at <https://plaid.com/docs/api/processors/#processoridentityget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "processor_token": processor_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/processor/identity/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ProcessorIdentityGetResponse.from_json(data)
    async def processor_balance_get(self, processor_token: model.ProcessorToken, options: Optional[model.ProcessorBalanceGetRequestOptions] = None) -> model.model.ProcessorBalanceGetResponse:
        """Retrieve Balance data
        
        The `/processor/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/processor/balance/get` forces the available and current balance fields to be refreshed rather than cached. 
        
        See endpoint docs at <https://plaid.com/docs/api/processors/#processorbalanceget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "processor_token": processor_token,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/processor/balance/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ProcessorBalanceGetResponse.from_json(data)
    async def item_webhook_update(self, access_token: model.AccessToken, webhook: Optional[Optional[str]] = None) -> model.model.ItemWebhookUpdateResponse:
        """Update Webhook URL
        
        The POST `/item/webhook/update` allows you to update the webhook URL associated with an Item. This request triggers a [`WEBHOOK_UPDATE_ACKNOWLEDGED`](https://plaid.com/docs/api/items/#webhook_update_acknowledged) webhook to the newly specified webhook URL.
        
        See endpoint docs at <https://plaid.com/docs/api/items/#itemwebhookupdate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "webhook": webhook,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/item/webhook/update", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ItemWebhookUpdateResponse.from_json(data)
    async def item_access_token_invalidate(self, access_token: model.AccessToken) -> model.model.ItemAccessTokenInvalidateResponse:
        """Invalidate access_token
        
        By default, the `access_token` associated with an Item does not expire and should be stored in a persistent, secure manner.
        
        You can use the `/item/access_token/invalidate` endpoint to rotate the `access_token` associated with an Item. The endpoint returns a new `access_token` and immediately invalidates the previous `access_token`.
        
        
        See endpoint docs at <https://plaid.com/docs/api/tokens/#itemaccess_tokeninvalidate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/item/access_token/invalidate", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ItemAccessTokenInvalidateResponse.from_json(data)
    async def webhook_verification_key_get(self, key_id: str) -> model.model.WebhookVerificationKeyGetResponse:
        """Get webhook verification key
        
        Plaid signs all outgoing webhooks and provides JSON Web Tokens (JWTs) so that you can verify the authenticity of any incoming webhooks to your application. A message signature is included in the `Plaid-Verification` header.
        
        The `/webhook_verification_key/get` endpoint provides a JSON Web Key (JWK) that can be used to verify a JWT.
        
        See endpoint docs at <https://plaid.com/docs/api/webhooks/webhook-verification/#webhook_verification_keyget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "key_id": key_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/webhook_verification_key/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.WebhookVerificationKeyGetResponse.from_json(data)
    async def liabilities_get(self, access_token: model.AccessToken, options: Optional[model.LiabilitiesGetRequestOptions] = None) -> model.model.LiabilitiesGetResponse:
        """Retrieve Liabilities data
        
        The `/liabilities/get` endpoint returns various details about an Item with loan or credit accounts. Liabilities data is available primarily for US financial institutions, with some limited coverage of Canadian institutions. Currently supported account types are account type `credit` with account subtype `credit card` or `paypal`, and account type `loan` with account subtype `student` or `mortgage`. To limit accounts listed in Link to types and subtypes supported by Liabilities, you can use the `account_filters` parameter when [creating a Link token](https://plaid.com/docs/api/tokens/#linktokencreate).
        
        The types of information returned by Liabilities can include balances and due dates, loan terms, and account details such as original loan amount and guarantor. Data is refreshed approximately once per day; the latest data can be retrieved by calling `/liabilities/get`.
        
        Note: This request may take some time to complete if `liabilities` was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the additional data.
        
        See endpoint docs at <https://plaid.com/docs/api/products/liabilities/#liabilitiesget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/liabilities/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.LiabilitiesGetResponse.from_json(data)
    async def payment_initiation_recipient_create(self, name: str, iban: Optional[Optional[str]] = None, bacs: Optional[Optional[model.RecipientBacsNullable]] = None, address: Optional[Optional[model.PaymentInitiationAddress]] = None) -> model.model.PaymentInitiationRecipientCreateResponse:
        """Create payment recipient
        
        Create a payment recipient for payment initiation.  The recipient must be in Europe, within a country that is a member of the Single Euro Payment Area (SEPA).  For a standing order (recurring) payment, the recipient must be in the UK.
        
        The endpoint is idempotent: if a developer has already made a request with the same payment details, Plaid will return the same `recipient_id`.
        
        
        See endpoint docs at <https://plaid.com/docs/api/products/payment-initiation/#payment_initiationrecipientcreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "name": name,
            "iban": iban,
            "bacs": bacs,
            "address": address,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/payment_initiation/recipient/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaymentInitiationRecipientCreateResponse.from_json(data)
    async def payment_initiation_payment_reverse(self, payment_id: str, idempotency_key: model.WalletTransactionIdempotencyKey, reference: str) -> model.model.PaymentInitiationPaymentReverseResponse:
        """Reverse an existing payment
        
        Reverse a previously initiated payment.
        
        A payment can only be reversed once and will be refunded to the original sender's account.
        
        
        See endpoint docs at <https://plaid.com/docs/api/products/payment-initiation/#payment_initiationpaymentreverse>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "payment_id": payment_id,
            "idempotency_key": idempotency_key,
            "reference": reference,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/payment_initiation/payment/reverse", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaymentInitiationPaymentReverseResponse.from_json(data)
    async def payment_initiation_recipient_get(self, recipient_id: str) -> model.model.PaymentInitiationRecipientGetResponse:
        """Get payment recipient
        
        Get details about a payment recipient you have previously created.
        
        See endpoint docs at <https://plaid.com/docs/api/products/payment-initiation/#payment_initiationrecipientget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "recipient_id": recipient_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/payment_initiation/recipient/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaymentInitiationRecipientGetResponse.from_json(data)
    async def payment_initiation_recipient_list(self) -> model.model.PaymentInitiationRecipientListResponse:
        """List payment recipients
        
        The `/payment_initiation/recipient/list` endpoint list the payment recipients that you have previously created.
        
        See endpoint docs at <https://plaid.com/docs/api/products/payment-initiation/#payment_initiationrecipientlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/payment_initiation/recipient/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaymentInitiationRecipientListResponse.from_json(data)
    async def payment_initiation_payment_create(self, recipient_id: str, reference: str, amount: model.PaymentAmount, schedule: Optional[model.ExternalPaymentScheduleRequest] = None, options: Optional[Optional[model.ExternalPaymentOptions]] = None) -> model.model.PaymentInitiationPaymentCreateResponse:
        """Create a payment
        
        After creating a payment recipient, you can use the `/payment_initiation/payment/create` endpoint to create a payment to that recipient.  Payments can be one-time or standing order (recurring) and can be denominated in either EUR or GBP.  If making domestic GBP-denominated payments, your recipient must have been created with BACS numbers. In general, EUR-denominated payments will be sent via SEPA Credit Transfer and GBP-denominated payments will be sent via the Faster Payments network, but the payment network used will be determined by the institution. Payments sent via Faster Payments will typically arrive immediately, while payments sent via SEPA Credit Transfer will typically arrive in one business day.
        
        Standing orders (recurring payments) must be denominated in GBP and can only be sent to recipients in the UK. Once created, standing order payments cannot be modified or canceled via the API. An end user can cancel or modify a standing order directly on their banking application or website, or by contacting the bank. Standing orders will follow the payment rules of the underlying rails (Faster Payments in UK). Payments can be sent Monday to Friday, excluding bank holidays. If the pre-arranged date falls on a weekend or bank holiday, the payment is made on the next working day. It is not possible to guarantee the exact time the payment will reach the recipient’s account, although at least 90% of standing order payments are sent by 6am.
        
        In the Development environment, payments must be below 5 GBP / EUR. For details on any payment limits in Production, contact your Plaid Account Manager.
        
        See endpoint docs at <https://plaid.com/docs/api/products/payment-initiation/#payment_initiationpaymentcreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "recipient_id": recipient_id,
            "reference": reference,
            "amount": amount,
            "schedule": schedule,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/payment_initiation/payment/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaymentInitiationPaymentCreateResponse.from_json(data)
    async def create_payment_token(self, payment_id: str) -> model.model.PaymentInitiationPaymentTokenCreateResponse:
        """Create payment token
        
        The `/payment_initiation/payment/token/create` endpoint has been deprecated. New Plaid customers will be unable to use this endpoint, and existing customers are encouraged to migrate to the newer, `link_token`-based flow. The recommended flow is to provide the `payment_id` to `/link/token/create`, which returns a `link_token` used to initialize Link.
        
        The `/payment_initiation/payment/token/create` is used to create a `payment_token`, which can then be used in Link initialization to enter a payment initiation flow. You can only use a `payment_token` once. If this attempt fails, the end user aborts the flow, or the token expires, you will need to create a new payment token. Creating a new payment token does not require end user input.
        
        See endpoint docs at <https://plaid.com/docs/link/maintain-legacy-integration/#creating-a-payment-token>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "payment_id": payment_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/payment_initiation/payment/token/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaymentInitiationPaymentTokenCreateResponse.from_json(data)
    async def payment_initiation_consent_create(self, recipient_id: str, reference: str, scopes: List[model.PaymentInitiationConsentScope], constraints: model.PaymentInitiationConsentConstraints, options: Optional[Optional[model.ExternalPaymentInitiationConsentOptions]] = None) -> model.model.PaymentInitiationConsentCreateResponse:
        """Create payment consent
        
        The `/payment_initiation/consent/create` endpoint is used to create a payment consent, which can be used to initiate payments on behalf of the user. Payment consents are created with `UNAUTHORISED` status by default and must be authorised by the user before payments can be initiated.
        
        Consents can be limited in time and scope, and have constraints that describe limitations for payments.
        
        See endpoint docs at <https://plaid.com/docs/api/products/payment-initiation/#payment_initiationconsentcreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "recipient_id": recipient_id,
            "reference": reference,
            "scopes": scopes,
            "constraints": constraints,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/payment_initiation/consent/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaymentInitiationConsentCreateResponse.from_json(data)
    async def payment_initiation_consent_get(self, consent_id: str) -> model.model.PaymentInitiationConsentGetResponse:
        """Get payment consent
        
        The `/payment_initiation/consent/get` endpoint can be used to check the status of a payment consent, as well as to receive basic information such as recipient and constraints.
        
        See endpoint docs at <https://plaid.com/docs/api/products/payment-initiation/#payment_initiationconsentget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "consent_id": consent_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/payment_initiation/consent/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaymentInitiationConsentGetResponse.from_json(data)
    async def payment_initiation_consent_revoke(self, consent_id: str) -> model.model.PaymentInitiationConsentRevokeResponse:
        """Revoke payment consent
        
        The `/payment_initiation/consent/revoke` endpoint can be used to revoke the payment consent. Once the consent is revoked, it is not possible to initiate payments using it.
        
        See endpoint docs at <https://plaid.com/docs/api/products/payment-initiation/#payment_initiationconsentrevoke>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "consent_id": consent_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/payment_initiation/consent/revoke", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaymentInitiationConsentRevokeResponse.from_json(data)
    async def payment_initiation_consent_payment_execute(self, consent_id: str, amount: model.PaymentAmount, idempotency_key: model.ConsentPaymentIdempotencyKey) -> model.model.PaymentInitiationConsentPaymentExecuteResponse:
        """Execute a single payment using consent
        
        The `/payment_initiation/consent/payment/execute` endpoint can be used to execute payments using payment consent.
        
        See endpoint docs at <https://plaid.com/docs/api/products/payment-initiation/#payment_initiationconsentpaymentexecute>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "consent_id": consent_id,
            "amount": amount,
            "idempotency_key": idempotency_key,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/payment_initiation/consent/payment/execute", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaymentInitiationConsentPaymentExecuteResponse.from_json(data)
    async def sandbox_item_reset_login(self, access_token: model.AccessToken) -> model.model.SandboxItemResetLoginResponse:
        """Force a Sandbox Item into an error state
        
        `/sandbox/item/reset_login/` forces an Item into an `ITEM_LOGIN_REQUIRED` state in order to simulate an Item whose login is no longer valid. This makes it easy to test Link's [update mode](https://plaid.com/docs/link/update-mode) flow in the Sandbox environment.  After calling `/sandbox/item/reset_login`, You can then use Plaid Link update mode to restore the Item to a good state. An `ITEM_LOGIN_REQUIRED` webhook will also be fired after a call to this endpoint, if one is associated with the Item.
        
        
        In the Sandbox, Items will transition to an `ITEM_LOGIN_REQUIRED` error state automatically after 30 days, even if this endpoint is not called.
        
        See endpoint docs at <https://plaid.com/docs/api/sandbox/#sandboxitemreset_login>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/sandbox/item/reset_login", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SandboxItemResetLoginResponse.from_json(data)
    async def sandbox_item_set_verification_status(self, access_token: model.AccessToken, account_id: str, verification_status: str) -> model.model.SandboxItemSetVerificationStatusResponse:
        """Set verification status for Sandbox account
        
        The `/sandbox/item/set_verification_status` endpoint can be used to change the verification status of an Item in in the Sandbox in order to simulate the Automated Micro-deposit flow.
        
        Note that not all Plaid developer accounts are enabled for micro-deposit based verification by default. Your account must be enabled for this feature in order to test it in Sandbox. To enable this features or check your status, contact your account manager or [submit a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access).
        
        For more information on testing Automated Micro-deposits in Sandbox, see [Auth full coverage testing](https://plaid.com/docs/auth/coverage/testing#).
        
        See endpoint docs at <https://plaid.com/docs/api/sandbox/#sandboxitemset_verification_status>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "account_id": account_id,
            "verification_status": verification_status,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/sandbox/item/set_verification_status", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SandboxItemSetVerificationStatusResponse.from_json(data)
    async def item_public_token_exchange(self, public_token: str) -> model.model.ItemPublicTokenExchangeResponse:
        """Exchange public token for an access token
        
        Exchange a Link `public_token` for an API `access_token`. Link hands off the `public_token` client-side via the `onSuccess` callback once a user has successfully created an Item. The `public_token` is ephemeral and expires after 30 minutes. An `access_token` does not expire, but can be revoked by calling `/item/remove`.
        
        The response also includes an `item_id` that should be stored with the `access_token`. The `item_id` is used to identify an Item in a webhook. The `item_id` can also be retrieved by making an `/item/get` request.
        
        See endpoint docs at <https://plaid.com/docs/api/tokens/#itempublic_tokenexchange>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "public_token": public_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/item/public_token/exchange", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ItemPublicTokenExchangeResponse.from_json(data)
    async def item_create_public_token(self, access_token: model.AccessToken) -> model.model.ItemPublicTokenCreateResponse:
        """Create public token
        
        Note: As of July 2020, the `/item/public_token/create` endpoint is deprecated. Instead, use `/link/token/create` with an `access_token` to create a Link token for use with [update mode](https://plaid.com/docs/link/update-mode).
        
        If you need your user to take action to restore or resolve an error associated with an Item, generate a public token with the `/item/public_token/create` endpoint and then initialize Link with that `public_token`.
        
        A `public_token` is one-time use and expires after 30 minutes. You use a `public_token` to initialize Link in [update mode](https://plaid.com/docs/link/update-mode) for a particular Item. You can generate a `public_token` for an Item even if you did not use Link to create the Item originally.
        
        The `/item/public_token/create` endpoint is **not** used to create your initial `public_token`. If you have not already received an `access_token` for a specific Item, use Link to obtain your `public_token` instead. See the [Quickstart](https://plaid.com/docs/quickstart) for more information.
        
        See endpoint docs at <https://plaid.com/docs/api/tokens/#itempublic_tokencreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/item/public_token/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ItemPublicTokenCreateResponse.from_json(data)
    async def user_create(self, client_user_id: str) -> model.model.UserCreateResponse:
        """Create user
        
        This endpoint should be called for each of your end users before they begin a Plaid income flow. This provides you a single token to access all income data associated with the user. You should only create one per end user.
        
        If you call the endpoint multiple times with the same `client_user_id`, the first creation call will succeed and the rest will fail with an error message indicating that the user has been created for the given `client_user_id`.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#usercreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "client_user_id": client_user_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/user/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.UserCreateResponse.from_json(data)
    async def payment_initiation_payment_get(self, payment_id: str) -> model.model.PaymentInitiationPaymentGetResponse:
        """Get payment details
        
        The `/payment_initiation/payment/get` endpoint can be used to check the status of a payment, as well as to receive basic information such as recipient and payment amount. In the case of standing orders, the `/payment_initiation/payment/get` endpoint will provide information about the status of the overall standing order itself; the API cannot be used to retrieve payment status for individual payments within a standing order.
        
        See endpoint docs at <https://plaid.com/docs/api/products/payment-initiation/#payment_initiationpaymentget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "payment_id": payment_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/payment_initiation/payment/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaymentInitiationPaymentGetResponse.from_json(data)
    async def payment_initiation_payment_list(self, count: Optional[Optional[int]] = None, cursor: Optional[Optional[str]] = None, consent_id: Optional[Optional[str]] = None) -> model.model.PaymentInitiationPaymentListResponse:
        """List payments
        
        The `/payment_initiation/payment/list` endpoint can be used to retrieve all created payments. By default, the 10 most recent payments are returned. You can request more payments and paginate through the results using the optional `count` and `cursor` parameters.
        
        See endpoint docs at <https://plaid.com/docs/api/products/payment-initiation/#payment_initiationpaymentlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "count": count,
            "cursor": cursor,
            "consent_id": consent_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/payment_initiation/payment/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaymentInitiationPaymentListResponse.from_json(data)
    async def asset_report_create(self, access_tokens: List[model.AccessToken], days_requested: int, options: Optional[model.AssetReportCreateRequestOptions] = None) -> model.model.AssetReportCreateResponse:
        """Create an Asset Report
        
        The `/asset_report/create` endpoint initiates the process of creating an Asset Report, which can then be retrieved by passing the `asset_report_token` return value to the `/asset_report/get` or `/asset_report/pdf/get` endpoints.
        
        The Asset Report takes some time to be created and is not available immediately after calling `/asset_report/create`. When the Asset Report is ready to be retrieved using `/asset_report/get` or `/asset_report/pdf/get`, Plaid will fire a `PRODUCT_READY` webhook. For full details of the webhook schema, see [Asset Report webhooks](https://plaid.com/docs/api/products/assets/#webhooks).
        
        The `/asset_report/create` endpoint creates an Asset Report at a moment in time. Asset Reports are immutable. To get an updated Asset Report, use the `/asset_report/refresh` endpoint.
        
        See endpoint docs at <https://plaid.com/docs/api/products/assets/#asset_reportcreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_tokens": access_tokens,
            "days_requested": days_requested,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/asset_report/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AssetReportCreateResponse.from_json(data)
    async def asset_report_refresh(self, asset_report_token: model.AssetReportRefreshAssetReportToken, days_requested: Optional[Optional[int]] = None, options: Optional[model.AssetReportRefreshRequestOptions] = None) -> model.model.AssetReportRefreshResponse:
        """Refresh an Asset Report
        
        An Asset Report is an immutable snapshot of a user's assets. In order to "refresh" an Asset Report you created previously, you can use the `/asset_report/refresh` endpoint to create a new Asset Report based on the old one, but with the most recent data available.
        
        The new Asset Report will contain the same Items as the original Report, as well as the same filters applied by any call to `/asset_report/filter`. By default, the new Asset Report will also use the same parameters you submitted with your original `/asset_report/create` request, but the original `days_requested` value and the values of any parameters in the `options` object can be overridden with new values. To change these arguments, simply supply new values for them in your request to `/asset_report/refresh`. Submit an empty string ("") for any previously-populated fields you would like set as empty.
        
        See endpoint docs at <https://plaid.com/docs/api/products/assets/#asset_reportrefresh>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "asset_report_token": asset_report_token,
            "days_requested": days_requested,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/asset_report/refresh", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AssetReportRefreshResponse.from_json(data)
    async def asset_report_relay_refresh(self, asset_relay_token: str, webhook: Optional[Optional[str]] = None) -> model.model.AssetReportRelayRefreshResponse:
        """Refresh a Relay Token's Asset Report
        
        The `/asset_report/relay/refresh` endpoint allows third parties to refresh an Asset Report that was relayed to them, using an `asset_relay_token` that was created by the report owner. A new Asset Report will be created based on the old one, but with the most recent data available.
        
        See endpoint docs at <https://plaid.com/docs/api/products/#asset_reportrelayrefresh>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "asset_relay_token": asset_relay_token,
            "webhook": webhook,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/asset_report/relay/refresh", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AssetReportRelayRefreshResponse.from_json(data)
    async def asset_report_remove(self, asset_report_token: model.AssetReportToken) -> model.model.AssetReportRemoveResponse:
        """Delete an Asset Report
        
        The `/item/remove` endpoint allows you to invalidate an `access_token`, meaning you will not be able to create new Asset Reports with it. Removing an Item does not affect any Asset Reports or Audit Copies you have already created, which will remain accessible until you remove them specifically.
        
        The `/asset_report/remove` endpoint allows you to remove an Asset Report. Removing an Asset Report invalidates its `asset_report_token`, meaning you will no longer be able to use it to access Report data or create new Audit Copies. Removing an Asset Report does not affect the underlying Items, but does invalidate any `audit_copy_tokens` associated with the Asset Report.
        
        See endpoint docs at <https://plaid.com/docs/api/products/assets/#asset_reportremove>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "asset_report_token": asset_report_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/asset_report/remove", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AssetReportRemoveResponse.from_json(data)
    async def asset_report_filter(self, asset_report_token: model.AssetReportToken, account_ids_to_exclude: List[str]) -> model.model.AssetReportFilterResponse:
        """Filter Asset Report
        
        By default, an Asset Report will contain all of the accounts on a given Item. In some cases, you may not want the Asset Report to contain all accounts. For example, you might have the end user choose which accounts are relevant in Link using the Account Select view, which you can enable in the dashboard. Or, you might always exclude certain account types or subtypes, which you can identify by using the `/accounts/get` endpoint. To narrow an Asset Report to only a subset of accounts, use the `/asset_report/filter` endpoint.
        
        To exclude certain Accounts from an Asset Report, first use the `/asset_report/create` endpoint to create the report, then send the `asset_report_token` along with a list of `account_ids` to exclude to the `/asset_report/filter` endpoint, to create a new Asset Report which contains only a subset of the original Asset Report's data.
        
        Because Asset Reports are immutable, calling `/asset_report/filter` does not alter the original Asset Report in any way; rather, `/asset_report/filter` creates a new Asset Report with a new token and id. Asset Reports created via `/asset_report/filter` do not contain new Asset data, and are not billed.
        
        Plaid will fire a [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook once generation of the filtered Asset Report has completed.
        
        See endpoint docs at <https://plaid.com/docs/api/products/assets/#asset_reportfilter>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "asset_report_token": asset_report_token,
            "account_ids_to_exclude": account_ids_to_exclude,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/asset_report/filter", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AssetReportFilterResponse.from_json(data)
    async def asset_report_get(self, asset_report_token: model.AssetReportToken, include_insights: Optional[bool] = None, fast_report: Optional[bool] = None) -> model.model.AssetReportGetResponse:
        """Retrieve an Asset Report
        
        The `/asset_report/get` endpoint retrieves the Asset Report in JSON format. Before calling `/asset_report/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.
        
        By default, an Asset Report includes transaction descriptions as returned by the bank, as opposed to parsed and categorized by Plaid. You can also receive cleaned and categorized transactions, as well as additional insights like merchant name or location information. We call this an Asset Report with Insights. An Asset Report with Insights provides transaction category, location, and merchant information in addition to the transaction strings provided in a standard Asset Report.
        
        To retrieve an Asset Report with Insights, call the `/asset_report/get` endpoint with `include_insights` set to `true`.
        
        See endpoint docs at <https://plaid.com/docs/api/products/assets/#asset_reportget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "asset_report_token": asset_report_token,
            "include_insights": include_insights,
            "fast_report": fast_report,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/asset_report/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AssetReportGetResponse.from_json(data)
    async def asset_report_pdf_get(self, asset_report_token: model.AssetReportToken) -> None:
        """Retrieve a PDF Asset Report
        
        The `/asset_report/pdf/get` endpoint retrieves the Asset Report in PDF format. Before calling `/asset_report/pdf/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.
        
        The response to `/asset_report/pdf/get` is the PDF binary data. The `request_id`  is returned in the `Plaid-Request-ID` header.
        
        [View a sample PDF Asset Report](https://plaid.com/documents/sample-asset-report.pdf).
        
        See endpoint docs at <https://plaid.com/docs/api/products/assets/#asset_reportpdfget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "asset_report_token": asset_report_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/asset_report/pdf/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
    async def asset_report_audit_copy_create(self, asset_report_token: model.AssetReportToken, auditor_id: str) -> model.model.AssetReportAuditCopyCreateResponse:
        """Create Asset Report Audit Copy
        
        Plaid can provide an Audit Copy of any Asset Report directly to a participating third party on your behalf. For example, Plaid can supply an Audit Copy directly to Fannie Mae on your behalf if you participate in the Day 1 Certainty™ program. An Audit Copy contains the same underlying data as the Asset Report.
        
        To grant access to an Audit Copy, use the `/asset_report/audit_copy/create` endpoint to create an `audit_copy_token` and then pass that token to the third party who needs access. Each third party has its own `auditor_id`, for example `fannie_mae`. You’ll need to create a separate Audit Copy for each third party to whom you want to grant access to the Report.
        
        See endpoint docs at <https://plaid.com/docs/api/products/assets/#asset_reportaudit_copycreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "asset_report_token": asset_report_token,
            "auditor_id": auditor_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/asset_report/audit_copy/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AssetReportAuditCopyCreateResponse.from_json(data)
    async def asset_report_audit_copy_remove(self, audit_copy_token: str) -> model.model.AssetReportAuditCopyRemoveResponse:
        """Remove Asset Report Audit Copy
        
        The `/asset_report/audit_copy/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Asset Report, the Asset Report itself and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.
        
        See endpoint docs at <https://plaid.com/docs/api/products/assets/#asset_reportaudit_copyremove>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "audit_copy_token": audit_copy_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/asset_report/audit_copy/remove", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AssetReportAuditCopyRemoveResponse.from_json(data)
    async def asset_report_relay_create(self, asset_report_token: model.AssetReportToken, secondary_client_id: str, webhook: Optional[Optional[str]] = None) -> model.model.AssetReportRelayCreateResponse:
        """Create an `asset_relay_token` to share an Asset Report with a partner client
        
        Plaid can share an Asset Report directly with a participating third party on your behalf. The shared Asset Report is the exact same Asset Report originally created in `/asset_report/create`.
        
        To grant access to an Asset Report to a third party, use the `/asset_report/relay/create` endpoint to create an `asset_relay_token` and then pass that token to the third party who needs access. Each third party has its own `secondary_client_id`, for example `ce5bd328dcd34123456`. You'll need to create a separate `asset_relay_token` for each third party to whom you want to grant access to the Report.
        
        See endpoint docs at <https://plaid.com/docs/none/>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "asset_report_token": asset_report_token,
            "secondary_client_id": secondary_client_id,
            "webhook": webhook,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/asset_report/relay/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AssetReportRelayCreateResponse.from_json(data)
    async def asset_report_relay_get(self, asset_relay_token: str) -> model.model.AssetReportGetResponse:
        """Retrieve an Asset Report that was shared with you
        
        `/asset_report/relay/get` allows third parties to get an Asset Report that was shared with them, using an `asset_relay_token` that was created by the report owner.
        
        See endpoint docs at <https://plaid.com/docs/none/>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "asset_relay_token": asset_relay_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/asset_report/relay/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AssetReportGetResponse.from_json(data)
    async def asset_report_relay_remove(self, asset_relay_token: str) -> model.model.AssetReportRelayRemoveResponse:
        """Remove Asset Report Relay Token
        
        The `/asset_report/relay/remove` endpoint allows you to invalidate an `asset_relay_token`, meaning the third party holding the token will no longer be able to use it to access the Asset Report to which the `asset_relay_token` gives access to. The Asset Report, Items associated with it, and other Asset Relay Tokens that provide access to the same Asset Report are not affected and will remain accessible after removing the given `asset_relay_token.
        
        See endpoint docs at <https://plaid.com/docs/none/>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "asset_relay_token": asset_relay_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/asset_report/relay/remove", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AssetReportRelayRemoveResponse.from_json(data)
    async def investments_holdings_get(self, access_token: model.AccessToken, options: Optional[model.InvestmentHoldingsGetRequestOptions] = None) -> model.model.InvestmentsHoldingsGetResponse:
        """Get Investment holdings
        
        The `/investments/holdings/get` endpoint allows developers to receive user-authorized stock position data for `investment`-type accounts.
        
        See endpoint docs at <https://plaid.com/docs/api/products/investments/#investmentsholdingsget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/investments/holdings/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.InvestmentsHoldingsGetResponse.from_json(data)
    async def investments_transactions_get(self, access_token: model.AccessToken, start_date: str, end_date: str, options: Optional[model.InvestmentsTransactionsGetRequestOptions] = None) -> model.model.InvestmentsTransactionsGetResponse:
        """Get investment transactions
        
        The `/investments/transactions/get` endpoint allows developers to retrieve up to 24 months of user-authorized transaction data for investment accounts.
        
        Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.
        
        Due to the potentially large number of investment transactions associated with an Item, results are paginated. Manipulate the count and offset parameters in conjunction with the `total_investment_transactions` response body field to fetch all available investment transactions.
        
        See endpoint docs at <https://plaid.com/docs/api/products/investments/#investmentstransactionsget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "start_date": start_date,
            "end_date": end_date,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/investments/transactions/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.InvestmentsTransactionsGetResponse.from_json(data)
    async def processor_token_create(self, access_token: model.AccessToken, account_id: str, processor: str) -> model.model.ProcessorTokenCreateResponse:
        """Create processor token
        
        Used to create a token suitable for sending to one of Plaid's partners to enable integrations. Note that Stripe partnerships use bank account tokens instead; see `/processor/stripe/bank_account_token/create` for creating tokens for use with Stripe integrations. Processor tokens can also be revoked, using `/item/remove`.
        
        See endpoint docs at <https://plaid.com/docs/api/processors/#processortokencreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "account_id": account_id,
            "processor": processor,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/processor/token/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ProcessorTokenCreateResponse.from_json(data)
    async def processor_stripe_bank_account_token_create(self, access_token: model.AccessToken, account_id: str) -> model.model.ProcessorStripeBankAccountTokenCreateResponse:
        """Create Stripe bank account token
        
        Used to create a token suitable for sending to Stripe to enable Plaid-Stripe integrations. For a detailed guide on integrating Stripe, see [Add Stripe to your app](https://plaid.com/docs/auth/partnerships/stripe/). Bank account tokens can also be revoked, using `/item/remove`.
        
        See endpoint docs at <https://plaid.com/docs/api/processors/#processorstripebank_account_tokencreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "account_id": account_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/processor/stripe/bank_account_token/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ProcessorStripeBankAccountTokenCreateResponse.from_json(data)
    async def processor_apex_processor_token_create(self, access_token: model.AccessToken, account_id: str) -> model.model.ProcessorTokenCreateResponse:
        """Create Apex bank account token
        
        Used to create a token suitable for sending to Apex to enable Plaid-Apex integrations.
        
        See endpoint docs at <https://plaid.com/docs/none/>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "account_id": account_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/processor/apex/processor_token/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ProcessorTokenCreateResponse.from_json(data)
    async def deposit_switch_create(self, target_access_token: str, target_account_id: str, country_code: Optional[Optional[str]] = None, options: Optional[model.DepositSwitchCreateRequestOptions] = None) -> model.model.DepositSwitchCreateResponse:
        """Create a deposit switch
        
        This endpoint creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.
        
        See endpoint docs at <https://plaid.com/docs/deposit-switch/reference#deposit_switchcreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "target_access_token": target_access_token,
            "target_account_id": target_account_id,
            "country_code": country_code,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/deposit_switch/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.DepositSwitchCreateResponse.from_json(data)
    async def item_import(self, products: List[model.Products], user_auth: model.ItemImportRequestUserAuth, options: Optional[model.ItemImportRequestOptions] = None) -> model.model.ItemImportResponse:
        """Import Item
        
        `/item/import` creates an Item via your Plaid Exchange Integration and returns an `access_token`. As part of an `/item/import` request, you will include a User ID (`user_auth.user_id`) and Authentication Token (`user_auth.auth_token`) that enable data aggregation through your Plaid Exchange API endpoints. These authentication principals are to be chosen by you.
        
        Upon creating an Item via `/item/import`, Plaid will automatically begin an extraction of that Item through the Plaid Exchange infrastructure you have already integrated. This will automatically generate the Plaid native account ID for the account the user will switch their direct deposit to (`target_account_id`).
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "products": products,
            "user_auth": user_auth,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/item/import", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.ItemImportResponse.from_json(data)
    async def deposit_switch_token_create(self, deposit_switch_id: str) -> model.model.DepositSwitchTokenCreateResponse:
        """Create a deposit switch token
        
        In order for the end user to take action, you will need to create a public token representing the deposit switch. This token is used to initialize Link. It can be used one time and expires after 30 minutes.
        
        
        See endpoint docs at <https://plaid.com/docs/deposit-switch/reference#deposit_switchtokencreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "deposit_switch_id": deposit_switch_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/deposit_switch/token/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.DepositSwitchTokenCreateResponse.from_json(data)
    async def link_token_create(self, client_name: str, language: str, country_codes: List[model.CountryCode], user: model.LinkTokenCreateRequestUser, products: Optional[List[model.Products]] = None, additional_consented_products: Optional[List[model.Products]] = None, webhook: Optional[str] = None, access_token: Optional[str] = None, link_customization_name: Optional[str] = None, redirect_uri: Optional[str] = None, android_package_name: Optional[str] = None, institution_data: Optional[model.LinkTokenCreateInstitutionData] = None, account_filters: Optional[model.LinkTokenAccountFilters] = None, eu_config: Optional[model.LinkTokenEuConfig] = None, institution_id: Optional[str] = None, payment_initiation: Optional[model.LinkTokenCreateRequestPaymentInitiation] = None, deposit_switch: Optional[model.LinkTokenCreateRequestDepositSwitch] = None, income_verification: Optional[model.LinkTokenCreateRequestIncomeVerification] = None, auth: Optional[model.LinkTokenCreateRequestAuth] = None, transfer: Optional[model.LinkTokenCreateRequestTransfer] = None, update: Optional[model.LinkTokenCreateRequestUpdate] = None, identity_verification: Optional[model.LinkTokenCreateRequestIdentityVerification] = None, user_token: Optional[str] = None) -> model.model.LinkTokenCreateResponse:
        """Create Link Token
        
        The `/link/token/create` endpoint creates a `link_token`, which is required as a parameter when initializing Link. Once Link has been initialized, it returns a `public_token`, which can then be exchanged for an `access_token` via `/item/public_token/exchange` as part of the main Link flow.
        
        A `link_token` generated by `/link/token/create` is also used to initialize other Link flows, such as the update mode flow for tokens with expired credentials, or the Payment Initiation (Europe) flow.
        
        See endpoint docs at <https://plaid.com/docs/api/tokens/#linktokencreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "client_name": client_name,
            "language": language,
            "country_codes": country_codes,
            "user": user,
            "products": products,
            "additional_consented_products": additional_consented_products,
            "webhook": webhook,
            "access_token": access_token,
            "link_customization_name": link_customization_name,
            "redirect_uri": redirect_uri,
            "android_package_name": android_package_name,
            "institution_data": institution_data,
            "account_filters": account_filters,
            "eu_config": eu_config,
            "institution_id": institution_id,
            "payment_initiation": payment_initiation,
            "deposit_switch": deposit_switch,
            "income_verification": income_verification,
            "auth": auth,
            "transfer": transfer,
            "update": update,
            "identity_verification": identity_verification,
            "user_token": user_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/link/token/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.LinkTokenCreateResponse.from_json(data)
    async def link_token_get(self, link_token: str) -> model.model.LinkTokenGetResponse:
        """Get Link Token
        
        The `/link/token/get` endpoint gets information about a previously-created `link_token` using the
        `/link/token/create` endpoint. It can be useful for debugging purposes.
        
        See endpoint docs at <https://plaid.com/docs/api/tokens/#linktokenget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "link_token": link_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/link/token/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.LinkTokenGetResponse.from_json(data)
    async def asset_report_audit_copy_get(self, audit_copy_token: str) -> model.model.AssetReportGetResponse:
        """Retrieve an Asset Report Audit Copy
        
        `/asset_report/audit_copy/get` allows auditors to get a copy of an Asset Report that was previously shared via the `/asset_report/audit_copy/create` endpoint.  The caller of `/asset_report/audit_copy/create` must provide the `audit_copy_token` to the auditor.  This token can then be used to call `/asset_report/audit_copy/create`.
        
        See endpoint docs at <https://plaid.com/docs/none/>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "audit_copy_token": audit_copy_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/asset_report/audit_copy/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AssetReportGetResponse.from_json(data)
    async def deposit_switch_get(self, deposit_switch_id: str) -> model.model.DepositSwitchGetResponse:
        """Retrieve a deposit switch
        
        This endpoint returns information related to how the user has configured their payroll allocation and the state of the switch. You can use this information to build logic related to the user's direct deposit allocation preferences.
        
        See endpoint docs at <https://plaid.com/docs/deposit-switch/reference#deposit_switchget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "deposit_switch_id": deposit_switch_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/deposit_switch/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.DepositSwitchGetResponse.from_json(data)
    async def transfer_get(self, transfer_id: model.TransferId) -> model.model.TransferGetResponse:
        """Retrieve a transfer
        
        The `/transfer/get` fetches information about the transfer corresponding to the given `transfer_id`.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#transferget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "transfer_id": transfer_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transfer/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransferGetResponse.from_json(data)
    async def bank_transfer_get(self, bank_transfer_id: model.BankTransferId) -> model.model.BankTransferGetResponse:
        """Retrieve a bank transfer
        
        The `/bank_transfer/get` fetches information about the bank transfer corresponding to the given `bank_transfer_id`.
        
        See endpoint docs at <https://plaid.com/docs/bank-transfers/reference#bank_transferget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "bank_transfer_id": bank_transfer_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/bank_transfer/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.BankTransferGetResponse.from_json(data)
    async def transfer_authorization_create(self, access_token: Optional[model.TransferAccessToken] = None, account_id: Optional[str] = None, type_: model.TransferType, network: model.TransferNetwork, amount: model.TransferAmount, ach_class: model.AchClass, user: model.TransferAuthorizationUserInRequest, device: Optional[model.TransferAuthorizationDevice] = None, origination_account_id: Optional[str] = None, iso_currency_code: Optional[str] = None, user_present: Optional[Optional[bool]] = None, payment_profile_id: Optional[model.PaymentProfileId] = None) -> model.model.TransferAuthorizationCreateResponse:
        """Create a transfer authorization
        
        Use the `/transfer/authorization/create` endpoint to determine transfer failure risk.
        
        In Plaid's sandbox environment the decisions will be returned as follows:
        
          - To approve a transfer with null rationale code, make an authorization request with an `amount` less than the available balance in the account.
        
          - To approve a transfer with the rationale code `MANUALLY_VERIFIED_ITEM`, create an Item in Link through the [Same Day Micro-deposits flow](https://plaid.com/docs/auth/coverage/testing/#testing-same-day-micro-deposits).
        
          - To approve a transfer with the rationale code `LOGIN_REQUIRED`, [reset the login for an Item](https://plaid.com/docs/sandbox/#item_login_required).
        
          - To decline a transfer with the rationale code `NSF`, the available balance on the account must be less than the authorization `amount`. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.
        
          - To decline a transfer with the rationale code `RISK`, the available balance on the account must be exactly $0. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.
        
        For guaranteed ACH customers, the following fields are required : `user.phone_number` (optional if `email_address` provided), `user.email_address` (optional if `phone_number` provided), `device.ip_address`, `device.user_agent`, and `user_present`.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#transferauthorizationcreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "account_id": account_id,
            "type": type,
            "network": network,
            "amount": amount,
            "ach_class": ach_class,
            "user": user,
            "device": device,
            "origination_account_id": origination_account_id,
            "iso_currency_code": iso_currency_code,
            "user_present": user_present,
            "payment_profile_id": payment_profile_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transfer/authorization/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransferAuthorizationCreateResponse.from_json(data)
    async def transfer_create(self, idempotency_key: Optional[model.TransferCreateIdempotencyKey] = None, access_token: Optional[model.TransferAccessToken] = None, account_id: Optional[str] = None, authorization_id: str, type_: model.TransferType, network: model.TransferNetwork, amount: model.TransferAmount, description: str, ach_class: model.AchClass, user: model.TransferUserInRequest, metadata: Optional[Optional[model.TransferMetadata]] = None, origination_account_id: Optional[Optional[str]] = None, iso_currency_code: Optional[str] = None, payment_profile_id: Optional[model.PaymentProfileId] = None) -> model.model.TransferCreateResponse:
        """Create a transfer
        
        Use the `/transfer/create` endpoint to initiate a new transfer.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#transfercreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "idempotency_key": idempotency_key,
            "access_token": access_token,
            "account_id": account_id,
            "authorization_id": authorization_id,
            "type": type,
            "network": network,
            "amount": amount,
            "description": description,
            "ach_class": ach_class,
            "user": user,
            "metadata": metadata,
            "origination_account_id": origination_account_id,
            "iso_currency_code": iso_currency_code,
            "payment_profile_id": payment_profile_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transfer/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransferCreateResponse.from_json(data)
    async def bank_transfer_create(self, idempotency_key: model.BankTransferIdempotencyKey, access_token: model.BankTransferAccessToken, account_id: str, type_: model.BankTransferType, network: model.BankTransferNetwork, amount: model.BankTransferAmount, iso_currency_code: str, description: str, ach_class: Optional[model.AchClass] = None, user: model.BankTransferUser, custom_tag: Optional[Optional[str]] = None, metadata: Optional[Optional[model.BankTransferMetadata]] = None, origination_account_id: Optional[Optional[str]] = None) -> model.model.BankTransferCreateResponse:
        """Create a bank transfer
        
        Use the `/bank_transfer/create` endpoint to initiate a new bank transfer.
        
        See endpoint docs at <https://plaid.com/docs/bank-transfers/reference#bank_transfercreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "idempotency_key": idempotency_key,
            "access_token": access_token,
            "account_id": account_id,
            "type": type,
            "network": network,
            "amount": amount,
            "iso_currency_code": iso_currency_code,
            "description": description,
            "ach_class": ach_class,
            "user": user,
            "custom_tag": custom_tag,
            "metadata": metadata,
            "origination_account_id": origination_account_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/bank_transfer/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.BankTransferCreateResponse.from_json(data)
    async def transfer_list(self, start_date: Optional[Optional[str]] = None, end_date: Optional[Optional[str]] = None, count: Optional[int] = None, offset: Optional[int] = None, origination_account_id: Optional[Optional[str]] = None) -> model.model.TransferListResponse:
        """List transfers
        
        Use the `/transfer/list` endpoint to see a list of all your transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired transfers.
        
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#transferlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "start_date": start_date,
            "end_date": end_date,
            "count": count,
            "offset": offset,
            "origination_account_id": origination_account_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transfer/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransferListResponse.from_json(data)
    async def bank_transfer_list(self, start_date: Optional[Optional[str]] = None, end_date: Optional[Optional[str]] = None, count: Optional[int] = None, offset: Optional[int] = None, origination_account_id: Optional[Optional[str]] = None, direction: Optional[Optional[model.BankTransferDirection]] = None) -> model.model.BankTransferListResponse:
        """List bank transfers
        
        Use the `/bank_transfer/list` endpoint to see a list of all your bank transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired bank transfers.
        
        
        See endpoint docs at <https://plaid.com/docs/bank-transfers/reference#bank_transferlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "start_date": start_date,
            "end_date": end_date,
            "count": count,
            "offset": offset,
            "origination_account_id": origination_account_id,
            "direction": direction,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/bank_transfer/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.BankTransferListResponse.from_json(data)
    async def transfer_cancel(self, transfer_id: model.TransferId) -> model.model.TransferCancelResponse:
        """Cancel a transfer
        
        Use the `/transfer/cancel` endpoint to cancel a transfer.  A transfer is eligible for cancelation if the `cancellable` property returned by `/transfer/get` is `true`.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#transfercancel>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "transfer_id": transfer_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transfer/cancel", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransferCancelResponse.from_json(data)
    async def bank_transfer_cancel(self, bank_transfer_id: model.BankTransferId) -> model.model.BankTransferCancelResponse:
        """Cancel a bank transfer
        
        Use the `/bank_transfer/cancel` endpoint to cancel a bank transfer.  A transfer is eligible for cancelation if the `cancellable` property returned by `/bank_transfer/get` is `true`.
        
        See endpoint docs at <https://plaid.com/docs/bank-transfers/reference#bank_transfercancel>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "bank_transfer_id": bank_transfer_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/bank_transfer/cancel", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.BankTransferCancelResponse.from_json(data)
    async def transfer_event_list(self, start_date: Optional[Optional[str]] = None, end_date: Optional[Optional[str]] = None, transfer_id: Optional[Optional[str]] = None, account_id: Optional[Optional[str]] = None, transfer_type: Optional[Optional[model.TransferEventListTransferType]] = None, event_types: Optional[List[model.TransferEventType]] = None, sweep_id: Optional[str] = None, count: Optional[Optional[int]] = None, offset: Optional[Optional[int]] = None, origination_account_id: Optional[Optional[str]] = None) -> model.model.TransferEventListResponse:
        """List transfer events
        
        Use the `/transfer/event/list` endpoint to get a list of transfer events based on specified filter criteria.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#transfereventlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "start_date": start_date,
            "end_date": end_date,
            "transfer_id": transfer_id,
            "account_id": account_id,
            "transfer_type": transfer_type,
            "event_types": event_types,
            "sweep_id": sweep_id,
            "count": count,
            "offset": offset,
            "origination_account_id": origination_account_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transfer/event/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransferEventListResponse.from_json(data)
    async def bank_transfer_event_list(self, start_date: Optional[Optional[str]] = None, end_date: Optional[Optional[str]] = None, bank_transfer_id: Optional[Optional[str]] = None, account_id: Optional[Optional[str]] = None, bank_transfer_type: Optional[Optional[model.BankTransferEventListBankTransferType]] = None, event_types: Optional[List[model.BankTransferEventType]] = None, count: Optional[Optional[int]] = None, offset: Optional[Optional[int]] = None, origination_account_id: Optional[Optional[str]] = None, direction: Optional[Optional[model.BankTransferEventListDirection]] = None) -> model.model.BankTransferEventListResponse:
        """List bank transfer events
        
        Use the `/bank_transfer/event/list` endpoint to get a list of bank transfer events based on specified filter criteria.
        
        See endpoint docs at <https://plaid.com/docs/bank-transfers/reference#bank_transfereventlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "start_date": start_date,
            "end_date": end_date,
            "bank_transfer_id": bank_transfer_id,
            "account_id": account_id,
            "bank_transfer_type": bank_transfer_type,
            "event_types": event_types,
            "count": count,
            "offset": offset,
            "origination_account_id": origination_account_id,
            "direction": direction,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/bank_transfer/event/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.BankTransferEventListResponse.from_json(data)
    async def transfer_event_sync(self, after_id: int, count: Optional[Optional[int]] = None) -> model.model.TransferEventSyncResponse:
        """Sync transfer events
        
        `/transfer/event/sync` allows you to request up to the next 25 transfer events that happened after a specific `event_id`. Use the `/transfer/event/sync` endpoint to guarantee you have seen all transfer events.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#transfereventsync>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "after_id": after_id,
            "count": count,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transfer/event/sync", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransferEventSyncResponse.from_json(data)
    async def bank_transfer_event_sync(self, after_id: int, count: Optional[Optional[int]] = None) -> model.model.BankTransferEventSyncResponse:
        """Sync bank transfer events
        
        `/bank_transfer/event/sync` allows you to request up to the next 25 bank transfer events that happened after a specific `event_id`. Use the `/bank_transfer/event/sync` endpoint to guarantee you have seen all bank transfer events.
        
        See endpoint docs at <https://plaid.com/docs/bank-transfers/reference#bank_transfereventsync>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "after_id": after_id,
            "count": count,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/bank_transfer/event/sync", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.BankTransferEventSyncResponse.from_json(data)
    async def transfer_sweep_get(self, sweep_id: str) -> model.model.TransferSweepGetResponse:
        """Retrieve a sweep
        
        The `/transfer/sweep/get` endpoint fetches a sweep corresponding to the given `sweep_id`.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#transfersweepget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "sweep_id": sweep_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transfer/sweep/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransferSweepGetResponse.from_json(data)
    async def bank_transfer_sweep_get(self, sweep_id: str) -> model.model.BankTransferSweepGetResponse:
        """Retrieve a sweep
        
        The `/bank_transfer/sweep/get` endpoint fetches information about the sweep corresponding to the given `sweep_id`.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#bank_transfersweepget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "sweep_id": sweep_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/bank_transfer/sweep/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.BankTransferSweepGetResponse.from_json(data)
    async def transfer_sweep_list(self, start_date: Optional[Optional[str]] = None, end_date: Optional[Optional[str]] = None, count: Optional[Optional[int]] = None, offset: Optional[int] = None) -> model.model.TransferSweepListResponse:
        """List sweeps
        
        The `/transfer/sweep/list` endpoint fetches sweeps matching the given filters.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#transfersweeplist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "start_date": start_date,
            "end_date": end_date,
            "count": count,
            "offset": offset,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transfer/sweep/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransferSweepListResponse.from_json(data)
    async def bank_transfer_sweep_list(self, origination_account_id: Optional[Optional[str]] = None, start_time: Optional[Optional[str]] = None, end_time: Optional[Optional[str]] = None, count: Optional[Optional[int]] = None) -> model.model.BankTransferSweepListResponse:
        """List sweeps
        
        The `/bank_transfer/sweep/list` endpoint fetches information about the sweeps matching the given filters.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#bank_transfersweeplist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "origination_account_id": origination_account_id,
            "start_time": start_time,
            "end_time": end_time,
            "count": count,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/bank_transfer/sweep/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.BankTransferSweepListResponse.from_json(data)
    async def bank_transfer_balance_get(self, origination_account_id: Optional[Optional[str]] = None) -> model.model.BankTransferBalanceGetResponse:
        """Get balance of your Bank Transfer account
        
        Use the `/bank_transfer/balance/get` endpoint to see the available balance in your bank transfer account. Debit transfers increase this balance once their status is posted. Credit transfers decrease this balance when they are created.
        
        The transactable balance shows the amount in your account that you are able to use for transfers, and is essentially your available balance minus your minimum balance.
        
        Note that this endpoint can only be used with FBO accounts, when using Bank Transfers in the Full Service configuration. It cannot be used on your own account when using Bank Transfers in the BTS Platform configuration.
        
        See endpoint docs at <https://plaid.com/docs/bank-transfers/reference#bank_transferbalanceget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "origination_account_id": origination_account_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/bank_transfer/balance/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.BankTransferBalanceGetResponse.from_json(data)
    async def bank_transfer_migrate_account(self, account_number: str, routing_number: str, wire_routing_number: Optional[str] = None, account_type: str) -> model.model.BankTransferMigrateAccountResponse:
        """Migrate account into Bank Transfers
        
        As an alternative to adding Items via Link, you can also use the `/bank_transfer/migrate_account` endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Bank Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to `/bank_transfer/migrate_account` is not enabled by default; to obtain access, contact your Plaid Account Manager.
        
        See endpoint docs at <https://plaid.com/docs/bank-transfers/reference#bank_transfermigrate_account>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "account_number": account_number,
            "routing_number": routing_number,
            "wire_routing_number": wire_routing_number,
            "account_type": account_type,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/bank_transfer/migrate_account", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.BankTransferMigrateAccountResponse.from_json(data)
    async def transfer_migrate_account(self, account_number: str, routing_number: str, wire_routing_number: Optional[str] = None, account_type: str) -> model.model.TransferMigrateAccountResponse:
        """Migrate account into Transfers
        
        As an alternative to adding Items via Link, you can also use the `/transfer/migrate_account` endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to `/transfer/migrate_account` is not enabled by default; to obtain access, contact your Plaid Account Manager.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#transfermigrate_account>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "account_number": account_number,
            "routing_number": routing_number,
            "wire_routing_number": wire_routing_number,
            "account_type": account_type,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transfer/migrate_account", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransferMigrateAccountResponse.from_json(data)
    async def transfer_intent_create(self, account_id: Optional[Optional[str]] = None, mode: model.TransferIntentCreateMode, amount: model.TransferAmount, description: str, ach_class: model.AchClass, origination_account_id: Optional[Optional[str]] = None, user: model.TransferUserInRequest, metadata: Optional[Optional[model.TransferMetadata]] = None, iso_currency_code: Optional[str] = None, require_guarantee: Optional[Optional[bool]] = None) -> model.model.TransferIntentCreateResponse:
        """Create a transfer intent object to invoke the Transfer UI
        
        Use the `/transfer/intent/create` endpoint to generate a transfer intent object and invoke the Transfer UI.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#transferintentcreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "account_id": account_id,
            "mode": mode,
            "amount": amount,
            "description": description,
            "ach_class": ach_class,
            "origination_account_id": origination_account_id,
            "user": user,
            "metadata": metadata,
            "iso_currency_code": iso_currency_code,
            "require_guarantee": require_guarantee,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transfer/intent/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransferIntentCreateResponse.from_json(data)
    async def transfer_intent_get(self, transfer_intent_id: str) -> model.model.TransferIntentGetResponse:
        """Retrieve more information about a transfer intent
        
        Use the `/transfer/intent/get` endpoint to retrieve more information about a transfer intent.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#transferintentget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "transfer_intent_id": transfer_intent_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transfer/intent/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransferIntentGetResponse.from_json(data)
    async def transfer_repayment_list(self, start_date: Optional[Optional[str]] = None, end_date: Optional[Optional[str]] = None, count: Optional[Optional[int]] = None, offset: Optional[int] = None) -> model.model.TransferRepaymentListResponse:
        """Lists historical repayments
        
        The `/transfer/repayment/list` endpoint fetches repayments matching the given filters. Repayments are returned in reverse-chronological order (most recent first) starting at the given `start_time`.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#transferrepaymentlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "start_date": start_date,
            "end_date": end_date,
            "count": count,
            "offset": offset,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transfer/repayment/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransferRepaymentListResponse.from_json(data)
    async def transfer_repayment_return_list(self, repayment_id: str, count: Optional[Optional[int]] = None, offset: Optional[int] = None) -> model.model.TransferRepaymentReturnListResponse:
        """List the returns included in a repayment
        
        The `/transfer/repayment/return/list` endpoint retrieves the set of returns that were batched together into the specified repayment. The sum of amounts of returns retrieved by this request equals the amount of the repayment.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#transferrepaymentreturnlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "repayment_id": repayment_id,
            "count": count,
            "offset": offset,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/transfer/repayment/return/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransferRepaymentReturnListResponse.from_json(data)
    async def sandbox_bank_transfer_simulate(self, bank_transfer_id: model.BankTransferId, event_type: str, failure_reason: Optional[Optional[model.BankTransferFailure]] = None) -> model.model.SandboxBankTransferSimulateResponse:
        """Simulate a bank transfer event in Sandbox
        
        Use the `/sandbox/bank_transfer/simulate` endpoint to simulate a bank transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/bank_transfer/event/sync` or `/bank_transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.
        
        See endpoint docs at <https://plaid.com/docs/bank-transfers/reference/#sandboxbank_transfersimulate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "bank_transfer_id": bank_transfer_id,
            "event_type": event_type,
            "failure_reason": failure_reason,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/sandbox/bank_transfer/simulate", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SandboxBankTransferSimulateResponse.from_json(data)
    async def sandbox_transfer_sweep_simulate(self) -> model.model.SandboxTransferSweepSimulateResponse:
        """Simulate creating a sweep
        
        Use the `/sandbox/transfer/sweep/simulate` endpoint to create a sweep and associated events in the Sandbox environment. Upon calling this endpoint, all `posted` or `pending` transfers with a sweep status of `unswept` will become `swept`, and all `returned` transfers with a sweep status of `swept` will become `return_swept`.
        
        See endpoint docs at <https://plaid.com/docs/api/sandbox/#sandboxtransfersweepsimulate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/sandbox/transfer/sweep/simulate", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SandboxTransferSweepSimulateResponse.from_json(data)
    async def sandbox_transfer_simulate(self, transfer_id: model.TransferId, event_type: str, failure_reason: Optional[Optional[model.TransferFailure]] = None) -> model.model.SandboxTransferSimulateResponse:
        """Simulate a transfer event in Sandbox
        
        Use the `/sandbox/transfer/simulate` endpoint to simulate a transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/transfer/event/sync` or `/transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.
        
        See endpoint docs at <https://plaid.com/docs/api/sandbox/#sandboxtransfersimulate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "transfer_id": transfer_id,
            "event_type": event_type,
            "failure_reason": failure_reason,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/sandbox/transfer/simulate", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SandboxTransferSimulateResponse.from_json(data)
    async def sandbox_transfer_repayment_simulate(self) -> model.model.SandboxTransferRepaymentSimulateResponse:
        """Trigger the creation of a repayment
        
        Use the `/sandbox/transfer/repayment/simulate` endpoint to trigger the creation of a repayment. As a side effect of calling this route, a repayment is created that includes all unreimbursed returns of guaranteed transfers. If there are no such returns, an 400 error is returned.
        
        See endpoint docs at <https://plaid.com/docs/api/sandbox/#sandboxtransferrepaymentsimulate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/sandbox/transfer/repayment/simulate", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SandboxTransferRepaymentSimulateResponse.from_json(data)
    async def sandbox_transfer_fire_webhook(self, webhook: str) -> model.model.SandboxTransferFireWebhookResponse:
        """Manually fire a Transfer webhook
        
        Use the `/sandbox/transfer/fire_webhook` endpoint to manually trigger a Transfer webhook in the Sandbox environment.
        
        See endpoint docs at <https://plaid.com/docs/api/sandbox/#sandboxtransferfire_webhook>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "webhook": webhook,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/sandbox/transfer/fire_webhook", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SandboxTransferFireWebhookResponse.from_json(data)
    async def employers_search(self, query: str, products: List[str]) -> model.model.EmployersSearchResponse:
        """Search employer database
        
        `/employers/search` allows you the ability to search Plaid’s database of known employers, for use with Deposit Switch. You can use this endpoint to look up a user's employer in order to confirm that they are supported. Users with non-supported employers can then be routed out of the Deposit Switch flow.
        
        The data in the employer database is currently limited. As the Deposit Switch and Income products progress through their respective beta periods, more employers are being regularly added. Because the employer database is frequently updated, we recommend that you do not cache or store data from this endpoint for more than a day.
        
        See endpoint docs at <https://plaid.com/docs/api/employers/#employerssearch>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "query": query,
            "products": products,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/employers/search", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.EmployersSearchResponse.from_json(data)
    async def income_verification_create(self, webhook: str, precheck_id: Optional[str] = None, options: Optional[model.IncomeVerificationCreateRequestOptions] = None) -> model.model.IncomeVerificationCreateResponse:
        """(Deprecated) Create an income verification instance
        
        `/income/verification/create` begins the income verification process by returning an `income_verification_id`. You can then provide the `income_verification_id` to `/link/token/create` under the `income_verification` parameter in order to create a Link instance that will prompt the user to go through the income verification flow. Plaid will fire an `INCOME` webhook once the user completes the Payroll Income flow, or when the uploaded documents in the Document Income flow have finished processing. 
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#incomeverificationcreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "webhook": webhook,
            "precheck_id": precheck_id,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/income/verification/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.IncomeVerificationCreateResponse.from_json(data)
    async def income_verification_paystubs_get(self, income_verification_id: Optional[Optional[str]] = None, access_token: Optional[Optional[model.AccessTokenNullable]] = None) -> model.model.IncomeVerificationPaystubsGetResponse:
        """(Deprecated) Retrieve information from the paystubs used for income verification
        
        `/income/verification/paystubs/get` returns the information collected from the paystubs that were used to verify an end user's income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.
        
        This endpoint has been deprecated; new integrations should use `/credit/payroll_income/get` instead.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#incomeverificationpaystubsget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "income_verification_id": income_verification_id,
            "access_token": access_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/income/verification/paystubs/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.IncomeVerificationPaystubsGetResponse.from_json(data)
    async def income_verification_documents_download(self, income_verification_id: Optional[Optional[str]] = None, access_token: Optional[Optional[model.AccessTokenNullable]] = None, document_id: Optional[Optional[str]] = None) -> None:
        """(Deprecated) Download the original documents used for income verification
        
        `/income/verification/documents/download` provides the ability to download the source documents associated with the verification.
        
        If Document Income was used, the documents will be those the user provided in Link. For Payroll Income, the most recent files available
        for download from the payroll provider will be available from this endpoint.
        
        The response to `/income/verification/documents/download` is a ZIP file in binary data. If a `document_id` is passed, a single document will be contained in this file.
        If not, the response will contain all documents associated with the verification.
        
        The `request_id` is returned in the `Plaid-Request-ID` header.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#incomeverificationdocumentsdownload>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "income_verification_id": income_verification_id,
            "access_token": access_token,
            "document_id": document_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/income/verification/documents/download", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
    async def income_verification_refresh(self, income_verification_id: Optional[Optional[str]] = None, access_token: Optional[Optional[model.AccessTokenNullable]] = None) -> model.model.IncomeVerificationRefreshResponse:
        """(Deprecated) Refresh an income verification
        
        `/income/verification/refresh` refreshes a given income verification.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#incomeverificationrefresh>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "income_verification_id": income_verification_id,
            "access_token": access_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/income/verification/refresh", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.IncomeVerificationRefreshResponse.from_json(data)
    async def income_verification_taxforms_get(self, income_verification_id: Optional[Optional[str]] = None, access_token: Optional[Optional[model.AccessTokenNullable]] = None) -> model.model.IncomeVerificationTaxformsGetResponse:
        """(Deprecated) Retrieve information from the tax documents used for income verification
        
        `/income/verification/taxforms/get` returns the information collected from forms that were used to verify an end user''s income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.
        
        This endpoint has been deprecated; new integrations should use `/credit/payroll_income/get` instead.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#incomeverificationtaxformsget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "income_verification_id": income_verification_id,
            "access_token": access_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/income/verification/taxforms/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.IncomeVerificationTaxformsGetResponse.from_json(data)
    async def income_verification_precheck(self, user: Optional[Optional[model.IncomeVerificationPrecheckUser]] = None, employer: Optional[Optional[model.IncomeVerificationPrecheckEmployer]] = None, transactions_access_token: Optional[Any] = None, transactions_access_tokens: Optional[List[model.AccessToken]] = None, us_military_info: Optional[Optional[model.IncomeVerificationPrecheckMilitaryInfo]] = None) -> model.model.IncomeVerificationPrecheckResponse:
        """(Deprecated) Check digital income verification eligibility and optimize conversion
        
        `/income/verification/precheck` is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification and returns a `precheck_id` that can be provided to `/link/token/create`. If the user is eligible for digital verification, providing the `precheck_id` in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the `precheck_id` can still be provided to `/link/token/create` and the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.
        
        While all request fields are optional, providing either `employer` or `transactions_access_tokens` data will increase the chance of receiving a useful result.
        
        This endpoint has been deprecated; new integrations should use `/credit/payroll_income/precheck` instead.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#incomeverificationprecheck>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "user": user,
            "employer": employer,
            "transactions_access_token": transactions_access_token,
            "transactions_access_tokens": transactions_access_tokens,
            "us_military_info": us_military_info,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/income/verification/precheck", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.IncomeVerificationPrecheckResponse.from_json(data)
    async def employment_verification_get(self, access_token: model.AccessToken) -> model.model.EmploymentVerificationGetResponse:
        """(Deprecated) Retrieve a summary of an individual's employment information
        
        `/employment/verification/get` returns a list of employments through a user payroll that was verified by an end user.
        
        This endpoint has been deprecated; new integrations should use `/credit/employment/get` instead.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#employmentverificationget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/employment/verification/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.EmploymentVerificationGetResponse.from_json(data)
    async def deposit_switch_alt_create(self, target_account: model.DepositSwitchTargetAccount, target_user: model.DepositSwitchTargetUser, options: Optional[model.DepositSwitchCreateRequestOptions] = None, country_code: Optional[Optional[str]] = None) -> model.model.DepositSwitchAltCreateResponse:
        """Create a deposit switch without using Plaid Exchange
        
        This endpoint provides an alternative to `/deposit_switch/create` for customers who have not yet fully integrated with Plaid Exchange. Like `/deposit_switch/create`, it creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.
        
        See endpoint docs at <https://plaid.com/docs/deposit-switch/reference#deposit_switchaltcreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "target_account": target_account,
            "target_user": target_user,
            "options": options,
            "country_code": country_code,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/deposit_switch/alt/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.DepositSwitchAltCreateResponse.from_json(data)
    async def credit_audit_copy_token_create(self, report_tokens: List[model.ReportToken], auditor_id: str) -> model.model.CreditAuditCopyTokenCreateResponse:
        """Create Asset or Income Report Audit Copy Token
        
        Plaid can provide an Audit Copy token of an Asset Report and/or Income Report directly to a participating third party on your behalf. For example, Plaid can supply an Audit Copy token directly to Fannie Mae on your behalf if you participate in the Day 1 Certainty™ program. An Audit Copy token contains the same underlying data as the Asset Report and/or Income Report (result of /credit/payroll_income/get).
        
        To grant access to an Audit Copy token, use the `/credit/audit_copy_token/create` endpoint to create an `audit_copy_token` and then pass that token to the third party who needs access. Each third party has its own `auditor_id`, for example `fannie_mae`. You’ll need to create a separate Audit Copy for each third party to whom you want to grant access to the Report.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#creditaudit_copy_tokencreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "report_tokens": report_tokens,
            "auditor_id": auditor_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/credit/audit_copy_token/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.CreditAuditCopyTokenCreateResponse.from_json(data)
    async def credit_report_audit_copy_remove(self, audit_copy_token: str) -> model.model.CreditAuditCopyTokenRemoveResponse:
        """Remove an Audit Copy token
        
        The `/credit/audit_copy_token/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Report data and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#creditaudit_copy_tokenremove>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "audit_copy_token": audit_copy_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/credit/audit_copy_token/remove", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.CreditAuditCopyTokenRemoveResponse.from_json(data)
    async def credit_bank_income_get(self, user_token: Optional[model.UserToken] = None, options: Optional[model.CreditBankIncomeGetRequestOptions] = None) -> model.model.CreditBankIncomeGetResponse:
        """Retrieve information from the bank accounts used for income verification
        
        `/credit/bank_income/get` returns the bank income report(s) for a specified user.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#creditbank_incomeget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "user_token": user_token,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/credit/bank_income/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.CreditBankIncomeGetResponse.from_json(data)
    async def credit_bank_income_pdf_get(self, user_token: model.UserToken) -> None:
        """Retrieve information from the bank accounts used for income verification in PDF format
        
        `/credit/bank_income/pdf/get` returns the most recent bank income report for a specified user in PDF format.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#creditbank_incomepdfget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "user_token": user_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/credit/bank_income/pdf/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
    async def credit_bank_income_refresh(self, user_token: model.UserToken, options: Optional[model.CreditBankIncomeRefreshRequestOptions] = None) -> model.model.CreditBankIncomeRefreshResponse:
        """Refresh a user's bank income information
        
        `/credit/bank_income/refresh` refreshes the bank income report data for a specific user.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#creditbank_incomerefresh>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "user_token": user_token,
            "options": options,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/credit/bank_income/refresh", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.CreditBankIncomeRefreshResponse.from_json(data)
    async def credit_payroll_income_get(self, user_token: Optional[model.UserToken] = None) -> model.model.CreditPayrollIncomeGetResponse:
        """Retrieve a user's payroll information
        
        This endpoint gets payroll income information for a specific user, either as a result of the user connecting to their payroll provider or uploading a pay related document.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#creditpayroll_incomeget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "user_token": user_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/credit/payroll_income/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.CreditPayrollIncomeGetResponse.from_json(data)
    async def credit_payroll_income_precheck(self, user_token: Optional[model.UserToken] = None, access_tokens: Optional[List[model.AccessToken]] = None, employer: Optional[Optional[model.IncomeVerificationPrecheckEmployer]] = None, us_military_info: Optional[Optional[model.IncomeVerificationPrecheckMilitaryInfo]] = None) -> model.model.CreditPayrollIncomePrecheckResponse:
        """Check income verification eligibility and optimize conversion
        
        `/credit/payroll_income/precheck` is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification. If the user is eligible for digital verification, that information will be associated with the user token, and in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.
        
        While all request fields are optional, providing `employer` data will increase the chance of receiving a useful result.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#creditpayroll_incomeprecheck>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "user_token": user_token,
            "access_tokens": access_tokens,
            "employer": employer,
            "us_military_info": us_military_info,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/credit/payroll_income/precheck", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.CreditPayrollIncomePrecheckResponse.from_json(data)
    async def credit_employment_get(self, user_token: model.UserToken) -> model.model.CreditEmploymentGetResponse:
        """Retrieve a summary of an individual's employment information
        
        `/credit/employment/get` returns a list of items with employment information from a user's payroll provider that was verified by an end user.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#creditemploymentget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "user_token": user_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/credit/employment/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.CreditEmploymentGetResponse.from_json(data)
    async def credit_payroll_income_refresh(self, user_token: Optional[model.UserToken] = None) -> model.model.CreditPayrollIncomeRefreshResponse:
        """Refresh a digital payroll income verification
        
        `/credit/payroll_income/refresh` refreshes a given digital payroll income verification.
        
        See endpoint docs at <https://plaid.com/docs/api/products/income/#creditpayroll_incomerefresh>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "user_token": user_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/credit/payroll_income/refresh", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.CreditPayrollIncomeRefreshResponse.from_json(data)
    async def credit_relay_create(self, report_tokens: List[model.ReportToken], secondary_client_id: str, webhook: Optional[Optional[str]] = None) -> model.model.CreditRelayCreateResponse:
        """Create a `relay_token` to share an Asset Report with a partner client
        
        Plaid can share an Asset Report directly with a participating third party on your behalf. The shared Asset Report is the exact same Asset Report originally created in `/asset_report/create`.
        
        To grant access to an Asset Report to a third party, use the `/credit/relay/create` endpoint to create a `relay_token` and then pass that token to the third party who needs access. Each third party has its own `secondary_client_id`, for example `ce5bd328dcd34123456`. You'll need to create a separate `relay_token` for each third party to whom you want to grant access to the Report.
        
        See endpoint docs at <https://plaid.com/docs/none/>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "report_tokens": report_tokens,
            "secondary_client_id": secondary_client_id,
            "webhook": webhook,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/credit/relay/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.CreditRelayCreateResponse.from_json(data)
    async def credit_relay_get(self, relay_token: str, report_type: model.ReportType) -> model.model.AssetReportGetResponse:
        """Retrieve the reports associated with a Relay token that was shared with you
        
        `/credit/relay/get` allows third parties to get a report that was shared with them, using an `relay_token` that was created by the report owner.
        
        See endpoint docs at <https://plaid.com/docs/none/>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "relay_token": relay_token,
            "report_type": report_type,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/credit/relay/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.AssetReportGetResponse.from_json(data)
    async def credit_relay_refresh(self, relay_token: str, report_type: model.ReportType, webhook: Optional[Optional[str]] = None) -> model.model.CreditRelayRefreshResponse:
        """Refresh a report of a Relay Token
        
        The `/credit/relay/refresh` endpoint allows third parties to refresh an report that was relayed to them, using a `relay_token` that was created by the report owner. A new report will be created based on the old one, but with the most recent data available.
        
        See endpoint docs at <https://plaid.com/docs/api/products/#creditrelayrefresh>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "relay_token": relay_token,
            "report_type": report_type,
            "webhook": webhook,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/credit/relay/refresh", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.CreditRelayRefreshResponse.from_json(data)
    async def credit_relay_remove(self, relay_token: str) -> model.model.CreditRelayRemoveResponse:
        """Remove Credit Relay Token
        
        The `/credit/relay/remove` endpoint allows you to invalidate a `relay_token`, meaning the third party holding the token will no longer be able to use it to access the reports to which the `relay_token` gives access to. The report, items associated with it, and other Relay tokens that provide access to the same report are not affected and will remain accessible after removing the given `relay_token.
        
        See endpoint docs at <https://plaid.com/docs/none/>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "relay_token": relay_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/credit/relay/remove", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.CreditRelayRemoveResponse.from_json(data)
    async def sandbox_bank_transfer_fire_webhook(self, webhook: str) -> model.model.SandboxBankTransferFireWebhookResponse:
        """Manually fire a Bank Transfer webhook
        
        Use the `/sandbox/bank_transfer/fire_webhook` endpoint to manually trigger a Bank Transfers webhook in the Sandbox environment.
        
        See endpoint docs at <https://plaid.com/docs/bank-transfers/reference/#sandboxbank_transferfire_webhook>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "webhook": webhook,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/sandbox/bank_transfer/fire_webhook", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SandboxBankTransferFireWebhookResponse.from_json(data)
    async def sandbox_income_fire_webhook(self, item_id: str, user_id: Optional[model.UserId] = None, webhook: str, verification_status: str) -> model.model.SandboxIncomeFireWebhookResponse:
        """Manually fire an Income webhook
        
        Use the `/sandbox/income/fire_webhook` endpoint to manually trigger an Income webhook in the Sandbox environment.
        
        See endpoint docs at <https://plaid.com/docs/api/sandbox/#sandboxincomefire_webhook>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "item_id": item_id,
            "user_id": user_id,
            "webhook": webhook,
            "verification_status": verification_status,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/sandbox/income/fire_webhook", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SandboxIncomeFireWebhookResponse.from_json(data)
    async def sandbox_oauth_select_accounts(self, oauth_state_id: str, accounts: List[str]) -> model.model.SandboxOauthSelectAccountsResponse:
        """Save the selected accounts when connecting to the Platypus Oauth institution
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "oauth_state_id": oauth_state_id,
            "accounts": accounts,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/sandbox/oauth/select_accounts", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SandboxOauthSelectAccountsResponse.from_json(data)
    async def signal_evaluate(self, access_token: model.AccessToken, account_id: str, client_transaction_id: str, amount: float, user_present: Optional[Optional[bool]] = None, client_user_id: Optional[str] = None, user: Optional[model.SignalUser] = None, device: Optional[model.SignalDevice] = None) -> model.model.SignalEvaluateResponse:
        """Evaluate a planned ACH transaction
        
        Use `/signal/evaluate` to evaluate a planned ACH transaction to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.
        
        In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying cause. If `/signal/evaluate` is called on the same transaction multiple times within a 24-hour period, cached results may be returned.
        
        See endpoint docs at <https://plaid.com/docs/signal/reference#signalevaluate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "account_id": account_id,
            "client_transaction_id": client_transaction_id,
            "amount": amount,
            "user_present": user_present,
            "client_user_id": client_user_id,
            "user": user,
            "device": device,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/signal/evaluate", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SignalEvaluateResponse.from_json(data)
    async def signal_decision_report(self, client_transaction_id: str, initiated: bool, days_funds_on_hold: Optional[Optional[int]] = None) -> model.model.SignalDecisionReportResponse:
        """Report whether you initiated an ACH transaction
        
        After calling `/signal/evaluate`, call `/signal/decision/report` to report whether the transaction was initiated. This endpoint will return an `INVALID_REQUEST` error if called a second time with a different value for `initiated`.
        
        See endpoint docs at <https://plaid.com/docs/signal/reference#signaldecisionreport>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "client_transaction_id": client_transaction_id,
            "initiated": initiated,
            "days_funds_on_hold": days_funds_on_hold,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/signal/decision/report", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SignalDecisionReportResponse.from_json(data)
    async def signal_return_report(self, client_transaction_id: str, return_code: str) -> model.model.SignalReturnReportResponse:
        """Report a return for an ACH transaction
        
        Call the `/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.
        
        See endpoint docs at <https://plaid.com/docs/signal/reference#signalreturnreport>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "client_transaction_id": client_transaction_id,
            "return_code": return_code,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/signal/return/report", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SignalReturnReportResponse.from_json(data)
    async def signal_prepare(self, access_token: model.AccessToken) -> model.model.SignalPrepareResponse:
        """Prepare the Signal product before calling `/signal/evaluate`
        
        Call `/signal/prepare` with Plaid-linked bank account information at least 10 seconds before calling `/signal/evaluate` or as soon as an end-user enters the ACH deposit flow in your application.
        
        See endpoint docs at <https://plaid.com/docs/signal/reference#signalprepare>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/signal/prepare", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.SignalPrepareResponse.from_json(data)
    async def wallet_create(self, iso_currency_code: model.WalletIsoCurrencyCode) -> model.model.WalletCreateResponse:
        """Create an e-wallet
        
        Create an e-wallet. The response is the newly created e-wallet object.
        
        See endpoint docs at <https://plaid.com/docs/api/products/#walletcreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "iso_currency_code": iso_currency_code,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/wallet/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.WalletCreateResponse.from_json(data)
    async def wallet_get(self, wallet_id: str) -> model.model.WalletGetResponse:
        """Fetch an e-wallet
        
        Fetch an e-wallet. The response includes the current balance.
        
        See endpoint docs at <https://plaid.com/docs/api/products/#walletget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "wallet_id": wallet_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/wallet/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.WalletGetResponse.from_json(data)
    async def wallet_list(self, iso_currency_code: Optional[model.WalletIsoCurrencyCode] = None, cursor: Optional[str] = None, count: Optional[int] = None) -> model.model.WalletListResponse:
        """Fetch a list of e-wallets
        
        This endpoint lists all e-wallets in descending order of creation.
        
        See endpoint docs at <https://plaid.com/docs/api/products/#walletlist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "iso_currency_code": iso_currency_code,
            "cursor": cursor,
            "count": count,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/wallet/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.WalletListResponse.from_json(data)
    async def wallet_transaction_execute(self, idempotency_key: model.WalletTransactionIdempotencyKey, wallet_id: str, counterparty: model.WalletTransactionCounterparty, amount: model.WalletTransactionAmount, reference: str) -> model.model.WalletTransactionExecuteResponse:
        """Execute a transaction using an e-wallet
        
        Execute a transaction using the specified e-wallet.
        Specify the e-wallet to debit from, the counterparty to credit to, the idempotency key to prevent duplicate payouts, the amount and reference for the payout.
        The payouts are executed over the Faster Payment rails, where settlement usually only takes a few seconds.
        
        See endpoint docs at <https://plaid.com/docs/api/products/#wallettransactionexecute>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "idempotency_key": idempotency_key,
            "wallet_id": wallet_id,
            "counterparty": counterparty,
            "amount": amount,
            "reference": reference,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/wallet/transaction/execute", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.WalletTransactionExecuteResponse.from_json(data)
    async def wallet_transaction_get(self, transaction_id: str) -> model.model.WalletTransactionGetResponse:
        """Fetch a specific e-wallet transaction
        
        See endpoint docs at <https://plaid.com/docs/api/products/#wallettransactionget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "transaction_id": transaction_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/wallet/transaction/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.WalletTransactionGetResponse.from_json(data)
    async def wallet_transactions_list(self, wallet_id: str, cursor: Optional[str] = None, count: Optional[int] = None) -> model.model.WalletTransactionsListResponse:
        """List e-wallet transactions
        
        This endpoint lists the latest transactions of the specified e-wallet. Transactions are returned in descending order by the `created_at` time.
        
        See endpoint docs at <https://plaid.com/docs/api/products/#wallettransactionslist>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "wallet_id": wallet_id,
            "cursor": cursor,
            "count": count,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/wallet/transactions/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.WalletTransactionsListResponse.from_json(data)
    async def transactions_enhance(self, account_type: str, transactions: List[model.ClientProvidedRawTransaction]) -> model.model.TransactionsEnhanceGetResponse:
        """enhance locally-held transaction data
        
        The '/beta/transactions/v1/enhance' endpoint enriches raw transaction data provided directly by clients.
        
        The product is currently in beta.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "account_type": account_type,
            "transactions": transactions,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/beta/transactions/v1/enhance", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransactionsEnhanceGetResponse.from_json(data)
    async def transactions_rules_create(self, access_token: model.AccessToken, personal_finance_category: str, rule_details: model.TransactionsRuleDetails) -> model.model.TransactionsRulesCreateResponse:
        """Create transaction category rule
        
        The `/transactions/rules/v1/create` endpoint creates transaction categorization rules.
        
        Rules will be applied on the Item's transactions returned in `/transactions/get` response.
        
        The product is currently in beta. To request access, contact transactions-feedback@plaid.com.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "personal_finance_category": personal_finance_category,
            "rule_details": rule_details,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/beta/transactions/rules/v1/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransactionsRulesCreateResponse.from_json(data)
    async def transactions_rules_list(self, access_token: model.AccessToken) -> model.model.TransactionsRulesListResponse:
        """Return a list of rules created for the Item associated with the access token.
        
        The `/transactions/rules/v1/list` returns a list of transaction rules created for the Item associated with the access token.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/beta/transactions/rules/v1/list", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransactionsRulesListResponse.from_json(data)
    async def transactions_rules_remove(self, access_token: model.AccessToken, rule_id: str) -> model.model.TransactionsRulesRemoveResponse:
        """Remove transaction rule
        
        The `/transactions/rules/v1/remove` endpoint is used to remove a transaction rule.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "access_token": access_token,
            "rule_id": rule_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/beta/transactions/rules/v1/remove", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.TransactionsRulesRemoveResponse.from_json(data)
    async def payment_profile_create(self) -> model.model.PaymentProfileCreateResponse:
        """Create payment profile
        
        Use `/payment_profile/create` endpoint to create a new payment profile, the return value is a Payment Profile ID. Attach it to the link token create request and the link workflow will then "activate" this Payment Profile if the linkage is successful. It can then be used to create Transfers using `/transfer/authorization/create` and /transfer/create`.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#payment_profilecreate>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/payment_profile/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaymentProfileCreateResponse.from_json(data)
    async def payment_profile_get(self, payment_profile_id: model.PaymentProfileId) -> model.model.PaymentProfileGetResponse:
        """Get payment profile
        
        Use the `/payment_profile/get` endpoint to get the status of a given Payment Profile.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#payment_profileget>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "payment_profile_id": payment_profile_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/payment_profile/get", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaymentProfileGetResponse.from_json(data)
    async def payment_profile_remove(self, payment_profile_id: model.PaymentProfileId) -> model.model.PaymentProfileRemoveResponse:
        """Remove payment profile
        
        Use the `/payment_profile/remove` endpoint to remove a given Payment Profile. Once it’s removed, it can no longer be used to create transfers.
        
        See endpoint docs at <https://plaid.com/docs/api/products/transfer/#payment_profileremove>.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "payment_profile_id": payment_profile_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/payment_profile/remove", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PaymentProfileRemoveResponse.from_json(data)
    async def partner_customers_create(self, company_name: str, is_diligence_attested: bool, products: List[model.Products], create_link_customization: Optional[bool] = None) -> model.model.PartnerCustomersCreateResponse:
        """Creates a new client for a reseller partner end customer.
        
        The `/partner/v1/customers/create` endpoint is used by reseller partners to create an end customer client.
        
        :raises requests.exceptions.HTTPError: if a non-200 status code is returned"""
        headers = {
            
        }
        params = {
            
        }
        data = {
            "company_name": company_name,
            "is_diligence_attested": is_diligence_attested,
            "products": products,
            "create_link_customization": create_link_customization,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + "/beta/partner/v1/customers/create", params=params, headers=headers, data=data) as r:
                self._raise_for_status(r)
                data = await r.json()
                return model.model.PartnerCustomersCreateResponse.from_json(data)
    @classmethod
    def from_env(cls) :
        
        return cls(os.environ["PLAID_URL"])

