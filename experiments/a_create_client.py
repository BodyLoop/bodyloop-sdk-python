#!/usr/bin/env python3

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the src directory (src-layout project) so `bodyloop_sdk` can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from bodyloop_sdk.client import AuthenticatedClient

base_url = os.getenv("BODYLOOP_BASE_URL")
api_token = os.getenv("BODYLOOP_API_TOKEN")

# Create a client with SSL verification disabled for local IP
# Note: In production, you should use proper SSL certificates
client = AuthenticatedClient(
    base_url=base_url,
    verify_ssl=False,
    token=api_token,
    timeout=10.0
)

print(f"Client configured for: {base_url}")
