# Usage Guide

## Quick Start

### 1. Import and Initialize

```python
from kotak_api_wn import NeoAPI

# Create client with credentials
client = NeoAPI(
    consumer_key="your_consumer_key",
    environment="prod"  # "prod" for live, "uat" for testing
)
```

### 2. Authentication (TOTP)

```python
# Login with TOTP
totp_response = client.totp_login(
    mobile_number="9876543210",
    ucc="your_ucc",
    totp="123456"  # 6-digit code from authenticator app
)

# Validate with MPIN
client.totp_validate(mpin="123456")
```

## Trading Operations

### Place Order

```python
# Market Order
order = client.place_order(
    exchange_segment="NSE",      # NSE, BSE, NFO, etc.
    product="MIS",               # MIS, CNC, NRML
    price="0",                   # 0 for market orders
    order_type="MKT",            # MKT, L (limit), SL, SL-M
    quantity="10",
    validity="DAY",              # DAY, IOC
    trading_symbol="RELIANCE-EQ",
    transaction_type="B"         # B (buy), S (sell)
)
print(f"Order ID: {order.get('nOrdNo')}")

# Limit Order
limit_order = client.place_order(
    exchange_segment="NSE",
    product="CNC",
    price="2500.50",
    order_type="L",
    quantity="5",
    validity="DAY",
    trading_symbol="RELIANCE-EQ",
    transaction_type="B"
)

# Stop Loss Order
sl_order = client.place_order(
    exchange_segment="NSE",
    product="MIS",
    price="2450.00",
    order_type="SL",
    quantity="10",
    validity="DAY",
    trading_symbol="RELIANCE-EQ",
    transaction_type="S",
    trigger_price="2455.00"
)

# Bracket Order (BO)
bracket_order = client.place_order(
    exchange_segment="NSE",
    product="BO",
    price="2500.00",
    order_type="L",
    quantity="10",
    validity="DAY",
    trading_symbol="RELIANCE-EQ",
    transaction_type="B",
    scrip_token="11536",  # Instrument token
    sot="2480.00",        # Stop loss trigger price
    slt="2475.00"         # Stop loss limit price
)

# Cover Order (CO)
cover_order = client.place_order(
    exchange_segment="NSE",
    product="CO",
    price="2500.00",
    order_type="L",
    quantity="10",
    validity="DAY",
    trading_symbol="RELIANCE-EQ",
    transaction_type="B"
)
```

### Modify Order

```python
# Modify with order ID only (fetches details automatically)
modified = client.modify_order(
    order_id="221206000012345",
    price="2510.00",
    order_type="L",
    quantity="5",
    validity="DAY"
)

# Modify with full details (faster)
modified = client.modify_order(
    order_id="221206000012345",
    price="2510.00",
    order_type="L",
    quantity="5",
    validity="DAY",
    instrument_token="11536",
    exchange_segment="NSE",
    product="CNC",
    trading_symbol="RELIANCE-EQ",
    transaction_type="B"
)
```

### Cancel Order

```python
# Cancel regular order
cancel_response = client.cancel_order(
    order_id="221206000012345",
    isVerify=True  # Verify status before cancelling
)
print(cancel_response)

# Cancel cover order
cover_cancel = client.cancel_cover_order(order_id="221206000012346")

# Cancel bracket order
bracket_cancel = client.cancel_bracket_order(order_id="221206000012347")
```

## Portfolio & Positions

### Get Holdings

```python
holdings = client.holdings()
for holding in holdings.get('data', []):
    print(f"{holding['symbol']}: {holding['quantity']} @ {holding['avgPrice']}")
```

### Get Positions

```python
positions = client.positions()
for pos in positions.get('data', []):
    print(f"{pos['tradingSymbol']}: {pos['netQty']} P&L: {pos['pnl']}")
```

### Get Limits/Margins

```python
# All limits
limits = client.limits()
print(f"Available: {limits.get('data', {}).get('availablecash')}")

# Segment-specific limits
cash_limits = client.limits(segment="CASH", exchange="NSE")
```

## Order Reports

### Order Book

```python
orders = client.order_report()
for order in orders.get('data', []):
    print(f"{order['nOrdNo']}: {order['trdSym']} {order['ordSt']}")
```

### Order History

```python
history = client.order_history(order_id="221206000012345")
for event in history.get('data', []):
    print(f"{event['ordSt']} at {event['flDtTm']}")
```

### Trade Report

```python
# All trades
trades = client.trade_report()

# Trades for specific order
order_trades = client.trade_report(order_id="221206000012345")
```

## Market Data

### Search Scrip

```python
# Search by symbol
scrips = client.search_scrip(
    exchange_segment="NSE",
    symbol="RELIANCE"
)

# Search F&O
fo_scrips = client.search_scrip(
    exchange_segment="NFO",
    symbol="NIFTY",
    expiry="202312",
    option_type="CE",
    strike_price="20000"
)
```

### Get Quotes

```python
# Set up callbacks first
def on_message(message):
    print(f"Quote: {message}")

def on_error(error):
    print(f"Error: {error}")

client.on_message = on_message
client.on_error = on_error

# Get quotes
quotes = client.quotes(
    instrument_tokens=[
        {"exchange_segment": "nse_cm", "instrument_token": "11536"},
        {"exchange_segment": "nse_cm", "instrument_token": "1594"}
    ],
    quote_type="ltp"  # ltp, ohlc, market_depth, 52w, circuit_limits
)
```

## WebSocket Streaming

### Subscribe to Live Feed

```python
# Set up callbacks
def on_message(message):
    if message.get('type') == 'stock_feed':
        data = message.get('data', [])
        for tick in data:
            print(f"LTP: {tick.get('ltp')}")

def on_open():
    print("WebSocket connected!")

def on_close():
    print("WebSocket disconnected!")

def on_error(error):
    print(f"WebSocket error: {error}")

# Assign callbacks
client.on_message = on_message
client.on_open = on_open
client.on_close = on_close
client.on_error = on_error

# Subscribe to instruments
client.subscribe(
    instrument_tokens=[
        {"exchange_segment": "nse_cm", "instrument_token": "11536"},
        {"exchange_segment": "nse_cm", "instrument_token": "1594"}
    ],
    isIndex=False,
    isDepth=False
)
```

### Subscribe to Order Feed

```python
# Get real-time order updates
client.subscribe_to_orderfeed()
```

### Unsubscribe

```python
client.un_subscribe(
    instrument_tokens=[
        {"exchange_segment": "nse_cm", "instrument_token": "11536"}
    ]
)
```

## Session Management

### Reusing Existing Sessions

For better performance and to avoid repeated authentication, you can save and reuse session tokens. After successful authentication, save the following tokens for future use:

#### What to Save After Login

After successful TOTP login and validation, save these authentication tokens:

```python
# After successful totp_login() and totp_validate()
session_data = {
    "view_token": client.configuration.view_token,    # For read operations
    "edit_token": client.configuration.edit_token,    # For trading operations
    "edit_sid": client.configuration.edit_sid,        # Session ID for trading
    "edit_rid": client.configuration.edit_rid,        # Request ID for trading
    "sid": client.configuration.sid,                  # Base session ID
    "serverId": client.configuration.serverId         # Server identifier (optional)
}
```

#### Reusing Saved Session

To reuse a saved session without re-authentication:

```python
from kotak_api_wn import NeoAPI

# Create client with consumer_key (required for proper API authentication)
client = NeoAPI(
    consumer_key="your_consumer_key",
    environment="prod"
)

# Restore saved tokens
client.configuration.view_token = saved_session["view_token"]
client.configuration.edit_token = saved_session["edit_token"]
client.configuration.edit_sid = saved_session["edit_sid"]
client.configuration.edit_rid = saved_session["edit_rid"]
client.configuration.sid = saved_session["sid"]

# Optional: restore server ID if saved
if "serverId" in saved_session:
    client.configuration.serverId = saved_session["serverId"]

# Validate session (recommended for trading operations)
try:
    validation = client.totp_validate(mpin="your_mpin")
    if validation.get("status") == "success":
        print("Session validated - ready for trading")
    else:
        print("Session validation failed - re-authentication required")
except Exception as e:
    print(f"Session validation error: {e}")
    # Fall back to fresh TOTP login
```

#### Session Persistence Strategy

1. **Save After Fresh Login**: Store tokens after successful TOTP authentication
2. **Validate on Reuse**: Always validate with MPIN before trading operations
3. **Handle Expiration**: Sessions may expire, so implement fallback to fresh login
4. **Security**: Store tokens securely (encrypted) and refresh periodically

#### Token Types and Usage

- **view_token**: Used for read-only operations (quotes, holdings, positions)
- **edit_token**: Required for trading operations (place, modify, cancel orders)
- **sid/edit_sid**: Session identifiers for API requests
- **edit_rid**: Request identifier for trading operations

**Note**: The `edit_token` provides trading permissions and may have shorter validity than `view_token`. Always validate sessions before critical operations.

### Logout

```python
client.logout()
```

## Error Handling

```python
try:
    order = client.place_order(...)
    
    if 'error' in order:
        print(f"Order failed: {order['error']}")
    else:
        print(f"Order placed: {order.get('nOrdNo')}")
        
except Exception as e:
    print(f"Exception: {e}")
```

## Best Practices

1. **Use orjson** - Install with `pip install orjson` for best performance
2. **Reuse sessions** - Avoid repeated login calls
3. **Batch operations** - Subscribe to multiple instruments at once
4. **Handle callbacks** - Always set up error handlers
5. **Use correct environments** - "uat" for testing, "prod" for live trading
