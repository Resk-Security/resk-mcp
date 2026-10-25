#!/usr/bin/env python
from setuptools import setup, find_packages

# Read README.md content for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mcp-resk",
    version="0.1.4",
    author="RESK Team",
    author_email="contact@resk.fr",
    description="RESK-MCP is an open-source Python library designed to add a robust security and management layer over the official MCP Library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Resk-Security/resk-mcp",
    project_urls={
        "Homepage": "https://resk.fr/projects/resk-mcp.html",
        "Documentation": "https://resk.fr/docs/resk-mcp/",
        "Source": "https://github.com/Resk-Security/resk-mcp",
        "Bug Tracker": "https://github.com/Resk-Security/resk-mcp/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    include_package_data=True,
    # Dashboard UI assets must ship in the wheel: the dashboard resolves them
    # from resk_mcp/static at runtime.
    package_data={"resk_mcp": ["static/*.html", "static/images/*"]},
    python_requires=">=3.11",
    install_requires=[
        "fastapi>=0.115.12",
        "mcp[cli]>=1.9.0",
        "pydantic>=2.11.4",
        "pyjwt[crypto]>=2.15.0",
        "cryptography>=50.0.0",
        "aiohttp>=3.14.3",
        "python-dotenv>=1.1.0",
        "pyyaml>=6.0.2",
        "requests>=2.32.3",
        "urllib3>=2.8.0",
        "certifi>=2026.10.19",
        "slowapi>=0.1.9",
        "types-pyyaml>=6.0.12.20250516",
        "uvicorn>=0.34.2",
    ],
    extras_require={
        "dev": [
            "build>=1.2.2.post1",
            "flake8>=7.2.0",
            "mypy>=1.15.0",
            "pytest>=8.3.5",
            "pytest-asyncio>=0.26.0",
            "jsonschema>=4.17.0",
            "resk-llm>=0.5.0",
            "types-pyyaml>=6.0.12.20250516",
        ],
    },
    entry_points={
        "console_scripts": [
            "resk-mcp=resk_mcp.server:main",
        ],
    },
) 