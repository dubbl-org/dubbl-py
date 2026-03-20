<div align="center">

# dubbl

**Official Python SDK for the [Dubbl](https://dubbl.dev) double-entry bookkeeping API**

[![PyPI version](https://img.shields.io/pypi/v/dubbl.svg)](https://pypi.org/project/dubbl/)
[![Python versions](https://img.shields.io/pypi/pyversions/dubbl.svg)](https://pypi.org/project/dubbl/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CI](https://github.com/dubbldev/dubbl-py/actions/workflows/ci.yml/badge.svg)](https://github.com/dubbldev/dubbl-py/actions/workflows/ci.yml)
[![Typed](https://img.shields.io/badge/typing-typed-blue.svg)](https://peps.python.org/pep-0561/)

</div>

---

The Dubbl Python SDK provides a convenient, fully-typed interface to the [Dubbl API](https://docs.dubbl.dev) — an open-source, double-entry bookkeeping platform. Both **synchronous** and **asynchronous** clients are included.

## Installation

```bash
pip install dubbl
```

## Quick Start

```python
import dubbl

client = dubbl.Dubbl(api_key="dk_live_...")

# Create a contact
contact = client.contacts.create(
    name="Acme Corp",
    email="billing@acme.com",
    type="customer",
)

# Create an invoice
invoice = client.invoices.create(
    contact_id=contact["id"],
    issue_date="2025-01-15",
    lines=[
        {
            "description": "Consulting services",
            "quantity": 10,
            "unitPrice": 15000,  # $150.00 in cents
        }
    ],
)

# List all accounts
accounts = client.accounts.list()
```

### Async Usage

```python
import asyncio
import dubbl

async def main():
    async with dubbl.AsyncDubbl(api_key="dk_live_...") as client:
        invoices = await client.invoices.list(status="sent")
        print(invoices)

asyncio.run(main())
```

## Configuration

```python
client = dubbl.Dubbl(
    api_key="dk_live_...",          # or set DUBBL_API_KEY env var
    organization_id="org_...",      # or set DUBBL_ORGANIZATION_ID env var
    base_url="https://app.dubbl.dev",  # or set DUBBL_BASE_URL env var
    timeout=30.0,                   # request timeout in seconds (default: 60)
    max_retries=3,                  # retry attempts for transient errors (default: 2)
)
```

### Environment Variables

| Variable | Description |
|----------|-------------|
| `DUBBL_API_KEY` | Your API key (starts with `dk_live_`) |
| `DUBBL_ORGANIZATION_ID` | Default organization ID |
| `DUBBL_BASE_URL` | Override the API base URL |

## Resources

The SDK provides access to all Dubbl API resources:

### Core Bookkeeping

| Resource | Description |
|----------|-------------|
| `client.accounts` | Chart of accounts management |
| `client.entries` | Journal entries (create, post, void) |
| `client.fiscal_years` | Fiscal year management |
| `client.tax_rates` | Tax rate configuration |
| `client.cost_centers` | Cost center tracking |
| `client.budgets` | Budget creation and tracking |

### Sales & Purchasing

| Resource | Description |
|----------|-------------|
| `client.invoices` | Invoice management (create, send, pay, void, PDF) |
| `client.bills` | Bill management (create, approve, pay, void) |
| `client.quotes` | Quote management (create, send, accept, convert) |
| `client.credit_notes` | Credit note management |
| `client.purchase_orders` | Purchase order management |
| `client.recurring` | Recurring invoices and expenses |

### Contacts & Payments

| Resource | Description |
|----------|-------------|
| `client.contacts` | Customer and supplier management |
| `client.payments` | Payment recording and allocation |

### Banking

| Resource | Description |
|----------|-------------|
| `client.bank_accounts` | Bank account management |
| `client.bank_transactions` | Transaction reconciliation, matching, splitting |

### Expenses & Inventory

| Resource | Description |
|----------|-------------|
| `client.expenses` | Expense claims (submit, approve, pay) |
| `client.inventory` | Inventory items, categories, stock takes, assemblies |
| `client.fixed_assets` | Fixed asset management and depreciation |

### Reports

| Resource | Description |
|----------|-------------|
| `client.reports` | Financial reports (P&L, balance sheet, cash flow, etc.) |

```python
# Trial balance
trial_balance = client.reports.trial_balance(from_date="2025-01-01", to_date="2025-12-31")

# Profit and loss
pnl = client.reports.profit_and_loss(from_date="2025-01-01", to_date="2025-03-31")

# Aged receivables
aged = client.reports.aged_receivables()

# Custom report
report = client.reports.run(
    data_source="invoices",
    filters=[{"field": "status", "operator": "eq", "value": "overdue"}],
    group_by=["contactId"],
    columns=["contactName", "total", "amountDue"],
)
```

### Organization & Settings

| Resource | Description |
|----------|-------------|
| `client.organization` | Organization settings |
| `client.members` | Team member management |
| `client.roles` | Role and permission management |
| `client.api_keys` | API key management |
| `client.webhooks` | Webhook configuration |

### Data Management

| Resource | Description |
|----------|-------------|
| `client.documents` | Document storage |
| `client.attachments` | File attachments (pre-signed uploads) |
| `client.tags` | Tag management |
| `client.audit_log` | Audit trail |
| `client.trash` | Soft-deleted item recovery |
| `client.export` | Data export |
| `client.backups` | Backup and restore |
| `client.user` | Current user profile |
| `client.projects` | Project and time tracking |

## Error Handling

The SDK raises specific exceptions for different error types:

```python
import dubbl
from dubbl import AuthenticationError, NotFoundError, ValidationError, DubblError

client = dubbl.Dubbl(api_key="dk_live_...")

try:
    invoice = client.invoices.retrieve("non-existent-id")
except AuthenticationError:
    print("Invalid API key")
except NotFoundError:
    print("Invoice not found")
except ValidationError as e:
    print(f"Invalid request: {e.message}")
except DubblError as e:
    print(f"Something went wrong: {e}")
```

### Exception Hierarchy

```
DubblError
├── APIError
│   ├── ValidationError        (400)
│   ├── AuthenticationError    (401)
│   ├── PermissionDeniedError  (403)
│   ├── NotFoundError          (404)
│   ├── ConflictError          (409)
│   ├── RateLimitError         (429)
│   └── InternalServerError    (500)
├── APIConnectionError
└── APITimeoutError
```

## Common Patterns

### Pagination

```python
# Paginated listing
page1 = client.invoices.list(page=1, limit=50)
for invoice in page1["items"]:
    print(invoice["invoiceNumber"], invoice["total"])

# Next page
page2 = client.invoices.list(page=2, limit=50)
```

### Invoice Workflow

```python
# Create -> Send -> Record Payment
invoice = client.invoices.create(
    contact_id="...",
    issue_date="2025-01-15",
    lines=[{"description": "Services", "quantity": 1, "unitPrice": 50000}],
)

client.invoices.send(invoice["id"])

client.payments.create(
    contact_id=invoice["contactId"],
    type="received",
    date="2025-02-01",
    amount=50000,
    allocations=[
        {"documentType": "invoice", "documentId": invoice["id"], "amount": 50000}
    ],
)
```

### Journal Entry Workflow

```python
# Create -> Post
entry = client.entries.create(
    date="2025-01-15",
    description="Office supplies purchase",
    lines=[
        {"accountId": "expense-account-id", "debitAmount": 5000, "creditAmount": 0},
        {"accountId": "cash-account-id", "debitAmount": 0, "creditAmount": 5000},
    ],
)

client.entries.post(entry["id"])
```

### Download Invoice PDF

```python
pdf_bytes = client.invoices.pdf("invoice-id")
with open("invoice.pdf", "wb") as f:
    f.write(pdf_bytes)
```

## Requirements

- Python 3.8+
- [httpx](https://www.python-httpx.org/) (automatically installed)

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
