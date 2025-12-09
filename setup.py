"""
Kotak API WN - Optimized Kotak Neo Trading API Client
Setup configuration for the package.
"""

from setuptools import setup, find_packages
import os

# Read version from package __init__.py
def get_version():
    init_path = os.path.join(os.path.dirname(__file__), 'kotak_api_wn', '__init__.py')
    with open(init_path, 'r') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[1].strip().strip('"').strip("'")
    return '1.0.0'

# Read README for long description
def get_long_description():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

setup(
    name='kotak_api_wn',
    version=get_version(),
    author='wavenodes',
    author_email='',
    description='High-performance Kotak Neo Trading API Client with optimized latency',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/wavenodes/KotakAPIModule',
    packages=find_packages(exclude=['tests', 'tests.*', 'docs', 'docs.*']),
    package_data={
        'kotak_api_wn': ['api/*.csv'],
    },
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=[
        'requests>=2.28.0',
        'websocket-client>=1.4.0',
        'six>=1.16.0',
        'urllib3>=1.26.0',
        'PyJWT>=2.6.0',
        'bidict>=0.22.1',
        'numpy>=2.1.0',
        'pyjsparser>=2.7.1',
        'python-dotenv>=1.0.0',
        'websockets>=8.1',
        'pandas>=2.2.3',
    ],
    extras_require={
        'fast': [
            'orjson>=3.8.0',  # 3-10x faster JSON serialization
        ],
        'async': [
            'aiohttp>=3.8.0',  # Async HTTP support
        ],
        'all': [
            'orjson>=3.8.0',
            'aiohttp>=3.8.0',
        ],
        'dev': [
            'pytest>=7.0.0',
            'pytest-asyncio>=0.20.0',
            'pytest-benchmark>=4.0.0',
            'black>=22.0.0',
            'isort>=5.10.0',
            'mypy>=0.990',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=[
        'kotak', 'neo', 'trading', 'api', 'stock', 'market',
        'finance', 'investment', 'broker', 'low-latency', 'hft'
    ],
    project_urls={
        'Documentation': 'https://github.com/wavenodes/KotakAPIModule/tree/master/kotak_api_wn/docs',
        'Source': 'https://github.com/wavenodes/KotakAPIModule',
        'Bug Reports': 'https://github.com/wavenodes/KotakAPIModule/issues',
    },
)
