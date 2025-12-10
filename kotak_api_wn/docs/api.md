# API Reference

## NeoAPI Class

The main client class for interacting with Kotak Neo Trading API.

### Constructor

```python
NeoAPI(
    environment: str = "uat",
    access_token: str = None,
    neo_fin_key: str = None,
    consumer_key: str = None
)
```

**Parameters:**
- `environment` - `"prod"` for live trading, `"uat"` for testing
- `access_token` - Pre-existing access token (optional)
- `neo_fin_key` - Financial key for tracking (optional)
- `consumer_key` - Your API consumer key (from Neo app)

---

## Authentication Methods

### totp_login()

```python
totp_login(
    mobile_number: str = None,
    ucc: str = None,
    totp: str = None
) -> dict
```

**Primary authentication method.** Login using TOTP (Time-based One-Time Password) from authenticator app.

**Parameters:**
- `mobile_number` - Registered mobile number
- `ucc` - Unique Client Code
- `totp` - 6-digit TOTP from authenticator app

**Returns:** `dict` with session tokens

---

### totp_validate()

```python
totp_validate(mpin: str = None) -> dict
```

Validates TOTP session with MPIN.

**Parameters:**
- `mpin` - 6-digit MPIN

**Returns:** `dict` with access token

---

### logout()

```python
logout() -> dict
```

Logs out and invalidates the session.

---

## Order Methods

### place_order()

```python
place_order(
    exchange_segment: str,
    product: str,
    price: str,
    order_type: str,
    quantity: str,
    validity: str,
    trading_symbol: str,
    transaction_type: str,
    amo: str = "NO",
    disclosed_quantity: str = "0",
    market_protection: str = "0",
    pf: str = "N",
    trigger_price: str = "0",
    tag: str = None,
    scrip_token: str = None,
    sot: str = None,
    slt: str = None
) -> dict
```

Places a new order. Supports regular orders, cover orders (CO), and bracket orders (BO).

**Parameters:**
| Parameter | Values | Description |
|-----------|--------|-------------|
| `exchange_segment` | NSE, BSE, NFO, BFO, CDS, BCD, MCX | Exchange |
| `product` | CNC, MIS, NRML, CO, BO | Product type |
| `price` | String | Order price ("0" for market) |
| `order_type` | L, MKT, SL, SL-M | Order type |
| `quantity` | String | Order quantity |
| `validity` | DAY, IOC | Order validity |
| `trading_symbol` | String | Symbol (e.g., "RELIANCE-EQ") |
| `transaction_type` | B, S | Buy or Sell |
| `amo` | YES, NO | After Market Order |
| `trigger_price` | String | Trigger price for SL orders |
| `tag` | String | Order tag (optional) |
| `scrip_token` | String | Instrument token (for bracket orders) |
| `sot` | String | Stop loss trigger price (for bracket orders) |
| `slt` | String | Stop loss limit price (for bracket orders) |

**Returns:** `dict` with order number `nOrdNo`

---

### modify_order()

```python
modify_order(
    order_id: str,
    price: str,
    order_type: str,
    quantity: str,
    validity: str,
    instrument_token: str = None,
    exchange_segment: str = None,
    product: str = None,
    trading_symbol: str = None,
    transaction_type: str = None,
    trigger_price: str = "0",
    dd: str = "NA",
    market_protection: str = "0",
    disclosed_quantity: str = "0",
    filled_quantity: str = "0",
    amo: str = "NO"
) -> dict
```

Modifies an existing order.

**Note:** If `instrument_token`, `exchange_segment`, `product`, and `trading_symbol` are provided, modification is faster. Otherwise, details are fetched from order book.

---

### cancel_order()

```python
cancel_order(
    order_id: str,
    amo: str = "NO",
    isVerify: bool = False
) -> dict
```

Cancels an order.

**Parameters:**
- `order_id` - Order number to cancel
- `amo` - "YES" for AMO orders
- `isVerify` - If True, checks order status before cancelling

---

### cancel_cover_order()

```python
cancel_cover_order(order_id: str) -> dict
```

Cancels a cover order.

**Parameters:**
- `order_id` - Cover order number to cancel

---

### cancel_bracket_order()

```python
cancel_bracket_order(order_id: str) -> dict
```

Cancels a bracket order.

**Parameters:**
- `order_id` - Bracket order number to cancel

---

## Portfolio Methods

### holdings()

```python
holdings() -> dict
```

Returns current portfolio holdings.

**Response fields:**
- `symbol` - Stock symbol
- `quantity` - Holding quantity
- `avgPrice` - Average buy price
- `ltp` - Last traded price
- `pnl` - Profit/Loss

---

### positions()

```python
positions() -> dict
```

Returns intraday and carryforward positions.

**Response fields:**
- `tradingSymbol` - Symbol
- `netQty` - Net quantity
- `avgPrice` - Average price
- `ltp` - Last traded price
- `pnl` - Profit/Loss

---

### limits()

```python
limits(
    segment: str = "ALL",
    exchange: str = "ALL",
    product: str = "ALL"
) -> dict
```

Returns trading limits and margins.

**Parameters:**
- `segment` - CASH, CUR, FO, ALL
- `exchange` - NSE, BSE, ALL
- `product` - CNC, MIS, NRML, ALL

---

### margin_required()

```python
margin_required(
    exchange_segment: str,
    price: str,
    order_type: str,
    product: str,
    quantity: str,
    instrument_token: str,
    transaction_type: str,
    trigger_price: str = None,
    broker_name: str = "KOTAK",
    branch_id: str = "ONLINE",
    ...
) -> dict
```

Calculates margin required for a trade.

---

## Order Reports

### order_report()

```python
order_report() -> dict
```

Returns order book with all orders for the day.

---

### order_history()

```python
order_history(order_id: str) -> dict
```

Returns history/audit trail for a specific order.

---

### trade_report()

```python
trade_report(order_id: str = None) -> dict
```

Returns executed trades. Pass `order_id` to filter.

---

## Market Data

### search_scrip()

```python
search_scrip(
    exchange_segment: str,
    symbol: str = "",
    expiry: str = None,
    option_type: str = None,
    strike_price: str = None,
    ignore_50multiple: bool = True
) -> dict
```

Searches for scrips matching criteria.

**Parameters:**
- `exchange_segment` - NSE, BSE, NFO, etc.
- `symbol` - Stock symbol to search
- `expiry` - Expiry date (YYYYMM format)
- `option_type` - CE or PE
- `strike_price` - Strike price

---

### scrip_master()

```python
scrip_master(exchange_segment: str = None) -> dict
```

Returns master list of all scrips for an exchange.

---

### quotes()

```python
quotes(
    instrument_tokens: list,
    quote_type: str = None,
    isIndex: bool = False,
    session_token: str = None,
    sid: str = None,
    server_id: str = None
) -> dict
```

Gets quotes for instruments.

**Parameters:**
- `instrument_tokens` - List of `{"exchange_segment": "nse_cm", "instrument_token": "11536"}`
- `quote_type` - ltp, ohlc, market_depth, 52w, circuit_limits, scrip_details

---

## WebSocket Methods

### subscribe()

```python
subscribe(
    instrument_tokens: list,
    isIndex: bool = False,
    isDepth: bool = False
)
```

Subscribes to live market data feed.

---

### un_subscribe()

```python
un_subscribe(
    instrument_tokens: list,
    isIndex: bool = False,
    isDepth: bool = False
)
```

Unsubscribes from market data feed.

---

### subscribe_to_orderfeed()

```python
subscribe_to_orderfeed()
```

Subscribes to real-time order updates.

---

## Callback Properties

Set these before calling WebSocket methods:

```python
client.on_message = lambda msg: print(msg)
client.on_error = lambda err: print(err)
client.on_open = lambda: print("Connected")
client.on_close = lambda: print("Disconnected")
```

---

## Helper Methods

### help()

```python
help(function_name: str = None)
```

Displays help for a function or lists all available functions.

```python
client.help()  # List all functions
client.help("place_order")  # Help for place_order
```
