# Kotak API WN - High-Performance Trading API Client

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A high-performance, optimized Python client for the Kotak Neo Trading API v2. This library is designed for low-latency trading applications with significant performance improvements over the standard client.

## ✨ Features

- **3-10x Faster JSON Processing** - Uses `orjson` for serialization/deserialization
- **Connection Pooling** - Persistent HTTP connections reduce latency
- **API Instance Caching** - Reduces object instantiation overhead
- **Optimized Data Structures** - Frozensets for O(1) membership testing
- **WebSocket Support** - Real-time market data and order feeds
- **Full API Coverage** - Orders, positions, holdings, margins, and more
- **TOTP Authentication** - Secure time-based one-time password support
- **Bracket Orders** - Advanced order types with stop loss and target
- **API v2 Support** - Latest Kotak Neo API endpoints and features

## 🚀 Quick Start

```python
from kotak_api_wn import NeoAPI

# Initialize the client
client = NeoAPI(
    consumer_key="your_consumer_key",
    environment="prod"  # or "uat" for testing
)

# Login with TOTP (recommended)
client.totp_login(
    mobile_number="9876543210",
    ucc="your_ucc",
    totp="123456"  # From authenticator app
)

# Validate with MPIN
client.totp_validate(mpin="123456")

# Place an order
response = client.place_order(
    exchange_segment="NSE",
    product="MIS",
    price="0",
    order_type="MKT",
    quantity="1",
    validity="DAY",
    trading_symbol="RELIANCE-EQ",
    transaction_type="B"
)
print(response)
```

## 📦 Installation

### From GitHub (v2 - Recommended)
```bash
# Install v2 branch directly from GitHub
pip install git+https://github.com/wavenodes/KotakAPIModule.git@v2

# With performance optimizations (recommended)
pip install "git+https://github.com/wavenodes/KotakAPIModule.git@v2#egg=kotak_api_wn[fast]"
```

### Local Development
```bash
# Clone v2 branch
git clone -b v2 https://github.com/wavenodes/KotakAPIModule.git
cd KotakAPIModule

# Install in editable mode
pip install -e ".[fast]"
```

### Installation Options
- **Basic**: `pip install -e .`
- **Fast** (recommended): `pip install -e ".[fast]"` - Includes orjson for 9x faster JSON
- **Full**: `pip install -e ".[all]"` - All features

## 📊 Performance Improvements

| Operation | Original | Optimized | Improvement |
|-----------|----------|-----------|-------------|
| JSON Serialization | ~20.5μs | ~2.3μs | **9.0x faster** |
| JSON Deserialization | ~15.1μs | ~5.5μs | **2.7x faster** |
| WebSocket Lookups | ~327μs | ~12.2μs | **26.8x faster** |
| API Instance Caching | ~1.0μs | ~0.5μs | **2.1x faster** |
| Regex Pre-compilation | ~6.2μs | ~3.2μs | **1.9x faster** |
| Validation (Frozenset) | ~23.3μs | ~14.9μs | **1.6x faster** |
| HTTP Session Pooling | ~1089μs | ~831μs | **1.3x faster** |

## 📖 Documentation

- [Installation Guide](kotak_api_wn/docs/install.md)
- [Usage Guide](kotak_api_wn/docs/usage.md)
- [Performance Improvements](kotak_api_wn/docs/improvements.md)
- [API Reference](kotak_api_wn/docs/api.md)

## 🔧 Requirements

- Python 3.8+
- `requests>=2.28.0`
- `websocket-client>=1.4.0`
- `PyJWT>=2.6.0`
- `orjson>=3.8.0` (optional, for best performance)

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

## ⚠️ Disclaimer

This software is a modified version of the original Kotak Neo API client, optimized for performance in a few high-impact areas including JSON serialization, HTTP connection pooling, API instance caching, and validation lookups. The original code belongs to **Kotak Securities** and can be found at:

🔗 **Original Repository:** [https://github.com/Kotak-Neo/kotak-neo-api](https://github.com/Kotak-Neo/kotak-neo-api)

This is an unofficial modification and is not affiliated with or endorsed by Kotak Securities.
