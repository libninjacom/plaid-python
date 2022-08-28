
from typing import Any, Dict, List, Optional, Union

class AuthGetRequest:
    
    def __init__(self, access_token: AccessToken, options: AuthGetRequestOptions) :
        
        self.access_token = access_token;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],options = data["options"])


class AuthGetRequestOptions:
    
    def __init__(self, account_ids: List[str]) :
        
        self.account_ids = account_ids
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_ids = data["account_ids"])


class AuthGetResponse:
    
    def __init__(self, accounts: List[AccountBase], numbers: AuthGetNumbers, item: Item, request_id: RequestId) :
        
        self.accounts = accounts;self.numbers = numbers;self.item = item;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(accounts = data["accounts"],numbers = data["numbers"],item = data["item"],request_id = data["request_id"])


class AuthGetNumbers:
    
    def __init__(self, ach: List[NumbersAch], eft: List[NumbersEft], international: List[NumbersInternational], bacs: List[NumbersBacs]) :
        
        self.ach = ach;self.eft = eft;self.international = international;self.bacs = bacs
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(ach = data["ach"],eft = data["eft"],international = data["international"],bacs = data["bacs"])


class TransactionsGetRequest:
    
    def __init__(self, options: TransactionsGetRequestOptions, access_token: AccessToken, start_date: str, end_date: str) :
        
        self.options = options;self.access_token = access_token;self.start_date = start_date;self.end_date = end_date
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(options = data["options"],access_token = data["access_token"],start_date = data["start_date"],end_date = data["end_date"])


class TransactionsGetRequestOptions:
    
    def __init__(self, account_ids: List[str], count: int, offset: int, include_original_description: Optional[bool], include_personal_finance_category_beta: bool, include_personal_finance_category: bool) :
        
        self.account_ids = account_ids;self.count = count;self.offset = offset;self.include_original_description = include_original_description;self.include_personal_finance_category_beta = include_personal_finance_category_beta;self.include_personal_finance_category = include_personal_finance_category
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_ids = data["account_ids"],count = data["count"],offset = data["offset"],include_original_description = data["include_original_description"],include_personal_finance_category_beta = data["include_personal_finance_category_beta"],include_personal_finance_category = data["include_personal_finance_category"])


class TransactionsGetResponse:
    
    def __init__(self, accounts: List[AccountBase], transactions: List[Transaction], total_transactions: int, item: Item, request_id: RequestId) :
        
        self.accounts = accounts;self.transactions = transactions;self.total_transactions = total_transactions;self.item = item;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(accounts = data["accounts"],transactions = data["transactions"],total_transactions = data["total_transactions"],item = data["item"],request_id = data["request_id"])


class TransactionsRefreshRequest:
    
    def __init__(self, access_token: AccessToken) :
        
        self.access_token = access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"])


class TransactionsRefreshResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class TransactionsRecurringGetRequest:
    
    def __init__(self, access_token: AccessToken, options: TransactionsRecurringGetRequestOptions, account_ids: List[str]) :
        
        self.access_token = access_token;self.options = options;self.account_ids = account_ids
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],options = data["options"],account_ids = data["account_ids"])


class TransactionsRecurringGetRequestOptions:
    
    def __init__(self, include_personal_finance_category: bool) :
        
        self.include_personal_finance_category = include_personal_finance_category
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(include_personal_finance_category = data["include_personal_finance_category"])


class TransactionsRecurringGetResponse:
    
    def __init__(self, inflow_streams: List[TransactionStream], outflow_streams: List[TransactionStream], updated_datetime: str, request_id: RequestId) :
        
        self.inflow_streams = inflow_streams;self.outflow_streams = outflow_streams;self.updated_datetime = updated_datetime;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(inflow_streams = data["inflow_streams"],outflow_streams = data["outflow_streams"],updated_datetime = data["updated_datetime"],request_id = data["request_id"])


class TransactionsRulesCreateRequest:
    
    def __init__(self, access_token: AccessToken, personal_finance_category: str, rule_details: TransactionsRuleDetails) :
        
        self.access_token = access_token;self.personal_finance_category = personal_finance_category;self.rule_details = rule_details
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],personal_finance_category = data["personal_finance_category"],rule_details = data["rule_details"])


class TransactionsRulesCreateResponse:
    
    def __init__(self, rule: TransactionsCategoryRule, request_id: RequestId) :
        
        self.rule = rule;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(rule = data["rule"],request_id = data["request_id"])


class TransactionsRulesListRequest:
    
    def __init__(self, access_token: AccessToken) :
        
        self.access_token = access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"])


class TransactionsRulesListResponse:
    
    def __init__(self, rules: List[TransactionsCategoryRule], request_id: RequestId) :
        
        self.rules = rules;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(rules = data["rules"],request_id = data["request_id"])


class TransactionsRulesRemoveRequest:
    
    def __init__(self, access_token: AccessToken, rule_id: str) :
        
        self.access_token = access_token;self.rule_id = rule_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],rule_id = data["rule_id"])


class TransactionsRulesRemoveResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class TransactionsSyncRequest:
    
    def __init__(self, access_token: AccessToken, cursor: str, count: int, options: TransactionsSyncRequestOptions) :
        
        self.access_token = access_token;self.cursor = cursor;self.count = count;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],cursor = data["cursor"],count = data["count"],options = data["options"])


class TransactionsSyncRequestOptions:
    
    def __init__(self, include_original_description: Optional[bool], include_personal_finance_category: bool) :
        
        self.include_original_description = include_original_description;self.include_personal_finance_category = include_personal_finance_category
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(include_original_description = data["include_original_description"],include_personal_finance_category = data["include_personal_finance_category"])


class TransactionsSyncResponse:
    
    def __init__(self, added: List[Transaction], modified: List[Transaction], removed: List[RemovedTransaction], next_cursor: str, has_more: bool, request_id: RequestId) :
        
        self.added = added;self.modified = modified;self.removed = removed;self.next_cursor = next_cursor;self.has_more = has_more;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(added = data["added"],modified = data["modified"],removed = data["removed"],next_cursor = data["next_cursor"],has_more = data["has_more"],request_id = data["request_id"])


class InstitutionsGetRequest:
    
    def __init__(self, count: int, offset: int, country_codes: List[CountryCode], options: InstitutionsGetRequestOptions) :
        
        self.count = count;self.offset = offset;self.country_codes = country_codes;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(count = data["count"],offset = data["offset"],country_codes = data["country_codes"],options = data["options"])


class InstitutionsGetRequestOptions:
    
    def __init__(self, products: Optional[List[Products]], routing_numbers: Optional[List[str]], oauth: Optional[bool], include_optional_metadata: bool, include_auth_metadata: bool, include_payment_initiation_metadata: bool) :
        
        self.products = products;self.routing_numbers = routing_numbers;self.oauth = oauth;self.include_optional_metadata = include_optional_metadata;self.include_auth_metadata = include_auth_metadata;self.include_payment_initiation_metadata = include_payment_initiation_metadata
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(products = data["products"],routing_numbers = data["routing_numbers"],oauth = data["oauth"],include_optional_metadata = data["include_optional_metadata"],include_auth_metadata = data["include_auth_metadata"],include_payment_initiation_metadata = data["include_payment_initiation_metadata"])


class InstitutionsGetResponse:
    
    def __init__(self, institutions: List[Institution], total: int, request_id: RequestId) :
        
        self.institutions = institutions;self.total = total;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(institutions = data["institutions"],total = data["total"],request_id = data["request_id"])


class InstitutionsSearchRequest:
    
    def __init__(self, query: str, products: Optional[List[Products]], country_codes: List[CountryCode], options: InstitutionsSearchRequestOptions) :
        
        self.query = query;self.products = products;self.country_codes = country_codes;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(query = data["query"],products = data["products"],country_codes = data["country_codes"],options = data["options"])


class InstitutionsSearchRequestOptions:
    
    def __init__(self, oauth: Optional[bool], include_optional_metadata: bool, include_auth_metadata: Optional[bool], include_payment_initiation_metadata: Optional[bool], payment_initiation: Optional[InstitutionsSearchPaymentInitiationOptions]) :
        
        self.oauth = oauth;self.include_optional_metadata = include_optional_metadata;self.include_auth_metadata = include_auth_metadata;self.include_payment_initiation_metadata = include_payment_initiation_metadata;self.payment_initiation = payment_initiation
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(oauth = data["oauth"],include_optional_metadata = data["include_optional_metadata"],include_auth_metadata = data["include_auth_metadata"],include_payment_initiation_metadata = data["include_payment_initiation_metadata"],payment_initiation = data["payment_initiation"])


class InstitutionsSearchPaymentInitiationOptions:
    
    def __init__(self, payment_id: Optional[str], consent_id: Optional[str]) :
        
        self.payment_id = payment_id;self.consent_id = consent_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(payment_id = data["payment_id"],consent_id = data["consent_id"])


class InstitutionsSearchResponse:
    
    def __init__(self, institutions: List[Institution], request_id: RequestId) :
        
        self.institutions = institutions;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(institutions = data["institutions"],request_id = data["request_id"])


class InstitutionsGetByIdRequest:
    
    def __init__(self, institution_id: str, country_codes: List[CountryCode], options: InstitutionsGetByIdRequestOptions) :
        
        self.institution_id = institution_id;self.country_codes = country_codes;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(institution_id = data["institution_id"],country_codes = data["country_codes"],options = data["options"])


class InstitutionsGetByIdRequestOptions:
    
    def __init__(self, include_optional_metadata: bool, include_status: bool, include_auth_metadata: bool, include_payment_initiation_metadata: bool) :
        
        self.include_optional_metadata = include_optional_metadata;self.include_status = include_status;self.include_auth_metadata = include_auth_metadata;self.include_payment_initiation_metadata = include_payment_initiation_metadata
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(include_optional_metadata = data["include_optional_metadata"],include_status = data["include_status"],include_auth_metadata = data["include_auth_metadata"],include_payment_initiation_metadata = data["include_payment_initiation_metadata"])


class InstitutionsGetByIdResponse:
    
    def __init__(self, institution: Institution, request_id: RequestId) :
        
        self.institution = institution;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(institution = data["institution"],request_id = data["request_id"])


class AccountsGetRequest:
    
    def __init__(self, access_token: AccessToken, options: AccountsGetRequestOptions) :
        
        self.access_token = access_token;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],options = data["options"])


class AccountsGetRequestOptions:
    
    def __init__(self, account_ids: List[str]) :
        
        self.account_ids = account_ids
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_ids = data["account_ids"])


class AccountsGetResponse:
    
    def __init__(self, accounts: List[AccountBase], item: Item, request_id: RequestId) :
        
        self.accounts = accounts;self.item = item;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(accounts = data["accounts"],item = data["item"],request_id = data["request_id"])


class CategoriesGetRequest:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class CategoriesGetResponse:
    
    def __init__(self, categories: List[Category], request_id: RequestId) :
        
        self.categories = categories;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(categories = data["categories"],request_id = data["request_id"])


class SandboxOverridePassword:
    
    def __init__(self, sandbox_override_password: Optional[str]) :
        
        self.sandbox_override_password = sandbox_override_password
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class SandboxOverrideUsername:
    
    def __init__(self, sandbox_override_username: Optional[str]) :
        
        self.sandbox_override_username = sandbox_override_username
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class SandboxProcessorTokenCreateRequest:
    
    def __init__(self, institution_id: str, options: SandboxProcessorTokenCreateRequestOptions) :
        
        self.institution_id = institution_id;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(institution_id = data["institution_id"],options = data["options"])


class SandboxProcessorTokenCreateRequestOptions:
    
    def __init__(self, override_username: Optional[SandboxOverrideUsername], override_password: Optional[SandboxOverridePassword]) :
        
        self.override_username = override_username;self.override_password = override_password
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(override_username = data["override_username"],override_password = data["override_password"])


class SandboxProcessorTokenCreateResponse:
    
    def __init__(self, processor_token: str, request_id: RequestId) :
        
        self.processor_token = processor_token;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(processor_token = data["processor_token"],request_id = data["request_id"])


class SandboxPublicTokenCreateRequest:
    
    def __init__(self, institution_id: str, initial_products: List[Products], options: SandboxPublicTokenCreateRequestOptions, user_token: UserToken) :
        
        self.institution_id = institution_id;self.initial_products = initial_products;self.options = options;self.user_token = user_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(institution_id = data["institution_id"],initial_products = data["initial_products"],options = data["options"],user_token = data["user_token"])


class SandboxPublicTokenCreateRequestOptions:
    
    def __init__(self, webhook: str, override_username: Optional[SandboxOverrideUsername], override_password: Optional[SandboxOverridePassword], transactions: SandboxPublicTokenCreateRequestOptionsTransactions) :
        
        self.webhook = webhook;self.override_username = override_username;self.override_password = override_password;self.transactions = transactions
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook = data["webhook"],override_username = data["override_username"],override_password = data["override_password"],transactions = data["transactions"])


class SandboxPublicTokenCreateRequestOptionsTransactions:
    
    def __init__(self, start_date: str, end_date: str) :
        
        self.start_date = start_date;self.end_date = end_date
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(start_date = data["start_date"],end_date = data["end_date"])


class SandboxPublicTokenCreateResponse:
    
    def __init__(self, public_token: str, request_id: RequestId) :
        
        self.public_token = public_token;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(public_token = data["public_token"],request_id = data["request_id"])


class SandboxItemFireWebhookRequest:
    
    def __init__(self, access_token: AccessToken, webhook_type: WebhookType, webhook_code: str) :
        
        self.access_token = access_token;self.webhook_type = webhook_type;self.webhook_code = webhook_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],webhook_type = data["webhook_type"],webhook_code = data["webhook_code"])


class WebhookType:
    
    def __init__(self, webhook_type: str) :
        
        self.webhook_type = webhook_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class SandboxItemFireWebhookResponse:
    
    def __init__(self, webhook_fired: bool, request_id: RequestId) :
        
        self.webhook_fired = webhook_fired;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_fired = data["webhook_fired"],request_id = data["request_id"])


class AccountsBalanceGetRequest:
    
    def __init__(self, access_token: AccessToken, options: AccountsBalanceGetRequestOptions) :
        
        self.access_token = access_token;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],options = data["options"])


class AccountsBalanceGetRequestOptions:
    
    def __init__(self, account_ids: List[str], min_last_updated_datetime: MinLastUpdatedDatetime) :
        
        self.account_ids = account_ids;self.min_last_updated_datetime = min_last_updated_datetime
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_ids = data["account_ids"],min_last_updated_datetime = data["min_last_updated_datetime"])


class MinLastUpdatedDatetime:
    
    def __init__(self, min_last_updated_datetime: str) :
        
        self.min_last_updated_datetime = min_last_updated_datetime
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IdentityGetRequest:
    
    def __init__(self, access_token: AccessToken, options: IdentityGetRequestOptions) :
        
        self.access_token = access_token;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],options = data["options"])


class IdentityGetRequestOptions:
    
    def __init__(self, account_ids: List[str]) :
        
        self.account_ids = account_ids
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_ids = data["account_ids"])


class IdentityGetResponse:
    
    def __init__(self, accounts: List[AccountIdentity], item: Item, request_id: RequestId) :
        
        self.accounts = accounts;self.item = item;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(accounts = data["accounts"],item = data["item"],request_id = data["request_id"])


class IdentityMatchRequest:
    
    def __init__(self, access_token: AccessToken, user: IdentityMatchUser, options: IdentityMatchRequestOptions) :
        
        self.access_token = access_token;self.user = user;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],user = data["user"],options = data["options"])


class IdentityMatchRequestOptions:
    
    def __init__(self, account_ids: List[str]) :
        
        self.account_ids = account_ids
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_ids = data["account_ids"])


class IdentityMatchUser:
    
    def __init__(self, legal_name: Optional[str], phone_number: Optional[str], email_address: Optional[str], address: Optional[AddressDataNullable]) :
        
        self.legal_name = legal_name;self.phone_number = phone_number;self.email_address = email_address;self.address = address
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(legal_name = data["legal_name"],phone_number = data["phone_number"],email_address = data["email_address"],address = data["address"])


class IdentityMatchResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class ProcessorAuthGetRequest:
    
    def __init__(self, processor_token: ProcessorToken) :
        
        self.processor_token = processor_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(processor_token = data["processor_token"])


class ProcessorAuthGetResponse:
    
    def __init__(self, request_id: RequestId, numbers: ProcessorNumber, account: AccountBase) :
        
        self.request_id = request_id;self.numbers = numbers;self.account = account
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"],numbers = data["numbers"],account = data["account"])


class ProcessorBankTransferCreateRequest:
    
    def __init__(self, idempotency_key: BankTransferIdempotencyKey, processor_token: ProcessorToken, type_: BankTransferType, network: BankTransferNetwork, amount: BankTransferAmount, iso_currency_code: str, description: str, ach_class: AchClass, user: BankTransferUser, custom_tag: Optional[str], metadata: Optional[BankTransferMetadata], origination_account_id: Optional[str]) :
        
        self.idempotency_key = idempotency_key;self.processor_token = processor_token;self.type_ = type_;self.network = network;self.amount = amount;self.iso_currency_code = iso_currency_code;self.description = description;self.ach_class = ach_class;self.user = user;self.custom_tag = custom_tag;self.metadata = metadata;self.origination_account_id = origination_account_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(idempotency_key = data["idempotency_key"],processor_token = data["processor_token"],type_ = data["type_"],network = data["network"],amount = data["amount"],iso_currency_code = data["iso_currency_code"],description = data["description"],ach_class = data["ach_class"],user = data["user"],custom_tag = data["custom_tag"],metadata = data["metadata"],origination_account_id = data["origination_account_id"])


class ProcessorBankTransferCreateResponse:
    
    def __init__(self, bank_transfer: BankTransfer, request_id: RequestId) :
        
        self.bank_transfer = bank_transfer;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(bank_transfer = data["bank_transfer"],request_id = data["request_id"])


class ProcessorNumber:
    
    def __init__(self, ach: Optional[NumbersAchNullable], eft: Optional[NumbersEftNullable], international: Optional[NumbersInternationalNullable], bacs: Optional[NumbersBacsNullable]) :
        
        self.ach = ach;self.eft = eft;self.international = international;self.bacs = bacs
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(ach = data["ach"],eft = data["eft"],international = data["international"],bacs = data["bacs"])


class ProcessorIdentityGetRequest:
    
    def __init__(self, processor_token: ProcessorToken) :
        
        self.processor_token = processor_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(processor_token = data["processor_token"])


class ProcessorIdentityGetResponse:
    
    def __init__(self, account: AccountIdentity, request_id: RequestId) :
        
        self.account = account;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account = data["account"],request_id = data["request_id"])


class ProcessorBalanceGetRequest:
    
    def __init__(self, processor_token: ProcessorToken, options: ProcessorBalanceGetRequestOptions) :
        
        self.processor_token = processor_token;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(processor_token = data["processor_token"],options = data["options"])


class ProcessorBalanceGetRequestOptions:
    
    def __init__(self, min_last_updated_datetime: MinLastUpdatedDatetime) :
        
        self.min_last_updated_datetime = min_last_updated_datetime
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(min_last_updated_datetime = data["min_last_updated_datetime"])


class ProcessorBalanceGetResponse:
    
    def __init__(self, account: AccountBase, request_id: RequestId) :
        
        self.account = account;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account = data["account"],request_id = data["request_id"])


class WebhookVerificationKeyGetRequest:
    
    def __init__(self, key_id: str) :
        
        self.key_id = key_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(key_id = data["key_id"])


class WebhookVerificationKeyGetResponse:
    
    def __init__(self, key: JwkPublicKey, request_id: RequestId) :
        
        self.key = key;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(key = data["key"],request_id = data["request_id"])


class JwkPublicKey:
    
    def __init__(self, alg: str, crv: str, kid: str, kty: str, use_: str, x: str, y: str, created_at: int, expired_at: Optional[int]) :
        
        self.alg = alg;self.crv = crv;self.kid = kid;self.kty = kty;self.use_ = use_;self.x = x;self.y = y;self.created_at = created_at;self.expired_at = expired_at
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(alg = data["alg"],crv = data["crv"],kid = data["kid"],kty = data["kty"],use_ = data["use_"],x = data["x"],y = data["y"],created_at = data["created_at"],expired_at = data["expired_at"])


class LiabilitiesGetRequest:
    
    def __init__(self, access_token: AccessToken, options: LiabilitiesGetRequestOptions) :
        
        self.access_token = access_token;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],options = data["options"])


class LiabilitiesGetRequestOptions:
    
    def __init__(self, account_ids: List[str]) :
        
        self.account_ids = account_ids
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_ids = data["account_ids"])


class LiabilitiesGetResponse:
    
    def __init__(self, accounts: List[AccountBase], item: Item, liabilities: LiabilitiesObject, request_id: RequestId) :
        
        self.accounts = accounts;self.item = item;self.liabilities = liabilities;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(accounts = data["accounts"],item = data["item"],liabilities = data["liabilities"],request_id = data["request_id"])


class PaymentInitiationRecipientCreateRequest:
    
    def __init__(self, name: str, iban: Optional[str], bacs: Optional[RecipientBacsNullable], address: Optional[PaymentInitiationAddress]) :
        
        self.name = name;self.iban = iban;self.bacs = bacs;self.address = address
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(name = data["name"],iban = data["iban"],bacs = data["bacs"],address = data["address"])


class PaymentInitiationRecipientCreateResponse:
    
    def __init__(self, recipient_id: str, request_id: RequestId) :
        
        self.recipient_id = recipient_id;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(recipient_id = data["recipient_id"],request_id = data["request_id"])


class PaymentInitiationRefundStatus:
    
    def __init__(self, payment_initiation_refund_status: str) :
        
        self.payment_initiation_refund_status = payment_initiation_refund_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentInitiationPaymentReverseResponse:
    
    def __init__(self, refund_id: str, status: PaymentInitiationRefundStatus, request_id: RequestId) :
        
        self.refund_id = refund_id;self.status = status;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(refund_id = data["refund_id"],status = data["status"],request_id = data["request_id"])


class PaymentInitiationRecipientGetRequest:
    
    def __init__(self, recipient_id: str) :
        
        self.recipient_id = recipient_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(recipient_id = data["recipient_id"])


class PaymentInitiationRecipientGetResponse:
    
    def __init__(self, payment_initiation_recipient_get_response: Any) :
        
        self.payment_initiation_recipient_get_response = payment_initiation_recipient_get_response
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentInitiationRecipient:
    
    def __init__(self, recipient_id: str, name: str, address: Optional[PaymentInitiationAddress], iban: Optional[str], bacs: Optional[RecipientBacsNullable]) :
        
        self.recipient_id = recipient_id;self.name = name;self.address = address;self.iban = iban;self.bacs = bacs
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(recipient_id = data["recipient_id"],name = data["name"],address = data["address"],iban = data["iban"],bacs = data["bacs"])


class PaymentInitiationRecipientListRequest:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class PaymentInitiationRecipientListResponse:
    
    def __init__(self, recipients: List[PaymentInitiationRecipient], request_id: RequestId) :
        
        self.recipients = recipients;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(recipients = data["recipients"],request_id = data["request_id"])


class PaymentInitiationPaymentCreateRequest:
    
    def __init__(self, recipient_id: str, reference: str, amount: PaymentAmount, schedule: ExternalPaymentScheduleRequest, options: Optional[ExternalPaymentOptions]) :
        
        self.recipient_id = recipient_id;self.reference = reference;self.amount = amount;self.schedule = schedule;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(recipient_id = data["recipient_id"],reference = data["reference"],amount = data["amount"],schedule = data["schedule"],options = data["options"])


class PaymentInitiationPaymentReverseRequest:
    
    def __init__(self, payment_id: str, idempotency_key: WalletTransactionIdempotencyKey, reference: str) :
        
        self.payment_id = payment_id;self.idempotency_key = idempotency_key;self.reference = reference
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(payment_id = data["payment_id"],idempotency_key = data["idempotency_key"],reference = data["reference"])


class PaymentInitiationPaymentCreateStatus:
    
    def __init__(self, payment_initiation_payment_create_status: str) :
        
        self.payment_initiation_payment_create_status = payment_initiation_payment_create_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentInitiationPaymentCreateResponse:
    
    def __init__(self, payment_id: str, status: PaymentInitiationPaymentCreateStatus, request_id: RequestId) :
        
        self.payment_id = payment_id;self.status = status;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(payment_id = data["payment_id"],status = data["status"],request_id = data["request_id"])


class SandboxItemResetLoginRequest:
    
    def __init__(self, access_token: AccessToken) :
        
        self.access_token = access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"])


class SandboxItemResetLoginResponse:
    
    def __init__(self, reset_login: bool, request_id: RequestId) :
        
        self.reset_login = reset_login;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(reset_login = data["reset_login"],request_id = data["request_id"])


class SandboxItemSetVerificationStatusRequest:
    
    def __init__(self, access_token: AccessToken, account_id: str, verification_status: str) :
        
        self.access_token = access_token;self.account_id = account_id;self.verification_status = verification_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],account_id = data["account_id"],verification_status = data["verification_status"])


class SandboxItemSetVerificationStatusResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class UserCreateRequest:
    
    def __init__(self, client_user_id: str) :
        
        self.client_user_id = client_user_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(client_user_id = data["client_user_id"])


class UserCreateResponse:
    
    def __init__(self, user_token: UserToken, user_id: UserId, request_id: RequestId) :
        
        self.user_token = user_token;self.user_id = user_id;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(user_token = data["user_token"],user_id = data["user_id"],request_id = data["request_id"])


class PaymentInitiationPaymentGetRequest:
    
    def __init__(self, payment_id: str) :
        
        self.payment_id = payment_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(payment_id = data["payment_id"])


class PaymentInitiationPaymentGetResponse:
    
    def __init__(self, payment_initiation_payment_get_response: Any) :
        
        self.payment_initiation_payment_get_response = payment_initiation_payment_get_response
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentInitiationPaymentStatus:
    
    def __init__(self, payment_initiation_payment_status: str) :
        
        self.payment_initiation_payment_status = payment_initiation_payment_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentInitiationPayment:
    
    def __init__(self, payment_id: str, amount: PaymentAmount, status: PaymentInitiationPaymentStatus, recipient_id: str, reference: str, adjusted_reference: Optional[str], last_status_update: str, schedule: Optional[ExternalPaymentScheduleGet], refund_details: Optional[ExternalPaymentRefundDetails], bacs: Optional[SenderBacsNullable], iban: Optional[str], refund_ids: List[str], wallet_id: Optional[str], scheme: Optional[PaymentScheme], adjusted_scheme: Optional[PaymentScheme], consent_id: Optional[str]) :
        
        self.payment_id = payment_id;self.amount = amount;self.status = status;self.recipient_id = recipient_id;self.reference = reference;self.adjusted_reference = adjusted_reference;self.last_status_update = last_status_update;self.schedule = schedule;self.refund_details = refund_details;self.bacs = bacs;self.iban = iban;self.refund_ids = refund_ids;self.wallet_id = wallet_id;self.scheme = scheme;self.adjusted_scheme = adjusted_scheme;self.consent_id = consent_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(payment_id = data["payment_id"],amount = data["amount"],status = data["status"],recipient_id = data["recipient_id"],reference = data["reference"],adjusted_reference = data["adjusted_reference"],last_status_update = data["last_status_update"],schedule = data["schedule"],refund_details = data["refund_details"],bacs = data["bacs"],iban = data["iban"],refund_ids = data["refund_ids"],wallet_id = data["wallet_id"],scheme = data["scheme"],adjusted_scheme = data["adjusted_scheme"],consent_id = data["consent_id"])


class PaymentInitiationPaymentTokenCreateRequest:
    
    def __init__(self, payment_id: str) :
        
        self.payment_id = payment_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(payment_id = data["payment_id"])


class PaymentInitiationPaymentTokenCreateResponse:
    
    def __init__(self, payment_token: str, payment_token_expiration_time: str, request_id: RequestId) :
        
        self.payment_token = payment_token;self.payment_token_expiration_time = payment_token_expiration_time;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(payment_token = data["payment_token"],payment_token_expiration_time = data["payment_token_expiration_time"],request_id = data["request_id"])


class PaymentInitiationConsentCreateRequest:
    
    def __init__(self, recipient_id: str, reference: str, scopes: List[PaymentInitiationConsentScope], constraints: PaymentInitiationConsentConstraints, options: Optional[ExternalPaymentInitiationConsentOptions]) :
        
        self.recipient_id = recipient_id;self.reference = reference;self.scopes = scopes;self.constraints = constraints;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(recipient_id = data["recipient_id"],reference = data["reference"],scopes = data["scopes"],constraints = data["constraints"],options = data["options"])


class PaymentInitiationConsentCreateResponse:
    
    def __init__(self, consent_id: str, status: PaymentInitiationConsentStatus, request_id: RequestId) :
        
        self.consent_id = consent_id;self.status = status;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(consent_id = data["consent_id"],status = data["status"],request_id = data["request_id"])


class PaymentInitiationConsentGetRequest:
    
    def __init__(self, consent_id: str) :
        
        self.consent_id = consent_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(consent_id = data["consent_id"])


class PaymentInitiationConsentGetResponse:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class PaymentInitiationConsent:
    
    def __init__(self, consent_id: str, status: PaymentInitiationConsentStatus, created_at: str, recipient_id: str, reference: str, constraints: PaymentInitiationConsentConstraints, scopes: List[PaymentInitiationConsentScope]) :
        
        self.consent_id = consent_id;self.status = status;self.created_at = created_at;self.recipient_id = recipient_id;self.reference = reference;self.constraints = constraints;self.scopes = scopes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(consent_id = data["consent_id"],status = data["status"],created_at = data["created_at"],recipient_id = data["recipient_id"],reference = data["reference"],constraints = data["constraints"],scopes = data["scopes"])


class PaymentInitiationConsentStatus:
    
    def __init__(self, payment_initiation_consent_status: str) :
        
        self.payment_initiation_consent_status = payment_initiation_consent_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentInitiationConsentRevokeRequest:
    
    def __init__(self, consent_id: str) :
        
        self.consent_id = consent_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(consent_id = data["consent_id"])


class PaymentInitiationConsentRevokeResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class PaymentInitiationConsentPaymentExecuteRequest:
    
    def __init__(self, consent_id: str, amount: PaymentAmount, idempotency_key: ConsentPaymentIdempotencyKey) :
        
        self.consent_id = consent_id;self.amount = amount;self.idempotency_key = idempotency_key
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(consent_id = data["consent_id"],amount = data["amount"],idempotency_key = data["idempotency_key"])


class PaymentInitiationConsentPaymentExecuteResponse:
    
    def __init__(self, payment_id: str, status: PaymentInitiationPaymentStatus, request_id: RequestId) :
        
        self.payment_id = payment_id;self.status = status;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(payment_id = data["payment_id"],status = data["status"],request_id = data["request_id"])


class PaymentInitiationPaymentListRequest:
    
    def __init__(self, count: Optional[int], cursor: Optional[str], consent_id: Optional[str]) :
        
        self.count = count;self.cursor = cursor;self.consent_id = consent_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(count = data["count"],cursor = data["cursor"],consent_id = data["consent_id"])


class PaymentInitiationPaymentListResponse:
    
    def __init__(self, payments: List[PaymentInitiationPayment], next_cursor: Optional[str], request_id: RequestId) :
        
        self.payments = payments;self.next_cursor = next_cursor;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(payments = data["payments"],next_cursor = data["next_cursor"],request_id = data["request_id"])


class AssetReportCreateRequest:
    
    def __init__(self, access_tokens: List[AccessToken], days_requested: int, options: AssetReportCreateRequestOptions) :
        
        self.access_tokens = access_tokens;self.days_requested = days_requested;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_tokens = data["access_tokens"],days_requested = data["days_requested"],options = data["options"])


class AssetReportCreateRequestOptions:
    
    def __init__(self, client_report_id: Optional[str], webhook: Optional[str], include_fast_report: Optional[bool], products: List[str], user: AssetReportUser) :
        
        self.client_report_id = client_report_id;self.webhook = webhook;self.include_fast_report = include_fast_report;self.products = products;self.user = user
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(client_report_id = data["client_report_id"],webhook = data["webhook"],include_fast_report = data["include_fast_report"],products = data["products"],user = data["user"])


class AssetReportCreateResponse:
    
    def __init__(self, asset_report_token: AssetReportToken, asset_report_id: AssetReportId, request_id: RequestId) :
        
        self.asset_report_token = asset_report_token;self.asset_report_id = asset_report_id;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_report_token = data["asset_report_token"],asset_report_id = data["asset_report_id"],request_id = data["request_id"])


class AssetReportRefreshRequest:
    
    def __init__(self, asset_report_token: AssetReportRefreshAssetReportToken, days_requested: Optional[int], options: AssetReportRefreshRequestOptions) :
        
        self.asset_report_token = asset_report_token;self.days_requested = days_requested;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_report_token = data["asset_report_token"],days_requested = data["days_requested"],options = data["options"])


class AssetReportRefreshRequestOptions:
    
    def __init__(self, client_report_id: Optional[str], webhook: Optional[str], user: AssetReportUser) :
        
        self.client_report_id = client_report_id;self.webhook = webhook;self.user = user
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(client_report_id = data["client_report_id"],webhook = data["webhook"],user = data["user"])


class AssetReportRefreshResponse:
    
    def __init__(self, asset_report_id: AssetReportId, asset_report_token: AssetReportToken, request_id: RequestId) :
        
        self.asset_report_id = asset_report_id;self.asset_report_token = asset_report_token;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_report_id = data["asset_report_id"],asset_report_token = data["asset_report_token"],request_id = data["request_id"])


class AssetReportRelayRefreshRequest:
    
    def __init__(self, asset_relay_token: str, webhook: Optional[str]) :
        
        self.asset_relay_token = asset_relay_token;self.webhook = webhook
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_relay_token = data["asset_relay_token"],webhook = data["webhook"])


class AssetReportRelayRefreshResponse:
    
    def __init__(self, asset_relay_token: str, asset_report_id: AssetReportId, request_id: RequestId) :
        
        self.asset_relay_token = asset_relay_token;self.asset_report_id = asset_report_id;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_relay_token = data["asset_relay_token"],asset_report_id = data["asset_report_id"],request_id = data["request_id"])


class AssetReportRemoveRequest:
    
    def __init__(self, asset_report_token: AssetReportToken) :
        
        self.asset_report_token = asset_report_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_report_token = data["asset_report_token"])


class AssetReportRemoveResponse:
    
    def __init__(self, removed: bool, request_id: RequestId) :
        
        self.removed = removed;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(removed = data["removed"],request_id = data["request_id"])


class AssetReportFilterRequest:
    
    def __init__(self, asset_report_token: AssetReportToken, account_ids_to_exclude: List[str]) :
        
        self.asset_report_token = asset_report_token;self.account_ids_to_exclude = account_ids_to_exclude
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_report_token = data["asset_report_token"],account_ids_to_exclude = data["account_ids_to_exclude"])


class AssetReportFilterResponse:
    
    def __init__(self, asset_report_token: AssetReportToken, asset_report_id: AssetReportId, request_id: RequestId) :
        
        self.asset_report_token = asset_report_token;self.asset_report_id = asset_report_id;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_report_token = data["asset_report_token"],asset_report_id = data["asset_report_id"],request_id = data["request_id"])


class AssetReportGetRequest:
    
    def __init__(self, asset_report_token: AssetReportToken, include_insights: bool, fast_report: bool) :
        
        self.asset_report_token = asset_report_token;self.include_insights = include_insights;self.fast_report = fast_report
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_report_token = data["asset_report_token"],include_insights = data["include_insights"],fast_report = data["fast_report"])


class AssetReportGetResponse:
    
    def __init__(self, report: AssetReport, warnings: List[Warning], request_id: RequestId) :
        
        self.report = report;self.warnings = warnings;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(report = data["report"],warnings = data["warnings"],request_id = data["request_id"])


class AssetReportPdfGetRequest:
    
    def __init__(self, asset_report_token: AssetReportToken) :
        
        self.asset_report_token = asset_report_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_report_token = data["asset_report_token"])


class AssetReportPdfGetResponse:
    
    def __init__(self, asset_report_pdf_get_response: str) :
        
        self.asset_report_pdf_get_response = asset_report_pdf_get_response
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class AssetReportAuditCopyCreateRequest:
    
    def __init__(self, asset_report_token: AssetReportToken, auditor_id: str) :
        
        self.asset_report_token = asset_report_token;self.auditor_id = auditor_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_report_token = data["asset_report_token"],auditor_id = data["auditor_id"])


class AssetReportAuditCopyCreateResponse:
    
    def __init__(self, audit_copy_token: str, request_id: RequestId) :
        
        self.audit_copy_token = audit_copy_token;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(audit_copy_token = data["audit_copy_token"],request_id = data["request_id"])


class AssetReportAuditCopyRemoveRequest:
    
    def __init__(self, audit_copy_token: str) :
        
        self.audit_copy_token = audit_copy_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(audit_copy_token = data["audit_copy_token"])


class AssetReportAuditCopyRemoveResponse:
    
    def __init__(self, removed: bool, request_id: RequestId) :
        
        self.removed = removed;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(removed = data["removed"],request_id = data["request_id"])


class AssetReportRelayCreateRequest:
    
    def __init__(self, asset_report_token: AssetReportToken, secondary_client_id: str, webhook: Optional[str]) :
        
        self.asset_report_token = asset_report_token;self.secondary_client_id = secondary_client_id;self.webhook = webhook
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_report_token = data["asset_report_token"],secondary_client_id = data["secondary_client_id"],webhook = data["webhook"])


class AssetReportRelayCreateResponse:
    
    def __init__(self, asset_relay_token: str, request_id: RequestId) :
        
        self.asset_relay_token = asset_relay_token;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_relay_token = data["asset_relay_token"],request_id = data["request_id"])


class AssetReportRelayGetRequest:
    
    def __init__(self, asset_relay_token: str) :
        
        self.asset_relay_token = asset_relay_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_relay_token = data["asset_relay_token"])


class AssetReportRelayRemoveRequest:
    
    def __init__(self, asset_relay_token: str) :
        
        self.asset_relay_token = asset_relay_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_relay_token = data["asset_relay_token"])


class AssetReportRelayRemoveResponse:
    
    def __init__(self, removed: bool, request_id: RequestId) :
        
        self.removed = removed;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(removed = data["removed"],request_id = data["request_id"])


class InvestmentsHoldingsGetRequest:
    
    def __init__(self, access_token: AccessToken, options: InvestmentHoldingsGetRequestOptions) :
        
        self.access_token = access_token;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],options = data["options"])


class InvestmentHoldingsGetRequestOptions:
    
    def __init__(self, account_ids: List[str]) :
        
        self.account_ids = account_ids
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_ids = data["account_ids"])


class InvestmentsHoldingsGetResponse:
    
    def __init__(self, accounts: List[AccountBase], holdings: List[Holding], securities: List[Security], item: Item, request_id: RequestId) :
        
        self.accounts = accounts;self.holdings = holdings;self.securities = securities;self.item = item;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(accounts = data["accounts"],holdings = data["holdings"],securities = data["securities"],item = data["item"],request_id = data["request_id"])


class InvestmentsTransactionsGetRequest:
    
    def __init__(self, access_token: AccessToken, start_date: str, end_date: str, options: InvestmentsTransactionsGetRequestOptions) :
        
        self.access_token = access_token;self.start_date = start_date;self.end_date = end_date;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],start_date = data["start_date"],end_date = data["end_date"],options = data["options"])


class InvestmentsTransactionsGetRequestOptions:
    
    def __init__(self, account_ids: List[str], count: int, offset: int) :
        
        self.account_ids = account_ids;self.count = count;self.offset = offset
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_ids = data["account_ids"],count = data["count"],offset = data["offset"])


class InvestmentsTransactionsGetResponse:
    
    def __init__(self, item: Item, accounts: List[AccountBase], securities: List[Security], investment_transactions: List[InvestmentTransaction], total_investment_transactions: int, request_id: RequestId) :
        
        self.item = item;self.accounts = accounts;self.securities = securities;self.investment_transactions = investment_transactions;self.total_investment_transactions = total_investment_transactions;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(item = data["item"],accounts = data["accounts"],securities = data["securities"],investment_transactions = data["investment_transactions"],total_investment_transactions = data["total_investment_transactions"],request_id = data["request_id"])


class ProcessorTokenCreateRequest:
    
    def __init__(self, access_token: AccessToken, account_id: str, processor: str) :
        
        self.access_token = access_token;self.account_id = account_id;self.processor = processor
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],account_id = data["account_id"],processor = data["processor"])


class ProcessorTokenCreateResponse:
    
    def __init__(self, processor_token: str, request_id: RequestId) :
        
        self.processor_token = processor_token;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(processor_token = data["processor_token"],request_id = data["request_id"])


class ProcessorStripeBankAccountTokenCreateRequest:
    
    def __init__(self, access_token: AccessToken, account_id: str) :
        
        self.access_token = access_token;self.account_id = account_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],account_id = data["account_id"])


class ProcessorStripeBankAccountTokenCreateResponse:
    
    def __init__(self, stripe_bank_account_token: str, request_id: RequestId) :
        
        self.stripe_bank_account_token = stripe_bank_account_token;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(stripe_bank_account_token = data["stripe_bank_account_token"],request_id = data["request_id"])


class ProcessorApexProcessorTokenCreateRequest:
    
    def __init__(self, access_token: AccessToken, account_id: str) :
        
        self.access_token = access_token;self.account_id = account_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],account_id = data["account_id"])


class DepositSwitchCreateRequest:
    
    def __init__(self, target_access_token: str, target_account_id: str, country_code: Optional[str], options: DepositSwitchCreateRequestOptions) :
        
        self.target_access_token = target_access_token;self.target_account_id = target_account_id;self.country_code = country_code;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(target_access_token = data["target_access_token"],target_account_id = data["target_account_id"],country_code = data["country_code"],options = data["options"])


class DepositSwitchCreateRequestOptions:
    
    def __init__(self, webhook: Optional[str], transaction_item_access_tokens: List[AccessToken]) :
        
        self.webhook = webhook;self.transaction_item_access_tokens = transaction_item_access_tokens
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook = data["webhook"],transaction_item_access_tokens = data["transaction_item_access_tokens"])


class DepositSwitchCreateResponse:
    
    def __init__(self, deposit_switch_id: str, request_id: RequestId) :
        
        self.deposit_switch_id = deposit_switch_id;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(deposit_switch_id = data["deposit_switch_id"],request_id = data["request_id"])


class DepositSwitchTokenCreateRequest:
    
    def __init__(self, deposit_switch_id: str) :
        
        self.deposit_switch_id = deposit_switch_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(deposit_switch_id = data["deposit_switch_id"])


class DepositSwitchTokenCreateResponse:
    
    def __init__(self, deposit_switch_token: str, deposit_switch_token_expiration_time: str, request_id: RequestId) :
        
        self.deposit_switch_token = deposit_switch_token;self.deposit_switch_token_expiration_time = deposit_switch_token_expiration_time;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(deposit_switch_token = data["deposit_switch_token"],deposit_switch_token_expiration_time = data["deposit_switch_token_expiration_time"],request_id = data["request_id"])


class LinkTokenGetRequest:
    
    def __init__(self, link_token: str) :
        
        self.link_token = link_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(link_token = data["link_token"])


class LinkTokenCreateRequest:
    
    def __init__(self, client_name: str, language: str, country_codes: List[CountryCode], user: LinkTokenCreateRequestUser, products: List[Products], additional_consented_products: List[Products], webhook: str, access_token: str, link_customization_name: str, redirect_uri: str, android_package_name: str, institution_data: LinkTokenCreateInstitutionData, account_filters: LinkTokenAccountFilters, eu_config: LinkTokenEuConfig, institution_id: str, payment_initiation: LinkTokenCreateRequestPaymentInitiation, deposit_switch: LinkTokenCreateRequestDepositSwitch, income_verification: LinkTokenCreateRequestIncomeVerification, auth: LinkTokenCreateRequestAuth, transfer: LinkTokenCreateRequestTransfer, update: LinkTokenCreateRequestUpdate, identity_verification: LinkTokenCreateRequestIdentityVerification, user_token: str) :
        
        self.client_name = client_name;self.language = language;self.country_codes = country_codes;self.user = user;self.products = products;self.additional_consented_products = additional_consented_products;self.webhook = webhook;self.access_token = access_token;self.link_customization_name = link_customization_name;self.redirect_uri = redirect_uri;self.android_package_name = android_package_name;self.institution_data = institution_data;self.account_filters = account_filters;self.eu_config = eu_config;self.institution_id = institution_id;self.payment_initiation = payment_initiation;self.deposit_switch = deposit_switch;self.income_verification = income_verification;self.auth = auth;self.transfer = transfer;self.update = update;self.identity_verification = identity_verification;self.user_token = user_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(client_name = data["client_name"],language = data["language"],country_codes = data["country_codes"],user = data["user"],products = data["products"],additional_consented_products = data["additional_consented_products"],webhook = data["webhook"],access_token = data["access_token"],link_customization_name = data["link_customization_name"],redirect_uri = data["redirect_uri"],android_package_name = data["android_package_name"],institution_data = data["institution_data"],account_filters = data["account_filters"],eu_config = data["eu_config"],institution_id = data["institution_id"],payment_initiation = data["payment_initiation"],deposit_switch = data["deposit_switch"],income_verification = data["income_verification"],auth = data["auth"],transfer = data["transfer"],update = data["update"],identity_verification = data["identity_verification"],user_token = data["user_token"])


class LinkTokenAccountFilters:
    
    def __init__(self, depository: DepositoryFilter, credit: CreditFilter, loan: LoanFilter, investment: InvestmentFilter) :
        
        self.depository = depository;self.credit = credit;self.loan = loan;self.investment = investment
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(depository = data["depository"],credit = data["credit"],loan = data["loan"],investment = data["investment"])


class LinkTokenEuConfig:
    
    def __init__(self, headless: bool) :
        
        self.headless = headless
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(headless = data["headless"])


class LinkTokenCreateRequestPaymentInitiation:
    
    def __init__(self, payment_id: str, consent_id: str) :
        
        self.payment_id = payment_id;self.consent_id = consent_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(payment_id = data["payment_id"],consent_id = data["consent_id"])


class LinkTokenCreateRequestDepositSwitch:
    
    def __init__(self, deposit_switch_id: str) :
        
        self.deposit_switch_id = deposit_switch_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(deposit_switch_id = data["deposit_switch_id"])


class LinkTokenCreateRequestTransfer:
    
    def __init__(self, intent_id: str, payment_profile_id: str) :
        
        self.intent_id = intent_id;self.payment_profile_id = payment_profile_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(intent_id = data["intent_id"],payment_profile_id = data["payment_profile_id"])


class LinkTokenCreateRequestUserStatedIncomeSource:
    
    def __init__(self, employer: str, category: UserStatedIncomeSourceCategory, pay_per_cycle: float, pay_annual: float, pay_type: UserStatedIncomeSourcePayType, pay_frequency: UserStatedIncomeSourceFrequency) :
        
        self.employer = employer;self.category = category;self.pay_per_cycle = pay_per_cycle;self.pay_annual = pay_annual;self.pay_type = pay_type;self.pay_frequency = pay_frequency
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(employer = data["employer"],category = data["category"],pay_per_cycle = data["pay_per_cycle"],pay_annual = data["pay_annual"],pay_type = data["pay_type"],pay_frequency = data["pay_frequency"])


class UserStatedIncomeSourceCategory:
    
    def __init__(self, user_stated_income_source_category: str) :
        
        self.user_stated_income_source_category = user_stated_income_source_category
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class UserStatedIncomeSourceFrequency:
    
    def __init__(self, user_stated_income_source_frequency: str) :
        
        self.user_stated_income_source_frequency = user_stated_income_source_frequency
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class UserStatedIncomeSourcePayType:
    
    def __init__(self, user_stated_income_source_pay_type: str) :
        
        self.user_stated_income_source_pay_type = user_stated_income_source_pay_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class LinkTokenCreateRequestAuth:
    
    def __init__(self, auth_type_select_enabled: bool, automated_microdeposits_enabled: bool, instant_match_enabled: bool, same_day_microdeposits_enabled: bool, flow_type: str) :
        
        self.auth_type_select_enabled = auth_type_select_enabled;self.automated_microdeposits_enabled = automated_microdeposits_enabled;self.instant_match_enabled = instant_match_enabled;self.same_day_microdeposits_enabled = same_day_microdeposits_enabled;self.flow_type = flow_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(auth_type_select_enabled = data["auth_type_select_enabled"],automated_microdeposits_enabled = data["automated_microdeposits_enabled"],instant_match_enabled = data["instant_match_enabled"],same_day_microdeposits_enabled = data["same_day_microdeposits_enabled"],flow_type = data["flow_type"])


class LinkTokenCreateRequestIdentityVerification:
    
    def __init__(self, template_id: IdentityVerificationTemplateId, consent: Any, gave_consent: IdentityVerificationConsent) :
        
        self.template_id = template_id;self.consent = consent;self.gave_consent = gave_consent
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(template_id = data["template_id"],consent = data["consent"],gave_consent = data["gave_consent"])


class LinkTokenCreateInstitutionData:
    
    def __init__(self, routing_number: str) :
        
        self.routing_number = routing_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(routing_number = data["routing_number"])


class LinkTokenCreateRequestUser:
    
    def __init__(self, client_user_id: str, legal_name: str, name: Any, phone_number: str, phone_number_verified_time: str, email_address: str, email_address_verified_time: str, ssn: str, date_of_birth: str, address: Optional[UserAddress], id_number: Optional[UserIdNumber]) :
        
        self.client_user_id = client_user_id;self.legal_name = legal_name;self.name = name;self.phone_number = phone_number;self.phone_number_verified_time = phone_number_verified_time;self.email_address = email_address;self.email_address_verified_time = email_address_verified_time;self.ssn = ssn;self.date_of_birth = date_of_birth;self.address = address;self.id_number = id_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(client_user_id = data["client_user_id"],legal_name = data["legal_name"],name = data["name"],phone_number = data["phone_number"],phone_number_verified_time = data["phone_number_verified_time"],email_address = data["email_address"],email_address_verified_time = data["email_address_verified_time"],ssn = data["ssn"],date_of_birth = data["date_of_birth"],address = data["address"],id_number = data["id_number"])


class LinkTokenCreateRequestUpdate:
    
    def __init__(self, account_selection_enabled: bool) :
        
        self.account_selection_enabled = account_selection_enabled
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_selection_enabled = data["account_selection_enabled"])


class LinkTokenCreateRequestAccountSubtypes:
    
    def __init__(self, depository: LinkTokenCreateDepositoryFilter, credit: LinkTokenCreateCreditFilter, loan: LinkTokenCreateLoanFilter, investment: LinkTokenCreateInvestmentFilter) :
        
        self.depository = depository;self.credit = credit;self.loan = loan;self.investment = investment
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(depository = data["depository"],credit = data["credit"],loan = data["loan"],investment = data["investment"])


class LinkTokenCreateDepositoryFilter:
    
    def __init__(self, account_subtypes: DepositoryAccountSubtypes) :
        
        self.account_subtypes = account_subtypes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_subtypes = data["account_subtypes"])


class LinkTokenCreateCreditFilter:
    
    def __init__(self, account_subtypes: CreditAccountSubtypes) :
        
        self.account_subtypes = account_subtypes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_subtypes = data["account_subtypes"])


class LinkTokenCreateLoanFilter:
    
    def __init__(self, account_subtypes: LoanAccountSubtypes) :
        
        self.account_subtypes = account_subtypes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_subtypes = data["account_subtypes"])


class LinkTokenCreateInvestmentFilter:
    
    def __init__(self, account_subtypes: InvestmentAccountSubtypes) :
        
        self.account_subtypes = account_subtypes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_subtypes = data["account_subtypes"])


class LinkTokenGetResponse:
    
    def __init__(self, link_token: str, created_at: Optional[str], expiration: Optional[str], metadata: LinkTokenGetMetadataResponse, request_id: RequestId) :
        
        self.link_token = link_token;self.created_at = created_at;self.expiration = expiration;self.metadata = metadata;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(link_token = data["link_token"],created_at = data["created_at"],expiration = data["expiration"],metadata = data["metadata"],request_id = data["request_id"])


class LinkTokenGetMetadataResponse:
    
    def __init__(self, initial_products: List[Products], webhook: Optional[str], country_codes: List[CountryCode], language: Optional[str], institution_data: LinkTokenCreateInstitutionData, account_filters: AccountFiltersResponse, redirect_uri: Optional[str], client_name: Optional[str]) :
        
        self.initial_products = initial_products;self.webhook = webhook;self.country_codes = country_codes;self.language = language;self.institution_data = institution_data;self.account_filters = account_filters;self.redirect_uri = redirect_uri;self.client_name = client_name
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(initial_products = data["initial_products"],webhook = data["webhook"],country_codes = data["country_codes"],language = data["language"],institution_data = data["institution_data"],account_filters = data["account_filters"],redirect_uri = data["redirect_uri"],client_name = data["client_name"])


class LinkTokenCreateResponse:
    
    def __init__(self, link_token: str, expiration: str, request_id: RequestId) :
        
        self.link_token = link_token;self.expiration = expiration;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(link_token = data["link_token"],expiration = data["expiration"],request_id = data["request_id"])


class PlaidError:
    
    def __init__(self, plaid_error: Optional[Any]) :
        
        self.plaid_error = plaid_error
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Error:
    
    def __init__(self, error_type: str, error_code: str, error_message: str, display_message: Optional[str], request_id: str, causes: List[Any], status: Optional[float], documentation_url: str, suggested_action: Optional[str]) :
        
        self.error_type = error_type;self.error_code = error_code;self.error_message = error_message;self.display_message = display_message;self.request_id = request_id;self.causes = causes;self.status = status;self.documentation_url = documentation_url;self.suggested_action = suggested_action
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(error_type = data["error_type"],error_code = data["error_code"],error_message = data["error_message"],display_message = data["display_message"],request_id = data["request_id"],causes = data["causes"],status = data["status"],documentation_url = data["documentation_url"],suggested_action = data["suggested_action"])


class AccountType:
    
    def __init__(self, account_type: str) :
        
        self.account_type = account_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class OverrideAccountType:
    
    def __init__(self, override_account_type: str) :
        
        self.override_account_type = override_account_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class AccountBase:
    
    def __init__(self, account_id: str, balances: AccountBalance, mask: Optional[str], name: str, official_name: Optional[str], type_: AccountType, subtype: Optional[AccountSubtype], verification_status: str) :
        
        self.account_id = account_id;self.balances = balances;self.mask = mask;self.name = name;self.official_name = official_name;self.type_ = type_;self.subtype = subtype;self.verification_status = verification_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],balances = data["balances"],mask = data["mask"],name = data["name"],official_name = data["official_name"],type_ = data["type_"],subtype = data["subtype"],verification_status = data["verification_status"])


class AccountBalance:
    
    def __init__(self, available: Optional[float], current: Optional[float], limit: Optional[float], iso_currency_code: Optional[str], unofficial_currency_code: Optional[str], last_updated_datetime: Optional[str]) :
        
        self.available = available;self.current = current;self.limit = limit;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code;self.last_updated_datetime = last_updated_datetime
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(available = data["available"],current = data["current"],limit = data["limit"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"],last_updated_datetime = data["last_updated_datetime"])


class AccountSubtype:
    
    def __init__(self, account_subtype: Optional[str]) :
        
        self.account_subtype = account_subtype
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class NumbersAch:
    
    def __init__(self, account_id: str, account: str, routing: str, wire_routing: Optional[str]) :
        
        self.account_id = account_id;self.account = account;self.routing = routing;self.wire_routing = wire_routing
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],account = data["account"],routing = data["routing"],wire_routing = data["wire_routing"])


class NumbersAchNullable:
    
    def __init__(self, numbers_ach_nullable: Optional[Any]) :
        
        self.numbers_ach_nullable = numbers_ach_nullable
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class NumbersEft:
    
    def __init__(self, account_id: str, account: str, institution: str, branch: str) :
        
        self.account_id = account_id;self.account = account;self.institution = institution;self.branch = branch
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],account = data["account"],institution = data["institution"],branch = data["branch"])


class NumbersEftNullable:
    
    def __init__(self, numbers_eft_nullable: Optional[Any]) :
        
        self.numbers_eft_nullable = numbers_eft_nullable
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class NumbersInternational:
    
    def __init__(self, account_id: str, iban: str, bic: str) :
        
        self.account_id = account_id;self.iban = iban;self.bic = bic
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],iban = data["iban"],bic = data["bic"])


class NumbersInternationalNullable:
    
    def __init__(self, numbers_international_nullable: Optional[Any]) :
        
        self.numbers_international_nullable = numbers_international_nullable
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class NumbersBacs:
    
    def __init__(self, account_id: str, account: str, sort_code: str) :
        
        self.account_id = account_id;self.account = account;self.sort_code = sort_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],account = data["account"],sort_code = data["sort_code"])


class NumbersBacsNullable:
    
    def __init__(self, numbers_bacs_nullable: Optional[Any]) :
        
        self.numbers_bacs_nullable = numbers_bacs_nullable
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class NumbersInternationalIban:
    
    def __init__(self, iban: NumbersIban, bic: str) :
        
        self.iban = iban;self.bic = bic
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(iban = data["iban"],bic = data["bic"])


class NumbersIban:
    
    def __init__(self, numbers_iban: str) :
        
        self.numbers_iban = numbers_iban
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class NumbersIbanNullable:
    
    def __init__(self, numbers_iban_nullable: Optional[str]) :
        
        self.numbers_iban_nullable = numbers_iban_nullable
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class RecipientBacs:
    
    def __init__(self, account: str, sort_code: str) :
        
        self.account = account;self.sort_code = sort_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account = data["account"],sort_code = data["sort_code"])


class RecipientBacsNullable:
    
    def __init__(self, recipient_bacs_nullable: Optional[Any]) :
        
        self.recipient_bacs_nullable = recipient_bacs_nullable
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class SenderBacsNullable:
    
    def __init__(self, sender_bacs_nullable: Optional[Any]) :
        
        self.sender_bacs_nullable = sender_bacs_nullable
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentInitiationOptionalRestrictionBacs:
    
    def __init__(self, payment_initiation_optional_restriction_bacs: Optional[Any]) :
        
        self.payment_initiation_optional_restriction_bacs = payment_initiation_optional_restriction_bacs
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreditPullId:
    
    def __init__(self, credit_pull_id: str) :
        
        self.credit_pull_id = credit_pull_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class RemovedTransaction:
    
    def __init__(self, transaction_id: str) :
        
        self.transaction_id = transaction_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transaction_id = data["transaction_id"])


class RequestId:
    
    def __init__(self, request_id: str) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransactionsRuleDetails:
    
    def __init__(self, field: TransactionsRuleField, type_: TransactionsRuleType, query: str) :
        
        self.field = field;self.type_ = type_;self.query = query
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(field = data["field"],type_ = data["type_"],query = data["query"])


class TransactionsRuleField:
    
    def __init__(self, transactions_rule_field: str) :
        
        self.transactions_rule_field = transactions_rule_field
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransactionsRuleType:
    
    def __init__(self, transactions_rule_type: str) :
        
        self.transactions_rule_type = transactions_rule_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransactionsCategoryRule:
    
    def __init__(self, id: str, item_id: str, created_at: str, personal_finance_category: str, rule_details: TransactionsRuleDetails) :
        
        self.id = id;self.item_id = item_id;self.created_at = created_at;self.personal_finance_category = personal_finance_category;self.rule_details = rule_details
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],item_id = data["item_id"],created_at = data["created_at"],personal_finance_category = data["personal_finance_category"],rule_details = data["rule_details"])


class TransactionBase:
    
    def __init__(self, transaction_type: str, pending_transaction_id: Optional[str], category_id: Optional[str], category: Optional[List[str]], location: Location, payment_meta: PaymentMeta, account_owner: Optional[str], name: str, original_description: Optional[str], account_id: str, amount: float, iso_currency_code: Optional[str], unofficial_currency_code: Optional[str], date: str, pending: bool, transaction_id: str, merchant_name: Optional[str], check_number: Optional[str]) :
        
        self.transaction_type = transaction_type;self.pending_transaction_id = pending_transaction_id;self.category_id = category_id;self.category = category;self.location = location;self.payment_meta = payment_meta;self.account_owner = account_owner;self.name = name;self.original_description = original_description;self.account_id = account_id;self.amount = amount;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code;self.date = date;self.pending = pending;self.transaction_id = transaction_id;self.merchant_name = merchant_name;self.check_number = check_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transaction_type = data["transaction_type"],pending_transaction_id = data["pending_transaction_id"],category_id = data["category_id"],category = data["category"],location = data["location"],payment_meta = data["payment_meta"],account_owner = data["account_owner"],name = data["name"],original_description = data["original_description"],account_id = data["account_id"],amount = data["amount"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"],date = data["date"],pending = data["pending"],transaction_id = data["transaction_id"],merchant_name = data["merchant_name"],check_number = data["check_number"])


class Transaction:
    
    def __init__(self, transaction: Any) :
        
        self.transaction = transaction
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Location:
    
    def __init__(self, address: Optional[str], city: Optional[str], region: Optional[str], postal_code: Optional[str], country: Optional[str], lat: Optional[float], lon: Optional[float], store_number: Optional[str]) :
        
        self.address = address;self.city = city;self.region = region;self.postal_code = postal_code;self.country = country;self.lat = lat;self.lon = lon;self.store_number = store_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(address = data["address"],city = data["city"],region = data["region"],postal_code = data["postal_code"],country = data["country"],lat = data["lat"],lon = data["lon"],store_number = data["store_number"])


class TransactionStream:
    
    def __init__(self, account_id: str, stream_id: str, category_id: str, category: List[str], description: str, merchant_name: Optional[str], first_date: str, last_date: str, frequency: RecurringTransactionFrequency, transaction_ids: List[str], average_amount: TransactionStreamAmount, last_amount: TransactionStreamAmount, is_active: bool, status: TransactionStreamStatus, personal_finance_category: Optional[PersonalFinanceCategory]) :
        
        self.account_id = account_id;self.stream_id = stream_id;self.category_id = category_id;self.category = category;self.description = description;self.merchant_name = merchant_name;self.first_date = first_date;self.last_date = last_date;self.frequency = frequency;self.transaction_ids = transaction_ids;self.average_amount = average_amount;self.last_amount = last_amount;self.is_active = is_active;self.status = status;self.personal_finance_category = personal_finance_category
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],stream_id = data["stream_id"],category_id = data["category_id"],category = data["category"],description = data["description"],merchant_name = data["merchant_name"],first_date = data["first_date"],last_date = data["last_date"],frequency = data["frequency"],transaction_ids = data["transaction_ids"],average_amount = data["average_amount"],last_amount = data["last_amount"],is_active = data["is_active"],status = data["status"],personal_finance_category = data["personal_finance_category"])


class TransactionStreamAmount:
    
    def __init__(self, amount: float, iso_currency_code: Optional[str], unofficial_currency_code: Optional[str]) :
        
        self.amount = amount;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(amount = data["amount"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"])


class RecurringTransactionFrequency:
    
    def __init__(self, recurring_transaction_frequency: str) :
        
        self.recurring_transaction_frequency = recurring_transaction_frequency
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransactionStreamStatus:
    
    def __init__(self, transaction_stream_status: str) :
        
        self.transaction_stream_status = transaction_stream_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Institution:
    
    def __init__(self, institution_id: str, name: str, products: List[Products], country_codes: List[CountryCode], url: Optional[str], primary_color: Optional[str], logo: Optional[str], routing_numbers: List[str], oauth: bool, status: Optional[InstitutionStatus], payment_initiation_metadata: Optional[PaymentInitiationMetadata], auth_metadata: Optional[AuthMetadata]) :
        
        self.institution_id = institution_id;self.name = name;self.products = products;self.country_codes = country_codes;self.url = url;self.primary_color = primary_color;self.logo = logo;self.routing_numbers = routing_numbers;self.oauth = oauth;self.status = status;self.payment_initiation_metadata = payment_initiation_metadata;self.auth_metadata = auth_metadata
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(institution_id = data["institution_id"],name = data["name"],products = data["products"],country_codes = data["country_codes"],url = data["url"],primary_color = data["primary_color"],logo = data["logo"],routing_numbers = data["routing_numbers"],oauth = data["oauth"],status = data["status"],payment_initiation_metadata = data["payment_initiation_metadata"],auth_metadata = data["auth_metadata"])


class InstitutionStatus:
    
    def __init__(self, item_logins: ProductStatus, transactions_updates: ProductStatus, auth: ProductStatus, identity: ProductStatus, investments_updates: ProductStatus, liabilities_updates: ProductStatus, liabilities: ProductStatus, investments: ProductStatus, health_incidents: Optional[List[HealthIncident]]) :
        
        self.item_logins = item_logins;self.transactions_updates = transactions_updates;self.auth = auth;self.identity = identity;self.investments_updates = investments_updates;self.liabilities_updates = liabilities_updates;self.liabilities = liabilities;self.investments = investments;self.health_incidents = health_incidents
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(item_logins = data["item_logins"],transactions_updates = data["transactions_updates"],auth = data["auth"],identity = data["identity"],investments_updates = data["investments_updates"],liabilities_updates = data["liabilities_updates"],liabilities = data["liabilities"],investments = data["investments"],health_incidents = data["health_incidents"])


class CountryCode:
    
    def __init__(self, country_code: str) :
        
        self.country_code = country_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentMeta:
    
    def __init__(self, reference_number: Optional[str], ppd_id: Optional[str], payee: Optional[str], by_order_of: Optional[str], payer: Optional[str], payment_method: Optional[str], payment_processor: Optional[str], reason: Optional[str]) :
        
        self.reference_number = reference_number;self.ppd_id = ppd_id;self.payee = payee;self.by_order_of = by_order_of;self.payer = payer;self.payment_method = payment_method;self.payment_processor = payment_processor;self.reason = reason
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(reference_number = data["reference_number"],ppd_id = data["ppd_id"],payee = data["payee"],by_order_of = data["by_order_of"],payer = data["payer"],payment_method = data["payment_method"],payment_processor = data["payment_processor"],reason = data["reason"])


class TransactionCode:
    
    def __init__(self, transaction_code: Optional[str]) :
        
        self.transaction_code = transaction_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Category:
    
    def __init__(self, category_id: str, group: str, hierarchy: List[str]) :
        
        self.category_id = category_id;self.group = group;self.hierarchy = hierarchy
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(category_id = data["category_id"],group = data["group"],hierarchy = data["hierarchy"])


class PersonalFinanceCategory:
    
    def __init__(self, primary: str, detailed: str) :
        
        self.primary = primary;self.detailed = detailed
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(primary = data["primary"],detailed = data["detailed"])


class UserToken:
    
    def __init__(self, user_token: str) :
        
        self.user_token = user_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class AccessToken:
    
    def __init__(self, access_token: str) :
        
        self.access_token = access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class AccessTokenNullable:
    
    def __init__(self, access_token_nullable: Optional[str]) :
        
        self.access_token_nullable = access_token_nullable
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferAccessToken:
    
    def __init__(self, transfer_access_token: str) :
        
        self.transfer_access_token = transfer_access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class BankTransferAccessToken:
    
    def __init__(self, bank_transfer_access_token: str) :
        
        self.bank_transfer_access_token = bank_transfer_access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ApiSecret:
    
    def __init__(self, api_secret: str) :
        
        self.api_secret = api_secret
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ApiClientId:
    
    def __init__(self, api_client_id: str) :
        
        self.api_client_id = api_client_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ScreeningStatusUpdatedWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, screening_id: Any) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.screening_id = screening_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],screening_id = data["screening_id"])


class EntityScreeningStatusUpdatedWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, screening_id: Any) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.screening_id = screening_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],screening_id = data["screening_id"])


class IdentityVerificationStepUpdatedWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, identity_verification_id: Any) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.identity_verification_id = identity_verification_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],identity_verification_id = data["identity_verification_id"])


class IdentityVerificationRetriedWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, identity_verification_id: Any) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.identity_verification_id = identity_verification_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],identity_verification_id = data["identity_verification_id"])


class IdentityVerificationStatusUpdatedWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, identity_verification_id: Any) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.identity_verification_id = identity_verification_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],identity_verification_id = data["identity_verification_id"])


class TransactionsRemovedWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, error: Optional[PlaidError], removed_transactions: List[str], item_id: ItemId) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.error = error;self.removed_transactions = removed_transactions;self.item_id = item_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],error = data["error"],removed_transactions = data["removed_transactions"],item_id = data["item_id"])


class DefaultUpdateWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, error: Optional[PlaidError], new_transactions: float, item_id: str) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.error = error;self.new_transactions = new_transactions;self.item_id = item_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],error = data["error"],new_transactions = data["new_transactions"],item_id = data["item_id"])


class SyncUpdatesAvailableWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, item_id: ItemId, initial_update_complete: bool, historical_update_complete: bool) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.item_id = item_id;self.initial_update_complete = initial_update_complete;self.historical_update_complete = historical_update_complete
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],item_id = data["item_id"],initial_update_complete = data["initial_update_complete"],historical_update_complete = data["historical_update_complete"])


class RecurringTransactionsUpdateWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, item_id: ItemId, account_ids: List[str]) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.item_id = item_id;self.account_ids = account_ids
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],item_id = data["item_id"],account_ids = data["account_ids"])


class IdentityDefaultUpdateWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, item_id: ItemId, account_ids_with_updated_identity: AccountIdsWithUpdatedIdentity, error: Optional[PlaidError]) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.item_id = item_id;self.account_ids_with_updated_identity = account_ids_with_updated_identity;self.error = error
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],item_id = data["item_id"],account_ids_with_updated_identity = data["account_ids_with_updated_identity"],error = data["error"])


class AccountIdsWithUpdatedIdentity:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class IdentityUpdateTypes:
    
    def __init__(self, identity_update_types: str) :
        
        self.identity_update_types = identity_update_types
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class HistoricalUpdateWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, error: Optional[PlaidError], new_transactions: float, item_id: ItemId) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.error = error;self.new_transactions = new_transactions;self.item_id = item_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],error = data["error"],new_transactions = data["new_transactions"],item_id = data["item_id"])


class InitialUpdateWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, error: Optional[str], new_transactions: float, item_id: ItemId) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.error = error;self.new_transactions = new_transactions;self.item_id = item_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],error = data["error"],new_transactions = data["new_transactions"],item_id = data["item_id"])


class PhoneNumber:
    
    def __init__(self, data: str, primary: bool, type_: str) :
        
        self.data = data;self.primary = primary;self.type_ = type_
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data = data["data"],primary = data["primary"],type_ = data["type_"])


class Email:
    
    def __init__(self, data: str, primary: bool, type_: str) :
        
        self.data = data;self.primary = primary;self.type_ = type_
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data = data["data"],primary = data["primary"],type_ = data["type_"])


class Address:
    
    def __init__(self, data: AddressData, primary: bool) :
        
        self.data = data;self.primary = primary
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data = data["data"],primary = data["primary"])


class AddressNullable:
    
    def __init__(self, address_nullable: Optional[Any]) :
        
        self.address_nullable = address_nullable
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class AddressDataNullable:
    
    def __init__(self, address_data_nullable: Optional[Any]) :
        
        self.address_data_nullable = address_data_nullable
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class AddressData:
    
    def __init__(self, city: str, region: Optional[str], street: str, postal_code: Optional[str], country: Optional[str]) :
        
        self.city = city;self.region = region;self.street = street;self.postal_code = postal_code;self.country = country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(city = data["city"],region = data["region"],street = data["street"],postal_code = data["postal_code"],country = data["country"])


class ProcessorToken:
    
    def __init__(self, processor_token: str) :
        
        self.processor_token = processor_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class HistoricalBalance:
    
    def __init__(self, date: str, current: float, iso_currency_code: Optional[str], unofficial_currency_code: Optional[str]) :
        
        self.date = date;self.current = current;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(date = data["date"],current = data["current"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"])


class Owner:
    
    def __init__(self, names: List[str], phone_numbers: List[PhoneNumber], emails: List[Email], addresses: List[Address]) :
        
        self.names = names;self.phone_numbers = phone_numbers;self.emails = emails;self.addresses = addresses
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(names = data["names"],phone_numbers = data["phone_numbers"],emails = data["emails"],addresses = data["addresses"])


class OwnerOverride:
    
    def __init__(self, names: List[str], phone_numbers: List[PhoneNumber], emails: List[Email], addresses: List[Address]) :
        
        self.names = names;self.phone_numbers = phone_numbers;self.emails = emails;self.addresses = addresses
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(names = data["names"],phone_numbers = data["phone_numbers"],emails = data["emails"],addresses = data["addresses"])


class LiabilitiesObject:
    
    def __init__(self, credit: Optional[List[CreditCardLiability]], mortgage: Optional[List[MortgageLiability]], student: Optional[List[StudentLoan]]) :
        
        self.credit = credit;self.mortgage = mortgage;self.student = student
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(credit = data["credit"],mortgage = data["mortgage"],student = data["student"])


class StudentLoan:
    
    def __init__(self, account_id: Optional[str], account_number: Optional[str], disbursement_dates: Optional[List[str]], expected_payoff_date: Optional[str], guarantor: Optional[str], interest_rate_percentage: float, is_overdue: Optional[bool], last_payment_amount: Optional[float], last_payment_date: Optional[str], last_statement_issue_date: Optional[str], loan_name: Optional[str], loan_status: StudentLoanStatus, minimum_payment_amount: Optional[float], next_payment_due_date: Optional[str], origination_date: Optional[str], origination_principal_amount: Optional[float], outstanding_interest_amount: Optional[float], payment_reference_number: Optional[str], pslf_status: PslfStatus, repayment_plan: StudentRepaymentPlan, sequence_number: Optional[str], servicer_address: ServicerAddressData, ytd_interest_paid: Optional[float], ytd_principal_paid: Optional[float]) :
        
        self.account_id = account_id;self.account_number = account_number;self.disbursement_dates = disbursement_dates;self.expected_payoff_date = expected_payoff_date;self.guarantor = guarantor;self.interest_rate_percentage = interest_rate_percentage;self.is_overdue = is_overdue;self.last_payment_amount = last_payment_amount;self.last_payment_date = last_payment_date;self.last_statement_issue_date = last_statement_issue_date;self.loan_name = loan_name;self.loan_status = loan_status;self.minimum_payment_amount = minimum_payment_amount;self.next_payment_due_date = next_payment_due_date;self.origination_date = origination_date;self.origination_principal_amount = origination_principal_amount;self.outstanding_interest_amount = outstanding_interest_amount;self.payment_reference_number = payment_reference_number;self.pslf_status = pslf_status;self.repayment_plan = repayment_plan;self.sequence_number = sequence_number;self.servicer_address = servicer_address;self.ytd_interest_paid = ytd_interest_paid;self.ytd_principal_paid = ytd_principal_paid
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],account_number = data["account_number"],disbursement_dates = data["disbursement_dates"],expected_payoff_date = data["expected_payoff_date"],guarantor = data["guarantor"],interest_rate_percentage = data["interest_rate_percentage"],is_overdue = data["is_overdue"],last_payment_amount = data["last_payment_amount"],last_payment_date = data["last_payment_date"],last_statement_issue_date = data["last_statement_issue_date"],loan_name = data["loan_name"],loan_status = data["loan_status"],minimum_payment_amount = data["minimum_payment_amount"],next_payment_due_date = data["next_payment_due_date"],origination_date = data["origination_date"],origination_principal_amount = data["origination_principal_amount"],outstanding_interest_amount = data["outstanding_interest_amount"],payment_reference_number = data["payment_reference_number"],pslf_status = data["pslf_status"],repayment_plan = data["repayment_plan"],sequence_number = data["sequence_number"],servicer_address = data["servicer_address"],ytd_interest_paid = data["ytd_interest_paid"],ytd_principal_paid = data["ytd_principal_paid"])


class CreditCardLiability:
    
    def __init__(self, account_id: Optional[str], aprs: List[Apr], is_overdue: Optional[bool], last_payment_amount: Optional[float], last_payment_date: Optional[str], last_statement_issue_date: Optional[str], last_statement_balance: Optional[float], minimum_payment_amount: Optional[float], next_payment_due_date: Optional[str]) :
        
        self.account_id = account_id;self.aprs = aprs;self.is_overdue = is_overdue;self.last_payment_amount = last_payment_amount;self.last_payment_date = last_payment_date;self.last_statement_issue_date = last_statement_issue_date;self.last_statement_balance = last_statement_balance;self.minimum_payment_amount = minimum_payment_amount;self.next_payment_due_date = next_payment_due_date
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],aprs = data["aprs"],is_overdue = data["is_overdue"],last_payment_amount = data["last_payment_amount"],last_payment_date = data["last_payment_date"],last_statement_issue_date = data["last_statement_issue_date"],last_statement_balance = data["last_statement_balance"],minimum_payment_amount = data["minimum_payment_amount"],next_payment_due_date = data["next_payment_due_date"])


class MortgageLiability:
    
    def __init__(self, account_id: str, account_number: str, current_late_fee: Optional[float], escrow_balance: Optional[float], has_pmi: Optional[bool], has_prepayment_penalty: Optional[bool], interest_rate: MortgageInterestRate, last_payment_amount: Optional[float], last_payment_date: Optional[str], loan_type_description: Optional[str], loan_term: Optional[str], maturity_date: Optional[str], next_monthly_payment: Optional[float], next_payment_due_date: Optional[str], origination_date: Optional[str], origination_principal_amount: Optional[float], past_due_amount: Optional[float], property_address: MortgagePropertyAddress, ytd_interest_paid: Optional[float], ytd_principal_paid: Optional[float]) :
        
        self.account_id = account_id;self.account_number = account_number;self.current_late_fee = current_late_fee;self.escrow_balance = escrow_balance;self.has_pmi = has_pmi;self.has_prepayment_penalty = has_prepayment_penalty;self.interest_rate = interest_rate;self.last_payment_amount = last_payment_amount;self.last_payment_date = last_payment_date;self.loan_type_description = loan_type_description;self.loan_term = loan_term;self.maturity_date = maturity_date;self.next_monthly_payment = next_monthly_payment;self.next_payment_due_date = next_payment_due_date;self.origination_date = origination_date;self.origination_principal_amount = origination_principal_amount;self.past_due_amount = past_due_amount;self.property_address = property_address;self.ytd_interest_paid = ytd_interest_paid;self.ytd_principal_paid = ytd_principal_paid
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],account_number = data["account_number"],current_late_fee = data["current_late_fee"],escrow_balance = data["escrow_balance"],has_pmi = data["has_pmi"],has_prepayment_penalty = data["has_prepayment_penalty"],interest_rate = data["interest_rate"],last_payment_amount = data["last_payment_amount"],last_payment_date = data["last_payment_date"],loan_type_description = data["loan_type_description"],loan_term = data["loan_term"],maturity_date = data["maturity_date"],next_monthly_payment = data["next_monthly_payment"],next_payment_due_date = data["next_payment_due_date"],origination_date = data["origination_date"],origination_principal_amount = data["origination_principal_amount"],past_due_amount = data["past_due_amount"],property_address = data["property_address"],ytd_interest_paid = data["ytd_interest_paid"],ytd_principal_paid = data["ytd_principal_paid"])


class MortgageInterestRate:
    
    def __init__(self, percentage: Optional[float], type_: Optional[str]) :
        
        self.percentage = percentage;self.type_ = type_
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(percentage = data["percentage"],type_ = data["type_"])


class MortgagePropertyAddress:
    
    def __init__(self, city: Optional[str], country: Optional[str], postal_code: Optional[str], region: Optional[str], street: Optional[str]) :
        
        self.city = city;self.country = country;self.postal_code = postal_code;self.region = region;self.street = street
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(city = data["city"],country = data["country"],postal_code = data["postal_code"],region = data["region"],street = data["street"])


class StudentLoanStatus:
    
    def __init__(self, end_date: Optional[str], type_: Optional[str]) :
        
        self.end_date = end_date;self.type_ = type_
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(end_date = data["end_date"],type_ = data["type_"])


class StudentRepaymentPlan:
    
    def __init__(self, description: Optional[str], type_: Optional[str]) :
        
        self.description = description;self.type_ = type_
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(description = data["description"],type_ = data["type_"])


class PslfStatus:
    
    def __init__(self, estimated_eligibility_date: Optional[str], payments_made: Optional[float], payments_remaining: Optional[float]) :
        
        self.estimated_eligibility_date = estimated_eligibility_date;self.payments_made = payments_made;self.payments_remaining = payments_remaining
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(estimated_eligibility_date = data["estimated_eligibility_date"],payments_made = data["payments_made"],payments_remaining = data["payments_remaining"])


class ServicerAddressData:
    
    def __init__(self, city: Optional[str], region: Optional[str], street: Optional[str], postal_code: Optional[str], country: Optional[str]) :
        
        self.city = city;self.region = region;self.street = street;self.postal_code = postal_code;self.country = country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(city = data["city"],region = data["region"],street = data["street"],postal_code = data["postal_code"],country = data["country"])


class Apr:
    
    def __init__(self, apr_percentage: float, apr_type: str, balance_subject_to_apr: Optional[float], interest_charge_amount: Optional[float]) :
        
        self.apr_percentage = apr_percentage;self.apr_type = apr_type;self.balance_subject_to_apr = balance_subject_to_apr;self.interest_charge_amount = interest_charge_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(apr_percentage = data["apr_percentage"],apr_type = data["apr_type"],balance_subject_to_apr = data["balance_subject_to_apr"],interest_charge_amount = data["interest_charge_amount"])


class AuthMetadata:
    
    def __init__(self, supported_methods: Optional[AuthSupportedMethods]) :
        
        self.supported_methods = supported_methods
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(supported_methods = data["supported_methods"])


class AuthSupportedMethods:
    
    def __init__(self, instant_auth: bool, instant_match: bool, automated_micro_deposits: bool) :
        
        self.instant_auth = instant_auth;self.instant_match = instant_match;self.automated_micro_deposits = automated_micro_deposits
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(instant_auth = data["instant_auth"],instant_match = data["instant_match"],automated_micro_deposits = data["automated_micro_deposits"])


class PaymentInitiationMetadata:
    
    def __init__(self, supports_international_payments: bool, supports_sepa_instant: bool, maximum_payment_amount: PaymentInitiationMaximumPaymentAmount, supports_refund_details: bool, standing_order_metadata: Optional[PaymentInitiationStandingOrderMetadata]) :
        
        self.supports_international_payments = supports_international_payments;self.supports_sepa_instant = supports_sepa_instant;self.maximum_payment_amount = maximum_payment_amount;self.supports_refund_details = supports_refund_details;self.standing_order_metadata = standing_order_metadata
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(supports_international_payments = data["supports_international_payments"],supports_sepa_instant = data["supports_sepa_instant"],maximum_payment_amount = data["maximum_payment_amount"],supports_refund_details = data["supports_refund_details"],standing_order_metadata = data["standing_order_metadata"])


class PaymentInitiationMaximumPaymentAmount:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class PaymentInitiationStandingOrderMetadata:
    
    def __init__(self, supports_standing_order_end_date: bool, supports_standing_order_negative_execution_days: bool, valid_standing_order_intervals: List[PaymentScheduleInterval]) :
        
        self.supports_standing_order_end_date = supports_standing_order_end_date;self.supports_standing_order_negative_execution_days = supports_standing_order_negative_execution_days;self.valid_standing_order_intervals = valid_standing_order_intervals
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(supports_standing_order_end_date = data["supports_standing_order_end_date"],supports_standing_order_negative_execution_days = data["supports_standing_order_negative_execution_days"],valid_standing_order_intervals = data["valid_standing_order_intervals"])


class PaymentInitiationAddress:
    
    def __init__(self, street: List[str], city: str, postal_code: str, country: str) :
        
        self.street = street;self.city = city;self.postal_code = postal_code;self.country = country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(street = data["street"],city = data["city"],postal_code = data["postal_code"],country = data["country"])


class ExternalPaymentScheduleBase:
    
    def __init__(self, interval: PaymentScheduleInterval, interval_execution_day: int, start_date: str, end_date: Optional[str], adjusted_start_date: Optional[str]) :
        
        self.interval = interval;self.interval_execution_day = interval_execution_day;self.start_date = start_date;self.end_date = end_date;self.adjusted_start_date = adjusted_start_date
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(interval = data["interval"],interval_execution_day = data["interval_execution_day"],start_date = data["start_date"],end_date = data["end_date"],adjusted_start_date = data["adjusted_start_date"])


class ExternalPaymentScheduleRequest:
    
    def __init__(self, external_payment_schedule_request: Any) :
        
        self.external_payment_schedule_request = external_payment_schedule_request
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentScheduleInterval:
    
    def __init__(self, payment_schedule_interval: str) :
        
        self.payment_schedule_interval = payment_schedule_interval
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentScheme:
    
    def __init__(self, payment_scheme: Optional[str]) :
        
        self.payment_scheme = payment_scheme
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentInitiationConsentScope:
    
    def __init__(self, payment_initiation_consent_scope: str) :
        
        self.payment_initiation_consent_scope = payment_initiation_consent_scope
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ExternalPaymentInitiationConsentOptions:
    
    def __init__(self, wallet_id: Optional[str], request_refund_details: Optional[bool], iban: Optional[str], bacs: Optional[PaymentInitiationOptionalRestrictionBacs]) :
        
        self.wallet_id = wallet_id;self.request_refund_details = request_refund_details;self.iban = iban;self.bacs = bacs
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(wallet_id = data["wallet_id"],request_refund_details = data["request_refund_details"],iban = data["iban"],bacs = data["bacs"])


class PaymentInitiationConsentConstraints:
    
    def __init__(self, valid_date_time: Optional[PaymentConsentValidDateTime], max_payment_amount: PaymentConsentMaxPaymentAmount, periodic_amounts: List[PaymentConsentPeriodicAmount]) :
        
        self.valid_date_time = valid_date_time;self.max_payment_amount = max_payment_amount;self.periodic_amounts = periodic_amounts
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(valid_date_time = data["valid_date_time"],max_payment_amount = data["max_payment_amount"],periodic_amounts = data["periodic_amounts"])


class PaymentConsentMaxPaymentAmount:
    
    def __init__(self, payment_consent_max_payment_amount: Any) :
        
        self.payment_consent_max_payment_amount = payment_consent_max_payment_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ConsentPaymentIdempotencyKey:
    
    def __init__(self, consent_payment_idempotency_key: str) :
        
        self.consent_payment_idempotency_key = consent_payment_idempotency_key
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ExternalPaymentOptions:
    
    def __init__(self, request_refund_details: Optional[bool], iban: Optional[str], bacs: Optional[PaymentInitiationOptionalRestrictionBacs], wallet_id: Optional[str], scheme: Optional[PaymentScheme]) :
        
        self.request_refund_details = request_refund_details;self.iban = iban;self.bacs = bacs;self.wallet_id = wallet_id;self.scheme = scheme
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_refund_details = data["request_refund_details"],iban = data["iban"],bacs = data["bacs"],wallet_id = data["wallet_id"],scheme = data["scheme"])


class ExternalPaymentRefundDetails:
    
    def __init__(self, name: str, iban: Optional[str], bacs: Optional[RecipientBacsNullable]) :
        
        self.name = name;self.iban = iban;self.bacs = bacs
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(name = data["name"],iban = data["iban"],bacs = data["bacs"])


class ExternalPaymentScheduleGet:
    
    def __init__(self, external_payment_schedule_get: Optional[Any]) :
        
        self.external_payment_schedule_get = external_payment_schedule_get
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Products:
    
    def __init__(self, products: str) :
        
        self.products = products
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ProductStatus:
    
    def __init__(self, status: str, last_status_change: str, breakdown: ProductStatusBreakdown) :
        
        self.status = status;self.last_status_change = last_status_change;self.breakdown = breakdown
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(status = data["status"],last_status_change = data["last_status_change"],breakdown = data["breakdown"])


class ProductStatusBreakdown:
    
    def __init__(self, success: float, error_plaid: float, error_institution: float, refresh_interval: str) :
        
        self.success = success;self.error_plaid = error_plaid;self.error_institution = error_institution;self.refresh_interval = refresh_interval
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(success = data["success"],error_plaid = data["error_plaid"],error_institution = data["error_institution"],refresh_interval = data["refresh_interval"])


class UserCustomPassword:
    
    def __init__(self, version: Optional[str], seed: str, override_accounts: List[OverrideAccounts], mfa: Mfa, recaptcha: str, force_error: str) :
        
        self.version = version;self.seed = seed;self.override_accounts = override_accounts;self.mfa = mfa;self.recaptcha = recaptcha;self.force_error = force_error
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(version = data["version"],seed = data["seed"],override_accounts = data["override_accounts"],mfa = data["mfa"],recaptcha = data["recaptcha"],force_error = data["force_error"])


class Mfa:
    
    def __init__(self, type_: str, question_rounds: float, questions_per_round: float, selection_rounds: float, selections_per_question: float) :
        
        self.type_ = type_;self.question_rounds = question_rounds;self.questions_per_round = questions_per_round;self.selection_rounds = selection_rounds;self.selections_per_question = selections_per_question
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(type_ = data["type_"],question_rounds = data["question_rounds"],questions_per_round = data["questions_per_round"],selection_rounds = data["selection_rounds"],selections_per_question = data["selections_per_question"])


class OverrideAccounts:
    
    def __init__(self, type_: OverrideAccountType, subtype: Optional[AccountSubtype], starting_balance: float, force_available_balance: float, currency: str, meta: Meta, numbers: Numbers, transactions: List[TransactionOverride], holdings: HoldingsOverride, investment_transactions: InvestmentsTransactionsOverride, identity: OwnerOverride, liability: LiabilityOverride, inflow_model: InflowModel, income: IncomeOverride) :
        
        self.type_ = type_;self.subtype = subtype;self.starting_balance = starting_balance;self.force_available_balance = force_available_balance;self.currency = currency;self.meta = meta;self.numbers = numbers;self.transactions = transactions;self.holdings = holdings;self.investment_transactions = investment_transactions;self.identity = identity;self.liability = liability;self.inflow_model = inflow_model;self.income = income
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(type_ = data["type_"],subtype = data["subtype"],starting_balance = data["starting_balance"],force_available_balance = data["force_available_balance"],currency = data["currency"],meta = data["meta"],numbers = data["numbers"],transactions = data["transactions"],holdings = data["holdings"],investment_transactions = data["investment_transactions"],identity = data["identity"],liability = data["liability"],inflow_model = data["inflow_model"],income = data["income"])


class Meta:
    
    def __init__(self, name: str, official_name: str, limit: float) :
        
        self.name = name;self.official_name = official_name;self.limit = limit
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(name = data["name"],official_name = data["official_name"],limit = data["limit"])


class Numbers:
    
    def __init__(self, account: str, ach_routing: str, ach_wire_routing: str, eft_institution: str, eft_branch: str, international_bic: str, international_iban: str, bacs_sort_code: str) :
        
        self.account = account;self.ach_routing = ach_routing;self.ach_wire_routing = ach_wire_routing;self.eft_institution = eft_institution;self.eft_branch = eft_branch;self.international_bic = international_bic;self.international_iban = international_iban;self.bacs_sort_code = bacs_sort_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account = data["account"],ach_routing = data["ach_routing"],ach_wire_routing = data["ach_wire_routing"],eft_institution = data["eft_institution"],eft_branch = data["eft_branch"],international_bic = data["international_bic"],international_iban = data["international_iban"],bacs_sort_code = data["bacs_sort_code"])


class TransactionOverride:
    
    def __init__(self, date_transacted: str, date_posted: str, amount: float, description: str, currency: str) :
        
        self.date_transacted = date_transacted;self.date_posted = date_posted;self.amount = amount;self.description = description;self.currency = currency
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(date_transacted = data["date_transacted"],date_posted = data["date_posted"],amount = data["amount"],description = data["description"],currency = data["currency"])


class SecurityOverride:
    
    def __init__(self, isin: str, cusip: str, sedol: str, name: str, ticker_symbol: str, currency: str) :
        
        self.isin = isin;self.cusip = cusip;self.sedol = sedol;self.name = name;self.ticker_symbol = ticker_symbol;self.currency = currency
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(isin = data["isin"],cusip = data["cusip"],sedol = data["sedol"],name = data["name"],ticker_symbol = data["ticker_symbol"],currency = data["currency"])


class HoldingsOverride:
    
    def __init__(self, institution_price: float, institution_price_as_of: str, cost_basis: float, quantity: float, currency: str, security: SecurityOverride) :
        
        self.institution_price = institution_price;self.institution_price_as_of = institution_price_as_of;self.cost_basis = cost_basis;self.quantity = quantity;self.currency = currency;self.security = security
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(institution_price = data["institution_price"],institution_price_as_of = data["institution_price_as_of"],cost_basis = data["cost_basis"],quantity = data["quantity"],currency = data["currency"],security = data["security"])


class InvestmentsTransactionsOverride:
    
    def __init__(self, date: str, name: str, quantity: float, price: float, fees: float, type_: str, currency: str, security: SecurityOverride) :
        
        self.date = date;self.name = name;self.quantity = quantity;self.price = price;self.fees = fees;self.type_ = type_;self.currency = currency;self.security = security
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(date = data["date"],name = data["name"],quantity = data["quantity"],price = data["price"],fees = data["fees"],type_ = data["type_"],currency = data["currency"],security = data["security"])


class LiabilityOverride:
    
    def __init__(self, type_: str, purchase_apr: float, cash_apr: float, balance_transfer_apr: float, special_apr: float, last_payment_amount: float, minimum_payment_amount: float, is_overdue: bool, origination_date: str, principal: float, nominal_apr: float, interest_capitalization_grace_period_months: float, repayment_model: StudentLoanRepaymentModel, expected_payoff_date: str, guarantor: str, is_federal: bool, loan_name: str, loan_status: StudentLoanStatus, payment_reference_number: str, pslf_status: PslfStatus, repayment_plan_description: str, repayment_plan_type: str, sequence_number: str, servicer_address: Address) :
        
        self.type_ = type_;self.purchase_apr = purchase_apr;self.cash_apr = cash_apr;self.balance_transfer_apr = balance_transfer_apr;self.special_apr = special_apr;self.last_payment_amount = last_payment_amount;self.minimum_payment_amount = minimum_payment_amount;self.is_overdue = is_overdue;self.origination_date = origination_date;self.principal = principal;self.nominal_apr = nominal_apr;self.interest_capitalization_grace_period_months = interest_capitalization_grace_period_months;self.repayment_model = repayment_model;self.expected_payoff_date = expected_payoff_date;self.guarantor = guarantor;self.is_federal = is_federal;self.loan_name = loan_name;self.loan_status = loan_status;self.payment_reference_number = payment_reference_number;self.pslf_status = pslf_status;self.repayment_plan_description = repayment_plan_description;self.repayment_plan_type = repayment_plan_type;self.sequence_number = sequence_number;self.servicer_address = servicer_address
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(type_ = data["type_"],purchase_apr = data["purchase_apr"],cash_apr = data["cash_apr"],balance_transfer_apr = data["balance_transfer_apr"],special_apr = data["special_apr"],last_payment_amount = data["last_payment_amount"],minimum_payment_amount = data["minimum_payment_amount"],is_overdue = data["is_overdue"],origination_date = data["origination_date"],principal = data["principal"],nominal_apr = data["nominal_apr"],interest_capitalization_grace_period_months = data["interest_capitalization_grace_period_months"],repayment_model = data["repayment_model"],expected_payoff_date = data["expected_payoff_date"],guarantor = data["guarantor"],is_federal = data["is_federal"],loan_name = data["loan_name"],loan_status = data["loan_status"],payment_reference_number = data["payment_reference_number"],pslf_status = data["pslf_status"],repayment_plan_description = data["repayment_plan_description"],repayment_plan_type = data["repayment_plan_type"],sequence_number = data["sequence_number"],servicer_address = data["servicer_address"])


class StudentLoanRepaymentModel:
    
    def __init__(self, type_: str, non_repayment_months: float, repayment_months: float) :
        
        self.type_ = type_;self.non_repayment_months = non_repayment_months;self.repayment_months = repayment_months
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(type_ = data["type_"],non_repayment_months = data["non_repayment_months"],repayment_months = data["repayment_months"])


class InflowModel:
    
    def __init__(self, type_: str, income_amount: float, payment_day_of_month: float, transaction_name: str, statement_day_of_month: str) :
        
        self.type_ = type_;self.income_amount = income_amount;self.payment_day_of_month = payment_day_of_month;self.transaction_name = transaction_name;self.statement_day_of_month = statement_day_of_month
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(type_ = data["type_"],income_amount = data["income_amount"],payment_day_of_month = data["payment_day_of_month"],transaction_name = data["transaction_name"],statement_day_of_month = data["statement_day_of_month"])


class IncomeOverride:
    
    def __init__(self, paystubs: List[PaystubOverride]) :
        
        self.paystubs = paystubs
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(paystubs = data["paystubs"])


class PaystubOverride:
    
    def __init__(self, employer: PaystubOverrideEmployer, employee: PaystubOverrideEmployee, income_breakdown: List[IncomeBreakdown], pay_period_details: PayPeriodDetails) :
        
        self.employer = employer;self.employee = employee;self.income_breakdown = income_breakdown;self.pay_period_details = pay_period_details
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(employer = data["employer"],employee = data["employee"],income_breakdown = data["income_breakdown"],pay_period_details = data["pay_period_details"])


class PaystubOverrideEmployer:
    
    def __init__(self, name: str) :
        
        self.name = name
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(name = data["name"])


class PaystubOverrideEmployee:
    
    def __init__(self, name: str, address: PaystubOverrideEmployeeAddress) :
        
        self.name = name;self.address = address
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(name = data["name"],address = data["address"])


class PaystubOverrideEmployeeAddress:
    
    def __init__(self, city: str, region: str, street: str, postal_code: str, country: str) :
        
        self.city = city;self.region = region;self.street = street;self.postal_code = postal_code;self.country = country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(city = data["city"],region = data["region"],street = data["street"],postal_code = data["postal_code"],country = data["country"])


class ItemId:
    
    def __init__(self, item_id: str) :
        
        self.item_id = item_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class UserId:
    
    def __init__(self, user_id: str) :
        
        self.user_id = user_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class AutomaticallyVerifiedWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, account_id: str, item_id: ItemId) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.account_id = account_id;self.item_id = item_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],account_id = data["account_id"],item_id = data["item_id"])


class JwtHeader:
    
    def __init__(self, id: str) :
        
        self.id = id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"])


class VerificationExpiredWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, item_id: ItemId, account_id: str) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.item_id = item_id;self.account_id = account_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],item_id = data["item_id"],account_id = data["account_id"])


class WebhookUpdateAcknowledgedWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, item_id: ItemId, new_webhook_url: str, error: Optional[PlaidError]) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.item_id = item_id;self.new_webhook_url = new_webhook_url;self.error = error
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],item_id = data["item_id"],new_webhook_url = data["new_webhook_url"],error = data["error"])


class PendingExpirationWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, item_id: ItemId, consent_expiration_time: str) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.item_id = item_id;self.consent_expiration_time = consent_expiration_time
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],item_id = data["item_id"],consent_expiration_time = data["consent_expiration_time"])


class ItemErrorWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, item_id: ItemId, error: Optional[PlaidError]) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.item_id = item_id;self.error = error
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],item_id = data["item_id"],error = data["error"])


class ItemProductReadyWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, item_id: ItemId, error: Optional[PlaidError]) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.item_id = item_id;self.error = error
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],item_id = data["item_id"],error = data["error"])


class RecaptchaRequiredError:
    
    def __init__(self, error_type: str, error_code: str, display_message: str, http_code: str, link_user_experience: str, common_causes: str, troubleshooting_steps: str) :
        
        self.error_type = error_type;self.error_code = error_code;self.display_message = display_message;self.http_code = http_code;self.link_user_experience = link_user_experience;self.common_causes = common_causes;self.troubleshooting_steps = troubleshooting_steps
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(error_type = data["error_type"],error_code = data["error_code"],display_message = data["display_message"],http_code = data["http_code"],link_user_experience = data["link_user_experience"],common_causes = data["common_causes"],troubleshooting_steps = data["troubleshooting_steps"])


class BankTransfersEventsUpdateWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"])


class TransferEventsUpdateWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"])


class InvestmentsDefaultUpdateWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, item_id: ItemId, error: Optional[PlaidError], new_investments_transactions: float, canceled_investments_transactions: float) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.item_id = item_id;self.error = error;self.new_investments_transactions = new_investments_transactions;self.canceled_investments_transactions = canceled_investments_transactions
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],item_id = data["item_id"],error = data["error"],new_investments_transactions = data["new_investments_transactions"],canceled_investments_transactions = data["canceled_investments_transactions"])


class HoldingsDefaultUpdateWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, item_id: ItemId, error: Optional[PlaidError], new_holdings: float, updated_holdings: float) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.item_id = item_id;self.error = error;self.new_holdings = new_holdings;self.updated_holdings = updated_holdings
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],item_id = data["item_id"],error = data["error"],new_holdings = data["new_holdings"],updated_holdings = data["updated_holdings"])


class LiabilitiesDefaultUpdateWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, item_id: ItemId, error: Optional[PlaidError], account_ids_with_new_liabilities: List[str], account_ids_with_updated_liabilities: LiabilitiesAccountIdsWithUpdatedLiabilities) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.item_id = item_id;self.error = error;self.account_ids_with_new_liabilities = account_ids_with_new_liabilities;self.account_ids_with_updated_liabilities = account_ids_with_updated_liabilities
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],item_id = data["item_id"],error = data["error"],account_ids_with_new_liabilities = data["account_ids_with_new_liabilities"],account_ids_with_updated_liabilities = data["account_ids_with_updated_liabilities"])


class LiabilitiesAccountIdsWithUpdatedLiabilities:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class AssetsProductReadyWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, asset_report_id: str) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.asset_report_id = asset_report_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],asset_report_id = data["asset_report_id"])


class AssetsErrorWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, error: Optional[PlaidError], asset_report_id: str) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.error = error;self.asset_report_id = asset_report_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],error = data["error"],asset_report_id = data["asset_report_id"])


class AssetsRelayWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, relay_event: RelayEvent, secondary_client_id: str, asset_relay_token: str, asset_report_id: str) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.relay_event = relay_event;self.secondary_client_id = secondary_client_id;self.asset_relay_token = asset_relay_token;self.asset_report_id = asset_report_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],relay_event = data["relay_event"],secondary_client_id = data["secondary_client_id"],asset_relay_token = data["asset_relay_token"],asset_report_id = data["asset_report_id"])


class RelayEvent:
    
    def __init__(self, relay_event: str) :
        
        self.relay_event = relay_event
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Cause:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class Warning:
    
    def __init__(self, warning_type: str, warning_code: str, cause: Cause) :
        
        self.warning_type = warning_type;self.warning_code = warning_code;self.cause = cause
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(warning_type = data["warning_type"],warning_code = data["warning_code"],cause = data["cause"])


class PaymentAmountCurrency:
    
    def __init__(self, payment_amount_currency: str) :
        
        self.payment_amount_currency = payment_amount_currency
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentAmount:
    
    def __init__(self, currency: PaymentAmountCurrency, value: float) :
        
        self.currency = currency;self.value = value
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(currency = data["currency"],value = data["value"])


class PaymentConsentValidDateTime:
    
    def __init__(self, from: Optional[str], to: Optional[str]) :
        
        self.from = from;self.to = to
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(from = data["from"],to = data["to"])


class PaymentConsentPeriodicAmount:
    
    def __init__(self, amount: PaymentConsentPeriodicAmountAmount, interval: PaymentConsentPeriodicInterval, alignment: PaymentConsentPeriodicAlignment) :
        
        self.amount = amount;self.interval = interval;self.alignment = alignment
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(amount = data["amount"],interval = data["interval"],alignment = data["alignment"])


class PaymentConsentPeriodicAmountAmount:
    
    def __init__(self, payment_consent_periodic_amount_amount: Any) :
        
        self.payment_consent_periodic_amount_amount = payment_consent_periodic_amount_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentConsentPeriodicInterval:
    
    def __init__(self, payment_consent_periodic_interval: str) :
        
        self.payment_consent_periodic_interval = payment_consent_periodic_interval
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentConsentPeriodicAlignment:
    
    def __init__(self, payment_consent_periodic_alignment: str) :
        
        self.payment_consent_periodic_alignment = payment_consent_periodic_alignment
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class AssetReportUser:
    
    def __init__(self, client_user_id: Optional[str], first_name: Optional[str], middle_name: Optional[str], last_name: Optional[str], ssn: Optional[str], phone_number: Optional[str], email: Optional[str]) :
        
        self.client_user_id = client_user_id;self.first_name = first_name;self.middle_name = middle_name;self.last_name = last_name;self.ssn = ssn;self.phone_number = phone_number;self.email = email
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(client_user_id = data["client_user_id"],first_name = data["first_name"],middle_name = data["middle_name"],last_name = data["last_name"],ssn = data["ssn"],phone_number = data["phone_number"],email = data["email"])


class AssetReportId:
    
    def __init__(self, asset_report_id: str) :
        
        self.asset_report_id = asset_report_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class AssetReportToken:
    
    def __init__(self, asset_report_token: str) :
        
        self.asset_report_token = asset_report_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class AssetReportRefreshAssetReportToken:
    
    def __init__(self, asset_report_refresh_asset_report_token: str) :
        
        self.asset_report_refresh_asset_report_token = asset_report_refresh_asset_report_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class StandaloneCurrencyCodeList:
    
    def __init__(self, iso_currency_code: str, unofficial_currency_code: UnofficialCurrencyCodeList) :
        
        self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"])


class UnofficialCurrencyCodeList:
    
    def __init__(self, unofficial_currency_code_list: str) :
        
        self.unofficial_currency_code_list = unofficial_currency_code_list
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class StandaloneAccountType:
    
    def __init__(self, depository: DepositoryAccount, credit: CreditAccount, loan: LoanAccount, investment: InvestmentAccountSubtypeStandalone, other: str) :
        
        self.depository = depository;self.credit = credit;self.loan = loan;self.investment = investment;self.other = other
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(depository = data["depository"],credit = data["credit"],loan = data["loan"],investment = data["investment"],other = data["other"])


class DepositoryAccount:
    
    def __init__(self, depository_account: str) :
        
        self.depository_account = depository_account
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreditAccount:
    
    def __init__(self, credit_account: str) :
        
        self.credit_account = credit_account
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class LoanAccount:
    
    def __init__(self, loan_account: str) :
        
        self.loan_account = loan_account
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class InvestmentAccountSubtypeStandalone:
    
    def __init__(self, investment_account_subtype_standalone: str) :
        
        self.investment_account_subtype_standalone = investment_account_subtype_standalone
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class AssetReport:
    
    def __init__(self, asset_report_id: AssetReportId, client_report_id: Optional[str], date_generated: str, days_requested: float, user: AssetReportUser, items: List[AssetReportItem]) :
        
        self.asset_report_id = asset_report_id;self.client_report_id = client_report_id;self.date_generated = date_generated;self.days_requested = days_requested;self.user = user;self.items = items
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(asset_report_id = data["asset_report_id"],client_report_id = data["client_report_id"],date_generated = data["date_generated"],days_requested = data["days_requested"],user = data["user"],items = data["items"])


class AssetReportItem:
    
    def __init__(self, item_id: ItemId, institution_name: str, institution_id: str, date_last_updated: str, accounts: List[AccountAssets]) :
        
        self.item_id = item_id;self.institution_name = institution_name;self.institution_id = institution_id;self.date_last_updated = date_last_updated;self.accounts = accounts
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(item_id = data["item_id"],institution_name = data["institution_name"],institution_id = data["institution_id"],date_last_updated = data["date_last_updated"],accounts = data["accounts"])


class PaymentStatusUpdateWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, payment_id: str, new_payment_status: PaymentInitiationPaymentStatus, old_payment_status: PaymentInitiationPaymentStatus, original_reference: Optional[str], adjusted_reference: Optional[str], original_start_date: Optional[str], adjusted_start_date: Optional[str], timestamp: str, error: Optional[PlaidError]) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.payment_id = payment_id;self.new_payment_status = new_payment_status;self.old_payment_status = old_payment_status;self.original_reference = original_reference;self.adjusted_reference = adjusted_reference;self.original_start_date = original_start_date;self.adjusted_start_date = adjusted_start_date;self.timestamp = timestamp;self.error = error
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],payment_id = data["payment_id"],new_payment_status = data["new_payment_status"],old_payment_status = data["old_payment_status"],original_reference = data["original_reference"],adjusted_reference = data["adjusted_reference"],original_start_date = data["original_start_date"],adjusted_start_date = data["adjusted_start_date"],timestamp = data["timestamp"],error = data["error"])


class Holding:
    
    def __init__(self, account_id: str, security_id: str, institution_price: float, institution_price_as_of: Optional[str], institution_price_datetime: Optional[str], institution_value: float, cost_basis: Optional[float], quantity: float, iso_currency_code: Optional[str], unofficial_currency_code: Optional[str]) :
        
        self.account_id = account_id;self.security_id = security_id;self.institution_price = institution_price;self.institution_price_as_of = institution_price_as_of;self.institution_price_datetime = institution_price_datetime;self.institution_value = institution_value;self.cost_basis = cost_basis;self.quantity = quantity;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],security_id = data["security_id"],institution_price = data["institution_price"],institution_price_as_of = data["institution_price_as_of"],institution_price_datetime = data["institution_price_datetime"],institution_value = data["institution_value"],cost_basis = data["cost_basis"],quantity = data["quantity"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"])


class Security:
    
    def __init__(self, security_id: str, isin: Optional[str], cusip: Optional[str], sedol: Optional[str], institution_security_id: Optional[str], institution_id: Optional[str], proxy_security_id: Optional[str], name: Optional[str], ticker_symbol: Optional[str], is_cash_equivalent: Optional[bool], type_: Optional[str], close_price: Optional[float], close_price_as_of: Optional[str], update_datetime: Optional[str], iso_currency_code: Optional[str], unofficial_currency_code: Optional[str]) :
        
        self.security_id = security_id;self.isin = isin;self.cusip = cusip;self.sedol = sedol;self.institution_security_id = institution_security_id;self.institution_id = institution_id;self.proxy_security_id = proxy_security_id;self.name = name;self.ticker_symbol = ticker_symbol;self.is_cash_equivalent = is_cash_equivalent;self.type_ = type_;self.close_price = close_price;self.close_price_as_of = close_price_as_of;self.update_datetime = update_datetime;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(security_id = data["security_id"],isin = data["isin"],cusip = data["cusip"],sedol = data["sedol"],institution_security_id = data["institution_security_id"],institution_id = data["institution_id"],proxy_security_id = data["proxy_security_id"],name = data["name"],ticker_symbol = data["ticker_symbol"],is_cash_equivalent = data["is_cash_equivalent"],type_ = data["type_"],close_price = data["close_price"],close_price_as_of = data["close_price_as_of"],update_datetime = data["update_datetime"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"])


class InvestmentTransactionType:
    
    def __init__(self, investment_transaction_type: str) :
        
        self.investment_transaction_type = investment_transaction_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class InvestmentTransactionSubtype:
    
    def __init__(self, investment_transaction_subtype: str) :
        
        self.investment_transaction_subtype = investment_transaction_subtype
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class InvestmentTransaction:
    
    def __init__(self, investment_transaction_id: str, cancel_transaction_id: Optional[str], account_id: str, security_id: Optional[str], date: str, name: str, quantity: float, amount: float, price: float, fees: Optional[float], type_: InvestmentTransactionType, subtype: InvestmentTransactionSubtype, iso_currency_code: Optional[str], unofficial_currency_code: Optional[str]) :
        
        self.investment_transaction_id = investment_transaction_id;self.cancel_transaction_id = cancel_transaction_id;self.account_id = account_id;self.security_id = security_id;self.date = date;self.name = name;self.quantity = quantity;self.amount = amount;self.price = price;self.fees = fees;self.type_ = type_;self.subtype = subtype;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(investment_transaction_id = data["investment_transaction_id"],cancel_transaction_id = data["cancel_transaction_id"],account_id = data["account_id"],security_id = data["security_id"],date = data["date"],name = data["name"],quantity = data["quantity"],amount = data["amount"],price = data["price"],fees = data["fees"],type_ = data["type_"],subtype = data["subtype"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"])


class StandaloneInvestmentTransactionType:
    
    def __init__(self, buy: StandaloneInvestmentTransactionBuyType, sell: StandaloneInvestmentTransactionSellType, cancel: str, cash: StandaloneInvestmentTransactionCashType, fee: StandaloneInvestmentTransactionFeeType, transfer: StandaloneInvestmentTransactionTransferType) :
        
        self.buy = buy;self.sell = sell;self.cancel = cancel;self.cash = cash;self.fee = fee;self.transfer = transfer
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(buy = data["buy"],sell = data["sell"],cancel = data["cancel"],cash = data["cash"],fee = data["fee"],transfer = data["transfer"])


class StandaloneInvestmentTransactionBuyType:
    
    def __init__(self, standalone_investment_transaction_buy_type: str) :
        
        self.standalone_investment_transaction_buy_type = standalone_investment_transaction_buy_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class StandaloneInvestmentTransactionCashType:
    
    def __init__(self, standalone_investment_transaction_cash_type: str) :
        
        self.standalone_investment_transaction_cash_type = standalone_investment_transaction_cash_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class StandaloneInvestmentTransactionFeeType:
    
    def __init__(self, standalone_investment_transaction_fee_type: str) :
        
        self.standalone_investment_transaction_fee_type = standalone_investment_transaction_fee_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class StandaloneInvestmentTransactionSellType:
    
    def __init__(self, standalone_investment_transaction_sell_type: str) :
        
        self.standalone_investment_transaction_sell_type = standalone_investment_transaction_sell_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class StandaloneInvestmentTransactionTransferType:
    
    def __init__(self, standalone_investment_transaction_transfer_type: str) :
        
        self.standalone_investment_transaction_transfer_type = standalone_investment_transaction_transfer_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class AccountSubtypes:
    
    def __init__(self, account_subtypes: List[Optional[AccountSubtype]]) :
        
        self.account_subtypes = account_subtypes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(Optional[AccountSubtype].from_json(d) for d in data)


class UserPermissionRevokedWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, item_id: ItemId, error: Optional[PlaidError]) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.item_id = item_id;self.error = error
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],item_id = data["item_id"],error = data["error"])


class DepositSwitchGetRequest:
    
    def __init__(self, deposit_switch_id: str) :
        
        self.deposit_switch_id = deposit_switch_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(deposit_switch_id = data["deposit_switch_id"])


class DepositSwitchGetResponse:
    
    def __init__(self, deposit_switch_id: str, target_account_id: Optional[str], target_item_id: Optional[str], state: str, switch_method: Optional[str], account_has_multiple_allocations: Optional[bool], is_allocated_remainder: Optional[bool], percent_allocated: Optional[float], amount_allocated: Optional[float], employer_name: Optional[str], employer_id: Optional[str], institution_name: Optional[str], institution_id: Optional[str], date_created: str, date_completed: Optional[str], request_id: RequestId) :
        
        self.deposit_switch_id = deposit_switch_id;self.target_account_id = target_account_id;self.target_item_id = target_item_id;self.state = state;self.switch_method = switch_method;self.account_has_multiple_allocations = account_has_multiple_allocations;self.is_allocated_remainder = is_allocated_remainder;self.percent_allocated = percent_allocated;self.amount_allocated = amount_allocated;self.employer_name = employer_name;self.employer_id = employer_id;self.institution_name = institution_name;self.institution_id = institution_id;self.date_created = date_created;self.date_completed = date_completed;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(deposit_switch_id = data["deposit_switch_id"],target_account_id = data["target_account_id"],target_item_id = data["target_item_id"],state = data["state"],switch_method = data["switch_method"],account_has_multiple_allocations = data["account_has_multiple_allocations"],is_allocated_remainder = data["is_allocated_remainder"],percent_allocated = data["percent_allocated"],amount_allocated = data["amount_allocated"],employer_name = data["employer_name"],employer_id = data["employer_id"],institution_name = data["institution_name"],institution_id = data["institution_id"],date_created = data["date_created"],date_completed = data["date_completed"],request_id = data["request_id"])


class DepositSwitchStateUpdateWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, state: str, deposit_switch_id: str) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.state = state;self.deposit_switch_id = deposit_switch_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],state = data["state"],deposit_switch_id = data["deposit_switch_id"])


class AssetReportAuditCopyGetRequest:
    
    def __init__(self, audit_copy_token: str) :
        
        self.audit_copy_token = audit_copy_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(audit_copy_token = data["audit_copy_token"])


class TransferGetRequest:
    
    def __init__(self, transfer_id: TransferId) :
        
        self.transfer_id = transfer_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transfer_id = data["transfer_id"])


class BankTransferGetRequest:
    
    def __init__(self, bank_transfer_id: BankTransferId) :
        
        self.bank_transfer_id = bank_transfer_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(bank_transfer_id = data["bank_transfer_id"])


class TransferGetResponse:
    
    def __init__(self, transfer: Transfer, request_id: RequestId) :
        
        self.transfer = transfer;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transfer = data["transfer"],request_id = data["request_id"])


class BankTransferGetResponse:
    
    def __init__(self, bank_transfer: BankTransfer, request_id: RequestId) :
        
        self.bank_transfer = bank_transfer;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(bank_transfer = data["bank_transfer"],request_id = data["request_id"])


class TransferId:
    
    def __init__(self, transfer_id: str) :
        
        self.transfer_id = transfer_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferSweepId:
    
    def __init__(self, transfer_sweep_id: Optional[str]) :
        
        self.transfer_sweep_id = transfer_sweep_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferAuthorizationId:
    
    def __init__(self, transfer_authorization_id: str) :
        
        self.transfer_authorization_id = transfer_authorization_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class BankTransferId:
    
    def __init__(self, bank_transfer_id: str) :
        
        self.bank_transfer_id = bank_transfer_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Transfer:
    
    def __init__(self, id: TransferId, ach_class: AchClass, account_id: str, type_: TransferType, user: TransferUserInResponse, amount: TransferAmount, description: str, created: str, status: TransferStatus, sweep_status: Optional[TransferSweepStatus], network: TransferNetwork, cancellable: bool, failure_reason: Optional[TransferFailure], metadata: Optional[TransferMetadata], origination_account_id: str, guarantee_decision: Optional[TransferAuthorizationGuaranteeDecision], guarantee_decision_rationale: Optional[TransferAuthorizationGuaranteeDecisionRationale], iso_currency_code: str) :
        
        self.id = id;self.ach_class = ach_class;self.account_id = account_id;self.type_ = type_;self.user = user;self.amount = amount;self.description = description;self.created = created;self.status = status;self.sweep_status = sweep_status;self.network = network;self.cancellable = cancellable;self.failure_reason = failure_reason;self.metadata = metadata;self.origination_account_id = origination_account_id;self.guarantee_decision = guarantee_decision;self.guarantee_decision_rationale = guarantee_decision_rationale;self.iso_currency_code = iso_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],ach_class = data["ach_class"],account_id = data["account_id"],type_ = data["type_"],user = data["user"],amount = data["amount"],description = data["description"],created = data["created"],status = data["status"],sweep_status = data["sweep_status"],network = data["network"],cancellable = data["cancellable"],failure_reason = data["failure_reason"],metadata = data["metadata"],origination_account_id = data["origination_account_id"],guarantee_decision = data["guarantee_decision"],guarantee_decision_rationale = data["guarantee_decision_rationale"],iso_currency_code = data["iso_currency_code"])


class BankTransfer:
    
    def __init__(self, id: BankTransferId, ach_class: AchClass, account_id: str, type_: BankTransferType, user: BankTransferUser, amount: BankTransferAmount, iso_currency_code: str, description: str, created: str, status: BankTransferStatus, network: BankTransferNetwork, cancellable: bool, failure_reason: Optional[BankTransferFailure], custom_tag: Optional[str], metadata: Optional[BankTransferMetadata], origination_account_id: str, direction: Optional[BankTransferDirection]) :
        
        self.id = id;self.ach_class = ach_class;self.account_id = account_id;self.type_ = type_;self.user = user;self.amount = amount;self.iso_currency_code = iso_currency_code;self.description = description;self.created = created;self.status = status;self.network = network;self.cancellable = cancellable;self.failure_reason = failure_reason;self.custom_tag = custom_tag;self.metadata = metadata;self.origination_account_id = origination_account_id;self.direction = direction
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],ach_class = data["ach_class"],account_id = data["account_id"],type_ = data["type_"],user = data["user"],amount = data["amount"],iso_currency_code = data["iso_currency_code"],description = data["description"],created = data["created"],status = data["status"],network = data["network"],cancellable = data["cancellable"],failure_reason = data["failure_reason"],custom_tag = data["custom_tag"],metadata = data["metadata"],origination_account_id = data["origination_account_id"],direction = data["direction"])


class AchClass:
    
    def __init__(self, ach_class: str) :
        
        self.ach_class = ach_class
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferAmount:
    
    def __init__(self, transfer_amount: str) :
        
        self.transfer_amount = transfer_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferSweepAmount:
    
    def __init__(self, transfer_sweep_amount: Optional[str]) :
        
        self.transfer_sweep_amount = transfer_sweep_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferIntentGetFailureReason:
    
    def __init__(self, error_type: str, error_code: str, error_message: str) :
        
        self.error_type = error_type;self.error_code = error_code;self.error_message = error_message
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(error_type = data["error_type"],error_code = data["error_code"],error_message = data["error_message"])


class TransferIntentCreateMode:
    
    def __init__(self, transfer_intent_create_mode: str) :
        
        self.transfer_intent_create_mode = transfer_intent_create_mode
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class BankTransferAmount:
    
    def __init__(self, bank_transfer_amount: str) :
        
        self.bank_transfer_amount = bank_transfer_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferCreateIdempotencyKey:
    
    def __init__(self, transfer_create_idempotency_key: str) :
        
        self.transfer_create_idempotency_key = transfer_create_idempotency_key
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class BankTransferIdempotencyKey:
    
    def __init__(self, bank_transfer_idempotency_key: str) :
        
        self.bank_transfer_idempotency_key = bank_transfer_idempotency_key
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferAuthorizationUserInRequest:
    
    def __init__(self, legal_name: str, phone_number: str, email_address: str, address: TransferUserAddressInRequest) :
        
        self.legal_name = legal_name;self.phone_number = phone_number;self.email_address = email_address;self.address = address
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(legal_name = data["legal_name"],phone_number = data["phone_number"],email_address = data["email_address"],address = data["address"])


class TransferUserInRequest:
    
    def __init__(self, legal_name: str, phone_number: str, email_address: str, address: TransferUserAddressInRequest) :
        
        self.legal_name = legal_name;self.phone_number = phone_number;self.email_address = email_address;self.address = address
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(legal_name = data["legal_name"],phone_number = data["phone_number"],email_address = data["email_address"],address = data["address"])


class TransferUserInResponse:
    
    def __init__(self, legal_name: str, phone_number: Optional[str], email_address: Optional[str], address: Optional[TransferUserAddressInResponse]) :
        
        self.legal_name = legal_name;self.phone_number = phone_number;self.email_address = email_address;self.address = address
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(legal_name = data["legal_name"],phone_number = data["phone_number"],email_address = data["email_address"],address = data["address"])


class TransferUserAddressInRequest:
    
    def __init__(self, street: str, city: str, region: str, postal_code: str, country: str) :
        
        self.street = street;self.city = city;self.region = region;self.postal_code = postal_code;self.country = country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(street = data["street"],city = data["city"],region = data["region"],postal_code = data["postal_code"],country = data["country"])


class TransferUserAddressInResponse:
    
    def __init__(self, street: Optional[str], city: Optional[str], region: Optional[str], postal_code: Optional[str], country: Optional[str]) :
        
        self.street = street;self.city = city;self.region = region;self.postal_code = postal_code;self.country = country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(street = data["street"],city = data["city"],region = data["region"],postal_code = data["postal_code"],country = data["country"])


class BankTransferUser:
    
    def __init__(self, legal_name: str, email_address: Optional[str], routing_number: str) :
        
        self.legal_name = legal_name;self.email_address = email_address;self.routing_number = routing_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(legal_name = data["legal_name"],email_address = data["email_address"],routing_number = data["routing_number"])


class TransferAuthorizationDecisionRationaleCode:
    
    def __init__(self, transfer_authorization_decision_rationale_code: str) :
        
        self.transfer_authorization_decision_rationale_code = transfer_authorization_decision_rationale_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferAuthorizationDecisionRationale:
    
    def __init__(self, code: TransferAuthorizationDecisionRationaleCode, description: str) :
        
        self.code = code;self.description = description
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(code = data["code"],description = data["description"])


class TransferAuthorizationGuaranteeDecision:
    
    def __init__(self, transfer_authorization_guarantee_decision: Optional[str]) :
        
        self.transfer_authorization_guarantee_decision = transfer_authorization_guarantee_decision
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferAuthorizationGuaranteeDecisionRationaleCode:
    
    def __init__(self, transfer_authorization_guarantee_decision_rationale_code: str) :
        
        self.transfer_authorization_guarantee_decision_rationale_code = transfer_authorization_guarantee_decision_rationale_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferAuthorizationGuaranteeDecisionRationale:
    
    def __init__(self, code: TransferAuthorizationGuaranteeDecisionRationaleCode, description: str) :
        
        self.code = code;self.description = description
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(code = data["code"],description = data["description"])


class TransferAuthorizationProposedTransfer:
    
    def __init__(self, ach_class: AchClass, account_id: str, type_: TransferType, user: TransferUserInResponse, amount: TransferAmount, network: str, origination_account_id: str, iso_currency_code: str) :
        
        self.ach_class = ach_class;self.account_id = account_id;self.type_ = type_;self.user = user;self.amount = amount;self.network = network;self.origination_account_id = origination_account_id;self.iso_currency_code = iso_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(ach_class = data["ach_class"],account_id = data["account_id"],type_ = data["type_"],user = data["user"],amount = data["amount"],network = data["network"],origination_account_id = data["origination_account_id"],iso_currency_code = data["iso_currency_code"])


class TransferAuthorizationDevice:
    
    def __init__(self, ip_address: str, user_agent: str) :
        
        self.ip_address = ip_address;self.user_agent = user_agent
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(ip_address = data["ip_address"],user_agent = data["user_agent"])


class TransferMetadata:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class BankTransferMetadata:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class TransferType:
    
    def __init__(self, transfer_type: str) :
        
        self.transfer_type = transfer_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class BankTransferType:
    
    def __init__(self, bank_transfer_type: str) :
        
        self.bank_transfer_type = bank_transfer_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferStatus:
    
    def __init__(self, transfer_status: str) :
        
        self.transfer_status = transfer_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferSweepStatus:
    
    def __init__(self, transfer_sweep_status: Optional[str]) :
        
        self.transfer_sweep_status = transfer_sweep_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class BankTransferStatus:
    
    def __init__(self, bank_transfer_status: str) :
        
        self.bank_transfer_status = bank_transfer_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferNetwork:
    
    def __init__(self, transfer_network: str) :
        
        self.transfer_network = transfer_network
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class BankTransferNetwork:
    
    def __init__(self, bank_transfer_network: str) :
        
        self.bank_transfer_network = bank_transfer_network
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferFailure:
    
    def __init__(self, ach_return_code: Optional[str], description: str) :
        
        self.ach_return_code = ach_return_code;self.description = description
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(ach_return_code = data["ach_return_code"],description = data["description"])


class BankTransferFailure:
    
    def __init__(self, ach_return_code: Optional[str], description: str) :
        
        self.ach_return_code = ach_return_code;self.description = description
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(ach_return_code = data["ach_return_code"],description = data["description"])


class TransferAuthorizationCreateRequest:
    
    def __init__(self, access_token: TransferAccessToken, account_id: str, type_: TransferType, network: TransferNetwork, amount: TransferAmount, ach_class: AchClass, user: TransferAuthorizationUserInRequest, device: TransferAuthorizationDevice, origination_account_id: str, iso_currency_code: str, user_present: Optional[bool], payment_profile_id: PaymentProfileId) :
        
        self.access_token = access_token;self.account_id = account_id;self.type_ = type_;self.network = network;self.amount = amount;self.ach_class = ach_class;self.user = user;self.device = device;self.origination_account_id = origination_account_id;self.iso_currency_code = iso_currency_code;self.user_present = user_present;self.payment_profile_id = payment_profile_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],account_id = data["account_id"],type_ = data["type_"],network = data["network"],amount = data["amount"],ach_class = data["ach_class"],user = data["user"],device = data["device"],origination_account_id = data["origination_account_id"],iso_currency_code = data["iso_currency_code"],user_present = data["user_present"],payment_profile_id = data["payment_profile_id"])


class TransferCreateRequest:
    
    def __init__(self, idempotency_key: TransferCreateIdempotencyKey, access_token: TransferAccessToken, account_id: str, authorization_id: str, type_: TransferType, network: TransferNetwork, amount: TransferAmount, description: str, ach_class: AchClass, user: TransferUserInRequest, metadata: Optional[TransferMetadata], origination_account_id: Optional[str], iso_currency_code: str, payment_profile_id: PaymentProfileId) :
        
        self.idempotency_key = idempotency_key;self.access_token = access_token;self.account_id = account_id;self.authorization_id = authorization_id;self.type_ = type_;self.network = network;self.amount = amount;self.description = description;self.ach_class = ach_class;self.user = user;self.metadata = metadata;self.origination_account_id = origination_account_id;self.iso_currency_code = iso_currency_code;self.payment_profile_id = payment_profile_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(idempotency_key = data["idempotency_key"],access_token = data["access_token"],account_id = data["account_id"],authorization_id = data["authorization_id"],type_ = data["type_"],network = data["network"],amount = data["amount"],description = data["description"],ach_class = data["ach_class"],user = data["user"],metadata = data["metadata"],origination_account_id = data["origination_account_id"],iso_currency_code = data["iso_currency_code"],payment_profile_id = data["payment_profile_id"])


class BankTransferCreateRequest:
    
    def __init__(self, idempotency_key: BankTransferIdempotencyKey, access_token: BankTransferAccessToken, account_id: str, type_: BankTransferType, network: BankTransferNetwork, amount: BankTransferAmount, iso_currency_code: str, description: str, ach_class: AchClass, user: BankTransferUser, custom_tag: Optional[str], metadata: Optional[BankTransferMetadata], origination_account_id: Optional[str]) :
        
        self.idempotency_key = idempotency_key;self.access_token = access_token;self.account_id = account_id;self.type_ = type_;self.network = network;self.amount = amount;self.iso_currency_code = iso_currency_code;self.description = description;self.ach_class = ach_class;self.user = user;self.custom_tag = custom_tag;self.metadata = metadata;self.origination_account_id = origination_account_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(idempotency_key = data["idempotency_key"],access_token = data["access_token"],account_id = data["account_id"],type_ = data["type_"],network = data["network"],amount = data["amount"],iso_currency_code = data["iso_currency_code"],description = data["description"],ach_class = data["ach_class"],user = data["user"],custom_tag = data["custom_tag"],metadata = data["metadata"],origination_account_id = data["origination_account_id"])


class TransferAuthorizationCreateResponse:
    
    def __init__(self, authorization: TransferAuthorization, request_id: RequestId) :
        
        self.authorization = authorization;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(authorization = data["authorization"],request_id = data["request_id"])


class TransferAuthorizationDecision:
    
    def __init__(self, transfer_authorization_decision: str) :
        
        self.transfer_authorization_decision = transfer_authorization_decision
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferAuthorization:
    
    def __init__(self, id: TransferAuthorizationId, created: str, decision: TransferAuthorizationDecision, decision_rationale: Optional[TransferAuthorizationDecisionRationale], guarantee_decision: Optional[TransferAuthorizationGuaranteeDecision], guarantee_decision_rationale: Optional[TransferAuthorizationGuaranteeDecisionRationale], proposed_transfer: TransferAuthorizationProposedTransfer) :
        
        self.id = id;self.created = created;self.decision = decision;self.decision_rationale = decision_rationale;self.guarantee_decision = guarantee_decision;self.guarantee_decision_rationale = guarantee_decision_rationale;self.proposed_transfer = proposed_transfer
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],created = data["created"],decision = data["decision"],decision_rationale = data["decision_rationale"],guarantee_decision = data["guarantee_decision"],guarantee_decision_rationale = data["guarantee_decision_rationale"],proposed_transfer = data["proposed_transfer"])


class TransferCreateResponse:
    
    def __init__(self, transfer: Transfer, request_id: RequestId) :
        
        self.transfer = transfer;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transfer = data["transfer"],request_id = data["request_id"])


class BankTransferCreateResponse:
    
    def __init__(self, bank_transfer: BankTransfer, request_id: RequestId) :
        
        self.bank_transfer = bank_transfer;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(bank_transfer = data["bank_transfer"],request_id = data["request_id"])


class TransferListRequest:
    
    def __init__(self, start_date: Optional[str], end_date: Optional[str], count: int, offset: int, origination_account_id: Optional[str]) :
        
        self.start_date = start_date;self.end_date = end_date;self.count = count;self.offset = offset;self.origination_account_id = origination_account_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(start_date = data["start_date"],end_date = data["end_date"],count = data["count"],offset = data["offset"],origination_account_id = data["origination_account_id"])


class BankTransferListRequest:
    
    def __init__(self, start_date: Optional[str], end_date: Optional[str], count: int, offset: int, origination_account_id: Optional[str], direction: Optional[BankTransferDirection]) :
        
        self.start_date = start_date;self.end_date = end_date;self.count = count;self.offset = offset;self.origination_account_id = origination_account_id;self.direction = direction
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(start_date = data["start_date"],end_date = data["end_date"],count = data["count"],offset = data["offset"],origination_account_id = data["origination_account_id"],direction = data["direction"])


class TransferListResponse:
    
    def __init__(self, transfers: List[Transfer], request_id: RequestId) :
        
        self.transfers = transfers;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transfers = data["transfers"],request_id = data["request_id"])


class BankTransferListResponse:
    
    def __init__(self, bank_transfers: List[BankTransfer], request_id: RequestId) :
        
        self.bank_transfers = bank_transfers;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(bank_transfers = data["bank_transfers"],request_id = data["request_id"])


class BankTransferDirection:
    
    def __init__(self, bank_transfer_direction: Optional[str]) :
        
        self.bank_transfer_direction = bank_transfer_direction
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferCancelRequest:
    
    def __init__(self, transfer_id: TransferId) :
        
        self.transfer_id = transfer_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transfer_id = data["transfer_id"])


class BankTransferCancelRequest:
    
    def __init__(self, bank_transfer_id: BankTransferId) :
        
        self.bank_transfer_id = bank_transfer_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(bank_transfer_id = data["bank_transfer_id"])


class TransferCancelResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class BankTransferCancelResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class TransferEventListTransferType:
    
    def __init__(self, transfer_event_list_transfer_type: Optional[str]) :
        
        self.transfer_event_list_transfer_type = transfer_event_list_transfer_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferEventListRequest:
    
    def __init__(self, start_date: Optional[str], end_date: Optional[str], transfer_id: Optional[str], account_id: Optional[str], transfer_type: Optional[TransferEventListTransferType], event_types: List[TransferEventType], sweep_id: str, count: Optional[int], offset: Optional[int], origination_account_id: Optional[str]) :
        
        self.start_date = start_date;self.end_date = end_date;self.transfer_id = transfer_id;self.account_id = account_id;self.transfer_type = transfer_type;self.event_types = event_types;self.sweep_id = sweep_id;self.count = count;self.offset = offset;self.origination_account_id = origination_account_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(start_date = data["start_date"],end_date = data["end_date"],transfer_id = data["transfer_id"],account_id = data["account_id"],transfer_type = data["transfer_type"],event_types = data["event_types"],sweep_id = data["sweep_id"],count = data["count"],offset = data["offset"],origination_account_id = data["origination_account_id"])


class BankTransferEventListBankTransferType:
    
    def __init__(self, bank_transfer_event_list_bank_transfer_type: Optional[str]) :
        
        self.bank_transfer_event_list_bank_transfer_type = bank_transfer_event_list_bank_transfer_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class BankTransferEventListDirection:
    
    def __init__(self, bank_transfer_event_list_direction: Optional[str]) :
        
        self.bank_transfer_event_list_direction = bank_transfer_event_list_direction
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class BankTransferEventListRequest:
    
    def __init__(self, start_date: Optional[str], end_date: Optional[str], bank_transfer_id: Optional[str], account_id: Optional[str], bank_transfer_type: Optional[BankTransferEventListBankTransferType], event_types: List[BankTransferEventType], count: Optional[int], offset: Optional[int], origination_account_id: Optional[str], direction: Optional[BankTransferEventListDirection]) :
        
        self.start_date = start_date;self.end_date = end_date;self.bank_transfer_id = bank_transfer_id;self.account_id = account_id;self.bank_transfer_type = bank_transfer_type;self.event_types = event_types;self.count = count;self.offset = offset;self.origination_account_id = origination_account_id;self.direction = direction
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(start_date = data["start_date"],end_date = data["end_date"],bank_transfer_id = data["bank_transfer_id"],account_id = data["account_id"],bank_transfer_type = data["bank_transfer_type"],event_types = data["event_types"],count = data["count"],offset = data["offset"],origination_account_id = data["origination_account_id"],direction = data["direction"])


class TransferEventType:
    
    def __init__(self, transfer_event_type: str) :
        
        self.transfer_event_type = transfer_event_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class BankTransferEventType:
    
    def __init__(self, bank_transfer_event_type: str) :
        
        self.bank_transfer_event_type = bank_transfer_event_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferEvent:
    
    def __init__(self, event_id: int, timestamp: str, event_type: TransferEventType, account_id: str, transfer_id: TransferId, origination_account_id: Optional[str], transfer_type: TransferType, transfer_amount: TransferAmount, failure_reason: Optional[TransferFailure], sweep_id: Optional[TransferSweepId], sweep_amount: Optional[TransferSweepAmount]) :
        
        self.event_id = event_id;self.timestamp = timestamp;self.event_type = event_type;self.account_id = account_id;self.transfer_id = transfer_id;self.origination_account_id = origination_account_id;self.transfer_type = transfer_type;self.transfer_amount = transfer_amount;self.failure_reason = failure_reason;self.sweep_id = sweep_id;self.sweep_amount = sweep_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(event_id = data["event_id"],timestamp = data["timestamp"],event_type = data["event_type"],account_id = data["account_id"],transfer_id = data["transfer_id"],origination_account_id = data["origination_account_id"],transfer_type = data["transfer_type"],transfer_amount = data["transfer_amount"],failure_reason = data["failure_reason"],sweep_id = data["sweep_id"],sweep_amount = data["sweep_amount"])


class BankTransferEvent:
    
    def __init__(self, event_id: int, timestamp: str, event_type: BankTransferEventType, account_id: str, bank_transfer_id: BankTransferId, origination_account_id: Optional[str], bank_transfer_type: BankTransferType, bank_transfer_amount: str, bank_transfer_iso_currency_code: str, failure_reason: Optional[BankTransferFailure], direction: Optional[BankTransferDirection]) :
        
        self.event_id = event_id;self.timestamp = timestamp;self.event_type = event_type;self.account_id = account_id;self.bank_transfer_id = bank_transfer_id;self.origination_account_id = origination_account_id;self.bank_transfer_type = bank_transfer_type;self.bank_transfer_amount = bank_transfer_amount;self.bank_transfer_iso_currency_code = bank_transfer_iso_currency_code;self.failure_reason = failure_reason;self.direction = direction
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(event_id = data["event_id"],timestamp = data["timestamp"],event_type = data["event_type"],account_id = data["account_id"],bank_transfer_id = data["bank_transfer_id"],origination_account_id = data["origination_account_id"],bank_transfer_type = data["bank_transfer_type"],bank_transfer_amount = data["bank_transfer_amount"],bank_transfer_iso_currency_code = data["bank_transfer_iso_currency_code"],failure_reason = data["failure_reason"],direction = data["direction"])


class TransferEventListResponse:
    
    def __init__(self, transfer_events: List[TransferEvent], request_id: RequestId) :
        
        self.transfer_events = transfer_events;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transfer_events = data["transfer_events"],request_id = data["request_id"])


class BankTransferEventListResponse:
    
    def __init__(self, bank_transfer_events: List[BankTransferEvent], request_id: RequestId) :
        
        self.bank_transfer_events = bank_transfer_events;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(bank_transfer_events = data["bank_transfer_events"],request_id = data["request_id"])


class BankTransferEventSyncRequest:
    
    def __init__(self, after_id: int, count: Optional[int]) :
        
        self.after_id = after_id;self.count = count
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(after_id = data["after_id"],count = data["count"])


class TransferEventSyncRequest:
    
    def __init__(self, after_id: int, count: Optional[int]) :
        
        self.after_id = after_id;self.count = count
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(after_id = data["after_id"],count = data["count"])


class BankTransferEventSyncResponse:
    
    def __init__(self, bank_transfer_events: List[BankTransferEvent], request_id: RequestId) :
        
        self.bank_transfer_events = bank_transfer_events;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(bank_transfer_events = data["bank_transfer_events"],request_id = data["request_id"])


class TransferEventSyncResponse:
    
    def __init__(self, transfer_events: List[TransferEvent], request_id: RequestId) :
        
        self.transfer_events = transfer_events;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transfer_events = data["transfer_events"],request_id = data["request_id"])


class BankTransferSweepGetRequest:
    
    def __init__(self, sweep_id: str) :
        
        self.sweep_id = sweep_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(sweep_id = data["sweep_id"])


class TransferSweepGetRequest:
    
    def __init__(self, sweep_id: str) :
        
        self.sweep_id = sweep_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(sweep_id = data["sweep_id"])


class BankTransferSweepGetResponse:
    
    def __init__(self, sweep: BankTransferSweep, request_id: RequestId) :
        
        self.sweep = sweep;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(sweep = data["sweep"],request_id = data["request_id"])


class TransferSweepGetResponse:
    
    def __init__(self, sweep: TransferSweep, request_id: RequestId) :
        
        self.sweep = sweep;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(sweep = data["sweep"],request_id = data["request_id"])


class BankTransferSweepListRequest:
    
    def __init__(self, origination_account_id: Optional[str], start_time: Optional[str], end_time: Optional[str], count: Optional[int]) :
        
        self.origination_account_id = origination_account_id;self.start_time = start_time;self.end_time = end_time;self.count = count
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(origination_account_id = data["origination_account_id"],start_time = data["start_time"],end_time = data["end_time"],count = data["count"])


class TransferSweepListRequest:
    
    def __init__(self, start_date: Optional[str], end_date: Optional[str], count: Optional[int], offset: int) :
        
        self.start_date = start_date;self.end_date = end_date;self.count = count;self.offset = offset
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(start_date = data["start_date"],end_date = data["end_date"],count = data["count"],offset = data["offset"])


class TransferSweepListResponse:
    
    def __init__(self, sweeps: List[TransferSweep], request_id: RequestId) :
        
        self.sweeps = sweeps;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(sweeps = data["sweeps"],request_id = data["request_id"])


class BankTransferSweepListResponse:
    
    def __init__(self, sweeps: List[BankTransferSweep], request_id: RequestId) :
        
        self.sweeps = sweeps;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(sweeps = data["sweeps"],request_id = data["request_id"])


class BankTransferSweep:
    
    def __init__(self, id: str, created_at: str, amount: str, iso_currency_code: str) :
        
        self.id = id;self.created_at = created_at;self.amount = amount;self.iso_currency_code = iso_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],created_at = data["created_at"],amount = data["amount"],iso_currency_code = data["iso_currency_code"])


class TransferSweep:
    
    def __init__(self, id: str, created: str, amount: str, iso_currency_code: str) :
        
        self.id = id;self.created = created;self.amount = amount;self.iso_currency_code = iso_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],created = data["created"],amount = data["amount"],iso_currency_code = data["iso_currency_code"])


class SimulatedTransferSweep:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class BankTransferBalanceGetRequest:
    
    def __init__(self, origination_account_id: Optional[str]) :
        
        self.origination_account_id = origination_account_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(origination_account_id = data["origination_account_id"])


class BankTransferBalanceGetResponse:
    
    def __init__(self, balance: BankTransferBalance, origination_account_id: Optional[str], request_id: RequestId) :
        
        self.balance = balance;self.origination_account_id = origination_account_id;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(balance = data["balance"],origination_account_id = data["origination_account_id"],request_id = data["request_id"])


class BankTransferBalance:
    
    def __init__(self, available: str, transactable: str) :
        
        self.available = available;self.transactable = transactable
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(available = data["available"],transactable = data["transactable"])


class BankTransferMigrateAccountRequest:
    
    def __init__(self, account_number: str, routing_number: str, wire_routing_number: str, account_type: str) :
        
        self.account_number = account_number;self.routing_number = routing_number;self.wire_routing_number = wire_routing_number;self.account_type = account_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_number = data["account_number"],routing_number = data["routing_number"],wire_routing_number = data["wire_routing_number"],account_type = data["account_type"])


class BankTransferMigrateAccountResponse:
    
    def __init__(self, access_token: str, account_id: str, request_id: RequestId) :
        
        self.access_token = access_token;self.account_id = account_id;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],account_id = data["account_id"],request_id = data["request_id"])


class TransferMigrateAccountRequest:
    
    def __init__(self, account_number: str, routing_number: str, wire_routing_number: str, account_type: str) :
        
        self.account_number = account_number;self.routing_number = routing_number;self.wire_routing_number = wire_routing_number;self.account_type = account_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_number = data["account_number"],routing_number = data["routing_number"],wire_routing_number = data["wire_routing_number"],account_type = data["account_type"])


class TransferMigrateAccountResponse:
    
    def __init__(self, access_token: str, account_id: str, request_id: RequestId) :
        
        self.access_token = access_token;self.account_id = account_id;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],account_id = data["account_id"],request_id = data["request_id"])


class TransferRepaymentListRequest:
    
    def __init__(self, start_date: Optional[str], end_date: Optional[str], count: Optional[int], offset: int) :
        
        self.start_date = start_date;self.end_date = end_date;self.count = count;self.offset = offset
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(start_date = data["start_date"],end_date = data["end_date"],count = data["count"],offset = data["offset"])


class TransferRepaymentListResponse:
    
    def __init__(self, repayments: List[TransferRepayment], request_id: RequestId) :
        
        self.repayments = repayments;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(repayments = data["repayments"],request_id = data["request_id"])


class TransferRepayment:
    
    def __init__(self, repayment_id: str, created: str, amount: str, iso_currency_code: str) :
        
        self.repayment_id = repayment_id;self.created = created;self.amount = amount;self.iso_currency_code = iso_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(repayment_id = data["repayment_id"],created = data["created"],amount = data["amount"],iso_currency_code = data["iso_currency_code"])


class TransferRepaymentReturnListRequest:
    
    def __init__(self, repayment_id: str, count: Optional[int], offset: int) :
        
        self.repayment_id = repayment_id;self.count = count;self.offset = offset
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(repayment_id = data["repayment_id"],count = data["count"],offset = data["offset"])


class TransferRepaymentReturnListResponse:
    
    def __init__(self, repayment_returns: List[TransferRepaymentReturn], request_id: RequestId) :
        
        self.repayment_returns = repayment_returns;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(repayment_returns = data["repayment_returns"],request_id = data["request_id"])


class TransferRepaymentReturn:
    
    def __init__(self, transfer_id: str, event_id: int, amount: str, iso_currency_code: str) :
        
        self.transfer_id = transfer_id;self.event_id = event_id;self.amount = amount;self.iso_currency_code = iso_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transfer_id = data["transfer_id"],event_id = data["event_id"],amount = data["amount"],iso_currency_code = data["iso_currency_code"])


class TransferIntentCreateRequest:
    
    def __init__(self, account_id: Optional[str], mode: TransferIntentCreateMode, amount: TransferAmount, description: str, ach_class: AchClass, origination_account_id: Optional[str], user: TransferUserInRequest, metadata: Optional[TransferMetadata], iso_currency_code: str, require_guarantee: Optional[bool]) :
        
        self.account_id = account_id;self.mode = mode;self.amount = amount;self.description = description;self.ach_class = ach_class;self.origination_account_id = origination_account_id;self.user = user;self.metadata = metadata;self.iso_currency_code = iso_currency_code;self.require_guarantee = require_guarantee
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],mode = data["mode"],amount = data["amount"],description = data["description"],ach_class = data["ach_class"],origination_account_id = data["origination_account_id"],user = data["user"],metadata = data["metadata"],iso_currency_code = data["iso_currency_code"],require_guarantee = data["require_guarantee"])


class TransferIntentStatus:
    
    def __init__(self, transfer_intent_status: str) :
        
        self.transfer_intent_status = transfer_intent_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferIntentCreate:
    
    def __init__(self, id: str, created: str, status: TransferIntentStatus, account_id: Optional[str], origination_account_id: str, amount: TransferAmount, mode: TransferIntentCreateMode, ach_class: AchClass, user: TransferUserInResponse, description: str, metadata: Optional[TransferMetadata], iso_currency_code: str, require_guarantee: Optional[bool]) :
        
        self.id = id;self.created = created;self.status = status;self.account_id = account_id;self.origination_account_id = origination_account_id;self.amount = amount;self.mode = mode;self.ach_class = ach_class;self.user = user;self.description = description;self.metadata = metadata;self.iso_currency_code = iso_currency_code;self.require_guarantee = require_guarantee
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],created = data["created"],status = data["status"],account_id = data["account_id"],origination_account_id = data["origination_account_id"],amount = data["amount"],mode = data["mode"],ach_class = data["ach_class"],user = data["user"],description = data["description"],metadata = data["metadata"],iso_currency_code = data["iso_currency_code"],require_guarantee = data["require_guarantee"])


class TransferIntentCreateResponse:
    
    def __init__(self, transfer_intent: TransferIntentCreate, request_id: RequestId) :
        
        self.transfer_intent = transfer_intent;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transfer_intent = data["transfer_intent"],request_id = data["request_id"])


class TransferIntentGetRequest:
    
    def __init__(self, transfer_intent_id: str) :
        
        self.transfer_intent_id = transfer_intent_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transfer_intent_id = data["transfer_intent_id"])


class TransferIntentAuthorizationDecision:
    
    def __init__(self, transfer_intent_authorization_decision: Optional[str]) :
        
        self.transfer_intent_authorization_decision = transfer_intent_authorization_decision
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TransferIntentGet:
    
    def __init__(self, id: str, created: str, status: TransferIntentStatus, transfer_id: Optional[str], failure_reason: Optional[TransferIntentGetFailureReason], authorization_decision: Optional[TransferIntentAuthorizationDecision], authorization_decision_rationale: Optional[TransferAuthorizationDecisionRationale], account_id: Optional[str], origination_account_id: str, amount: TransferAmount, mode: TransferIntentCreateMode, ach_class: AchClass, user: TransferUserInResponse, description: str, metadata: Optional[TransferMetadata], iso_currency_code: str, require_guarantee: Optional[bool], guarantee_decision: Optional[TransferAuthorizationGuaranteeDecision], guarantee_decision_rationale: Optional[TransferAuthorizationGuaranteeDecisionRationale]) :
        
        self.id = id;self.created = created;self.status = status;self.transfer_id = transfer_id;self.failure_reason = failure_reason;self.authorization_decision = authorization_decision;self.authorization_decision_rationale = authorization_decision_rationale;self.account_id = account_id;self.origination_account_id = origination_account_id;self.amount = amount;self.mode = mode;self.ach_class = ach_class;self.user = user;self.description = description;self.metadata = metadata;self.iso_currency_code = iso_currency_code;self.require_guarantee = require_guarantee;self.guarantee_decision = guarantee_decision;self.guarantee_decision_rationale = guarantee_decision_rationale
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],created = data["created"],status = data["status"],transfer_id = data["transfer_id"],failure_reason = data["failure_reason"],authorization_decision = data["authorization_decision"],authorization_decision_rationale = data["authorization_decision_rationale"],account_id = data["account_id"],origination_account_id = data["origination_account_id"],amount = data["amount"],mode = data["mode"],ach_class = data["ach_class"],user = data["user"],description = data["description"],metadata = data["metadata"],iso_currency_code = data["iso_currency_code"],require_guarantee = data["require_guarantee"],guarantee_decision = data["guarantee_decision"],guarantee_decision_rationale = data["guarantee_decision_rationale"])


class TransferIntentGetResponse:
    
    def __init__(self, transfer_intent: TransferIntentGet, request_id: RequestId) :
        
        self.transfer_intent = transfer_intent;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transfer_intent = data["transfer_intent"],request_id = data["request_id"])


class SandboxBankTransferSimulateRequest:
    
    def __init__(self, bank_transfer_id: BankTransferId, event_type: str, failure_reason: Optional[BankTransferFailure]) :
        
        self.bank_transfer_id = bank_transfer_id;self.event_type = event_type;self.failure_reason = failure_reason
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(bank_transfer_id = data["bank_transfer_id"],event_type = data["event_type"],failure_reason = data["failure_reason"])


class SandboxTransferSimulateRequest:
    
    def __init__(self, transfer_id: TransferId, event_type: str, failure_reason: Optional[TransferFailure]) :
        
        self.transfer_id = transfer_id;self.event_type = event_type;self.failure_reason = failure_reason
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transfer_id = data["transfer_id"],event_type = data["event_type"],failure_reason = data["failure_reason"])


class SandboxTransferSweepSimulateRequest:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class SandboxBankTransferSimulateResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class SandboxTransferSimulateResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class SandboxTransferSweepSimulateResponse:
    
    def __init__(self, sweep: SimulatedTransferSweep, request_id: RequestId) :
        
        self.sweep = sweep;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(sweep = data["sweep"],request_id = data["request_id"])


class SandboxTransferRepaymentSimulateRequest:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class SandboxTransferRepaymentSimulateResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class AccountFiltersResponse:
    
    def __init__(self, depository: DepositoryFilter, credit: CreditFilter, loan: LoanFilter, investment: InvestmentFilter) :
        
        self.depository = depository;self.credit = credit;self.loan = loan;self.investment = investment
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(depository = data["depository"],credit = data["credit"],loan = data["loan"],investment = data["investment"])


class InstitutionsSearchAccountFilter:
    
    def __init__(self, loan: List[Optional[AccountSubtype]], depository: List[Optional[AccountSubtype]], credit: List[Optional[AccountSubtype]], investment: List[Optional[AccountSubtype]]) :
        
        self.loan = loan;self.depository = depository;self.credit = credit;self.investment = investment
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(loan = data["loan"],depository = data["depository"],credit = data["credit"],investment = data["investment"])


class AccountIdentity:
    
    def __init__(self, account_identity: Any) :
        
        self.account_identity = account_identity
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class AccountAssets:
    
    def __init__(self, account_assets: Any) :
        
        self.account_assets = account_assets
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class DepositoryFilter:
    
    def __init__(self, account_subtypes: DepositoryAccountSubtypes) :
        
        self.account_subtypes = account_subtypes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_subtypes = data["account_subtypes"])


class CreditFilter:
    
    def __init__(self, account_subtypes: CreditAccountSubtypes) :
        
        self.account_subtypes = account_subtypes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_subtypes = data["account_subtypes"])


class LoanFilter:
    
    def __init__(self, account_subtypes: LoanAccountSubtypes) :
        
        self.account_subtypes = account_subtypes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_subtypes = data["account_subtypes"])


class InvestmentFilter:
    
    def __init__(self, account_subtypes: InvestmentAccountSubtypes) :
        
        self.account_subtypes = account_subtypes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_subtypes = data["account_subtypes"])


class DepositoryAccountSubtypes:
    
    def __init__(self, depository_account_subtypes: List[DepositoryAccountSubtype]) :
        
        self.depository_account_subtypes = depository_account_subtypes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(DepositoryAccountSubtype.from_json(d) for d in data)


class CreditAccountSubtypes:
    
    def __init__(self, credit_account_subtypes: List[CreditAccountSubtype]) :
        
        self.credit_account_subtypes = credit_account_subtypes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(CreditAccountSubtype.from_json(d) for d in data)


class LoanAccountSubtypes:
    
    def __init__(self, loan_account_subtypes: List[LoanAccountSubtype]) :
        
        self.loan_account_subtypes = loan_account_subtypes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(LoanAccountSubtype.from_json(d) for d in data)


class InvestmentAccountSubtypes:
    
    def __init__(self, investment_account_subtypes: List[InvestmentAccountSubtype]) :
        
        self.investment_account_subtypes = investment_account_subtypes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(InvestmentAccountSubtype.from_json(d) for d in data)


class DepositoryAccountSubtype:
    
    def __init__(self, depository_account_subtype: str) :
        
        self.depository_account_subtype = depository_account_subtype
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreditAccountSubtype:
    
    def __init__(self, credit_account_subtype: str) :
        
        self.credit_account_subtype = credit_account_subtype
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class LoanAccountSubtype:
    
    def __init__(self, loan_account_subtype: str) :
        
        self.loan_account_subtype = loan_account_subtype
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class InvestmentAccountSubtype:
    
    def __init__(self, investment_account_subtype: str) :
        
        self.investment_account_subtype = investment_account_subtype
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class EmployersSearchRequest:
    
    def __init__(self, query: str, products: List[str]) :
        
        self.query = query;self.products = products
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(query = data["query"],products = data["products"])


class EmployersSearchResponse:
    
    def __init__(self, employers: List[Employer], request_id: RequestId) :
        
        self.employers = employers;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(employers = data["employers"],request_id = data["request_id"])


class Employer:
    
    def __init__(self, employer_id: str, name: str, address: Optional[AddressDataNullable], confidence_score: float) :
        
        self.employer_id = employer_id;self.name = name;self.address = address;self.confidence_score = confidence_score
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(employer_id = data["employer_id"],name = data["name"],address = data["address"],confidence_score = data["confidence_score"])


class IncomeVerificationCreateRequest:
    
    def __init__(self, webhook: str, precheck_id: str, options: IncomeVerificationCreateRequestOptions) :
        
        self.webhook = webhook;self.precheck_id = precheck_id;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook = data["webhook"],precheck_id = data["precheck_id"],options = data["options"])


class IncomeVerificationCreateRequestOptions:
    
    def __init__(self, access_tokens: List[AccessToken]) :
        
        self.access_tokens = access_tokens
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_tokens = data["access_tokens"])


class IncomeVerificationCreateResponse:
    
    def __init__(self, income_verification_id: str, request_id: RequestId) :
        
        self.income_verification_id = income_verification_id;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(income_verification_id = data["income_verification_id"],request_id = data["request_id"])


class IncomeVerificationPrecheckRequest:
    
    def __init__(self, user: Optional[IncomeVerificationPrecheckUser], employer: Optional[IncomeVerificationPrecheckEmployer], transactions_access_token: Any, transactions_access_tokens: List[AccessToken], us_military_info: Optional[IncomeVerificationPrecheckMilitaryInfo]) :
        
        self.user = user;self.employer = employer;self.transactions_access_token = transactions_access_token;self.transactions_access_tokens = transactions_access_tokens;self.us_military_info = us_military_info
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(user = data["user"],employer = data["employer"],transactions_access_token = data["transactions_access_token"],transactions_access_tokens = data["transactions_access_tokens"],us_military_info = data["us_military_info"])


class IncomeVerificationPrecheckEmployer:
    
    def __init__(self, name: Optional[str], address: Optional[IncomeVerificationPrecheckEmployerAddress], tax_id: Optional[str], url: Optional[str]) :
        
        self.name = name;self.address = address;self.tax_id = tax_id;self.url = url
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(name = data["name"],address = data["address"],tax_id = data["tax_id"],url = data["url"])


class IncomeVerificationPrecheckEmployerAddress:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class IncomeVerificationPrecheckEmployerAddressData:
    
    def __init__(self, city: str, country: str, postal_code: str, region: str, street: str) :
        
        self.city = city;self.country = country;self.postal_code = postal_code;self.region = region;self.street = street
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(city = data["city"],country = data["country"],postal_code = data["postal_code"],region = data["region"],street = data["street"])


class IncomeVerificationPrecheckMilitaryInfo:
    
    def __init__(self, is_active_duty: Optional[bool], branch: Optional[str]) :
        
        self.is_active_duty = is_active_duty;self.branch = branch
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(is_active_duty = data["is_active_duty"],branch = data["branch"])


class IncomeVerificationPrecheckUser:
    
    def __init__(self, first_name: Optional[str], last_name: Optional[str], email_address: Optional[str], home_address: Optional[SignalAddressData]) :
        
        self.first_name = first_name;self.last_name = last_name;self.email_address = email_address;self.home_address = home_address
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(first_name = data["first_name"],last_name = data["last_name"],email_address = data["email_address"],home_address = data["home_address"])


class IncomeVerificationPrecheckResponse:
    
    def __init__(self, precheck_id: str, request_id: RequestId, confidence: IncomeVerificationPrecheckConfidence) :
        
        self.precheck_id = precheck_id;self.request_id = request_id;self.confidence = confidence
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(precheck_id = data["precheck_id"],request_id = data["request_id"],confidence = data["confidence"])


class IncomeVerificationPrecheckConfidence:
    
    def __init__(self, income_verification_precheck_confidence: str) :
        
        self.income_verification_precheck_confidence = income_verification_precheck_confidence
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class LinkTokenCreateRequestIncomeVerification:
    
    def __init__(self, income_verification_id: str, asset_report_id: str, precheck_id: str, access_tokens: List[AccessToken], income_source_types: List[IncomeVerificationSourceType], bank_income: LinkTokenCreateRequestIncomeVerificationBankIncome, payroll_income: LinkTokenCreateRequestIncomeVerificationPayrollIncome, stated_income_sources: List[LinkTokenCreateRequestUserStatedIncomeSource]) :
        
        self.income_verification_id = income_verification_id;self.asset_report_id = asset_report_id;self.precheck_id = precheck_id;self.access_tokens = access_tokens;self.income_source_types = income_source_types;self.bank_income = bank_income;self.payroll_income = payroll_income;self.stated_income_sources = stated_income_sources
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(income_verification_id = data["income_verification_id"],asset_report_id = data["asset_report_id"],precheck_id = data["precheck_id"],access_tokens = data["access_tokens"],income_source_types = data["income_source_types"],bank_income = data["bank_income"],payroll_income = data["payroll_income"],stated_income_sources = data["stated_income_sources"])


class IncomeVerificationSourceType:
    
    def __init__(self, income_verification_source_type: str) :
        
        self.income_verification_source_type = income_verification_source_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class LinkTokenCreateRequestIncomeVerificationBankIncome:
    
    def __init__(self, days_requested: int, enable_multiple_items: Optional[bool]) :
        
        self.days_requested = days_requested;self.enable_multiple_items = enable_multiple_items
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(days_requested = data["days_requested"],enable_multiple_items = data["enable_multiple_items"])


class LinkTokenCreateRequestIncomeVerificationPayrollIncome:
    
    def __init__(self, flow_types: Optional[List[IncomeVerificationPayrollFlowType]], is_update_mode: bool) :
        
        self.flow_types = flow_types;self.is_update_mode = is_update_mode
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(flow_types = data["flow_types"],is_update_mode = data["is_update_mode"])


class IncomeVerificationPayrollFlowType:
    
    def __init__(self, income_verification_payroll_flow_type: str) :
        
        self.income_verification_payroll_flow_type = income_verification_payroll_flow_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IncomeVerificationStatusWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, item_id: str, user_id: UserId, verification_status: str) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.item_id = item_id;self.user_id = user_id;self.verification_status = verification_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],item_id = data["item_id"],user_id = data["user_id"],verification_status = data["verification_status"])


class IncomeVerificationRefreshRequest:
    
    def __init__(self, income_verification_id: Optional[str], access_token: Optional[AccessTokenNullable]) :
        
        self.income_verification_id = income_verification_id;self.access_token = access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(income_verification_id = data["income_verification_id"],access_token = data["access_token"])


class IncomeVerificationRefreshResponse:
    
    def __init__(self, request_id: RequestId, verification_refresh_status: VerificationRefreshStatus) :
        
        self.request_id = request_id;self.verification_refresh_status = verification_refresh_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"],verification_refresh_status = data["verification_refresh_status"])


class IncomeSummary:
    
    def __init__(self, employer_name: EmployerIncomeSummaryFieldString, employee_name: EmployeeIncomeSummaryFieldString, ytd_gross_income: YtdGrossIncomeSummaryFieldNumber, ytd_net_income: YtdNetIncomeSummaryFieldNumber, pay_frequency: Optional[PayFrequency], projected_wage: ProjectedIncomeSummaryFieldNumber, verified_transaction: Optional[TransactionData]) :
        
        self.employer_name = employer_name;self.employee_name = employee_name;self.ytd_gross_income = ytd_gross_income;self.ytd_net_income = ytd_net_income;self.pay_frequency = pay_frequency;self.projected_wage = projected_wage;self.verified_transaction = verified_transaction
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(employer_name = data["employer_name"],employee_name = data["employee_name"],ytd_gross_income = data["ytd_gross_income"],ytd_net_income = data["ytd_net_income"],pay_frequency = data["pay_frequency"],projected_wage = data["projected_wage"],verified_transaction = data["verified_transaction"])


class TransactionData:
    
    def __init__(self, description: str, amount: float, date: str, account_id: str, transaction_id: str) :
        
        self.description = description;self.amount = amount;self.date = date;self.account_id = account_id;self.transaction_id = transaction_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(description = data["description"],amount = data["amount"],date = data["date"],account_id = data["account_id"],transaction_id = data["transaction_id"])


class IncomeSummaryFieldString:
    
    def __init__(self, value: str, verification_status: VerificationStatus) :
        
        self.value = value;self.verification_status = verification_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(value = data["value"],verification_status = data["verification_status"])


class EmployerIncomeSummaryFieldString:
    
    def __init__(self, employer_income_summary_field_string: Any) :
        
        self.employer_income_summary_field_string = employer_income_summary_field_string
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class EmployeeIncomeSummaryFieldString:
    
    def __init__(self, employee_income_summary_field_string: Any) :
        
        self.employee_income_summary_field_string = employee_income_summary_field_string
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IncomeSummaryFieldNumber:
    
    def __init__(self, value: float, verification_status: VerificationStatus) :
        
        self.value = value;self.verification_status = verification_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(value = data["value"],verification_status = data["verification_status"])


class YtdGrossIncomeSummaryFieldNumber:
    
    def __init__(self, ytd_gross_income_summary_field_number: Any) :
        
        self.ytd_gross_income_summary_field_number = ytd_gross_income_summary_field_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class YtdNetIncomeSummaryFieldNumber:
    
    def __init__(self, ytd_net_income_summary_field_number: Any) :
        
        self.ytd_net_income_summary_field_number = ytd_net_income_summary_field_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ProjectedIncomeSummaryFieldNumber:
    
    def __init__(self, projected_income_summary_field_number: Any) :
        
        self.projected_income_summary_field_number = projected_income_summary_field_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PayFrequency:
    
    def __init__(self, value: PayFrequencyValue, verification_status: VerificationStatus) :
        
        self.value = value;self.verification_status = verification_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(value = data["value"],verification_status = data["verification_status"])


class PayFrequencyValue:
    
    def __init__(self, pay_frequency_value: str) :
        
        self.pay_frequency_value = pay_frequency_value
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class VerificationStatus:
    
    def __init__(self, verification_status: str) :
        
        self.verification_status = verification_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class VerificationRefreshStatus:
    
    def __init__(self, verification_refresh_status: str) :
        
        self.verification_refresh_status = verification_refresh_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreditPayrollIncomeRefreshStatus:
    
    def __init__(self, credit_payroll_income_refresh_status: str) :
        
        self.credit_payroll_income_refresh_status = credit_payroll_income_refresh_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IncomeVerificationPaystubsGetRequest:
    
    def __init__(self, income_verification_id: Optional[str], access_token: Optional[AccessTokenNullable]) :
        
        self.income_verification_id = income_verification_id;self.access_token = access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(income_verification_id = data["income_verification_id"],access_token = data["access_token"])


class IncomeVerificationPaystubsGetResponse:
    
    def __init__(self, document_metadata: List[DocumentMetadata], paystubs: List[Paystub], error: Optional[PlaidError], request_id: RequestId) :
        
        self.document_metadata = document_metadata;self.paystubs = paystubs;self.error = error;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(document_metadata = data["document_metadata"],paystubs = data["paystubs"],error = data["error"],request_id = data["request_id"])


class DocumentMetadata:
    
    def __init__(self, name: str, status: str, doc_id: str, doc_type: DocType) :
        
        self.name = name;self.status = status;self.doc_id = doc_id;self.doc_type = doc_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(name = data["name"],status = data["status"],doc_id = data["doc_id"],doc_type = data["doc_type"])


class DocType:
    
    def __init__(self, doc_type: str) :
        
        self.doc_type = doc_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Paystub:
    
    def __init__(self, deductions: Deductions, doc_id: str, earnings: Earnings, employee: Employee, employer: PaystubEmployer, employment_details: EmploymentDetails, net_pay: NetPay, pay_period_details: PayPeriodDetails, paystub_details: PaystubDetails, income_breakdown: List[IncomeBreakdown], ytd_earnings: PaystubYtdDetails, verification: Optional[PaystubVerification]) :
        
        self.deductions = deductions;self.doc_id = doc_id;self.earnings = earnings;self.employee = employee;self.employer = employer;self.employment_details = employment_details;self.net_pay = net_pay;self.pay_period_details = pay_period_details;self.paystub_details = paystub_details;self.income_breakdown = income_breakdown;self.ytd_earnings = ytd_earnings;self.verification = verification
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(deductions = data["deductions"],doc_id = data["doc_id"],earnings = data["earnings"],employee = data["employee"],employer = data["employer"],employment_details = data["employment_details"],net_pay = data["net_pay"],pay_period_details = data["pay_period_details"],paystub_details = data["paystub_details"],income_breakdown = data["income_breakdown"],ytd_earnings = data["ytd_earnings"],verification = data["verification"])


class Deductions:
    
    def __init__(self, subtotals: List[Total], breakdown: List[DeductionsBreakdown], totals: List[Total], total: DeductionsTotal) :
        
        self.subtotals = subtotals;self.breakdown = breakdown;self.totals = totals;self.total = total
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(subtotals = data["subtotals"],breakdown = data["breakdown"],totals = data["totals"],total = data["total"])


class DeductionsBreakdown:
    
    def __init__(self, current_amount: Optional[float], description: Optional[str], iso_currency_code: Optional[str], unofficial_currency_code: Optional[str], ytd_amount: Optional[float]) :
        
        self.current_amount = current_amount;self.description = description;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code;self.ytd_amount = ytd_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(current_amount = data["current_amount"],description = data["description"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"],ytd_amount = data["ytd_amount"])


class DeductionsTotal:
    
    def __init__(self, current_amount: Optional[float], iso_currency_code: Optional[str], unofficial_currency_code: Optional[str], ytd_amount: Optional[float]) :
        
        self.current_amount = current_amount;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code;self.ytd_amount = ytd_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(current_amount = data["current_amount"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"],ytd_amount = data["ytd_amount"])


class Total:
    
    def __init__(self, canonical_description: Optional[TotalCanonicalDescription], description: Optional[str], current_pay: Pay, ytd_pay: Pay) :
        
        self.canonical_description = canonical_description;self.description = description;self.current_pay = current_pay;self.ytd_pay = ytd_pay
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(canonical_description = data["canonical_description"],description = data["description"],current_pay = data["current_pay"],ytd_pay = data["ytd_pay"])


class TotalCanonicalDescription:
    
    def __init__(self, total_canonical_description: Optional[str]) :
        
        self.total_canonical_description = total_canonical_description
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Pay:
    
    def __init__(self, amount: Optional[float], currency: Optional[str]) :
        
        self.amount = amount;self.currency = currency
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(amount = data["amount"],currency = data["currency"])


class Earnings:
    
    def __init__(self, subtotals: List[EarningsTotal], totals: List[EarningsTotal], breakdown: List[EarningsBreakdown], total: EarningsTotal) :
        
        self.subtotals = subtotals;self.totals = totals;self.breakdown = breakdown;self.total = total
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(subtotals = data["subtotals"],totals = data["totals"],breakdown = data["breakdown"],total = data["total"])


class EarningsBreakdown:
    
    def __init__(self, canonical_description: Optional[EarningsBreakdownCanonicalDescription], current_amount: Optional[float], description: Optional[str], hours: Optional[float], iso_currency_code: Optional[str], rate: Optional[float], unofficial_currency_code: Optional[str], ytd_amount: Optional[float]) :
        
        self.canonical_description = canonical_description;self.current_amount = current_amount;self.description = description;self.hours = hours;self.iso_currency_code = iso_currency_code;self.rate = rate;self.unofficial_currency_code = unofficial_currency_code;self.ytd_amount = ytd_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(canonical_description = data["canonical_description"],current_amount = data["current_amount"],description = data["description"],hours = data["hours"],iso_currency_code = data["iso_currency_code"],rate = data["rate"],unofficial_currency_code = data["unofficial_currency_code"],ytd_amount = data["ytd_amount"])


class EarningsBreakdownCanonicalDescription:
    
    def __init__(self, earnings_breakdown_canonical_description: Optional[str]) :
        
        self.earnings_breakdown_canonical_description = earnings_breakdown_canonical_description
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class EarningsTotal:
    
    def __init__(self, current_amount: Optional[float], current_pay: Pay, ytd_pay: Pay, hours: Optional[float], iso_currency_code: Optional[str], unofficial_currency_code: Optional[str], ytd_amount: Optional[float]) :
        
        self.current_amount = current_amount;self.current_pay = current_pay;self.ytd_pay = ytd_pay;self.hours = hours;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code;self.ytd_amount = ytd_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(current_amount = data["current_amount"],current_pay = data["current_pay"],ytd_pay = data["ytd_pay"],hours = data["hours"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"],ytd_amount = data["ytd_amount"])


class EmploymentDetails:
    
    def __init__(self, annual_salary: Pay, hire_date: Optional[str]) :
        
        self.annual_salary = annual_salary;self.hire_date = hire_date
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(annual_salary = data["annual_salary"],hire_date = data["hire_date"])


class NetPay:
    
    def __init__(self, current_amount: Optional[float], description: Optional[str], iso_currency_code: Optional[str], unofficial_currency_code: Optional[str], ytd_amount: Optional[float], total: Total) :
        
        self.current_amount = current_amount;self.description = description;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code;self.ytd_amount = ytd_amount;self.total = total
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(current_amount = data["current_amount"],description = data["description"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"],ytd_amount = data["ytd_amount"],total = data["total"])


class PaystubDetails:
    
    def __init__(self, pay_period_start_date: Optional[str], pay_period_end_date: Optional[str], pay_date: Optional[str], paystub_provider: Optional[str], pay_frequency: Optional[PaystubPayFrequency]) :
        
        self.pay_period_start_date = pay_period_start_date;self.pay_period_end_date = pay_period_end_date;self.pay_date = pay_date;self.paystub_provider = paystub_provider;self.pay_frequency = pay_frequency
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(pay_period_start_date = data["pay_period_start_date"],pay_period_end_date = data["pay_period_end_date"],pay_date = data["pay_date"],paystub_provider = data["paystub_provider"],pay_frequency = data["pay_frequency"])


class PaystubPayFrequency:
    
    def __init__(self, paystub_pay_frequency: Optional[str]) :
        
        self.paystub_pay_frequency = paystub_pay_frequency
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IncomeBreakdown:
    
    def __init__(self, type_: Optional[IncomeBreakdownType], rate: Optional[float], hours: Optional[float], total: Optional[float]) :
        
        self.type_ = type_;self.rate = rate;self.hours = hours;self.total = total
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(type_ = data["type_"],rate = data["rate"],hours = data["hours"],total = data["total"])


class IncomeBreakdownType:
    
    def __init__(self, income_breakdown_type: Optional[str]) :
        
        self.income_breakdown_type = income_breakdown_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Employee:
    
    def __init__(self, address: PaystubAddress, name: Optional[str], marital_status: Optional[str], taxpayer_id: TaxpayerId) :
        
        self.address = address;self.name = name;self.marital_status = marital_status;self.taxpayer_id = taxpayer_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(address = data["address"],name = data["name"],marital_status = data["marital_status"],taxpayer_id = data["taxpayer_id"])


class TaxpayerId:
    
    def __init__(self, id_type: Optional[str], id_mask: Optional[str], last4_digits: Optional[str]) :
        
        self.id_type = id_type;self.id_mask = id_mask;self.last4_digits = last4_digits
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id_type = data["id_type"],id_mask = data["id_mask"],last4_digits = data["last4_digits"])


class PaystubEmployer:
    
    def __init__(self, address: PaystubAddress, name: Optional[str]) :
        
        self.address = address;self.name = name
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(address = data["address"],name = data["name"])


class PaystubAddress:
    
    def __init__(self, city: Optional[str], country: Optional[str], postal_code: Optional[str], region: Optional[str], street: Optional[str], line1: Optional[str], line2: Optional[str], state_code: Optional[str]) :
        
        self.city = city;self.country = country;self.postal_code = postal_code;self.region = region;self.street = street;self.line1 = line1;self.line2 = line2;self.state_code = state_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(city = data["city"],country = data["country"],postal_code = data["postal_code"],region = data["region"],street = data["street"],line1 = data["line1"],line2 = data["line2"],state_code = data["state_code"])


class PayPeriodDetails:
    
    def __init__(self, check_amount: Optional[float], distribution_breakdown: List[DistributionBreakdown], end_date: Optional[str], gross_earnings: Optional[float], pay_date: Optional[str], pay_frequency: Optional[str], pay_day: Optional[str], start_date: Optional[str]) :
        
        self.check_amount = check_amount;self.distribution_breakdown = distribution_breakdown;self.end_date = end_date;self.gross_earnings = gross_earnings;self.pay_date = pay_date;self.pay_frequency = pay_frequency;self.pay_day = pay_day;self.start_date = start_date
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(check_amount = data["check_amount"],distribution_breakdown = data["distribution_breakdown"],end_date = data["end_date"],gross_earnings = data["gross_earnings"],pay_date = data["pay_date"],pay_frequency = data["pay_frequency"],pay_day = data["pay_day"],start_date = data["start_date"])


class DistributionBreakdown:
    
    def __init__(self, account_name: Optional[str], bank_name: Optional[str], current_amount: Optional[float], iso_currency_code: Optional[str], mask: Optional[str], type_: Optional[str], unofficial_currency_code: Optional[str], current_pay: Pay) :
        
        self.account_name = account_name;self.bank_name = bank_name;self.current_amount = current_amount;self.iso_currency_code = iso_currency_code;self.mask = mask;self.type_ = type_;self.unofficial_currency_code = unofficial_currency_code;self.current_pay = current_pay
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_name = data["account_name"],bank_name = data["bank_name"],current_amount = data["current_amount"],iso_currency_code = data["iso_currency_code"],mask = data["mask"],type_ = data["type_"],unofficial_currency_code = data["unofficial_currency_code"],current_pay = data["current_pay"])


class PaystubDeduction:
    
    def __init__(self, type_: Optional[str], is_pretax: Optional[bool], total: Optional[float]) :
        
        self.type_ = type_;self.is_pretax = is_pretax;self.total = total
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(type_ = data["type_"],is_pretax = data["is_pretax"],total = data["total"])


class PaystubYtdDetails:
    
    def __init__(self, gross_earnings: Optional[float], net_earnings: Optional[float]) :
        
        self.gross_earnings = gross_earnings;self.net_earnings = net_earnings
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(gross_earnings = data["gross_earnings"],net_earnings = data["net_earnings"])


class PaystubVerification:
    
    def __init__(self, verification_status: Optional[PaystubVerificationStatus], verification_attributes: List[Optional[VerificationAttribute]]) :
        
        self.verification_status = verification_status;self.verification_attributes = verification_attributes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(verification_status = data["verification_status"],verification_attributes = data["verification_attributes"])


class PaystubVerificationStatus:
    
    def __init__(self, paystub_verification_status: Optional[str]) :
        
        self.paystub_verification_status = paystub_verification_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class VerificationAttribute:
    
    def __init__(self, type_: Optional[str]) :
        
        self.type_ = type_
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(type_ = data["type_"])


class IncomeVerificationDocumentsDownloadRequest:
    
    def __init__(self, income_verification_id: Optional[str], access_token: Optional[AccessTokenNullable], document_id: Optional[str]) :
        
        self.income_verification_id = income_verification_id;self.access_token = access_token;self.document_id = document_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(income_verification_id = data["income_verification_id"],access_token = data["access_token"],document_id = data["document_id"])


class IncomeVerificationTaxformsGetRequest:
    
    def __init__(self, income_verification_id: Optional[str], access_token: Optional[AccessTokenNullable]) :
        
        self.income_verification_id = income_verification_id;self.access_token = access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(income_verification_id = data["income_verification_id"],access_token = data["access_token"])


class IncomeVerificationTaxformsGetResponse:
    
    def __init__(self, request_id: RequestId, document_metadata: List[DocumentMetadata], taxforms: List[Taxform], error: Optional[PlaidError]) :
        
        self.request_id = request_id;self.document_metadata = document_metadata;self.taxforms = taxforms;self.error = error
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"],document_metadata = data["document_metadata"],taxforms = data["taxforms"],error = data["error"])


class Taxform:
    
    def __init__(self, doc_id: str, document_type: str, w2: W2) :
        
        self.doc_id = doc_id;self.document_type = document_type;self.w2 = w2
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(doc_id = data["doc_id"],document_type = data["document_type"],w2 = data["w2"])


class W2:
    
    def __init__(self, employer: PaystubEmployer, employee: Employee, tax_year: Optional[str], employer_id_number: Optional[str], wages_tips_other_comp: Optional[str], federal_income_tax_withheld: Optional[str], social_security_wages: Optional[str], social_security_tax_withheld: Optional[str], medicare_wages_and_tips: Optional[str], medicare_tax_withheld: Optional[str], social_security_tips: Optional[str], allocated_tips: Optional[str], box9: Optional[str], dependent_care_benefits: Optional[str], nonqualified_plans: Optional[str], box12: List[W2Box12], statutory_employee: Optional[str], retirement_plan: Optional[str], third_party_sick_pay: Optional[str], other: Optional[str], state_and_local_wages: List[W2StateAndLocalWages]) :
        
        self.employer = employer;self.employee = employee;self.tax_year = tax_year;self.employer_id_number = employer_id_number;self.wages_tips_other_comp = wages_tips_other_comp;self.federal_income_tax_withheld = federal_income_tax_withheld;self.social_security_wages = social_security_wages;self.social_security_tax_withheld = social_security_tax_withheld;self.medicare_wages_and_tips = medicare_wages_and_tips;self.medicare_tax_withheld = medicare_tax_withheld;self.social_security_tips = social_security_tips;self.allocated_tips = allocated_tips;self.box9 = box9;self.dependent_care_benefits = dependent_care_benefits;self.nonqualified_plans = nonqualified_plans;self.box12 = box12;self.statutory_employee = statutory_employee;self.retirement_plan = retirement_plan;self.third_party_sick_pay = third_party_sick_pay;self.other = other;self.state_and_local_wages = state_and_local_wages
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(employer = data["employer"],employee = data["employee"],tax_year = data["tax_year"],employer_id_number = data["employer_id_number"],wages_tips_other_comp = data["wages_tips_other_comp"],federal_income_tax_withheld = data["federal_income_tax_withheld"],social_security_wages = data["social_security_wages"],social_security_tax_withheld = data["social_security_tax_withheld"],medicare_wages_and_tips = data["medicare_wages_and_tips"],medicare_tax_withheld = data["medicare_tax_withheld"],social_security_tips = data["social_security_tips"],allocated_tips = data["allocated_tips"],box9 = data["box9"],dependent_care_benefits = data["dependent_care_benefits"],nonqualified_plans = data["nonqualified_plans"],box12 = data["box12"],statutory_employee = data["statutory_employee"],retirement_plan = data["retirement_plan"],third_party_sick_pay = data["third_party_sick_pay"],other = data["other"],state_and_local_wages = data["state_and_local_wages"])


class W2Box12:
    
    def __init__(self, code: Optional[str], amount: Optional[str]) :
        
        self.code = code;self.amount = amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(code = data["code"],amount = data["amount"])


class W2StateAndLocalWages:
    
    def __init__(self, state: Optional[str], employer_state_id_number: Optional[str], state_wages_tips: Optional[str], state_income_tax: Optional[str], local_wages_tips: Optional[str], local_income_tax: Optional[str], locality_name: Optional[str]) :
        
        self.state = state;self.employer_state_id_number = employer_state_id_number;self.state_wages_tips = state_wages_tips;self.state_income_tax = state_income_tax;self.local_wages_tips = local_wages_tips;self.local_income_tax = local_income_tax;self.locality_name = locality_name
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(state = data["state"],employer_state_id_number = data["employer_state_id_number"],state_wages_tips = data["state_wages_tips"],state_income_tax = data["state_income_tax"],local_wages_tips = data["local_wages_tips"],local_income_tax = data["local_income_tax"],locality_name = data["locality_name"])


class IncomeVerificationWebhookStatus:
    
    def __init__(self, id: str) :
        
        self.id = id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"])


class EmploymentVerificationGetRequest:
    
    def __init__(self, access_token: AccessToken) :
        
        self.access_token = access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"])


class EmploymentVerificationGetResponse:
    
    def __init__(self, employments: List[EmploymentVerification], request_id: RequestId) :
        
        self.employments = employments;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(employments = data["employments"],request_id = data["request_id"])


class EmploymentVerification:
    
    def __init__(self, status: Optional[EmploymentVerificationStatus], start_date: Optional[str], end_date: Optional[str], employer: EmployerVerification, title: Optional[str], platform_ids: PlatformIds) :
        
        self.status = status;self.start_date = start_date;self.end_date = end_date;self.employer = employer;self.title = title;self.platform_ids = platform_ids
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(status = data["status"],start_date = data["start_date"],end_date = data["end_date"],employer = data["employer"],title = data["title"],platform_ids = data["platform_ids"])


class EmploymentVerificationStatus:
    
    def __init__(self, employment_verification_status: Optional[str]) :
        
        self.employment_verification_status = employment_verification_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class EmployerVerification:
    
    def __init__(self, name: Optional[str]) :
        
        self.name = name
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(name = data["name"])


class PlatformIds:
    
    def __init__(self, employee_id: Optional[str], payroll_id: Optional[str], position_id: Optional[str]) :
        
        self.employee_id = employee_id;self.payroll_id = payroll_id;self.position_id = position_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(employee_id = data["employee_id"],payroll_id = data["payroll_id"],position_id = data["position_id"])


class AssetReportTransaction:
    
    def __init__(self, asset_report_transaction: Any) :
        
        self.asset_report_transaction = asset_report_transaction
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class HealthIncident:
    
    def __init__(self, start_date: str, end_date: str, title: str, incident_updates: List[IncidentUpdate]) :
        
        self.start_date = start_date;self.end_date = end_date;self.title = title;self.incident_updates = incident_updates
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(start_date = data["start_date"],end_date = data["end_date"],title = data["title"],incident_updates = data["incident_updates"])


class IncidentUpdate:
    
    def __init__(self, description: str, status: str, updated_date: str) :
        
        self.description = description;self.status = status;self.updated_date = updated_date
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(description = data["description"],status = data["status"],updated_date = data["updated_date"])


class DepositSwitchAltCreateRequest:
    
    def __init__(self, target_account: DepositSwitchTargetAccount, target_user: DepositSwitchTargetUser, options: DepositSwitchCreateRequestOptions, country_code: Optional[str]) :
        
        self.target_account = target_account;self.target_user = target_user;self.options = options;self.country_code = country_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(target_account = data["target_account"],target_user = data["target_user"],options = data["options"],country_code = data["country_code"])


class DepositSwitchAltCreateResponse:
    
    def __init__(self, deposit_switch_id: str, request_id: RequestId) :
        
        self.deposit_switch_id = deposit_switch_id;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(deposit_switch_id = data["deposit_switch_id"],request_id = data["request_id"])


class DepositSwitchTargetAccount:
    
    def __init__(self, account_number: str, routing_number: str, account_name: str, account_subtype: str) :
        
        self.account_number = account_number;self.routing_number = routing_number;self.account_name = account_name;self.account_subtype = account_subtype
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_number = data["account_number"],routing_number = data["routing_number"],account_name = data["account_name"],account_subtype = data["account_subtype"])


class DepositSwitchTargetUser:
    
    def __init__(self, given_name: str, family_name: str, phone: str, email: str, address: DepositSwitchAddressData, tax_payer_id: str) :
        
        self.given_name = given_name;self.family_name = family_name;self.phone = phone;self.email = email;self.address = address;self.tax_payer_id = tax_payer_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(given_name = data["given_name"],family_name = data["family_name"],phone = data["phone"],email = data["email"],address = data["address"],tax_payer_id = data["tax_payer_id"])


class DepositSwitchAddressData:
    
    def __init__(self, city: str, region: str, street: str, postal_code: str, country: str) :
        
        self.city = city;self.region = region;self.street = street;self.postal_code = postal_code;self.country = country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(city = data["city"],region = data["region"],street = data["street"],postal_code = data["postal_code"],country = data["country"])


class CreditBankIncomeGetRequest:
    
    def __init__(self, user_token: UserToken, options: CreditBankIncomeGetRequestOptions) :
        
        self.user_token = user_token;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(user_token = data["user_token"],options = data["options"])


class CreditBankIncomeGetRequestOptions:
    
    def __init__(self, count: int) :
        
        self.count = count
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(count = data["count"])


class CreditBankIncomeGetResponse:
    
    def __init__(self, bank_income: List[CreditBankIncome], request_id: RequestId) :
        
        self.bank_income = bank_income;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(bank_income = data["bank_income"],request_id = data["request_id"])


class CreditBankIncomePdfGetRequest:
    
    def __init__(self, user_token: UserToken) :
        
        self.user_token = user_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(user_token = data["user_token"])


class CreditBankIncomePdfGetResponse:
    
    def __init__(self, credit_bank_income_pdf_get_response: str) :
        
        self.credit_bank_income_pdf_get_response = credit_bank_income_pdf_get_response
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreditBankIncome:
    
    def __init__(self, bank_income_id: str, generated_time: str, days_requested: int, items: List[CreditBankIncomeItem], bank_income_summary: CreditBankIncomeSummary, warnings: List[CreditBankIncomeWarning]) :
        
        self.bank_income_id = bank_income_id;self.generated_time = generated_time;self.days_requested = days_requested;self.items = items;self.bank_income_summary = bank_income_summary;self.warnings = warnings
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(bank_income_id = data["bank_income_id"],generated_time = data["generated_time"],days_requested = data["days_requested"],items = data["items"],bank_income_summary = data["bank_income_summary"],warnings = data["warnings"])


class CreditBankIncomeItem:
    
    def __init__(self, bank_income_accounts: List[CreditBankIncomeAccount], bank_income_sources: List[CreditBankIncomeSource], last_updated_time: str, institution_id: str, institution_name: str, item_id: str) :
        
        self.bank_income_accounts = bank_income_accounts;self.bank_income_sources = bank_income_sources;self.last_updated_time = last_updated_time;self.institution_id = institution_id;self.institution_name = institution_name;self.item_id = item_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(bank_income_accounts = data["bank_income_accounts"],bank_income_sources = data["bank_income_sources"],last_updated_time = data["last_updated_time"],institution_id = data["institution_id"],institution_name = data["institution_name"],item_id = data["item_id"])


class CreditBankIncomeAccount:
    
    def __init__(self, account_id: str, mask: Optional[str], name: str, official_name: Optional[str], subtype: DepositoryAccountSubtype, type_: CreditBankIncomeAccountType, owners: List[Owner]) :
        
        self.account_id = account_id;self.mask = mask;self.name = name;self.official_name = official_name;self.subtype = subtype;self.type_ = type_;self.owners = owners
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],mask = data["mask"],name = data["name"],official_name = data["official_name"],subtype = data["subtype"],type_ = data["type_"],owners = data["owners"])


class CreditBankIncomeAccountType:
    
    def __init__(self, credit_bank_income_account_type: str) :
        
        self.credit_bank_income_account_type = credit_bank_income_account_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreditBankIncomeSource:
    
    def __init__(self, income_source_id: str, income_description: str, income_category: CreditBankIncomeCategory, account_id: str, start_date: str, end_date: str, pay_frequency: CreditBankIncomePayFrequency, total_amount: float, transaction_count: int, historical_summary: List[CreditBankIncomeHistoricalSummary]) :
        
        self.income_source_id = income_source_id;self.income_description = income_description;self.income_category = income_category;self.account_id = account_id;self.start_date = start_date;self.end_date = end_date;self.pay_frequency = pay_frequency;self.total_amount = total_amount;self.transaction_count = transaction_count;self.historical_summary = historical_summary
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(income_source_id = data["income_source_id"],income_description = data["income_description"],income_category = data["income_category"],account_id = data["account_id"],start_date = data["start_date"],end_date = data["end_date"],pay_frequency = data["pay_frequency"],total_amount = data["total_amount"],transaction_count = data["transaction_count"],historical_summary = data["historical_summary"])


class CreditBankIncomeCategory:
    
    def __init__(self, credit_bank_income_category: str) :
        
        self.credit_bank_income_category = credit_bank_income_category
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreditBankIncomePayFrequency:
    
    def __init__(self, credit_bank_income_pay_frequency: str) :
        
        self.credit_bank_income_pay_frequency = credit_bank_income_pay_frequency
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreditIsoCurrencyCode:
    
    def __init__(self, credit_iso_currency_code: Optional[str]) :
        
        self.credit_iso_currency_code = credit_iso_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreditUnofficialCurrencyCode:
    
    def __init__(self, credit_unofficial_currency_code: Optional[str]) :
        
        self.credit_unofficial_currency_code = credit_unofficial_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreditBankIncomeSummary:
    
    def __init__(self, total_amount: float, iso_currency_code: Optional[CreditIsoCurrencyCode], unofficial_currency_code: Optional[CreditUnofficialCurrencyCode], start_date: str, end_date: str, income_sources_count: int, income_categories_count: int, income_transactions_count: int, historical_summary: List[CreditBankIncomeHistoricalSummary]) :
        
        self.total_amount = total_amount;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code;self.start_date = start_date;self.end_date = end_date;self.income_sources_count = income_sources_count;self.income_categories_count = income_categories_count;self.income_transactions_count = income_transactions_count;self.historical_summary = historical_summary
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(total_amount = data["total_amount"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"],start_date = data["start_date"],end_date = data["end_date"],income_sources_count = data["income_sources_count"],income_categories_count = data["income_categories_count"],income_transactions_count = data["income_transactions_count"],historical_summary = data["historical_summary"])


class CreditBankIncomeHistoricalSummary:
    
    def __init__(self, total_amount: float, iso_currency_code: Optional[CreditIsoCurrencyCode], unofficial_currency_code: Optional[CreditUnofficialCurrencyCode], start_date: str, end_date: str, transactions: List[CreditBankIncomeTransaction]) :
        
        self.total_amount = total_amount;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code;self.start_date = start_date;self.end_date = end_date;self.transactions = transactions
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(total_amount = data["total_amount"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"],start_date = data["start_date"],end_date = data["end_date"],transactions = data["transactions"])


class CreditBankIncomeTransaction:
    
    def __init__(self, amount: float, date: str, name: str, original_description: Optional[str], pending: bool, transaction_id: str, check_number: Optional[str], iso_currency_code: Optional[CreditIsoCurrencyCode], unofficial_currency_code: Optional[CreditUnofficialCurrencyCode]) :
        
        self.amount = amount;self.date = date;self.name = name;self.original_description = original_description;self.pending = pending;self.transaction_id = transaction_id;self.check_number = check_number;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(amount = data["amount"],date = data["date"],name = data["name"],original_description = data["original_description"],pending = data["pending"],transaction_id = data["transaction_id"],check_number = data["check_number"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"])


class CreditBankIncomeRefreshRequest:
    
    def __init__(self, user_token: UserToken, options: CreditBankIncomeRefreshRequestOptions) :
        
        self.user_token = user_token;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(user_token = data["user_token"],options = data["options"])


class CreditBankIncomeRefreshRequestOptions:
    
    def __init__(self, days_requested: int, webhook: str) :
        
        self.days_requested = days_requested;self.webhook = webhook
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(days_requested = data["days_requested"],webhook = data["webhook"])


class CreditBankIncomeRefreshResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class CreditPayrollIncomeRiskSignalsGetRequest:
    
    def __init__(self, user_token: UserToken) :
        
        self.user_token = user_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(user_token = data["user_token"])


class CreditPayrollIncomeRiskSignalsGetResponse:
    
    def __init__(self, items: List[PayrollRiskSignalsItem], error: Optional[PlaidError], request_id: RequestId) :
        
        self.items = items;self.error = error;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(items = data["items"],error = data["error"],request_id = data["request_id"])


class PayrollRiskSignalsItem:
    
    def __init__(self, item_id: ItemId, verification_risk_signals: List[DocumentRiskSignalsObject]) :
        
        self.item_id = item_id;self.verification_risk_signals = verification_risk_signals
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(item_id = data["item_id"],verification_risk_signals = data["verification_risk_signals"])


class DocumentRiskSignalsObject:
    
    def __init__(self, account_id: Optional[str], single_document_risk_signals: List[SingleDocumentRiskSignal], multi_document_risk_signals: List[MultiDocumentRiskSignal]) :
        
        self.account_id = account_id;self.single_document_risk_signals = single_document_risk_signals;self.multi_document_risk_signals = multi_document_risk_signals
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],single_document_risk_signals = data["single_document_risk_signals"],multi_document_risk_signals = data["multi_document_risk_signals"])


class RiskSignalDocumentReference:
    
    def __init__(self, document_id: Optional[str], document_name: str) :
        
        self.document_id = document_id;self.document_name = document_name
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(document_id = data["document_id"],document_name = data["document_name"])


class SingleDocumentRiskSignal:
    
    def __init__(self, document_reference: RiskSignalDocumentReference, risk_signals: List[Optional[DocumentRiskSignal]]) :
        
        self.document_reference = document_reference;self.risk_signals = risk_signals
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(document_reference = data["document_reference"],risk_signals = data["risk_signals"])


class MultiDocumentRiskSignal:
    
    def __init__(self, document_references: List[RiskSignalDocumentReference], risk_signals: List[Optional[DocumentRiskSignal]]) :
        
        self.document_references = document_references;self.risk_signals = risk_signals
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(document_references = data["document_references"],risk_signals = data["risk_signals"])


class CreditAuditCopyTokenCreateRequest:
    
    def __init__(self, report_tokens: List[ReportToken], auditor_id: str) :
        
        self.report_tokens = report_tokens;self.auditor_id = auditor_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(report_tokens = data["report_tokens"],auditor_id = data["auditor_id"])


class CreditAuditCopyTokenCreateResponse:
    
    def __init__(self, audit_copy_token: str, request_id: RequestId) :
        
        self.audit_copy_token = audit_copy_token;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(audit_copy_token = data["audit_copy_token"],request_id = data["request_id"])


class CreditAuditCopyTokenRemoveRequest:
    
    def __init__(self, audit_copy_token: str) :
        
        self.audit_copy_token = audit_copy_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(audit_copy_token = data["audit_copy_token"])


class CreditAuditCopyTokenRemoveResponse:
    
    def __init__(self, removed: bool, request_id: RequestId) :
        
        self.removed = removed;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(removed = data["removed"],request_id = data["request_id"])


class CreditPayrollIncomeGetRequest:
    
    def __init__(self, user_token: UserToken) :
        
        self.user_token = user_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(user_token = data["user_token"])


class CreditPayrollIncomeGetResponse:
    
    def __init__(self, items: List[PayrollItem], error: Optional[PlaidError], request_id: RequestId) :
        
        self.items = items;self.error = error;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(items = data["items"],error = data["error"],request_id = data["request_id"])


class CreditDocumentMetadata:
    
    def __init__(self, name: str, document_type: Optional[CreditDocumentType], download_url: Optional[str], status: Optional[str]) :
        
        self.name = name;self.document_type = document_type;self.download_url = download_url;self.status = status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(name = data["name"],document_type = data["document_type"],download_url = data["download_url"],status = data["status"])


class CreditDocumentType:
    
    def __init__(self, credit_document_type: Optional[str]) :
        
        self.credit_document_type = credit_document_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PayrollItem:
    
    def __init__(self, item_id: ItemId, accounts: List[Optional[PayrollIncomeAccountData]], payroll_income: List[PayrollIncomeObject], status: Optional[PayrollItemStatus], pull_id: CreditPullId) :
        
        self.item_id = item_id;self.accounts = accounts;self.payroll_income = payroll_income;self.status = status;self.pull_id = pull_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(item_id = data["item_id"],accounts = data["accounts"],payroll_income = data["payroll_income"],status = data["status"],pull_id = data["pull_id"])


class PayrollIncomeAccountData:
    
    def __init__(self, account_id: Optional[str], rate_of_pay: PayrollIncomeRateOfPay, pay_frequency: Optional[str]) :
        
        self.account_id = account_id;self.rate_of_pay = rate_of_pay;self.pay_frequency = pay_frequency
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],rate_of_pay = data["rate_of_pay"],pay_frequency = data["pay_frequency"])


class PayrollIncomeObject:
    
    def __init__(self, account_id: Optional[str], pay_stubs: List[CreditPayStub], w2_s: List[CreditW2], form1099_s: List[Credit1099]) :
        
        self.account_id = account_id;self.pay_stubs = pay_stubs;self.w2_s = w2_s;self.form1099_s = form1099_s
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],pay_stubs = data["pay_stubs"],w2_s = data["w2_s"],form1099_s = data["form1099_s"])


class Credit1099:
    
    def __init__(self, document_id: Optional[str], document_metadata: CreditDocumentMetadata, form1099_type: Form1099Type, recipient: Credit1099Recipient, payer: Credit1099Payer, filer: Credit1099Filer, tax_year: Optional[str], rents: Optional[float], royalties: Optional[float], other_income: Optional[float], federal_income_tax_withheld: Optional[float], fishing_boat_proceeds: Optional[float], medical_and_healthcare_payments: Optional[float], nonemployee_compensation: Optional[float], substitute_payments_in_lieu_of_dividends_or_interest: Optional[float], payer_made_direct_sales_of5000_or_more_of_consumer_products_to_buyer: Optional[str], crop_insurance_proceeds: Optional[float], excess_golden_parachute_payments: Optional[float], gross_proceeds_paid_to_an_attorney: Optional[float], section409_a_deferrals: Optional[float], section409_a_income: Optional[float], state_tax_withheld: Optional[float], state_tax_withheld_lower: Optional[float], payer_state_number: Optional[str], payer_state_number_lower: Optional[str], state_income: Optional[float], state_income_lower: Optional[float], transactions_reported: Optional[str], pse_name: Optional[str], pse_telephone_number: Optional[str], gross_amount: Optional[float], card_not_present_transaction: Optional[float], merchant_category_code: Optional[str], number_of_payment_transactions: Optional[str], january_amount: Optional[float], february_amount: Optional[float], march_amount: Optional[float], april_amount: Optional[float], may_amount: Optional[float], june_amount: Optional[float], july_amount: Optional[float], august_amount: Optional[float], september_amount: Optional[float], october_amount: Optional[float], november_amount: Optional[float], december_amount: Optional[float], primary_state: Optional[str], secondary_state: Optional[str], primary_state_id: Optional[str], secondary_state_id: Optional[str], primary_state_income_tax: Optional[float], secondary_state_income_tax: Optional[float]) :
        
        self.document_id = document_id;self.document_metadata = document_metadata;self.form1099_type = form1099_type;self.recipient = recipient;self.payer = payer;self.filer = filer;self.tax_year = tax_year;self.rents = rents;self.royalties = royalties;self.other_income = other_income;self.federal_income_tax_withheld = federal_income_tax_withheld;self.fishing_boat_proceeds = fishing_boat_proceeds;self.medical_and_healthcare_payments = medical_and_healthcare_payments;self.nonemployee_compensation = nonemployee_compensation;self.substitute_payments_in_lieu_of_dividends_or_interest = substitute_payments_in_lieu_of_dividends_or_interest;self.payer_made_direct_sales_of5000_or_more_of_consumer_products_to_buyer = payer_made_direct_sales_of5000_or_more_of_consumer_products_to_buyer;self.crop_insurance_proceeds = crop_insurance_proceeds;self.excess_golden_parachute_payments = excess_golden_parachute_payments;self.gross_proceeds_paid_to_an_attorney = gross_proceeds_paid_to_an_attorney;self.section409_a_deferrals = section409_a_deferrals;self.section409_a_income = section409_a_income;self.state_tax_withheld = state_tax_withheld;self.state_tax_withheld_lower = state_tax_withheld_lower;self.payer_state_number = payer_state_number;self.payer_state_number_lower = payer_state_number_lower;self.state_income = state_income;self.state_income_lower = state_income_lower;self.transactions_reported = transactions_reported;self.pse_name = pse_name;self.pse_telephone_number = pse_telephone_number;self.gross_amount = gross_amount;self.card_not_present_transaction = card_not_present_transaction;self.merchant_category_code = merchant_category_code;self.number_of_payment_transactions = number_of_payment_transactions;self.january_amount = january_amount;self.february_amount = february_amount;self.march_amount = march_amount;self.april_amount = april_amount;self.may_amount = may_amount;self.june_amount = june_amount;self.july_amount = july_amount;self.august_amount = august_amount;self.september_amount = september_amount;self.october_amount = october_amount;self.november_amount = november_amount;self.december_amount = december_amount;self.primary_state = primary_state;self.secondary_state = secondary_state;self.primary_state_id = primary_state_id;self.secondary_state_id = secondary_state_id;self.primary_state_income_tax = primary_state_income_tax;self.secondary_state_income_tax = secondary_state_income_tax
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(document_id = data["document_id"],document_metadata = data["document_metadata"],form1099_type = data["form1099_type"],recipient = data["recipient"],payer = data["payer"],filer = data["filer"],tax_year = data["tax_year"],rents = data["rents"],royalties = data["royalties"],other_income = data["other_income"],federal_income_tax_withheld = data["federal_income_tax_withheld"],fishing_boat_proceeds = data["fishing_boat_proceeds"],medical_and_healthcare_payments = data["medical_and_healthcare_payments"],nonemployee_compensation = data["nonemployee_compensation"],substitute_payments_in_lieu_of_dividends_or_interest = data["substitute_payments_in_lieu_of_dividends_or_interest"],payer_made_direct_sales_of5000_or_more_of_consumer_products_to_buyer = data["payer_made_direct_sales_of5000_or_more_of_consumer_products_to_buyer"],crop_insurance_proceeds = data["crop_insurance_proceeds"],excess_golden_parachute_payments = data["excess_golden_parachute_payments"],gross_proceeds_paid_to_an_attorney = data["gross_proceeds_paid_to_an_attorney"],section409_a_deferrals = data["section409_a_deferrals"],section409_a_income = data["section409_a_income"],state_tax_withheld = data["state_tax_withheld"],state_tax_withheld_lower = data["state_tax_withheld_lower"],payer_state_number = data["payer_state_number"],payer_state_number_lower = data["payer_state_number_lower"],state_income = data["state_income"],state_income_lower = data["state_income_lower"],transactions_reported = data["transactions_reported"],pse_name = data["pse_name"],pse_telephone_number = data["pse_telephone_number"],gross_amount = data["gross_amount"],card_not_present_transaction = data["card_not_present_transaction"],merchant_category_code = data["merchant_category_code"],number_of_payment_transactions = data["number_of_payment_transactions"],january_amount = data["january_amount"],february_amount = data["february_amount"],march_amount = data["march_amount"],april_amount = data["april_amount"],may_amount = data["may_amount"],june_amount = data["june_amount"],july_amount = data["july_amount"],august_amount = data["august_amount"],september_amount = data["september_amount"],october_amount = data["october_amount"],november_amount = data["november_amount"],december_amount = data["december_amount"],primary_state = data["primary_state"],secondary_state = data["secondary_state"],primary_state_id = data["primary_state_id"],secondary_state_id = data["secondary_state_id"],primary_state_income_tax = data["primary_state_income_tax"],secondary_state_income_tax = data["secondary_state_income_tax"])


class Form1099Type:
    
    def __init__(self, form1099_type: str) :
        
        self.form1099_type = form1099_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Credit1099Payer:
    
    def __init__(self, address: CreditPayStubAddress, name: Optional[str], tin: Optional[str], telephone_number: Optional[str]) :
        
        self.address = address;self.name = name;self.tin = tin;self.telephone_number = telephone_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(address = data["address"],name = data["name"],tin = data["tin"],telephone_number = data["telephone_number"])


class Credit1099Recipient:
    
    def __init__(self, address: CreditPayStubAddress, name: Optional[str], tin: Optional[str], account_number: Optional[str], facta_filing_requirement: Optional[str], second_tin_exists: Optional[str]) :
        
        self.address = address;self.name = name;self.tin = tin;self.account_number = account_number;self.facta_filing_requirement = facta_filing_requirement;self.second_tin_exists = second_tin_exists
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(address = data["address"],name = data["name"],tin = data["tin"],account_number = data["account_number"],facta_filing_requirement = data["facta_filing_requirement"],second_tin_exists = data["second_tin_exists"])


class Credit1099Filer:
    
    def __init__(self, address: CreditPayStubAddress, name: Optional[str], tin: Optional[str], type_: Optional[str]) :
        
        self.address = address;self.name = name;self.tin = tin;self.type_ = type_
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(address = data["address"],name = data["name"],tin = data["tin"],type_ = data["type_"])


class CreditPayStub:
    
    def __init__(self, deductions: CreditPayStubDeductions, document_id: Optional[str], document_metadata: CreditDocumentMetadata, earnings: CreditPayStubEarnings, employee: CreditPayStubEmployee, employer: CreditPayStubEmployer, net_pay: CreditPayStubNetPay, pay_period_details: PayStubPayPeriodDetails, verification: Optional[CreditPayStubVerification]) :
        
        self.deductions = deductions;self.document_id = document_id;self.document_metadata = document_metadata;self.earnings = earnings;self.employee = employee;self.employer = employer;self.net_pay = net_pay;self.pay_period_details = pay_period_details;self.verification = verification
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(deductions = data["deductions"],document_id = data["document_id"],document_metadata = data["document_metadata"],earnings = data["earnings"],employee = data["employee"],employer = data["employer"],net_pay = data["net_pay"],pay_period_details = data["pay_period_details"],verification = data["verification"])


class CreditPayStubDeductions:
    
    def __init__(self, breakdown: List[PayStubDeductionsBreakdown], total: PayStubDeductionsTotal) :
        
        self.breakdown = breakdown;self.total = total
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(breakdown = data["breakdown"],total = data["total"])


class PayStubDeductionsBreakdown:
    
    def __init__(self, current_amount: Optional[float], description: Optional[str], iso_currency_code: Optional[str], unofficial_currency_code: Optional[str], ytd_amount: Optional[float]) :
        
        self.current_amount = current_amount;self.description = description;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code;self.ytd_amount = ytd_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(current_amount = data["current_amount"],description = data["description"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"],ytd_amount = data["ytd_amount"])


class PayStubDeductionsTotal:
    
    def __init__(self, current_amount: Optional[float], iso_currency_code: Optional[str], unofficial_currency_code: Optional[str], ytd_amount: Optional[float]) :
        
        self.current_amount = current_amount;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code;self.ytd_amount = ytd_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(current_amount = data["current_amount"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"],ytd_amount = data["ytd_amount"])


class CreditPayStubEarnings:
    
    def __init__(self, breakdown: List[PayStubEarningsBreakdown], total: PayStubEarningsTotal) :
        
        self.breakdown = breakdown;self.total = total
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(breakdown = data["breakdown"],total = data["total"])


class PayStubEarningsBreakdown:
    
    def __init__(self, canonical_description: Optional[PayStubEarningsBreakdownCanonicalDescription], current_amount: Optional[float], description: Optional[str], hours: Optional[float], iso_currency_code: Optional[str], rate: Optional[float], unofficial_currency_code: Optional[str], ytd_amount: Optional[float]) :
        
        self.canonical_description = canonical_description;self.current_amount = current_amount;self.description = description;self.hours = hours;self.iso_currency_code = iso_currency_code;self.rate = rate;self.unofficial_currency_code = unofficial_currency_code;self.ytd_amount = ytd_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(canonical_description = data["canonical_description"],current_amount = data["current_amount"],description = data["description"],hours = data["hours"],iso_currency_code = data["iso_currency_code"],rate = data["rate"],unofficial_currency_code = data["unofficial_currency_code"],ytd_amount = data["ytd_amount"])


class PayStubEarningsBreakdownCanonicalDescription:
    
    def __init__(self, pay_stub_earnings_breakdown_canonical_description: Optional[str]) :
        
        self.pay_stub_earnings_breakdown_canonical_description = pay_stub_earnings_breakdown_canonical_description
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PayStubEarningsTotal:
    
    def __init__(self, current_amount: Optional[float], hours: Optional[float], iso_currency_code: Optional[str], unofficial_currency_code: Optional[str], ytd_amount: Optional[float]) :
        
        self.current_amount = current_amount;self.hours = hours;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code;self.ytd_amount = ytd_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(current_amount = data["current_amount"],hours = data["hours"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"],ytd_amount = data["ytd_amount"])


class CreditPayStubEmployee:
    
    def __init__(self, address: CreditPayStubAddress, name: Optional[str], marital_status: Optional[str], taxpayer_id: PayStubTaxpayerId) :
        
        self.address = address;self.name = name;self.marital_status = marital_status;self.taxpayer_id = taxpayer_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(address = data["address"],name = data["name"],marital_status = data["marital_status"],taxpayer_id = data["taxpayer_id"])


class CreditPayStubAddress:
    
    def __init__(self, city: Optional[str], country: Optional[str], postal_code: Optional[str], region: Optional[str], street: Optional[str]) :
        
        self.city = city;self.country = country;self.postal_code = postal_code;self.region = region;self.street = street
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(city = data["city"],country = data["country"],postal_code = data["postal_code"],region = data["region"],street = data["street"])


class PayStubTaxpayerId:
    
    def __init__(self, id_type: Optional[str], id_mask: Optional[str]) :
        
        self.id_type = id_type;self.id_mask = id_mask
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id_type = data["id_type"],id_mask = data["id_mask"])


class CreditPayStubEmployer:
    
    def __init__(self, address: CreditPayStubAddress, name: Optional[str]) :
        
        self.address = address;self.name = name
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(address = data["address"],name = data["name"])


class CreditPayStubNetPay:
    
    def __init__(self, current_amount: Optional[float], description: Optional[str], iso_currency_code: Optional[str], unofficial_currency_code: Optional[str], ytd_amount: Optional[float]) :
        
        self.current_amount = current_amount;self.description = description;self.iso_currency_code = iso_currency_code;self.unofficial_currency_code = unofficial_currency_code;self.ytd_amount = ytd_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(current_amount = data["current_amount"],description = data["description"],iso_currency_code = data["iso_currency_code"],unofficial_currency_code = data["unofficial_currency_code"],ytd_amount = data["ytd_amount"])


class PayStubPayPeriodDetails:
    
    def __init__(self, pay_amount: Optional[float], distribution_breakdown: List[PayStubDistributionBreakdown], end_date: Optional[str], gross_earnings: Optional[float], iso_currency_code: Optional[str], pay_date: Optional[str], pay_frequency: Optional[str], start_date: Optional[str], unofficial_currency_code: Optional[str]) :
        
        self.pay_amount = pay_amount;self.distribution_breakdown = distribution_breakdown;self.end_date = end_date;self.gross_earnings = gross_earnings;self.iso_currency_code = iso_currency_code;self.pay_date = pay_date;self.pay_frequency = pay_frequency;self.start_date = start_date;self.unofficial_currency_code = unofficial_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(pay_amount = data["pay_amount"],distribution_breakdown = data["distribution_breakdown"],end_date = data["end_date"],gross_earnings = data["gross_earnings"],iso_currency_code = data["iso_currency_code"],pay_date = data["pay_date"],pay_frequency = data["pay_frequency"],start_date = data["start_date"],unofficial_currency_code = data["unofficial_currency_code"])


class PayStubDistributionBreakdown:
    
    def __init__(self, account_name: Optional[str], bank_name: Optional[str], current_amount: Optional[float], iso_currency_code: Optional[str], mask: Optional[str], type_: Optional[str], unofficial_currency_code: Optional[str]) :
        
        self.account_name = account_name;self.bank_name = bank_name;self.current_amount = current_amount;self.iso_currency_code = iso_currency_code;self.mask = mask;self.type_ = type_;self.unofficial_currency_code = unofficial_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_name = data["account_name"],bank_name = data["bank_name"],current_amount = data["current_amount"],iso_currency_code = data["iso_currency_code"],mask = data["mask"],type_ = data["type_"],unofficial_currency_code = data["unofficial_currency_code"])


class CreditPayStubVerification:
    
    def __init__(self, verification_status: Optional[CreditPayStubVerificationStatus], verification_attributes: List[Optional[PayStubVerificationAttribute]]) :
        
        self.verification_status = verification_status;self.verification_attributes = verification_attributes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(verification_status = data["verification_status"],verification_attributes = data["verification_attributes"])


class CreditPayStubVerificationStatus:
    
    def __init__(self, credit_pay_stub_verification_status: Optional[str]) :
        
        self.credit_pay_stub_verification_status = credit_pay_stub_verification_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PayStubVerificationAttribute:
    
    def __init__(self, type_: Optional[str]) :
        
        self.type_ = type_
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(type_ = data["type_"])


class ReportToken:
    
    def __init__(self, report_type: ReportType, token: str) :
        
        self.report_type = report_type;self.token = token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(report_type = data["report_type"],token = data["token"])


class ReportType:
    
    def __init__(self, report_type: str) :
        
        self.report_type = report_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class DocumentRiskSignal:
    
    def __init__(self, type_: Optional[str], field: Optional[str], has_fraud_risk: Optional[bool], institution_metadata: Optional[DocumentRiskSignalInstitutionMetadata], expected_value: Optional[str], actual_value: Optional[str], signal_description: Optional[str]) :
        
        self.type_ = type_;self.field = field;self.has_fraud_risk = has_fraud_risk;self.institution_metadata = institution_metadata;self.expected_value = expected_value;self.actual_value = actual_value;self.signal_description = signal_description
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(type_ = data["type_"],field = data["field"],has_fraud_risk = data["has_fraud_risk"],institution_metadata = data["institution_metadata"],expected_value = data["expected_value"],actual_value = data["actual_value"],signal_description = data["signal_description"])


class DocumentRiskSignalInstitutionMetadata:
    
    def __init__(self, item_id: ItemId) :
        
        self.item_id = item_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(item_id = data["item_id"])


class PayrollItemStatus:
    
    def __init__(self, processing_status: Optional[str]) :
        
        self.processing_status = processing_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(processing_status = data["processing_status"])


class CreditW2:
    
    def __init__(self, document_metadata: CreditDocumentMetadata, document_id: str, employer: CreditPayStubEmployer, employee: CreditPayStubEmployee, tax_year: Optional[str], employer_id_number: Optional[str], wages_tips_other_comp: Optional[str], federal_income_tax_withheld: Optional[str], social_security_wages: Optional[str], social_security_tax_withheld: Optional[str], medicare_wages_and_tips: Optional[str], medicare_tax_withheld: Optional[str], social_security_tips: Optional[str], allocated_tips: Optional[str], box9: Optional[str], dependent_care_benefits: Optional[str], nonqualified_plans: Optional[str], box12: List[W2Box12], statutory_employee: Optional[str], retirement_plan: Optional[str], third_party_sick_pay: Optional[str], other: Optional[str], state_and_local_wages: List[W2StateAndLocalWages]) :
        
        self.document_metadata = document_metadata;self.document_id = document_id;self.employer = employer;self.employee = employee;self.tax_year = tax_year;self.employer_id_number = employer_id_number;self.wages_tips_other_comp = wages_tips_other_comp;self.federal_income_tax_withheld = federal_income_tax_withheld;self.social_security_wages = social_security_wages;self.social_security_tax_withheld = social_security_tax_withheld;self.medicare_wages_and_tips = medicare_wages_and_tips;self.medicare_tax_withheld = medicare_tax_withheld;self.social_security_tips = social_security_tips;self.allocated_tips = allocated_tips;self.box9 = box9;self.dependent_care_benefits = dependent_care_benefits;self.nonqualified_plans = nonqualified_plans;self.box12 = box12;self.statutory_employee = statutory_employee;self.retirement_plan = retirement_plan;self.third_party_sick_pay = third_party_sick_pay;self.other = other;self.state_and_local_wages = state_and_local_wages
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(document_metadata = data["document_metadata"],document_id = data["document_id"],employer = data["employer"],employee = data["employee"],tax_year = data["tax_year"],employer_id_number = data["employer_id_number"],wages_tips_other_comp = data["wages_tips_other_comp"],federal_income_tax_withheld = data["federal_income_tax_withheld"],social_security_wages = data["social_security_wages"],social_security_tax_withheld = data["social_security_tax_withheld"],medicare_wages_and_tips = data["medicare_wages_and_tips"],medicare_tax_withheld = data["medicare_tax_withheld"],social_security_tips = data["social_security_tips"],allocated_tips = data["allocated_tips"],box9 = data["box9"],dependent_care_benefits = data["dependent_care_benefits"],nonqualified_plans = data["nonqualified_plans"],box12 = data["box12"],statutory_employee = data["statutory_employee"],retirement_plan = data["retirement_plan"],third_party_sick_pay = data["third_party_sick_pay"],other = data["other"],state_and_local_wages = data["state_and_local_wages"])


class PayrollIncomeRateOfPay:
    
    def __init__(self, pay_rate: Optional[str], pay_amount: Optional[float]) :
        
        self.pay_rate = pay_rate;self.pay_amount = pay_amount
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(pay_rate = data["pay_rate"],pay_amount = data["pay_amount"])


class CreditPayrollIncomePrecheckRequest:
    
    def __init__(self, user_token: UserToken, access_tokens: List[AccessToken], employer: Optional[IncomeVerificationPrecheckEmployer], us_military_info: Optional[IncomeVerificationPrecheckMilitaryInfo]) :
        
        self.user_token = user_token;self.access_tokens = access_tokens;self.employer = employer;self.us_military_info = us_military_info
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(user_token = data["user_token"],access_tokens = data["access_tokens"],employer = data["employer"],us_military_info = data["us_military_info"])


class CreditPayrollIncomePrecheckResponse:
    
    def __init__(self, request_id: RequestId, confidence: IncomeVerificationPrecheckConfidence) :
        
        self.request_id = request_id;self.confidence = confidence
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"],confidence = data["confidence"])


class CreditPayrollIncomeRefreshRequest:
    
    def __init__(self, user_token: UserToken) :
        
        self.user_token = user_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(user_token = data["user_token"])


class CreditPayrollIncomeRefreshResponse:
    
    def __init__(self, request_id: RequestId, verification_refresh_status: CreditPayrollIncomeRefreshStatus) :
        
        self.request_id = request_id;self.verification_refresh_status = verification_refresh_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"],verification_refresh_status = data["verification_refresh_status"])


class CreditEmploymentGetRequest:
    
    def __init__(self, user_token: UserToken) :
        
        self.user_token = user_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(user_token = data["user_token"])


class CreditEmploymentGetResponse:
    
    def __init__(self, items: List[CreditEmploymentItem], request_id: RequestId) :
        
        self.items = items;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(items = data["items"],request_id = data["request_id"])


class CreditEmploymentItem:
    
    def __init__(self, item_id: ItemId, employments: List[CreditEmploymentVerification], pull_id: CreditPullId) :
        
        self.item_id = item_id;self.employments = employments;self.pull_id = pull_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(item_id = data["item_id"],employments = data["employments"],pull_id = data["pull_id"])


class CreditEmploymentVerification:
    
    def __init__(self, account_id: Optional[str], status: Optional[CreditEmploymentVerificationStatus], start_date: Optional[str], end_date: Optional[str], employer: CreditEmployerVerification, title: Optional[str], platform_ids: CreditPlatformIds, employee_type: Optional[CreditEmploymentEmployeeType], last_paystub_date: Optional[str]) :
        
        self.account_id = account_id;self.status = status;self.start_date = start_date;self.end_date = end_date;self.employer = employer;self.title = title;self.platform_ids = platform_ids;self.employee_type = employee_type;self.last_paystub_date = last_paystub_date
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_id = data["account_id"],status = data["status"],start_date = data["start_date"],end_date = data["end_date"],employer = data["employer"],title = data["title"],platform_ids = data["platform_ids"],employee_type = data["employee_type"],last_paystub_date = data["last_paystub_date"])


class CreditEmploymentEmployeeType:
    
    def __init__(self, credit_employment_employee_type: Optional[str]) :
        
        self.credit_employment_employee_type = credit_employment_employee_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreditEmploymentVerificationStatus:
    
    def __init__(self, credit_employment_verification_status: Optional[str]) :
        
        self.credit_employment_verification_status = credit_employment_verification_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreditEmployerVerification:
    
    def __init__(self, name: Optional[str]) :
        
        self.name = name
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(name = data["name"])


class CreditPlatformIds:
    
    def __init__(self, employee_id: Optional[str], payroll_id: Optional[str], position_id: Optional[str]) :
        
        self.employee_id = employee_id;self.payroll_id = payroll_id;self.position_id = position_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(employee_id = data["employee_id"],payroll_id = data["payroll_id"],position_id = data["position_id"])


class CreditBankIncomeWarning:
    
    def __init__(self, warning_type: CreditBankIncomeWarningType, warning_code: CreditBankIncomeWarningCode, cause: CreditBankIncomeCause) :
        
        self.warning_type = warning_type;self.warning_code = warning_code;self.cause = cause
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(warning_type = data["warning_type"],warning_code = data["warning_code"],cause = data["cause"])


class CreditBankIncomeWarningType:
    
    def __init__(self, credit_bank_income_warning_type: str) :
        
        self.credit_bank_income_warning_type = credit_bank_income_warning_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreditBankIncomeWarningCode:
    
    def __init__(self, credit_bank_income_warning_code: str) :
        
        self.credit_bank_income_warning_code = credit_bank_income_warning_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreditBankIncomeCause:
    
    def __init__(self, error_type: CreditBankIncomeErrorType, error_code: str, error_message: str, display_message: str, item_id: str) :
        
        self.error_type = error_type;self.error_code = error_code;self.error_message = error_message;self.display_message = display_message;self.item_id = item_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(error_type = data["error_type"],error_code = data["error_code"],error_message = data["error_message"],display_message = data["display_message"],item_id = data["item_id"])


class CreditBankIncomeErrorType:
    
    def __init__(self, credit_bank_income_error_type: str) :
        
        self.credit_bank_income_error_type = credit_bank_income_error_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreditRelayCreateRequest:
    
    def __init__(self, report_tokens: List[ReportToken], secondary_client_id: str, webhook: Optional[str]) :
        
        self.report_tokens = report_tokens;self.secondary_client_id = secondary_client_id;self.webhook = webhook
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(report_tokens = data["report_tokens"],secondary_client_id = data["secondary_client_id"],webhook = data["webhook"])


class CreditRelayCreateResponse:
    
    def __init__(self, relay_token: str, request_id: RequestId) :
        
        self.relay_token = relay_token;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(relay_token = data["relay_token"],request_id = data["request_id"])


class CreditRelayGetRequest:
    
    def __init__(self, relay_token: str, report_type: ReportType) :
        
        self.relay_token = relay_token;self.report_type = report_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(relay_token = data["relay_token"],report_type = data["report_type"])


class CreditRelayRefreshRequest:
    
    def __init__(self, relay_token: str, report_type: ReportType, webhook: Optional[str]) :
        
        self.relay_token = relay_token;self.report_type = report_type;self.webhook = webhook
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(relay_token = data["relay_token"],report_type = data["report_type"],webhook = data["webhook"])


class CreditRelayRefreshResponse:
    
    def __init__(self, relay_token: str, asset_report_id: AssetReportId, request_id: RequestId) :
        
        self.relay_token = relay_token;self.asset_report_id = asset_report_id;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(relay_token = data["relay_token"],asset_report_id = data["asset_report_id"],request_id = data["request_id"])


class CreditRelayRemoveRequest:
    
    def __init__(self, relay_token: str) :
        
        self.relay_token = relay_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(relay_token = data["relay_token"])


class CreditRelayRemoveResponse:
    
    def __init__(self, removed: bool, request_id: RequestId) :
        
        self.removed = removed;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(removed = data["removed"],request_id = data["request_id"])


class SandboxBankTransferFireWebhookRequest:
    
    def __init__(self, webhook: str) :
        
        self.webhook = webhook
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook = data["webhook"])


class SandboxBankTransferFireWebhookResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class SandboxTransferFireWebhookRequest:
    
    def __init__(self, webhook: str) :
        
        self.webhook = webhook
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook = data["webhook"])


class SandboxTransferFireWebhookResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class ApplicationId:
    
    def __init__(self, application_id: str) :
        
        self.application_id = application_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Application:
    
    def __init__(self, application_id: ApplicationId, name: str, display_name: Optional[str], join_date: str, logo_url: Optional[str], application_url: Optional[str], reason_for_access: Optional[str], use_case: Optional[str], company_legal_name: Optional[str], city: Optional[str], region: Optional[str], postal_code: Optional[str], country_code: Optional[str]) :
        
        self.application_id = application_id;self.name = name;self.display_name = display_name;self.join_date = join_date;self.logo_url = logo_url;self.application_url = application_url;self.reason_for_access = reason_for_access;self.use_case = use_case;self.company_legal_name = company_legal_name;self.city = city;self.region = region;self.postal_code = postal_code;self.country_code = country_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(application_id = data["application_id"],name = data["name"],display_name = data["display_name"],join_date = data["join_date"],logo_url = data["logo_url"],application_url = data["application_url"],reason_for_access = data["reason_for_access"],use_case = data["use_case"],company_legal_name = data["company_legal_name"],city = data["city"],region = data["region"],postal_code = data["postal_code"],country_code = data["country_code"])


class ApplicationGetRequest:
    
    def __init__(self, application_id: ApplicationId) :
        
        self.application_id = application_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(application_id = data["application_id"])


class ApplicationGetResponse:
    
    def __init__(self, request_id: RequestId, application: Application) :
        
        self.request_id = request_id;self.application = application
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"],application = data["application"])


class ProductAccess:
    
    def __init__(self, statements: Optional[bool], identity: Optional[bool], auth: Optional[bool], transactions: Optional[bool], accounts_details_transactions: Optional[bool], accounts_routing_number: Optional[bool], accounts_statements: Optional[bool], accounts_tax_statements: Optional[bool], customers_profiles: Optional[bool]) :
        
        self.statements = statements;self.identity = identity;self.auth = auth;self.transactions = transactions;self.accounts_details_transactions = accounts_details_transactions;self.accounts_routing_number = accounts_routing_number;self.accounts_statements = accounts_statements;self.accounts_tax_statements = accounts_tax_statements;self.customers_profiles = customers_profiles
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(statements = data["statements"],identity = data["identity"],auth = data["auth"],transactions = data["transactions"],accounts_details_transactions = data["accounts_details_transactions"],accounts_routing_number = data["accounts_routing_number"],accounts_statements = data["accounts_statements"],accounts_tax_statements = data["accounts_tax_statements"],customers_profiles = data["customers_profiles"])


class AccountAccess:
    
    def __init__(self, unique_id: str, authorized: Optional[bool], account_product_access: Optional[AccountProductAccessNullable]) :
        
        self.unique_id = unique_id;self.authorized = authorized;self.account_product_access = account_product_access
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(unique_id = data["unique_id"],authorized = data["authorized"],account_product_access = data["account_product_access"])


class AccountProductAccessNullable:
    
    def __init__(self, account_product_access_nullable: Optional[Any]) :
        
        self.account_product_access_nullable = account_product_access_nullable
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class AccountProductAccess:
    
    def __init__(self, account_data: Optional[bool], statements: Optional[bool], tax_documents: Optional[bool]) :
        
        self.account_data = account_data;self.statements = statements;self.tax_documents = tax_documents
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_data = data["account_data"],statements = data["statements"],tax_documents = data["tax_documents"])


class ScopesNullable:
    
    def __init__(self, scopes_nullable: Optional[Any]) :
        
        self.scopes_nullable = scopes_nullable
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Scopes:
    
    def __init__(self, product_access: ProductAccess, accounts: List[AccountAccess], new_accounts: Optional[bool]) :
        
        self.product_access = product_access;self.accounts = accounts;self.new_accounts = new_accounts
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(product_access = data["product_access"],accounts = data["accounts"],new_accounts = data["new_accounts"])


class ScopesState:
    
    def __init__(self, scopes_state: str) :
        
        self.scopes_state = scopes_state
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ScopesContext:
    
    def __init__(self, scopes_context: str) :
        
        self.scopes_context = scopes_context
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ItemApplicationScopesUpdateRequest:
    
    def __init__(self, access_token: AccessToken, application_id: ApplicationId, scopes: Scopes, state: ScopesState, context: ScopesContext) :
        
        self.access_token = access_token;self.application_id = application_id;self.scopes = scopes;self.state = state;self.context = context
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],application_id = data["application_id"],scopes = data["scopes"],state = data["state"],context = data["context"])


class ItemApplicationScopesUpdateResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class ItemApplicationListRequest:
    
    def __init__(self, access_token: Optional[AccessTokenNullable]) :
        
        self.access_token = access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"])


class ItemApplicationListResponse:
    
    def __init__(self, request_id: RequestId, applications: List[ConnectedApplication]) :
        
        self.request_id = request_id;self.applications = applications
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"],applications = data["applications"])


class ConnectedApplication:
    
    def __init__(self, application_id: ApplicationId, name: str, display_name: Optional[str], logo_url: Optional[str], application_url: Optional[str], reason_for_access: Optional[str], created_at: str, scopes: Optional[ScopesNullable]) :
        
        self.application_id = application_id;self.name = name;self.display_name = display_name;self.logo_url = logo_url;self.application_url = application_url;self.reason_for_access = reason_for_access;self.created_at = created_at;self.scopes = scopes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(application_id = data["application_id"],name = data["name"],display_name = data["display_name"],logo_url = data["logo_url"],application_url = data["application_url"],reason_for_access = data["reason_for_access"],created_at = data["created_at"],scopes = data["scopes"])


class AccountSelectionCardinality:
    
    def __init__(self, account_selection_cardinality: str) :
        
        self.account_selection_cardinality = account_selection_cardinality
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class AccountFilter:
    
    def __init__(self, depository: AccountFilterSubtypes, credit: AccountFilterSubtypes, loan: AccountFilterSubtypes, investment: AccountFilterSubtypes) :
        
        self.depository = depository;self.credit = credit;self.loan = loan;self.investment = investment
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(depository = data["depository"],credit = data["credit"],loan = data["loan"],investment = data["investment"])


class AccountFilterSubtypes:
    
    def __init__(self, account_filter_subtypes: List[str]) :
        
        self.account_filter_subtypes = account_filter_subtypes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(str.from_json(d) for d in data)


class SandboxIncomeFireWebhookRequest:
    
    def __init__(self, item_id: str, user_id: UserId, webhook: str, verification_status: str) :
        
        self.item_id = item_id;self.user_id = user_id;self.webhook = webhook;self.verification_status = verification_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(item_id = data["item_id"],user_id = data["user_id"],webhook = data["webhook"],verification_status = data["verification_status"])


class SandboxIncomeFireWebhookResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class ItemApplicationListUserAuth:
    
    def __init__(self, user_id: Optional[str], fi_username_hash: Optional[str]) :
        
        self.user_id = user_id;self.fi_username_hash = fi_username_hash
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(user_id = data["user_id"],fi_username_hash = data["fi_username_hash"])


class SignalEvaluateRequest:
    
    def __init__(self, access_token: AccessToken, account_id: str, client_transaction_id: str, amount: float, user_present: Optional[bool], client_user_id: str, user: SignalUser, device: SignalDevice) :
        
        self.access_token = access_token;self.account_id = account_id;self.client_transaction_id = client_transaction_id;self.amount = amount;self.user_present = user_present;self.client_user_id = client_user_id;self.user = user;self.device = device
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],account_id = data["account_id"],client_transaction_id = data["client_transaction_id"],amount = data["amount"],user_present = data["user_present"],client_user_id = data["client_user_id"],user = data["user"],device = data["device"])


class SignalUser:
    
    def __init__(self, name: Optional[SignalPersonName], phone_number: Optional[str], email_address: Optional[str], address: Optional[SignalAddressData]) :
        
        self.name = name;self.phone_number = phone_number;self.email_address = email_address;self.address = address
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(name = data["name"],phone_number = data["phone_number"],email_address = data["email_address"],address = data["address"])


class SignalPersonName:
    
    def __init__(self, prefix: Optional[str], given_name: Optional[str], middle_name: Optional[str], family_name: Optional[str], suffix: Optional[str]) :
        
        self.prefix = prefix;self.given_name = given_name;self.middle_name = middle_name;self.family_name = family_name;self.suffix = suffix
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(prefix = data["prefix"],given_name = data["given_name"],middle_name = data["middle_name"],family_name = data["family_name"],suffix = data["suffix"])


class SignalAddressData:
    
    def __init__(self, city: str, region: Optional[str], street: str, postal_code: Optional[str], country: Optional[str]) :
        
        self.city = city;self.region = region;self.street = street;self.postal_code = postal_code;self.country = country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(city = data["city"],region = data["region"],street = data["street"],postal_code = data["postal_code"],country = data["country"])


class SignalDevice:
    
    def __init__(self, ip_address: Optional[str], user_agent: Optional[str]) :
        
        self.ip_address = ip_address;self.user_agent = user_agent
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(ip_address = data["ip_address"],user_agent = data["user_agent"])


class SignalEvaluateResponse:
    
    def __init__(self, request_id: RequestId, scores: SignalScores, core_attributes: SignalEvaluateCoreAttributes) :
        
        self.request_id = request_id;self.scores = scores;self.core_attributes = core_attributes
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"],scores = data["scores"],core_attributes = data["core_attributes"])


class SignalScores:
    
    def __init__(self, customer_initiated_return_risk: CustomerInitiatedReturnRisk, bank_initiated_return_risk: BankInitiatedReturnRisk) :
        
        self.customer_initiated_return_risk = customer_initiated_return_risk;self.bank_initiated_return_risk = bank_initiated_return_risk
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(customer_initiated_return_risk = data["customer_initiated_return_risk"],bank_initiated_return_risk = data["bank_initiated_return_risk"])


class SignalScore:
    
    def __init__(self, signal_score: int) :
        
        self.signal_score = signal_score
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CustomerInitiatedRiskTier:
    
    def __init__(self, customer_initiated_risk_tier: int) :
        
        self.customer_initiated_risk_tier = customer_initiated_risk_tier
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CustomerInitiatedReturnRisk:
    
    def __init__(self, score: SignalScore, risk_tier: CustomerInitiatedRiskTier) :
        
        self.score = score;self.risk_tier = risk_tier
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(score = data["score"],risk_tier = data["risk_tier"])


class BankInitiatedRiskTier:
    
    def __init__(self, bank_initiated_risk_tier: int) :
        
        self.bank_initiated_risk_tier = bank_initiated_risk_tier
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class BankInitiatedReturnRisk:
    
    def __init__(self, score: SignalScore, risk_tier: BankInitiatedRiskTier) :
        
        self.score = score;self.risk_tier = risk_tier
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(score = data["score"],risk_tier = data["risk_tier"])


class SignalEvaluateCoreAttributes:
    
    def __init__(self, unauthorized_transactions_count7_d: Optional[int], unauthorized_transactions_count30_d: Optional[int], unauthorized_transactions_count60_d: Optional[int], unauthorized_transactions_count90_d: Optional[int], nsf_overdraft_transactions_count7_d: Optional[int], nsf_overdraft_transactions_count30_d: Optional[int], nsf_overdraft_transactions_count60_d: Optional[int], nsf_overdraft_transactions_count90_d: Optional[int], days_since_first_plaid_connection: Optional[int], plaid_connections_count7_d: Optional[int], plaid_connections_count30_d: Optional[int], total_plaid_connections_count: Optional[int], is_savings_or_money_market_account: bool, total_credit_transactions_amount10_d: Optional[float], total_debit_transactions_amount10_d: Optional[float], p50_credit_transactions_amount28_d: Optional[float], p50_debit_transactions_amount28_d: Optional[float], p95_credit_transactions_amount28_d: Optional[float], p95_debit_transactions_amount28_d: Optional[float], days_with_negative_balance_count90_d: Optional[int], p90_eod_balance30_d: Optional[float], p90_eod_balance60_d: Optional[float], p90_eod_balance90_d: Optional[float], p10_eod_balance30_d: Optional[float], p10_eod_balance60_d: Optional[float], p10_eod_balance90_d: Optional[float], available_balance: Optional[float], current_balance: Optional[float], balance_last_updated: Optional[str], phone_change_count28_d: Optional[int], phone_change_count90_d: Optional[int], email_change_count28_d: Optional[int], email_change_count90_d: Optional[int], address_change_count28_d: Optional[int], address_change_count90_d: Optional[int], plaid_non_oauth_authentication_attempts_count3_d: Optional[int], plaid_non_oauth_authentication_attempts_count7_d: Optional[int], plaid_non_oauth_authentication_attempts_count30_d: Optional[int], failed_plaid_non_oauth_authentication_attempts_count3_d: Optional[int], failed_plaid_non_oauth_authentication_attempts_count7_d: Optional[int], failed_plaid_non_oauth_authentication_attempts_count30_d: Optional[int], debit_transactions_count10_d: Optional[int], credit_transactions_count10_d: Optional[int], debit_transactions_count30_d: Optional[int], credit_transactions_count30_d: Optional[int], debit_transactions_count60_d: Optional[int], credit_transactions_count60_d: Optional[int], debit_transactions_count90_d: Optional[int], credit_transactions_count90_d: Optional[int], total_debit_transactions_amount30_d: Optional[float], total_credit_transactions_amount30_d: Optional[float], total_debit_transactions_amount60_d: Optional[float], total_credit_transactions_amount60_d: Optional[float], total_debit_transactions_amount90_d: Optional[float], total_credit_transactions_amount90_d: Optional[float], p50_eod_balance30_d: Optional[float], p50_eod_balance60_d: Optional[float], p50_eod_balance90_d: Optional[float], p50_eod_balance31_d_to60_d: Optional[float], p50_eod_balance61_d_to90_d: Optional[float], p90_eod_balance31_d_to60_d: Optional[float], p90_eod_balance61_d_to90_d: Optional[float], p10_eod_balance31_d_to60_d: Optional[float], p10_eod_balance61_d_to90_d: Optional[float]) :
        
        self.unauthorized_transactions_count7_d = unauthorized_transactions_count7_d;self.unauthorized_transactions_count30_d = unauthorized_transactions_count30_d;self.unauthorized_transactions_count60_d = unauthorized_transactions_count60_d;self.unauthorized_transactions_count90_d = unauthorized_transactions_count90_d;self.nsf_overdraft_transactions_count7_d = nsf_overdraft_transactions_count7_d;self.nsf_overdraft_transactions_count30_d = nsf_overdraft_transactions_count30_d;self.nsf_overdraft_transactions_count60_d = nsf_overdraft_transactions_count60_d;self.nsf_overdraft_transactions_count90_d = nsf_overdraft_transactions_count90_d;self.days_since_first_plaid_connection = days_since_first_plaid_connection;self.plaid_connections_count7_d = plaid_connections_count7_d;self.plaid_connections_count30_d = plaid_connections_count30_d;self.total_plaid_connections_count = total_plaid_connections_count;self.is_savings_or_money_market_account = is_savings_or_money_market_account;self.total_credit_transactions_amount10_d = total_credit_transactions_amount10_d;self.total_debit_transactions_amount10_d = total_debit_transactions_amount10_d;self.p50_credit_transactions_amount28_d = p50_credit_transactions_amount28_d;self.p50_debit_transactions_amount28_d = p50_debit_transactions_amount28_d;self.p95_credit_transactions_amount28_d = p95_credit_transactions_amount28_d;self.p95_debit_transactions_amount28_d = p95_debit_transactions_amount28_d;self.days_with_negative_balance_count90_d = days_with_negative_balance_count90_d;self.p90_eod_balance30_d = p90_eod_balance30_d;self.p90_eod_balance60_d = p90_eod_balance60_d;self.p90_eod_balance90_d = p90_eod_balance90_d;self.p10_eod_balance30_d = p10_eod_balance30_d;self.p10_eod_balance60_d = p10_eod_balance60_d;self.p10_eod_balance90_d = p10_eod_balance90_d;self.available_balance = available_balance;self.current_balance = current_balance;self.balance_last_updated = balance_last_updated;self.phone_change_count28_d = phone_change_count28_d;self.phone_change_count90_d = phone_change_count90_d;self.email_change_count28_d = email_change_count28_d;self.email_change_count90_d = email_change_count90_d;self.address_change_count28_d = address_change_count28_d;self.address_change_count90_d = address_change_count90_d;self.plaid_non_oauth_authentication_attempts_count3_d = plaid_non_oauth_authentication_attempts_count3_d;self.plaid_non_oauth_authentication_attempts_count7_d = plaid_non_oauth_authentication_attempts_count7_d;self.plaid_non_oauth_authentication_attempts_count30_d = plaid_non_oauth_authentication_attempts_count30_d;self.failed_plaid_non_oauth_authentication_attempts_count3_d = failed_plaid_non_oauth_authentication_attempts_count3_d;self.failed_plaid_non_oauth_authentication_attempts_count7_d = failed_plaid_non_oauth_authentication_attempts_count7_d;self.failed_plaid_non_oauth_authentication_attempts_count30_d = failed_plaid_non_oauth_authentication_attempts_count30_d;self.debit_transactions_count10_d = debit_transactions_count10_d;self.credit_transactions_count10_d = credit_transactions_count10_d;self.debit_transactions_count30_d = debit_transactions_count30_d;self.credit_transactions_count30_d = credit_transactions_count30_d;self.debit_transactions_count60_d = debit_transactions_count60_d;self.credit_transactions_count60_d = credit_transactions_count60_d;self.debit_transactions_count90_d = debit_transactions_count90_d;self.credit_transactions_count90_d = credit_transactions_count90_d;self.total_debit_transactions_amount30_d = total_debit_transactions_amount30_d;self.total_credit_transactions_amount30_d = total_credit_transactions_amount30_d;self.total_debit_transactions_amount60_d = total_debit_transactions_amount60_d;self.total_credit_transactions_amount60_d = total_credit_transactions_amount60_d;self.total_debit_transactions_amount90_d = total_debit_transactions_amount90_d;self.total_credit_transactions_amount90_d = total_credit_transactions_amount90_d;self.p50_eod_balance30_d = p50_eod_balance30_d;self.p50_eod_balance60_d = p50_eod_balance60_d;self.p50_eod_balance90_d = p50_eod_balance90_d;self.p50_eod_balance31_d_to60_d = p50_eod_balance31_d_to60_d;self.p50_eod_balance61_d_to90_d = p50_eod_balance61_d_to90_d;self.p90_eod_balance31_d_to60_d = p90_eod_balance31_d_to60_d;self.p90_eod_balance61_d_to90_d = p90_eod_balance61_d_to90_d;self.p10_eod_balance31_d_to60_d = p10_eod_balance31_d_to60_d;self.p10_eod_balance61_d_to90_d = p10_eod_balance61_d_to90_d
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(unauthorized_transactions_count7_d = data["unauthorized_transactions_count7_d"],unauthorized_transactions_count30_d = data["unauthorized_transactions_count30_d"],unauthorized_transactions_count60_d = data["unauthorized_transactions_count60_d"],unauthorized_transactions_count90_d = data["unauthorized_transactions_count90_d"],nsf_overdraft_transactions_count7_d = data["nsf_overdraft_transactions_count7_d"],nsf_overdraft_transactions_count30_d = data["nsf_overdraft_transactions_count30_d"],nsf_overdraft_transactions_count60_d = data["nsf_overdraft_transactions_count60_d"],nsf_overdraft_transactions_count90_d = data["nsf_overdraft_transactions_count90_d"],days_since_first_plaid_connection = data["days_since_first_plaid_connection"],plaid_connections_count7_d = data["plaid_connections_count7_d"],plaid_connections_count30_d = data["plaid_connections_count30_d"],total_plaid_connections_count = data["total_plaid_connections_count"],is_savings_or_money_market_account = data["is_savings_or_money_market_account"],total_credit_transactions_amount10_d = data["total_credit_transactions_amount10_d"],total_debit_transactions_amount10_d = data["total_debit_transactions_amount10_d"],p50_credit_transactions_amount28_d = data["p50_credit_transactions_amount28_d"],p50_debit_transactions_amount28_d = data["p50_debit_transactions_amount28_d"],p95_credit_transactions_amount28_d = data["p95_credit_transactions_amount28_d"],p95_debit_transactions_amount28_d = data["p95_debit_transactions_amount28_d"],days_with_negative_balance_count90_d = data["days_with_negative_balance_count90_d"],p90_eod_balance30_d = data["p90_eod_balance30_d"],p90_eod_balance60_d = data["p90_eod_balance60_d"],p90_eod_balance90_d = data["p90_eod_balance90_d"],p10_eod_balance30_d = data["p10_eod_balance30_d"],p10_eod_balance60_d = data["p10_eod_balance60_d"],p10_eod_balance90_d = data["p10_eod_balance90_d"],available_balance = data["available_balance"],current_balance = data["current_balance"],balance_last_updated = data["balance_last_updated"],phone_change_count28_d = data["phone_change_count28_d"],phone_change_count90_d = data["phone_change_count90_d"],email_change_count28_d = data["email_change_count28_d"],email_change_count90_d = data["email_change_count90_d"],address_change_count28_d = data["address_change_count28_d"],address_change_count90_d = data["address_change_count90_d"],plaid_non_oauth_authentication_attempts_count3_d = data["plaid_non_oauth_authentication_attempts_count3_d"],plaid_non_oauth_authentication_attempts_count7_d = data["plaid_non_oauth_authentication_attempts_count7_d"],plaid_non_oauth_authentication_attempts_count30_d = data["plaid_non_oauth_authentication_attempts_count30_d"],failed_plaid_non_oauth_authentication_attempts_count3_d = data["failed_plaid_non_oauth_authentication_attempts_count3_d"],failed_plaid_non_oauth_authentication_attempts_count7_d = data["failed_plaid_non_oauth_authentication_attempts_count7_d"],failed_plaid_non_oauth_authentication_attempts_count30_d = data["failed_plaid_non_oauth_authentication_attempts_count30_d"],debit_transactions_count10_d = data["debit_transactions_count10_d"],credit_transactions_count10_d = data["credit_transactions_count10_d"],debit_transactions_count30_d = data["debit_transactions_count30_d"],credit_transactions_count30_d = data["credit_transactions_count30_d"],debit_transactions_count60_d = data["debit_transactions_count60_d"],credit_transactions_count60_d = data["credit_transactions_count60_d"],debit_transactions_count90_d = data["debit_transactions_count90_d"],credit_transactions_count90_d = data["credit_transactions_count90_d"],total_debit_transactions_amount30_d = data["total_debit_transactions_amount30_d"],total_credit_transactions_amount30_d = data["total_credit_transactions_amount30_d"],total_debit_transactions_amount60_d = data["total_debit_transactions_amount60_d"],total_credit_transactions_amount60_d = data["total_credit_transactions_amount60_d"],total_debit_transactions_amount90_d = data["total_debit_transactions_amount90_d"],total_credit_transactions_amount90_d = data["total_credit_transactions_amount90_d"],p50_eod_balance30_d = data["p50_eod_balance30_d"],p50_eod_balance60_d = data["p50_eod_balance60_d"],p50_eod_balance90_d = data["p50_eod_balance90_d"],p50_eod_balance31_d_to60_d = data["p50_eod_balance31_d_to60_d"],p50_eod_balance61_d_to90_d = data["p50_eod_balance61_d_to90_d"],p90_eod_balance31_d_to60_d = data["p90_eod_balance31_d_to60_d"],p90_eod_balance61_d_to90_d = data["p90_eod_balance61_d_to90_d"],p10_eod_balance31_d_to60_d = data["p10_eod_balance31_d_to60_d"],p10_eod_balance61_d_to90_d = data["p10_eod_balance61_d_to90_d"])


class SignalDecisionReportRequest:
    
    def __init__(self, client_transaction_id: str, initiated: bool, days_funds_on_hold: Optional[int]) :
        
        self.client_transaction_id = client_transaction_id;self.initiated = initiated;self.days_funds_on_hold = days_funds_on_hold
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(client_transaction_id = data["client_transaction_id"],initiated = data["initiated"],days_funds_on_hold = data["days_funds_on_hold"])


class SignalDecisionReportResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class SignalReturnReportRequest:
    
    def __init__(self, client_transaction_id: str, return_code: str) :
        
        self.client_transaction_id = client_transaction_id;self.return_code = return_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(client_transaction_id = data["client_transaction_id"],return_code = data["return_code"])


class SignalReturnReportResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class SignalPrepareRequest:
    
    def __init__(self, access_token: AccessToken) :
        
        self.access_token = access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"])


class SignalPrepareResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class SandboxOauthSelectAccountsRequest:
    
    def __init__(self, oauth_state_id: str, accounts: List[str]) :
        
        self.oauth_state_id = oauth_state_id;self.accounts = accounts
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(oauth_state_id = data["oauth_state_id"],accounts = data["accounts"])


class SandboxOauthSelectAccountsResponse:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class NewAccountsAvailableWebhook:
    
    def __init__(self, webhook_type: str, webhook_code: str, item_id: ItemId, error: Optional[PlaidError]) :
        
        self.webhook_type = webhook_type;self.webhook_code = webhook_code;self.item_id = item_id;self.error = error
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook_type = data["webhook_type"],webhook_code = data["webhook_code"],item_id = data["item_id"],error = data["error"])


class WalletCreateRequest:
    
    def __init__(self, iso_currency_code: WalletIsoCurrencyCode) :
        
        self.iso_currency_code = iso_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(iso_currency_code = data["iso_currency_code"])


class WalletCreateResponse:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class WalletGetRequest:
    
    def __init__(self, wallet_id: str) :
        
        self.wallet_id = wallet_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(wallet_id = data["wallet_id"])


class WalletGetResponse:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class WalletListRequest:
    
    def __init__(self, iso_currency_code: WalletIsoCurrencyCode, cursor: str, count: int) :
        
        self.iso_currency_code = iso_currency_code;self.cursor = cursor;self.count = count
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(iso_currency_code = data["iso_currency_code"],cursor = data["cursor"],count = data["count"])


class WalletListResponse:
    
    def __init__(self, wallets: List[Wallet], next_cursor: str, request_id: RequestId) :
        
        self.wallets = wallets;self.next_cursor = next_cursor;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(wallets = data["wallets"],next_cursor = data["next_cursor"],request_id = data["request_id"])


class Wallet:
    
    def __init__(self, wallet_id: str, balance: WalletBalance, numbers: WalletNumbers) :
        
        self.wallet_id = wallet_id;self.balance = balance;self.numbers = numbers
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(wallet_id = data["wallet_id"],balance = data["balance"],numbers = data["numbers"])


class WalletNumbers:
    
    def __init__(self, bacs: Optional[RecipientBacs], international: Optional[NumbersInternationalIban]) :
        
        self.bacs = bacs;self.international = international
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(bacs = data["bacs"],international = data["international"])


class WalletBalance:
    
    def __init__(self, iso_currency_code: str, current: float) :
        
        self.iso_currency_code = iso_currency_code;self.current = current
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(iso_currency_code = data["iso_currency_code"],current = data["current"])


class WalletIsoCurrencyCode:
    
    def __init__(self, wallet_iso_currency_code: str) :
        
        self.wallet_iso_currency_code = wallet_iso_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class WalletTransactionExecuteRequest:
    
    def __init__(self, idempotency_key: WalletTransactionIdempotencyKey, wallet_id: str, counterparty: WalletTransactionCounterparty, amount: WalletTransactionAmount, reference: str) :
        
        self.idempotency_key = idempotency_key;self.wallet_id = wallet_id;self.counterparty = counterparty;self.amount = amount;self.reference = reference
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(idempotency_key = data["idempotency_key"],wallet_id = data["wallet_id"],counterparty = data["counterparty"],amount = data["amount"],reference = data["reference"])


class WalletTransactionIdempotencyKey:
    
    def __init__(self, wallet_transaction_idempotency_key: str) :
        
        self.wallet_transaction_idempotency_key = wallet_transaction_idempotency_key
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class WalletTransactionCounterparty:
    
    def __init__(self, name: str, numbers: WalletTransactionCounterpartyNumbers) :
        
        self.name = name;self.numbers = numbers
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(name = data["name"],numbers = data["numbers"])


class WalletTransactionCounterpartyNumbers:
    
    def __init__(self, bacs: WalletTransactionCounterpartyBacs, international: Optional[WalletTransactionCounterpartyInternational]) :
        
        self.bacs = bacs;self.international = international
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(bacs = data["bacs"],international = data["international"])


class WalletTransactionCounterpartyBacs:
    
    def __init__(self, wallet_transaction_counterparty_bacs: Any) :
        
        self.wallet_transaction_counterparty_bacs = wallet_transaction_counterparty_bacs
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class WalletTransactionCounterpartyInternational:
    
    def __init__(self, iban: NumbersIban) :
        
        self.iban = iban
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(iban = data["iban"])


class WalletTransactionAmount:
    
    def __init__(self, iso_currency_code: WalletIsoCurrencyCode, value: float) :
        
        self.iso_currency_code = iso_currency_code;self.value = value
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(iso_currency_code = data["iso_currency_code"],value = data["value"])


class WalletTransactionExecuteResponse:
    
    def __init__(self, transaction_id: str, status: WalletTransactionStatus, request_id: RequestId) :
        
        self.transaction_id = transaction_id;self.status = status;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transaction_id = data["transaction_id"],status = data["status"],request_id = data["request_id"])


class WalletTransactionStatus:
    
    def __init__(self, wallet_transaction_status: str) :
        
        self.wallet_transaction_status = wallet_transaction_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class WalletTransactionGetRequest:
    
    def __init__(self, transaction_id: str) :
        
        self.transaction_id = transaction_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transaction_id = data["transaction_id"])


class WalletTransactionGetResponse:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class WalletTransactionsListRequest:
    
    def __init__(self, wallet_id: str, cursor: str, count: int) :
        
        self.wallet_id = wallet_id;self.cursor = cursor;self.count = count
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(wallet_id = data["wallet_id"],cursor = data["cursor"],count = data["count"])


class WalletTransactionsListResponse:
    
    def __init__(self, transactions: List[WalletTransaction], next_cursor: str, request_id: RequestId) :
        
        self.transactions = transactions;self.next_cursor = next_cursor;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transactions = data["transactions"],next_cursor = data["next_cursor"],request_id = data["request_id"])


class WalletTransaction:
    
    def __init__(self, transaction_id: str, reference: str, type_: str, amount: WalletTransactionAmount, counterparty: WalletTransactionCounterparty, status: WalletTransactionStatus, created_at: str) :
        
        self.transaction_id = transaction_id;self.reference = reference;self.type_ = type_;self.amount = amount;self.counterparty = counterparty;self.status = status;self.created_at = created_at
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(transaction_id = data["transaction_id"],reference = data["reference"],type_ = data["type_"],amount = data["amount"],counterparty = data["counterparty"],status = data["status"],created_at = data["created_at"])


class TransactionsEnhanceGetRequest:
    
    def __init__(self, account_type: str, transactions: List[ClientProvidedRawTransaction]) :
        
        self.account_type = account_type;self.transactions = transactions
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(account_type = data["account_type"],transactions = data["transactions"])


class ClientProvidedRawTransaction:
    
    def __init__(self, id: str, description: str, amount: float, iso_currency_code: str) :
        
        self.id = id;self.description = description;self.amount = amount;self.iso_currency_code = iso_currency_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],description = data["description"],amount = data["amount"],iso_currency_code = data["iso_currency_code"])


class TransactionsEnhanceGetResponse:
    
    def __init__(self, enhanced_transactions: List[ClientProvidedEnhancedTransaction]) :
        
        self.enhanced_transactions = enhanced_transactions
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(enhanced_transactions = data["enhanced_transactions"])


class ClientProvidedEnhancedTransaction:
    
    def __init__(self, id: str, description: str, amount: float, iso_currency_code: str, enhancements: Enhancements) :
        
        self.id = id;self.description = description;self.amount = amount;self.iso_currency_code = iso_currency_code;self.enhancements = enhancements
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],description = data["description"],amount = data["amount"],iso_currency_code = data["iso_currency_code"],enhancements = data["enhancements"])


class PaymentChannel:
    
    def __init__(self, payment_channel: str) :
        
        self.payment_channel = payment_channel
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Enhancements:
    
    def __init__(self, merchant_name: Optional[str], website: Optional[str], logo_url: Optional[str], check_number: Optional[str], payment_channel: PaymentChannel, category_id: Optional[str], category: List[str], location: Location, personal_finance_category: Optional[PersonalFinanceCategory], personal_finance_category_icon_url: str) :
        
        self.merchant_name = merchant_name;self.website = website;self.logo_url = logo_url;self.check_number = check_number;self.payment_channel = payment_channel;self.category_id = category_id;self.category = category;self.location = location;self.personal_finance_category = personal_finance_category;self.personal_finance_category_icon_url = personal_finance_category_icon_url
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(merchant_name = data["merchant_name"],website = data["website"],logo_url = data["logo_url"],check_number = data["check_number"],payment_channel = data["payment_channel"],category_id = data["category_id"],category = data["category"],location = data["location"],personal_finance_category = data["personal_finance_category"],personal_finance_category_icon_url = data["personal_finance_category_icon_url"])


class PaymentProfileCreateRequest:
    
    def __init__(self) :
        
        pass
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls()


class PaymentProfileCreateResponse:
    
    def __init__(self, payment_profile_id: PaymentProfileId, request_id: RequestId) :
        
        self.payment_profile_id = payment_profile_id;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(payment_profile_id = data["payment_profile_id"],request_id = data["request_id"])


class PaymentProfileId:
    
    def __init__(self, payment_profile_id: str) :
        
        self.payment_profile_id = payment_profile_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentProfileGetRequest:
    
    def __init__(self, payment_profile_id: PaymentProfileId) :
        
        self.payment_profile_id = payment_profile_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(payment_profile_id = data["payment_profile_id"])


class PaymentProfileGetResponse:
    
    def __init__(self, updated_at: str, created_at: str, status: PaymentProfileStatus, request_id: RequestId) :
        
        self.updated_at = updated_at;self.created_at = created_at;self.status = status;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(updated_at = data["updated_at"],created_at = data["created_at"],status = data["status"],request_id = data["request_id"])


class PaymentProfileStatus:
    
    def __init__(self, payment_profile_status: str) :
        
        self.payment_profile_status = payment_profile_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaymentProfileRemoveRequest:
    
    def __init__(self, payment_profile_id: PaymentProfileId) :
        
        self.payment_profile_id = payment_profile_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(payment_profile_id = data["payment_profile_id"])


class PaymentProfileRemoveResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class PartnerCustomersCreateRequest:
    
    def __init__(self, company_name: str, is_diligence_attested: bool, products: List[Products], create_link_customization: bool) :
        
        self.company_name = company_name;self.is_diligence_attested = is_diligence_attested;self.products = products;self.create_link_customization = create_link_customization
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(company_name = data["company_name"],is_diligence_attested = data["is_diligence_attested"],products = data["products"],create_link_customization = data["create_link_customization"])


class PartnerCustomersCreateResponse:
    
    def __init__(self, end_customer: PartnerEndCustomerClient, production_secret: str, request_id: RequestId) :
        
        self.end_customer = end_customer;self.production_secret = production_secret;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(end_customer = data["end_customer"],production_secret = data["production_secret"],request_id = data["request_id"])


class PartnerEndCustomerClient:
    
    def __init__(self, company_name: str) :
        
        self.company_name = company_name
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(company_name = data["company_name"])


class AddressPurposeLabel:
    
    def __init__(self, address_purpose_label: str) :
        
        self.address_purpose_label = address_purpose_label
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class City:
    
    def __init__(self, city: str) :
        
        self.city = city
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ClientUserId:
    
    def __init__(self, client_user_id: str) :
        
        self.client_user_id = client_user_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class CreateEntityScreeningRequest:
    
    def __init__(self, search_terms: EntityWatchlistSearchTerms, client_user_id: Optional[Any]) :
        
        self.search_terms = search_terms;self.client_user_id = client_user_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(search_terms = data["search_terms"],client_user_id = data["client_user_id"])


class CreateEntityWatchlistScreeningReviewRequest:
    
    def __init__(self, confirmed_hits: List[EntityWatchlistScreeningHitId], dismissed_hits: List[EntityWatchlistScreeningHitId], comment: Optional[ReviewComment], entity_watchlist_screening_id: EntityWatchlistScreeningId) :
        
        self.confirmed_hits = confirmed_hits;self.dismissed_hits = dismissed_hits;self.comment = comment;self.entity_watchlist_screening_id = entity_watchlist_screening_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(confirmed_hits = data["confirmed_hits"],dismissed_hits = data["dismissed_hits"],comment = data["comment"],entity_watchlist_screening_id = data["entity_watchlist_screening_id"])


class CreateIndividualWatchlistScreeningReviewRequest:
    
    def __init__(self, confirmed_hits: List[WatchlistScreeningHitId], dismissed_hits: List[WatchlistScreeningHitId], comment: Optional[ReviewComment], watchlist_screening_id: WatchlistScreeningIndividualId) :
        
        self.confirmed_hits = confirmed_hits;self.dismissed_hits = dismissed_hits;self.comment = comment;self.watchlist_screening_id = watchlist_screening_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(confirmed_hits = data["confirmed_hits"],dismissed_hits = data["dismissed_hits"],comment = data["comment"],watchlist_screening_id = data["watchlist_screening_id"])


class Cursor:
    
    def __init__(self, cursor: Optional[str]) :
        
        self.cursor = cursor
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class DashboardUser:
    
    def __init__(self, id: DashboardUserId, created_at: Timestamp, email_address: EmailAddress, status: DashboardUserStatus) :
        
        self.id = id;self.created_at = created_at;self.email_address = email_address;self.status = status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],created_at = data["created_at"],email_address = data["email_address"],status = data["status"])


class DashboardUserId:
    
    def __init__(self, dashboard_user_id: str) :
        
        self.dashboard_user_id = dashboard_user_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class DashboardUserResponse:
    
    def __init__(self, id: DashboardUserId, created_at: Timestamp, email_address: EmailAddress, status: DashboardUserStatus, request_id: RequestId) :
        
        self.id = id;self.created_at = created_at;self.email_address = email_address;self.status = status;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],created_at = data["created_at"],email_address = data["email_address"],status = data["status"],request_id = data["request_id"])


class DashboardUserStatus:
    
    def __init__(self, dashboard_user_status: str) :
        
        self.dashboard_user_status = dashboard_user_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Date:
    
    def __init__(self, date: str) :
        
        self.date = date
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class DateRange:
    
    def __init__(self, beginning: Date, ending: Date) :
        
        self.beginning = beginning;self.ending = ending
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(beginning = data["beginning"],ending = data["ending"])


class DocumentAnalysis:
    
    def __init__(self, authenticity: DocumentAuthenticityMatchCode, image_quality: ImageQuality, extracted_data: Optional[PhysicalDocumentExtractedDataAnalysis]) :
        
        self.authenticity = authenticity;self.image_quality = image_quality;self.extracted_data = extracted_data
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(authenticity = data["authenticity"],image_quality = data["image_quality"],extracted_data = data["extracted_data"])


class DocumentAuthenticityMatchCode:
    
    def __init__(self, document_authenticity_match_code: str) :
        
        self.document_authenticity_match_code = document_authenticity_match_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class DocumentDateOfBirthMatchCode:
    
    def __init__(self, document_date_of_birth_match_code: str) :
        
        self.document_date_of_birth_match_code = document_date_of_birth_match_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class DocumentImageBack:
    
    def __init__(self, document_image_back: Optional[str]) :
        
        self.document_image_back = document_image_back
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class DocumentImageCroppedBack:
    
    def __init__(self, document_image_cropped_back: Optional[str]) :
        
        self.document_image_cropped_back = document_image_cropped_back
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class DocumentImageCroppedFront:
    
    def __init__(self, document_image_cropped_front: Optional[str]) :
        
        self.document_image_cropped_front = document_image_cropped_front
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class DocumentImageFace:
    
    def __init__(self, document_image_face: Optional[str]) :
        
        self.document_image_face = document_image_face
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class DocumentImageFront:
    
    def __init__(self, document_image_front: str) :
        
        self.document_image_front = document_image_front
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class DocumentNameMatchCode:
    
    def __init__(self, document_name_match_code: str) :
        
        self.document_name_match_code = document_name_match_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class DocumentStatus:
    
    def __init__(self, document_status: str) :
        
        self.document_status = document_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class DocumentaryVerification:
    
    def __init__(self, status: str, documents: List[DocumentaryVerificationDocument]) :
        
        self.status = status;self.documents = documents
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(status = data["status"],documents = data["documents"])


class DocumentaryVerificationDocument:
    
    def __init__(self, status: DocumentStatus, attempt: float, images: PhysicalDocumentImages, extracted_data: Optional[PhysicalDocumentExtractedData], analysis: DocumentAnalysis) :
        
        self.status = status;self.attempt = attempt;self.images = images;self.extracted_data = extracted_data;self.analysis = analysis
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(status = data["status"],attempt = data["attempt"],images = data["images"],extracted_data = data["extracted_data"],analysis = data["analysis"])


class EmailAddress:
    
    def __init__(self, email_address: str) :
        
        self.email_address = email_address
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class EntityDocument:
    
    def __init__(self, type_: EntityDocumentType, number: WatchlistScreeningDocumentValue) :
        
        self.type_ = type_;self.number = number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(type_ = data["type_"],number = data["number"])


class EntityDocumentType:
    
    def __init__(self, entity_document_type: str) :
        
        self.entity_document_type = entity_document_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class EntityScreeningHitAnalysis:
    
    def __init__(self, documents: MatchSummaryCode, email_addresses: MatchSummaryCode, locations: MatchSummaryCode, names: MatchSummaryCode, phone_numbers: MatchSummaryCode, urls: MatchSummaryCode, search_terms_version: float) :
        
        self.documents = documents;self.email_addresses = email_addresses;self.locations = locations;self.names = names;self.phone_numbers = phone_numbers;self.urls = urls;self.search_terms_version = search_terms_version
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(documents = data["documents"],email_addresses = data["email_addresses"],locations = data["locations"],names = data["names"],phone_numbers = data["phone_numbers"],urls = data["urls"],search_terms_version = data["search_terms_version"])


class EntityScreeningHitData:
    
    def __init__(self, documents: List[EntityScreeningHitDocumentsItems], email_addresses: List[EntityScreeningHitEmailsItems], locations: List[GenericScreeningHitLocationItems], names: List[EntityScreeningHitNamesItems], phone_numbers: List[EntityScreeningHitsPhoneNumberItems], urls: List[EntityScreeningHitUrlsItems]) :
        
        self.documents = documents;self.email_addresses = email_addresses;self.locations = locations;self.names = names;self.phone_numbers = phone_numbers;self.urls = urls
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(documents = data["documents"],email_addresses = data["email_addresses"],locations = data["locations"],names = data["names"],phone_numbers = data["phone_numbers"],urls = data["urls"])


class EntityScreeningHitDocumentsItems:
    
    def __init__(self, analysis: MatchSummary, data: EntityDocument) :
        
        self.analysis = analysis;self.data = data
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(analysis = data["analysis"],data = data["data"])


class EntityScreeningHitEmails:
    
    def __init__(self, email_address: EmailAddress) :
        
        self.email_address = email_address
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(email_address = data["email_address"])


class EntityScreeningHitEmailsItems:
    
    def __init__(self, analysis: MatchSummary, data: EntityScreeningHitEmails) :
        
        self.analysis = analysis;self.data = data
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(analysis = data["analysis"],data = data["data"])


class EntityScreeningHitNames:
    
    def __init__(self, full: str, is_primary: bool, weak_alias_determination: WeakAliasDetermination) :
        
        self.full = full;self.is_primary = is_primary;self.weak_alias_determination = weak_alias_determination
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(full = data["full"],is_primary = data["is_primary"],weak_alias_determination = data["weak_alias_determination"])


class EntityScreeningHitNamesItems:
    
    def __init__(self, analysis: MatchSummary, data: EntityScreeningHitNames) :
        
        self.analysis = analysis;self.data = data
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(analysis = data["analysis"],data = data["data"])


class EntityScreeningHitPhoneNumbers:
    
    def __init__(self, type_: PhoneType, phone_number: WatchlistScreeningPhoneNumber) :
        
        self.type_ = type_;self.phone_number = phone_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(type_ = data["type_"],phone_number = data["phone_number"])


class EntityScreeningHitUrls:
    
    def __init__(self, url: Url) :
        
        self.url = url
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(url = data["url"])


class EntityScreeningHitUrlsItems:
    
    def __init__(self, analysis: MatchSummary, data: EntityScreeningHitUrls) :
        
        self.analysis = analysis;self.data = data
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(analysis = data["analysis"],data = data["data"])


class EntityScreeningHitsPhoneNumberItems:
    
    def __init__(self, analysis: MatchSummary, data: EntityScreeningHitPhoneNumbers) :
        
        self.analysis = analysis;self.data = data
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(analysis = data["analysis"],data = data["data"])


class EntityWatchlistCode:
    
    def __init__(self, entity_watchlist_code: str) :
        
        self.entity_watchlist_code = entity_watchlist_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class EntityWatchlistProgram:
    
    def __init__(self, id: EntityWatchlistProgramId, created_at: Timestamp, is_rescanning_enabled: bool, lists_enabled: List[EntityWatchlistCode], name: EntityWatchlistScreeningProgramName, name_sensitivity: ProgramNameSensitivity, audit_trail: WatchlistScreeningAuditTrail, is_archived: ProgramArchived) :
        
        self.id = id;self.created_at = created_at;self.is_rescanning_enabled = is_rescanning_enabled;self.lists_enabled = lists_enabled;self.name = name;self.name_sensitivity = name_sensitivity;self.audit_trail = audit_trail;self.is_archived = is_archived
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],created_at = data["created_at"],is_rescanning_enabled = data["is_rescanning_enabled"],lists_enabled = data["lists_enabled"],name = data["name"],name_sensitivity = data["name_sensitivity"],audit_trail = data["audit_trail"],is_archived = data["is_archived"])


class EntityWatchlistProgramId:
    
    def __init__(self, entity_watchlist_program_id: str) :
        
        self.entity_watchlist_program_id = entity_watchlist_program_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class EntityWatchlistProgramResponse:
    
    def __init__(self, id: EntityWatchlistProgramId, created_at: Timestamp, is_rescanning_enabled: bool, lists_enabled: List[EntityWatchlistCode], name: EntityWatchlistScreeningProgramName, name_sensitivity: ProgramNameSensitivity, audit_trail: WatchlistScreeningAuditTrail, is_archived: ProgramArchived, request_id: RequestId) :
        
        self.id = id;self.created_at = created_at;self.is_rescanning_enabled = is_rescanning_enabled;self.lists_enabled = lists_enabled;self.name = name;self.name_sensitivity = name_sensitivity;self.audit_trail = audit_trail;self.is_archived = is_archived;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],created_at = data["created_at"],is_rescanning_enabled = data["is_rescanning_enabled"],lists_enabled = data["lists_enabled"],name = data["name"],name_sensitivity = data["name_sensitivity"],audit_trail = data["audit_trail"],is_archived = data["is_archived"],request_id = data["request_id"])


class EntityWatchlistScreening:
    
    def __init__(self, id: EntityWatchlistScreeningId, search_terms: EntityWatchlistScreeningSearchTerms, assignee: Optional[Any], status: WatchlistScreeningStatus, client_user_id: Optional[Any], audit_trail: WatchlistScreeningAuditTrail) :
        
        self.id = id;self.search_terms = search_terms;self.assignee = assignee;self.status = status;self.client_user_id = client_user_id;self.audit_trail = audit_trail
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],search_terms = data["search_terms"],assignee = data["assignee"],status = data["status"],client_user_id = data["client_user_id"],audit_trail = data["audit_trail"])


class EntityWatchlistScreeningHit:
    
    def __init__(self, id: EntityWatchlistScreeningHitId, review_status: WatchlistScreeningHitStatus, first_active: Timestamp, inactive_since: Optional[TimestampNullable], historical_since: Optional[TimestampNullable], list_code: EntityWatchlistCode, plaid_uid: InternalUid, source_uid: Optional[SourceUid], analysis: EntityScreeningHitAnalysis, data: EntityScreeningHitData) :
        
        self.id = id;self.review_status = review_status;self.first_active = first_active;self.inactive_since = inactive_since;self.historical_since = historical_since;self.list_code = list_code;self.plaid_uid = plaid_uid;self.source_uid = source_uid;self.analysis = analysis;self.data = data
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],review_status = data["review_status"],first_active = data["first_active"],inactive_since = data["inactive_since"],historical_since = data["historical_since"],list_code = data["list_code"],plaid_uid = data["plaid_uid"],source_uid = data["source_uid"],analysis = data["analysis"],data = data["data"])


class EntityWatchlistScreeningHitId:
    
    def __init__(self, entity_watchlist_screening_hit_id: str) :
        
        self.entity_watchlist_screening_hit_id = entity_watchlist_screening_hit_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class EntityWatchlistScreeningId:
    
    def __init__(self, entity_watchlist_screening_id: str) :
        
        self.entity_watchlist_screening_id = entity_watchlist_screening_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class EntityWatchlistScreeningName:
    
    def __init__(self, entity_watchlist_screening_name: str) :
        
        self.entity_watchlist_screening_name = entity_watchlist_screening_name
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class EntityWatchlistScreeningProgramName:
    
    def __init__(self, entity_watchlist_screening_program_name: str) :
        
        self.entity_watchlist_screening_program_name = entity_watchlist_screening_program_name
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class EntityWatchlistScreeningResponse:
    
    def __init__(self, id: EntityWatchlistScreeningId, search_terms: EntityWatchlistScreeningSearchTerms, assignee: Optional[Any], status: WatchlistScreeningStatus, client_user_id: Optional[Any], audit_trail: WatchlistScreeningAuditTrail, request_id: RequestId) :
        
        self.id = id;self.search_terms = search_terms;self.assignee = assignee;self.status = status;self.client_user_id = client_user_id;self.audit_trail = audit_trail;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],search_terms = data["search_terms"],assignee = data["assignee"],status = data["status"],client_user_id = data["client_user_id"],audit_trail = data["audit_trail"],request_id = data["request_id"])


class EntityWatchlistScreeningReview:
    
    def __init__(self, id: EntityWatchlistScreeningReviewId, confirmed_hits: List[EntityWatchlistScreeningHitId], dismissed_hits: List[EntityWatchlistScreeningHitId], comment: Optional[ReviewComment], audit_trail: WatchlistScreeningAuditTrail) :
        
        self.id = id;self.confirmed_hits = confirmed_hits;self.dismissed_hits = dismissed_hits;self.comment = comment;self.audit_trail = audit_trail
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],confirmed_hits = data["confirmed_hits"],dismissed_hits = data["dismissed_hits"],comment = data["comment"],audit_trail = data["audit_trail"])


class EntityWatchlistScreeningReviewId:
    
    def __init__(self, entity_watchlist_screening_review_id: str) :
        
        self.entity_watchlist_screening_review_id = entity_watchlist_screening_review_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class EntityWatchlistScreeningReviewResponse:
    
    def __init__(self, id: EntityWatchlistScreeningReviewId, confirmed_hits: List[EntityWatchlistScreeningHitId], dismissed_hits: List[EntityWatchlistScreeningHitId], comment: Optional[ReviewComment], audit_trail: WatchlistScreeningAuditTrail, request_id: RequestId) :
        
        self.id = id;self.confirmed_hits = confirmed_hits;self.dismissed_hits = dismissed_hits;self.comment = comment;self.audit_trail = audit_trail;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],confirmed_hits = data["confirmed_hits"],dismissed_hits = data["dismissed_hits"],comment = data["comment"],audit_trail = data["audit_trail"],request_id = data["request_id"])


class EntityWatchlistScreeningSearchTerms:
    
    def __init__(self, entity_watchlist_program_id: EntityWatchlistProgramId, legal_name: EntityWatchlistScreeningName, document_number: Optional[Any], email_address: Optional[Any], country: Optional[Any], phone_number: Optional[Any], url: Optional[Any], version: float) :
        
        self.entity_watchlist_program_id = entity_watchlist_program_id;self.legal_name = legal_name;self.document_number = document_number;self.email_address = email_address;self.country = country;self.phone_number = phone_number;self.url = url;self.version = version
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(entity_watchlist_program_id = data["entity_watchlist_program_id"],legal_name = data["legal_name"],document_number = data["document_number"],email_address = data["email_address"],country = data["country"],phone_number = data["phone_number"],url = data["url"],version = data["version"])


class EntityWatchlistSearchTerms:
    
    def __init__(self, entity_watchlist_program_id: EntityWatchlistProgramId, legal_name: EntityWatchlistScreeningName, document_number: Optional[Any], email_address: Optional[Any], country: Optional[Any], phone_number: Optional[Any], url: Optional[Any]) :
        
        self.entity_watchlist_program_id = entity_watchlist_program_id;self.legal_name = legal_name;self.document_number = document_number;self.email_address = email_address;self.country = country;self.phone_number = phone_number;self.url = url
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(entity_watchlist_program_id = data["entity_watchlist_program_id"],legal_name = data["legal_name"],document_number = data["document_number"],email_address = data["email_address"],country = data["country"],phone_number = data["phone_number"],url = data["url"])


class ExpirationDate:
    
    def __init__(self, expiration_date: str) :
        
        self.expiration_date = expiration_date
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class FamilyNameField:
    
    def __init__(self, family_name_field: str) :
        
        self.family_name_field = family_name_field
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class GenericCountryCode:
    
    def __init__(self, generic_country_code: str) :
        
        self.generic_country_code = generic_country_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class GenericScreeningHitLocationItems:
    
    def __init__(self, analysis: MatchSummary, data: WatchlistScreeningHitLocations) :
        
        self.analysis = analysis;self.data = data
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(analysis = data["analysis"],data = data["data"])


class GetDashboardUserRequest:
    
    def __init__(self, dashboard_user_id: DashboardUserId) :
        
        self.dashboard_user_id = dashboard_user_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(dashboard_user_id = data["dashboard_user_id"])


class GetEntityWatchlistScreeningRequest:
    
    def __init__(self, entity_watchlist_screening_id: EntityWatchlistScreeningId) :
        
        self.entity_watchlist_screening_id = entity_watchlist_screening_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(entity_watchlist_screening_id = data["entity_watchlist_screening_id"])


class GetIdentityVerificationRequest:
    
    def __init__(self, identity_verification_id: IdentityVerificationId) :
        
        self.identity_verification_id = identity_verification_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(identity_verification_id = data["identity_verification_id"])


class GetIndividualWatchlistScreeningRequest:
    
    def __init__(self, watchlist_screening_id: WatchlistScreeningIndividualId) :
        
        self.watchlist_screening_id = watchlist_screening_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(watchlist_screening_id = data["watchlist_screening_id"])


class GetWatchlistScreeningEntityProgramRequest:
    
    def __init__(self, entity_watchlist_program_id: EntityWatchlistProgramId) :
        
        self.entity_watchlist_program_id = entity_watchlist_program_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(entity_watchlist_program_id = data["entity_watchlist_program_id"])


class GetWatchlistScreeningIndividualProgramRequest:
    
    def __init__(self, watchlist_program_id: WatchlistProgramId) :
        
        self.watchlist_program_id = watchlist_program_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(watchlist_program_id = data["watchlist_program_id"])


class GivenNameField:
    
    def __init__(self, given_name_field: str) :
        
        self.given_name_field = given_name_field
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IdNumberType:
    
    def __init__(self, id_number_type: str) :
        
        self.id_number_type = id_number_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IdNumberValue:
    
    def __init__(self, id_number_value: str) :
        
        self.id_number_value = id_number_value
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IpAddress:
    
    def __init__(self, ip_address: Optional[str]) :
        
        self.ip_address = ip_address
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Iso8601Date:
    
    def __init__(self, iso8601_date: Optional[str]) :
        
        self.iso8601_date = iso8601_date
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IdempotencyFlag:
    
    def __init__(self, idempotency_flag: Optional[bool]) :
        
        self.idempotency_flag = idempotency_flag
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IdentityVerification:
    
    def __init__(self, id: IdentityVerificationId, client_user_id: ClientUserId, created_at: Timestamp, completed_at: Optional[TimestampNullable], previous_attempt_id: Optional[PreviousIdentityVerificationAttemptId], shareable_url: Optional[ShareableUrl], template: IdentityVerificationTemplateReference, user: IdentityVerificationUserData, status: IdentityVerificationStatus, steps: IdentityVerificationStepSummary, documentary_verification: Optional[DocumentaryVerification], kyc_check: Optional[KycCheckDetails], watchlist_screening_id: Optional[Any]) :
        
        self.id = id;self.client_user_id = client_user_id;self.created_at = created_at;self.completed_at = completed_at;self.previous_attempt_id = previous_attempt_id;self.shareable_url = shareable_url;self.template = template;self.user = user;self.status = status;self.steps = steps;self.documentary_verification = documentary_verification;self.kyc_check = kyc_check;self.watchlist_screening_id = watchlist_screening_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],client_user_id = data["client_user_id"],created_at = data["created_at"],completed_at = data["completed_at"],previous_attempt_id = data["previous_attempt_id"],shareable_url = data["shareable_url"],template = data["template"],user = data["user"],status = data["status"],steps = data["steps"],documentary_verification = data["documentary_verification"],kyc_check = data["kyc_check"],watchlist_screening_id = data["watchlist_screening_id"])


class IdentityVerificationConsent:
    
    def __init__(self, identity_verification_consent: bool) :
        
        self.identity_verification_consent = identity_verification_consent
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IdentityVerificationCreateRequest:
    
    def __init__(self, is_shareable: bool, template_id: IdentityVerificationTemplateId, gave_consent: IdentityVerificationConsent, user: IdentityVerificationRequestUser, is_idempotent: Optional[IdempotencyFlag]) :
        
        self.is_shareable = is_shareable;self.template_id = template_id;self.gave_consent = gave_consent;self.user = user;self.is_idempotent = is_idempotent
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(is_shareable = data["is_shareable"],template_id = data["template_id"],gave_consent = data["gave_consent"],user = data["user"],is_idempotent = data["is_idempotent"])


class IdentityVerificationId:
    
    def __init__(self, identity_verification_id: str) :
        
        self.identity_verification_id = identity_verification_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IdentityVerificationRequestUser:
    
    def __init__(self, client_user_id: ClientUserId, email_address: Optional[Any], phone_number: Optional[IdentityVerificationUserPhoneNumber], date_of_birth: Optional[Iso8601Date], name: Optional[UserName], address: Optional[UserAddress], id_number: Optional[UserIdNumber]) :
        
        self.client_user_id = client_user_id;self.email_address = email_address;self.phone_number = phone_number;self.date_of_birth = date_of_birth;self.name = name;self.address = address;self.id_number = id_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(client_user_id = data["client_user_id"],email_address = data["email_address"],phone_number = data["phone_number"],date_of_birth = data["date_of_birth"],name = data["name"],address = data["address"],id_number = data["id_number"])


class IdentityVerificationResponse:
    
    def __init__(self, id: IdentityVerificationId, client_user_id: ClientUserId, created_at: Timestamp, completed_at: Optional[TimestampNullable], previous_attempt_id: Optional[PreviousIdentityVerificationAttemptId], shareable_url: Optional[ShareableUrl], template: IdentityVerificationTemplateReference, user: IdentityVerificationUserData, status: IdentityVerificationStatus, steps: IdentityVerificationStepSummary, documentary_verification: Optional[DocumentaryVerification], kyc_check: Optional[KycCheckDetails], watchlist_screening_id: Optional[Any], request_id: RequestId) :
        
        self.id = id;self.client_user_id = client_user_id;self.created_at = created_at;self.completed_at = completed_at;self.previous_attempt_id = previous_attempt_id;self.shareable_url = shareable_url;self.template = template;self.user = user;self.status = status;self.steps = steps;self.documentary_verification = documentary_verification;self.kyc_check = kyc_check;self.watchlist_screening_id = watchlist_screening_id;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],client_user_id = data["client_user_id"],created_at = data["created_at"],completed_at = data["completed_at"],previous_attempt_id = data["previous_attempt_id"],shareable_url = data["shareable_url"],template = data["template"],user = data["user"],status = data["status"],steps = data["steps"],documentary_verification = data["documentary_verification"],kyc_check = data["kyc_check"],watchlist_screening_id = data["watchlist_screening_id"],request_id = data["request_id"])


class IdentityVerificationRetryRequest:
    
    def __init__(self, client_user_id: ClientUserId, template_id: IdentityVerificationTemplateId, strategy: Strategy, steps: Optional[IdentityVerificationRetryRequestStepsObject]) :
        
        self.client_user_id = client_user_id;self.template_id = template_id;self.strategy = strategy;self.steps = steps
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(client_user_id = data["client_user_id"],template_id = data["template_id"],strategy = data["strategy"],steps = data["steps"])


class IdentityVerificationRetryRequestStepsObject:
    
    def __init__(self, verify_sms: bool, kyc_check: bool, documentary_verification: bool, selfie_check: bool) :
        
        self.verify_sms = verify_sms;self.kyc_check = kyc_check;self.documentary_verification = documentary_verification;self.selfie_check = selfie_check
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(verify_sms = data["verify_sms"],kyc_check = data["kyc_check"],documentary_verification = data["documentary_verification"],selfie_check = data["selfie_check"])


class IdentityVerificationStatus:
    
    def __init__(self, identity_verification_status: str) :
        
        self.identity_verification_status = identity_verification_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IdentityVerificationStepStatus:
    
    def __init__(self, identity_verification_step_status: str) :
        
        self.identity_verification_step_status = identity_verification_step_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IdentityVerificationStepSummary:
    
    def __init__(self, accept_tos: IdentityVerificationStepStatus, verify_sms: IdentityVerificationStepStatus, kyc_check: IdentityVerificationStepStatus, documentary_verification: IdentityVerificationStepStatus, selfie_check: IdentityVerificationStepStatus, watchlist_screening: IdentityVerificationStepStatus, risk_check: IdentityVerificationStepStatus) :
        
        self.accept_tos = accept_tos;self.verify_sms = verify_sms;self.kyc_check = kyc_check;self.documentary_verification = documentary_verification;self.selfie_check = selfie_check;self.watchlist_screening = watchlist_screening;self.risk_check = risk_check
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(accept_tos = data["accept_tos"],verify_sms = data["verify_sms"],kyc_check = data["kyc_check"],documentary_verification = data["documentary_verification"],selfie_check = data["selfie_check"],watchlist_screening = data["watchlist_screening"],risk_check = data["risk_check"])


class IdentityVerificationTemplateId:
    
    def __init__(self, identity_verification_template_id: str) :
        
        self.identity_verification_template_id = identity_verification_template_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IdentityVerificationTemplateReference:
    
    def __init__(self, id: IdentityVerificationTemplateId, version: IdentityVerificationTemplateVersion) :
        
        self.id = id;self.version = version
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],version = data["version"])


class IdentityVerificationTemplateVersion:
    
    def __init__(self, identity_verification_template_version: float) :
        
        self.identity_verification_template_version = identity_verification_template_version
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IdentityVerificationUserAddress:
    
    def __init__(self, street: Optional[Any], street2: Optional[Street2], city: Optional[Any], region: Optional[Any], postal_code: Optional[Any], country: GenericCountryCode) :
        
        self.street = street;self.street2 = street2;self.city = city;self.region = region;self.postal_code = postal_code;self.country = country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(street = data["street"],street2 = data["street2"],city = data["city"],region = data["region"],postal_code = data["postal_code"],country = data["country"])


class IdentityVerificationUserData:
    
    def __init__(self, phone_number: Optional[IdentityVerificationUserPhoneNumber], date_of_birth: Optional[Iso8601Date], ip_address: Optional[IpAddress], email_address: Optional[Any], name: Optional[UserName], address: Optional[IdentityVerificationUserAddress], id_number: Optional[UserIdNumber]) :
        
        self.phone_number = phone_number;self.date_of_birth = date_of_birth;self.ip_address = ip_address;self.email_address = email_address;self.name = name;self.address = address;self.id_number = id_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(phone_number = data["phone_number"],date_of_birth = data["date_of_birth"],ip_address = data["ip_address"],email_address = data["email_address"],name = data["name"],address = data["address"],id_number = data["id_number"])


class IdentityVerificationUserPhoneNumber:
    
    def __init__(self, identity_verification_user_phone_number: Optional[str]) :
        
        self.identity_verification_user_phone_number = identity_verification_user_phone_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ImageQuality:
    
    def __init__(self, image_quality: str) :
        
        self.image_quality = image_quality
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IndividualScreeningHitNames:
    
    def __init__(self, full: str, is_primary: bool, weak_alias_determination: WeakAliasDetermination) :
        
        self.full = full;self.is_primary = is_primary;self.weak_alias_determination = weak_alias_determination
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(full = data["full"],is_primary = data["is_primary"],weak_alias_determination = data["weak_alias_determination"])


class IndividualWatchlistCode:
    
    def __init__(self, individual_watchlist_code: str) :
        
        self.individual_watchlist_code = individual_watchlist_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IndividualWatchlistProgram:
    
    def __init__(self, id: WatchlistProgramId, created_at: Timestamp, is_rescanning_enabled: bool, lists_enabled: List[IndividualWatchlistCode], name: IndividualWatchlistScreeningProgramName, name_sensitivity: ProgramNameSensitivity, audit_trail: WatchlistScreeningAuditTrail, is_archived: ProgramArchived) :
        
        self.id = id;self.created_at = created_at;self.is_rescanning_enabled = is_rescanning_enabled;self.lists_enabled = lists_enabled;self.name = name;self.name_sensitivity = name_sensitivity;self.audit_trail = audit_trail;self.is_archived = is_archived
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],created_at = data["created_at"],is_rescanning_enabled = data["is_rescanning_enabled"],lists_enabled = data["lists_enabled"],name = data["name"],name_sensitivity = data["name_sensitivity"],audit_trail = data["audit_trail"],is_archived = data["is_archived"])


class IndividualWatchlistProgramResponse:
    
    def __init__(self, id: WatchlistProgramId, created_at: Timestamp, is_rescanning_enabled: bool, lists_enabled: List[IndividualWatchlistCode], name: IndividualWatchlistScreeningProgramName, name_sensitivity: ProgramNameSensitivity, audit_trail: WatchlistScreeningAuditTrail, is_archived: ProgramArchived, request_id: RequestId) :
        
        self.id = id;self.created_at = created_at;self.is_rescanning_enabled = is_rescanning_enabled;self.lists_enabled = lists_enabled;self.name = name;self.name_sensitivity = name_sensitivity;self.audit_trail = audit_trail;self.is_archived = is_archived;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],created_at = data["created_at"],is_rescanning_enabled = data["is_rescanning_enabled"],lists_enabled = data["lists_enabled"],name = data["name"],name_sensitivity = data["name_sensitivity"],audit_trail = data["audit_trail"],is_archived = data["is_archived"],request_id = data["request_id"])


class IndividualWatchlistScreeningProgramName:
    
    def __init__(self, individual_watchlist_screening_program_name: str) :
        
        self.individual_watchlist_screening_program_name = individual_watchlist_screening_program_name
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class InternalUid:
    
    def __init__(self, internal_uid: str) :
        
        self.internal_uid = internal_uid
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class IssuingCountry:
    
    def __init__(self, issuing_country: str) :
        
        self.issuing_country = issuing_country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class KycCheckAddressSummary:
    
    def __init__(self, summary: MatchSummaryCode, po_box: PoBoxStatus, type_: AddressPurposeLabel) :
        
        self.summary = summary;self.po_box = po_box;self.type_ = type_
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(summary = data["summary"],po_box = data["po_box"],type_ = data["type_"])


class KycCheckDateOfBirthSummary:
    
    def __init__(self, summary: MatchSummaryCode) :
        
        self.summary = summary
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(summary = data["summary"])


class KycCheckDetails:
    
    def __init__(self, status: str, address: KycCheckAddressSummary, name: KycCheckNameSummary, date_of_birth: KycCheckDateOfBirthSummary, id_number: KycCheckIdNumberSummary, phone_number: KycCheckPhoneSummary) :
        
        self.status = status;self.address = address;self.name = name;self.date_of_birth = date_of_birth;self.id_number = id_number;self.phone_number = phone_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(status = data["status"],address = data["address"],name = data["name"],date_of_birth = data["date_of_birth"],id_number = data["id_number"],phone_number = data["phone_number"])


class KycCheckIdNumberSummary:
    
    def __init__(self, summary: MatchSummaryCode) :
        
        self.summary = summary
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(summary = data["summary"])


class KycCheckNameSummary:
    
    def __init__(self, summary: MatchSummaryCode) :
        
        self.summary = summary
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(summary = data["summary"])


class KycCheckPhoneSummary:
    
    def __init__(self, summary: MatchSummaryCode) :
        
        self.summary = summary
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(summary = data["summary"])


class ListDashboardUserRequest:
    
    def __init__(self, cursor: Optional[Cursor]) :
        
        self.cursor = cursor
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(cursor = data["cursor"])


class ListEntityWatchlistScreeningRequest:
    
    def __init__(self, entity_watchlist_program_id: EntityWatchlistProgramId, client_user_id: Optional[Any], status: Optional[Any], assignee: Optional[Any], cursor: Optional[Cursor]) :
        
        self.entity_watchlist_program_id = entity_watchlist_program_id;self.client_user_id = client_user_id;self.status = status;self.assignee = assignee;self.cursor = cursor
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(entity_watchlist_program_id = data["entity_watchlist_program_id"],client_user_id = data["client_user_id"],status = data["status"],assignee = data["assignee"],cursor = data["cursor"])


class ListIdentityVerificationRequest:
    
    def __init__(self, template_id: IdentityVerificationTemplateId, client_user_id: ClientUserId, cursor: Optional[Cursor]) :
        
        self.template_id = template_id;self.client_user_id = client_user_id;self.cursor = cursor
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(template_id = data["template_id"],client_user_id = data["client_user_id"],cursor = data["cursor"])


class ListIndividualWatchlistScreeningRequest:
    
    def __init__(self, watchlist_program_id: WatchlistProgramId, client_user_id: Optional[Any], status: Optional[Any], assignee: Optional[Any], cursor: Optional[Cursor]) :
        
        self.watchlist_program_id = watchlist_program_id;self.client_user_id = client_user_id;self.status = status;self.assignee = assignee;self.cursor = cursor
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(watchlist_program_id = data["watchlist_program_id"],client_user_id = data["client_user_id"],status = data["status"],assignee = data["assignee"],cursor = data["cursor"])


class ListWatchlistScreeningEntityHistoryRequest:
    
    def __init__(self, entity_watchlist_screening_id: EntityWatchlistScreeningId, cursor: Optional[Cursor]) :
        
        self.entity_watchlist_screening_id = entity_watchlist_screening_id;self.cursor = cursor
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(entity_watchlist_screening_id = data["entity_watchlist_screening_id"],cursor = data["cursor"])


class ListWatchlistScreeningEntityHitRequest:
    
    def __init__(self, entity_watchlist_screening_id: EntityWatchlistScreeningId, cursor: Optional[Cursor]) :
        
        self.entity_watchlist_screening_id = entity_watchlist_screening_id;self.cursor = cursor
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(entity_watchlist_screening_id = data["entity_watchlist_screening_id"],cursor = data["cursor"])


class ListWatchlistScreeningEntityProgramsRequest:
    
    def __init__(self, cursor: Optional[Cursor]) :
        
        self.cursor = cursor
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(cursor = data["cursor"])


class ListWatchlistScreeningEntityReviewsRequest:
    
    def __init__(self, entity_watchlist_screening_id: EntityWatchlistScreeningId, cursor: Optional[Cursor]) :
        
        self.entity_watchlist_screening_id = entity_watchlist_screening_id;self.cursor = cursor
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(entity_watchlist_screening_id = data["entity_watchlist_screening_id"],cursor = data["cursor"])


class ListWatchlistScreeningIndividualHistoryRequest:
    
    def __init__(self, watchlist_screening_id: WatchlistScreeningIndividualId, cursor: Optional[Cursor]) :
        
        self.watchlist_screening_id = watchlist_screening_id;self.cursor = cursor
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(watchlist_screening_id = data["watchlist_screening_id"],cursor = data["cursor"])


class ListWatchlistScreeningIndividualHitRequest:
    
    def __init__(self, watchlist_screening_id: WatchlistScreeningIndividualId, cursor: Optional[Cursor]) :
        
        self.watchlist_screening_id = watchlist_screening_id;self.cursor = cursor
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(watchlist_screening_id = data["watchlist_screening_id"],cursor = data["cursor"])


class ListWatchlistScreeningIndividualProgramsRequest:
    
    def __init__(self, cursor: Optional[Cursor]) :
        
        self.cursor = cursor
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(cursor = data["cursor"])


class ListWatchlistScreeningIndividualReviewsRequest:
    
    def __init__(self, watchlist_screening_id: WatchlistScreeningIndividualId, cursor: Optional[Cursor]) :
        
        self.watchlist_screening_id = watchlist_screening_id;self.cursor = cursor
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(watchlist_screening_id = data["watchlist_screening_id"],cursor = data["cursor"])


class MatchSummary:
    
    def __init__(self, summary: MatchSummaryCode) :
        
        self.summary = summary
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(summary = data["summary"])


class MatchSummaryCode:
    
    def __init__(self, match_summary_code: str) :
        
        self.match_summary_code = match_summary_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PoBoxStatus:
    
    def __init__(self, po_box_status: str) :
        
        self.po_box_status = po_box_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PaginatedDashboardUserListResponse:
    
    def __init__(self, dashboard_users: List[DashboardUser], next_cursor: Optional[Cursor], request_id: RequestId) :
        
        self.dashboard_users = dashboard_users;self.next_cursor = next_cursor;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(dashboard_users = data["dashboard_users"],next_cursor = data["next_cursor"],request_id = data["request_id"])


class PaginatedEntityWatchlistProgramListResponse:
    
    def __init__(self, entity_watchlist_programs: List[EntityWatchlistProgram], next_cursor: Optional[Cursor], request_id: RequestId) :
        
        self.entity_watchlist_programs = entity_watchlist_programs;self.next_cursor = next_cursor;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(entity_watchlist_programs = data["entity_watchlist_programs"],next_cursor = data["next_cursor"],request_id = data["request_id"])


class PaginatedEntityWatchlistScreeningHitListResponse:
    
    def __init__(self, entity_watchlist_screening_hits: List[EntityWatchlistScreeningHit], next_cursor: Optional[Cursor], request_id: RequestId) :
        
        self.entity_watchlist_screening_hits = entity_watchlist_screening_hits;self.next_cursor = next_cursor;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(entity_watchlist_screening_hits = data["entity_watchlist_screening_hits"],next_cursor = data["next_cursor"],request_id = data["request_id"])


class PaginatedEntityWatchlistScreeningListResponse:
    
    def __init__(self, entity_watchlist_screenings: List[EntityWatchlistScreening], next_cursor: Optional[Cursor], request_id: RequestId) :
        
        self.entity_watchlist_screenings = entity_watchlist_screenings;self.next_cursor = next_cursor;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(entity_watchlist_screenings = data["entity_watchlist_screenings"],next_cursor = data["next_cursor"],request_id = data["request_id"])


class PaginatedEntityWatchlistScreeningReviewListResponse:
    
    def __init__(self, entity_watchlist_screening_reviews: List[EntityWatchlistScreeningReview], next_cursor: Optional[Cursor], request_id: RequestId) :
        
        self.entity_watchlist_screening_reviews = entity_watchlist_screening_reviews;self.next_cursor = next_cursor;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(entity_watchlist_screening_reviews = data["entity_watchlist_screening_reviews"],next_cursor = data["next_cursor"],request_id = data["request_id"])


class PaginatedIdentityVerificationListResponse:
    
    def __init__(self, identity_verifications: List[IdentityVerification], next_cursor: Optional[Cursor], request_id: RequestId) :
        
        self.identity_verifications = identity_verifications;self.next_cursor = next_cursor;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(identity_verifications = data["identity_verifications"],next_cursor = data["next_cursor"],request_id = data["request_id"])


class PaginatedIndividualWatchlistProgramListResponse:
    
    def __init__(self, watchlist_programs: List[IndividualWatchlistProgram], next_cursor: Optional[Cursor], request_id: RequestId) :
        
        self.watchlist_programs = watchlist_programs;self.next_cursor = next_cursor;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(watchlist_programs = data["watchlist_programs"],next_cursor = data["next_cursor"],request_id = data["request_id"])


class PaginatedIndividualWatchlistScreeningHitListResponse:
    
    def __init__(self, watchlist_screening_hits: List[WatchlistScreeningHit], next_cursor: Optional[Cursor], request_id: RequestId) :
        
        self.watchlist_screening_hits = watchlist_screening_hits;self.next_cursor = next_cursor;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(watchlist_screening_hits = data["watchlist_screening_hits"],next_cursor = data["next_cursor"],request_id = data["request_id"])


class PaginatedIndividualWatchlistScreeningListResponse:
    
    def __init__(self, watchlist_screenings: List[WatchlistScreeningIndividual], next_cursor: Optional[Cursor], request_id: RequestId) :
        
        self.watchlist_screenings = watchlist_screenings;self.next_cursor = next_cursor;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(watchlist_screenings = data["watchlist_screenings"],next_cursor = data["next_cursor"],request_id = data["request_id"])


class PaginatedIndividualWatchlistScreeningReviewListResponse:
    
    def __init__(self, watchlist_screening_reviews: List[WatchlistScreeningReview], next_cursor: Optional[Cursor], request_id: RequestId) :
        
        self.watchlist_screening_reviews = watchlist_screening_reviews;self.next_cursor = next_cursor;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(watchlist_screening_reviews = data["watchlist_screening_reviews"],next_cursor = data["next_cursor"],request_id = data["request_id"])


class PhoneType:
    
    def __init__(self, phone_type: str) :
        
        self.phone_type = phone_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PhysicalDocumentCategory:
    
    def __init__(self, physical_document_category: str) :
        
        self.physical_document_category = physical_document_category
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PhysicalDocumentExtractedData:
    
    def __init__(self, id_number: Optional[PhysicalDocumentIdNumber], category: PhysicalDocumentCategory, expiration_date: Optional[Any], issuing_country: GenericCountryCode) :
        
        self.id_number = id_number;self.category = category;self.expiration_date = expiration_date;self.issuing_country = issuing_country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id_number = data["id_number"],category = data["category"],expiration_date = data["expiration_date"],issuing_country = data["issuing_country"])


class PhysicalDocumentExtractedDataAnalysis:
    
    def __init__(self, name: DocumentNameMatchCode, date_of_birth: DocumentDateOfBirthMatchCode, expiration_date: ExpirationDate, issuing_country: IssuingCountry) :
        
        self.name = name;self.date_of_birth = date_of_birth;self.expiration_date = expiration_date;self.issuing_country = issuing_country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(name = data["name"],date_of_birth = data["date_of_birth"],expiration_date = data["expiration_date"],issuing_country = data["issuing_country"])


class PhysicalDocumentIdNumber:
    
    def __init__(self, physical_document_id_number: Optional[str]) :
        
        self.physical_document_id_number = physical_document_id_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PhysicalDocumentImages:
    
    def __init__(self, original_front: DocumentImageFront, original_back: Optional[DocumentImageBack], cropped_front: Optional[DocumentImageCroppedFront], cropped_back: Optional[DocumentImageCroppedBack], face: Optional[DocumentImageFace]) :
        
        self.original_front = original_front;self.original_back = original_back;self.cropped_front = cropped_front;self.cropped_back = cropped_back;self.face = face
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(original_front = data["original_front"],original_back = data["original_back"],cropped_front = data["cropped_front"],cropped_back = data["cropped_back"],face = data["face"])


class PostalCode:
    
    def __init__(self, postal_code: str) :
        
        self.postal_code = postal_code
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class PreviousIdentityVerificationAttemptId:
    
    def __init__(self, previous_identity_verification_attempt_id: Optional[str]) :
        
        self.previous_identity_verification_attempt_id = previous_identity_verification_attempt_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ProgramArchived:
    
    def __init__(self, program_archived: bool) :
        
        self.program_archived = program_archived
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ProgramNameSensitivity:
    
    def __init__(self, program_name_sensitivity: str) :
        
        self.program_name_sensitivity = program_name_sensitivity
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Region:
    
    def __init__(self, region: str) :
        
        self.region = region
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ReviewComment:
    
    def __init__(self, review_comment: Optional[str]) :
        
        self.review_comment = review_comment
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ScreeningHitAnalysis:
    
    def __init__(self, dates_of_birth: MatchSummaryCode, documents: MatchSummaryCode, locations: MatchSummaryCode, names: MatchSummaryCode, search_terms_version: float) :
        
        self.dates_of_birth = dates_of_birth;self.documents = documents;self.locations = locations;self.names = names;self.search_terms_version = search_terms_version
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(dates_of_birth = data["dates_of_birth"],documents = data["documents"],locations = data["locations"],names = data["names"],search_terms_version = data["search_terms_version"])


class ScreeningHitData:
    
    def __init__(self, dates_of_birth: List[ScreeningHitDateOfBirthItem], documents: List[ScreeningHitDocumentsItems], locations: List[GenericScreeningHitLocationItems], names: List[ScreeningHitNamesItems]) :
        
        self.dates_of_birth = dates_of_birth;self.documents = documents;self.locations = locations;self.names = names
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(dates_of_birth = data["dates_of_birth"],documents = data["documents"],locations = data["locations"],names = data["names"])


class ScreeningHitDateOfBirthItem:
    
    def __init__(self, analysis: MatchSummary, data: DateRange) :
        
        self.analysis = analysis;self.data = data
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(analysis = data["analysis"],data = data["data"])


class ScreeningHitDocumentsItems:
    
    def __init__(self, analysis: MatchSummary, data: WatchlistScreeningDocument) :
        
        self.analysis = analysis;self.data = data
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(analysis = data["analysis"],data = data["data"])


class ScreeningHitNamesItems:
    
    def __init__(self, analysis: MatchSummary, data: IndividualScreeningHitNames) :
        
        self.analysis = analysis;self.data = data
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(analysis = data["analysis"],data = data["data"])


class ShareableUrl:
    
    def __init__(self, shareable_url: Optional[str]) :
        
        self.shareable_url = shareable_url
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Source:
    
    def __init__(self, source: str) :
        
        self.source = source
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class SourceUid:
    
    def __init__(self, source_uid: Optional[str]) :
        
        self.source_uid = source_uid
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Strategy:
    
    def __init__(self, strategy: str) :
        
        self.strategy = strategy
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Street:
    
    def __init__(self, street: str) :
        
        self.street = street
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Street2:
    
    def __init__(self, street2: Optional[str]) :
        
        self.street2 = street2
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Timestamp:
    
    def __init__(self, timestamp: str) :
        
        self.timestamp = timestamp
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class TimestampNullable:
    
    def __init__(self, timestamp_nullable: Optional[str]) :
        
        self.timestamp_nullable = timestamp_nullable
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class Url:
    
    def __init__(self, url: str) :
        
        self.url = url
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class UpdateEntityScreeningRequest:
    
    def __init__(self, entity_watchlist_screening_id: EntityWatchlistScreeningId, search_terms: Optional[UpdateEntityScreeningRequestSearchTerms], assignee: Optional[Any], status: Optional[Any], client_user_id: Optional[Any], reset_fields: Optional[UpdateEntityScreeningRequestResettableFieldList]) :
        
        self.entity_watchlist_screening_id = entity_watchlist_screening_id;self.search_terms = search_terms;self.assignee = assignee;self.status = status;self.client_user_id = client_user_id;self.reset_fields = reset_fields
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(entity_watchlist_screening_id = data["entity_watchlist_screening_id"],search_terms = data["search_terms"],assignee = data["assignee"],status = data["status"],client_user_id = data["client_user_id"],reset_fields = data["reset_fields"])


class UpdateEntityScreeningRequestResettableField:
    
    def __init__(self, update_entity_screening_request_resettable_field: str) :
        
        self.update_entity_screening_request_resettable_field = update_entity_screening_request_resettable_field
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class UpdateEntityScreeningRequestResettableFieldList:
    
    def __init__(self, update_entity_screening_request_resettable_field_list: Optional[List[UpdateEntityScreeningRequestResettableField]]) :
        
        self.update_entity_screening_request_resettable_field_list = update_entity_screening_request_resettable_field_list
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(UpdateEntityScreeningRequestResettableField.from_json(d) for d in data)


class UpdateEntityScreeningRequestSearchTerms:
    
    def __init__(self, entity_watchlist_program_id: EntityWatchlistProgramId, legal_name: Optional[Any], document_number: Optional[Any], email_address: Optional[Any], country: Optional[Any], phone_number: Optional[Any], url: Optional[Any]) :
        
        self.entity_watchlist_program_id = entity_watchlist_program_id;self.legal_name = legal_name;self.document_number = document_number;self.email_address = email_address;self.country = country;self.phone_number = phone_number;self.url = url
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(entity_watchlist_program_id = data["entity_watchlist_program_id"],legal_name = data["legal_name"],document_number = data["document_number"],email_address = data["email_address"],country = data["country"],phone_number = data["phone_number"],url = data["url"])


class UpdateIndividualScreeningRequest:
    
    def __init__(self, watchlist_screening_id: WatchlistScreeningIndividualId, search_terms: Optional[UpdateIndividualScreeningRequestSearchTerms], assignee: Optional[Any], status: Optional[Any], client_user_id: Optional[Any], reset_fields: Optional[UpdateIndividualScreeningRequestResettableFieldList]) :
        
        self.watchlist_screening_id = watchlist_screening_id;self.search_terms = search_terms;self.assignee = assignee;self.status = status;self.client_user_id = client_user_id;self.reset_fields = reset_fields
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(watchlist_screening_id = data["watchlist_screening_id"],search_terms = data["search_terms"],assignee = data["assignee"],status = data["status"],client_user_id = data["client_user_id"],reset_fields = data["reset_fields"])


class UpdateIndividualScreeningRequestResettableField:
    
    def __init__(self, update_individual_screening_request_resettable_field: str) :
        
        self.update_individual_screening_request_resettable_field = update_individual_screening_request_resettable_field
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class UpdateIndividualScreeningRequestResettableFieldList:
    
    def __init__(self, update_individual_screening_request_resettable_field_list: Optional[List[UpdateIndividualScreeningRequestResettableField]]) :
        
        self.update_individual_screening_request_resettable_field_list = update_individual_screening_request_resettable_field_list
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(UpdateIndividualScreeningRequestResettableField.from_json(d) for d in data)


class UpdateIndividualScreeningRequestSearchTerms:
    
    def __init__(self, watchlist_program_id: Optional[Any], legal_name: Optional[Any], date_of_birth: Optional[Any], document_number: Optional[Any], country: Optional[Any]) :
        
        self.watchlist_program_id = watchlist_program_id;self.legal_name = legal_name;self.date_of_birth = date_of_birth;self.document_number = document_number;self.country = country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(watchlist_program_id = data["watchlist_program_id"],legal_name = data["legal_name"],date_of_birth = data["date_of_birth"],document_number = data["document_number"],country = data["country"])


class UserAddress:
    
    def __init__(self, street: Street, street2: Optional[Street2], city: City, region: Region, postal_code: PostalCode, country: GenericCountryCode) :
        
        self.street = street;self.street2 = street2;self.city = city;self.region = region;self.postal_code = postal_code;self.country = country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(street = data["street"],street2 = data["street2"],city = data["city"],region = data["region"],postal_code = data["postal_code"],country = data["country"])


class UserIdNumber:
    
    def __init__(self, value: IdNumberValue, type_: IdNumberType) :
        
        self.value = value;self.type_ = type_
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(value = data["value"],type_ = data["type_"])


class UserName:
    
    def __init__(self, given_name: GivenNameField, family_name: FamilyNameField) :
        
        self.given_name = given_name;self.family_name = family_name
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(given_name = data["given_name"],family_name = data["family_name"])


class WatchlistProgramId:
    
    def __init__(self, watchlist_program_id: str) :
        
        self.watchlist_program_id = watchlist_program_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class WatchlistScreeningAuditTrail:
    
    def __init__(self, source: Source, dashboard_user_id: Optional[Any], timestamp: Timestamp) :
        
        self.source = source;self.dashboard_user_id = dashboard_user_id;self.timestamp = timestamp
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(source = data["source"],dashboard_user_id = data["dashboard_user_id"],timestamp = data["timestamp"])


class WatchlistScreeningCreateRequest:
    
    def __init__(self, search_terms: WatchlistScreeningRequestSearchTerms, client_user_id: Optional[Any]) :
        
        self.search_terms = search_terms;self.client_user_id = client_user_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(search_terms = data["search_terms"],client_user_id = data["client_user_id"])


class WatchlistScreeningDocument:
    
    def __init__(self, type_: WatchlistScreeningDocumentType, number: WatchlistScreeningDocumentValue) :
        
        self.type_ = type_;self.number = number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(type_ = data["type_"],number = data["number"])


class WatchlistScreeningDocumentType:
    
    def __init__(self, watchlist_screening_document_type: str) :
        
        self.watchlist_screening_document_type = watchlist_screening_document_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class WatchlistScreeningDocumentValue:
    
    def __init__(self, watchlist_screening_document_value: str) :
        
        self.watchlist_screening_document_value = watchlist_screening_document_value
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class WatchlistScreeningHit:
    
    def __init__(self, id: WatchlistScreeningHitId, review_status: WatchlistScreeningHitStatus, first_active: Timestamp, inactive_since: Optional[TimestampNullable], historical_since: Optional[TimestampNullable], list_code: IndividualWatchlistCode, plaid_uid: InternalUid, source_uid: Optional[SourceUid], analysis: ScreeningHitAnalysis, data: ScreeningHitData) :
        
        self.id = id;self.review_status = review_status;self.first_active = first_active;self.inactive_since = inactive_since;self.historical_since = historical_since;self.list_code = list_code;self.plaid_uid = plaid_uid;self.source_uid = source_uid;self.analysis = analysis;self.data = data
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],review_status = data["review_status"],first_active = data["first_active"],inactive_since = data["inactive_since"],historical_since = data["historical_since"],list_code = data["list_code"],plaid_uid = data["plaid_uid"],source_uid = data["source_uid"],analysis = data["analysis"],data = data["data"])


class WatchlistScreeningHitId:
    
    def __init__(self, watchlist_screening_hit_id: str) :
        
        self.watchlist_screening_hit_id = watchlist_screening_hit_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class WatchlistScreeningHitLocations:
    
    def __init__(self, full: str, country: GenericCountryCode) :
        
        self.full = full;self.country = country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(full = data["full"],country = data["country"])


class WatchlistScreeningHitStatus:
    
    def __init__(self, watchlist_screening_hit_status: str) :
        
        self.watchlist_screening_hit_status = watchlist_screening_hit_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class WatchlistScreeningIndividual:
    
    def __init__(self, id: WatchlistScreeningIndividualId, search_terms: WatchlistScreeningSearchTerms, assignee: Optional[Any], status: WatchlistScreeningStatus, client_user_id: Optional[Any], audit_trail: WatchlistScreeningAuditTrail) :
        
        self.id = id;self.search_terms = search_terms;self.assignee = assignee;self.status = status;self.client_user_id = client_user_id;self.audit_trail = audit_trail
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],search_terms = data["search_terms"],assignee = data["assignee"],status = data["status"],client_user_id = data["client_user_id"],audit_trail = data["audit_trail"])


class WatchlistScreeningIndividualId:
    
    def __init__(self, watchlist_screening_individual_id: str) :
        
        self.watchlist_screening_individual_id = watchlist_screening_individual_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class WatchlistScreeningIndividualName:
    
    def __init__(self, watchlist_screening_individual_name: str) :
        
        self.watchlist_screening_individual_name = watchlist_screening_individual_name
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class WatchlistScreeningIndividualResponse:
    
    def __init__(self, id: WatchlistScreeningIndividualId, search_terms: WatchlistScreeningSearchTerms, assignee: Optional[Any], status: WatchlistScreeningStatus, client_user_id: Optional[Any], audit_trail: WatchlistScreeningAuditTrail, request_id: RequestId) :
        
        self.id = id;self.search_terms = search_terms;self.assignee = assignee;self.status = status;self.client_user_id = client_user_id;self.audit_trail = audit_trail;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],search_terms = data["search_terms"],assignee = data["assignee"],status = data["status"],client_user_id = data["client_user_id"],audit_trail = data["audit_trail"],request_id = data["request_id"])


class WatchlistScreeningPhoneNumber:
    
    def __init__(self, watchlist_screening_phone_number: str) :
        
        self.watchlist_screening_phone_number = watchlist_screening_phone_number
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class WatchlistScreeningRequestSearchTerms:
    
    def __init__(self, watchlist_program_id: WatchlistProgramId, legal_name: WatchlistScreeningIndividualName, date_of_birth: Optional[Any], document_number: Optional[Any], country: Optional[Any]) :
        
        self.watchlist_program_id = watchlist_program_id;self.legal_name = legal_name;self.date_of_birth = date_of_birth;self.document_number = document_number;self.country = country
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(watchlist_program_id = data["watchlist_program_id"],legal_name = data["legal_name"],date_of_birth = data["date_of_birth"],document_number = data["document_number"],country = data["country"])


class WatchlistScreeningReview:
    
    def __init__(self, id: WatchlistScreeningReviewId, confirmed_hits: List[WatchlistScreeningHitId], dismissed_hits: List[WatchlistScreeningHitId], comment: Optional[ReviewComment], audit_trail: WatchlistScreeningAuditTrail) :
        
        self.id = id;self.confirmed_hits = confirmed_hits;self.dismissed_hits = dismissed_hits;self.comment = comment;self.audit_trail = audit_trail
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],confirmed_hits = data["confirmed_hits"],dismissed_hits = data["dismissed_hits"],comment = data["comment"],audit_trail = data["audit_trail"])


class WatchlistScreeningReviewId:
    
    def __init__(self, watchlist_screening_review_id: str) :
        
        self.watchlist_screening_review_id = watchlist_screening_review_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class WatchlistScreeningReviewResponse:
    
    def __init__(self, id: WatchlistScreeningReviewId, confirmed_hits: List[WatchlistScreeningHitId], dismissed_hits: List[WatchlistScreeningHitId], comment: Optional[ReviewComment], audit_trail: WatchlistScreeningAuditTrail, request_id: RequestId) :
        
        self.id = id;self.confirmed_hits = confirmed_hits;self.dismissed_hits = dismissed_hits;self.comment = comment;self.audit_trail = audit_trail;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(id = data["id"],confirmed_hits = data["confirmed_hits"],dismissed_hits = data["dismissed_hits"],comment = data["comment"],audit_trail = data["audit_trail"],request_id = data["request_id"])


class WatchlistScreeningSearchTerms:
    
    def __init__(self, watchlist_program_id: WatchlistProgramId, legal_name: WatchlistScreeningIndividualName, date_of_birth: Optional[Any], document_number: Optional[Any], country: Optional[Any], version: float) :
        
        self.watchlist_program_id = watchlist_program_id;self.legal_name = legal_name;self.date_of_birth = date_of_birth;self.document_number = document_number;self.country = country;self.version = version
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(watchlist_program_id = data["watchlist_program_id"],legal_name = data["legal_name"],date_of_birth = data["date_of_birth"],document_number = data["document_number"],country = data["country"],version = data["version"])


class WatchlistScreeningStatus:
    
    def __init__(self, watchlist_screening_status: str) :
        
        self.watchlist_screening_status = watchlist_screening_status
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class WeakAliasDetermination:
    
    def __init__(self, weak_alias_determination: str) :
        
        self.weak_alias_determination = weak_alias_determination
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ItemGetRequest:
    
    def __init__(self, access_token: AccessToken) :
        
        self.access_token = access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"])


class ItemGetResponse:
    
    def __init__(self, item: Item, status: Optional[ItemStatusNullable], request_id: RequestId) :
        
        self.item = item;self.status = status;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(item = data["item"],status = data["status"],request_id = data["request_id"])


class ItemRemoveRequest:
    
    def __init__(self, access_token: AccessToken) :
        
        self.access_token = access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"])


class ItemRemoveResponse:
    
    def __init__(self, request_id: RequestId) :
        
        self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(request_id = data["request_id"])


class ItemWebhookUpdateRequest:
    
    def __init__(self, access_token: AccessToken, webhook: Optional[str]) :
        
        self.access_token = access_token;self.webhook = webhook
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],webhook = data["webhook"])


class ItemWebhookUpdateResponse:
    
    def __init__(self, item: Item, request_id: RequestId) :
        
        self.item = item;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(item = data["item"],request_id = data["request_id"])


class ItemAccessTokenInvalidateRequest:
    
    def __init__(self, access_token: AccessToken) :
        
        self.access_token = access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"])


class ItemAccessTokenInvalidateResponse:
    
    def __init__(self, new_access_token: AccessToken, request_id: RequestId) :
        
        self.new_access_token = new_access_token;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(new_access_token = data["new_access_token"],request_id = data["request_id"])


class ItemPublicTokenExchangeRequest:
    
    def __init__(self, public_token: str) :
        
        self.public_token = public_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(public_token = data["public_token"])


class ItemPublicTokenExchangeResponse:
    
    def __init__(self, access_token: AccessToken, item_id: str, request_id: RequestId) :
        
        self.access_token = access_token;self.item_id = item_id;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],item_id = data["item_id"],request_id = data["request_id"])


class ItemPublicTokenCreateRequest:
    
    def __init__(self, access_token: AccessToken) :
        
        self.access_token = access_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"])


class ItemPublicTokenCreateResponse:
    
    def __init__(self, public_token: str, expiration: str, request_id: RequestId) :
        
        self.public_token = public_token;self.expiration = expiration;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(public_token = data["public_token"],expiration = data["expiration"],request_id = data["request_id"])


class ItemImportRequest:
    
    def __init__(self, products: List[Products], user_auth: ItemImportRequestUserAuth, options: ItemImportRequestOptions) :
        
        self.products = products;self.user_auth = user_auth;self.options = options
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(products = data["products"],user_auth = data["user_auth"],options = data["options"])


class ItemImportRequestOptions:
    
    def __init__(self, webhook: str) :
        
        self.webhook = webhook
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(webhook = data["webhook"])


class ItemImportRequestUserAuth:
    
    def __init__(self, user_id: str, auth_token: str) :
        
        self.user_id = user_id;self.auth_token = auth_token
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(user_id = data["user_id"],auth_token = data["auth_token"])


class ItemImportResponse:
    
    def __init__(self, access_token: AccessToken, request_id: RequestId) :
        
        self.access_token = access_token;self.request_id = request_id
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(access_token = data["access_token"],request_id = data["request_id"])


class Item:
    
    def __init__(self, item_id: str, institution_id: Optional[str], webhook: Optional[str], error: Optional[PlaidError], available_products: List[Products], billed_products: List[Products], products: List[Products], consented_products: List[Products], consent_expiration_time: Optional[str], update_type: str) :
        
        self.item_id = item_id;self.institution_id = institution_id;self.webhook = webhook;self.error = error;self.available_products = available_products;self.billed_products = billed_products;self.products = products;self.consented_products = consented_products;self.consent_expiration_time = consent_expiration_time;self.update_type = update_type
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(item_id = data["item_id"],institution_id = data["institution_id"],webhook = data["webhook"],error = data["error"],available_products = data["available_products"],billed_products = data["billed_products"],products = data["products"],consented_products = data["consented_products"],consent_expiration_time = data["consent_expiration_time"],update_type = data["update_type"])


class ItemStatus:
    
    def __init__(self, investments: Optional[ItemStatusInvestments], transactions: Optional[ItemStatusTransactions], last_webhook: Optional[ItemStatusLastWebhook]) :
        
        self.investments = investments;self.transactions = transactions;self.last_webhook = last_webhook
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(investments = data["investments"],transactions = data["transactions"],last_webhook = data["last_webhook"])


class ItemStatusNullable:
    
    def __init__(self, item_status_nullable: Optional[Any]) :
        
        self.item_status_nullable = item_status_nullable
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(data)


class ItemStatusTransactions:
    
    def __init__(self, last_successful_update: Optional[str], last_failed_update: Optional[str]) :
        
        self.last_successful_update = last_successful_update;self.last_failed_update = last_failed_update
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(last_successful_update = data["last_successful_update"],last_failed_update = data["last_failed_update"])


class ItemStatusInvestments:
    
    def __init__(self, last_successful_update: Optional[str], last_failed_update: Optional[str]) :
        
        self.last_successful_update = last_successful_update;self.last_failed_update = last_failed_update
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(last_successful_update = data["last_successful_update"],last_failed_update = data["last_failed_update"])


class ItemStatusLastWebhook:
    
    def __init__(self, sent_at: Optional[str], code_sent: Optional[str]) :
        
        self.sent_at = sent_at;self.code_sent = code_sent
    
    @classmethod
    def from_json(cls, data: Any) :
        
        return cls(sent_at = data["sent_at"],code_sent = data["code_sent"])

