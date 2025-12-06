# Installation Guide

## Prerequisites

- **Python 3.8+** is required
- **pip** package manager
- Kotak Neo API credentials (consumer key and consumer secret)

## Installation Methods

### Method 1: Local Development Installation (Recommended)

For development or to use the latest optimized version:

```bash
# Clone the repository and navigate to it
git clone https://github.com/sacbhatia/KotakAPIModule.git
cd KotakAPIModule

# Install in development mode (editable)
pip install -e .

# Or with all performance optimizations
pip install -e ".[fast]"
```

### Method 2: Install from Requirements

```bash
# Install dependencies first
pip install -r requirements.txt

# Then add the package to your Python path
```

### Method 3: Direct Installation

```bash
# Basic installation
pip install .

# With fast JSON (recommended for production)
pip install ".[fast]"

# With all extras
pip install ".[all]"
```

## Installation Options

| Option | Command | Description |
|--------|---------|-------------|
| Basic | `pip install .` | Core functionality |
| Fast | `pip install ".[fast]"` | + orjson for 3-10x faster JSON |
| Async | `pip install ".[async]"` | + aiohttp for async HTTP |
| All | `pip install ".[all]"` | All performance features |
| Dev | `pip install ".[dev]"` | + testing and linting tools |

## Dependencies

### Required Dependencies
```
requests>=2.28.0        # HTTP client
websocket-client>=1.4.0 # WebSocket support
six>=1.16.0            # Python 2/3 compatibility
urllib3>=1.26.0        # URL handling
PyJWT>=2.6.0           # JWT token handling
```

### Optional Dependencies (Recommended)
```
orjson>=3.8.0          # Fast JSON (3-10x improvement)
aiohttp>=3.8.0         # Async HTTP support
```

## Verifying Installation

```python
# Test the installation
from kotak_api_wn import NeoAPI

# Check version
import kotak_api_wn
print(f"Version: {kotak_api_wn.__version__}")

# Check if orjson is available (for best performance)
try:
    import orjson
    print("✓ orjson installed - optimal JSON performance enabled")
except ImportError:
    print("⚠ orjson not installed - using standard json module")

# Verify client can be created
client = NeoAPI(
    consumer_key="test_key",
    consumer_secret="test_secret",
    environment="uat"
)
print("✓ NeoAPI client created successfully")
```

## Troubleshooting

### Import Error: Module Not Found
```bash
# Ensure you're in the repository root directory
cd KotakAPIModule
pip install -e .
```

### Permission Denied
```bash
# Use --user flag or run as administrator
pip install --user -e .
```

### Dependency Conflicts
```bash
# Create a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
pip install -e ".[fast]"
```

### orjson Installation Issues (Windows)
```bash
# orjson requires a C compiler. If installation fails:
pip install --only-binary :all: orjson
```

## Upgrading

```bash
# Pull latest changes (if using git)
git pull

# Reinstall
pip install -e ".[fast]" --upgrade
```

## Uninstalling

```bash
pip uninstall kotak_api_wn
```

## Next Steps

After installation, see the [Usage Guide](usage.md) to get started with the API.
