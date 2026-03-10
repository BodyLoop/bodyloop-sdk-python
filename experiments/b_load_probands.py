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

# (a) Create a client with SSL verification disabled for local IP)
client = AuthenticatedClient(
    base_url=base_url,
    verify_ssl=False,
    token=api_token,
    timeout=10.0
)

print(f"Client configured for: {base_url}")


# (b) Load probands
from functools import partial
from bodyloop_sdk.client.api.probands import get_probands_api_v2_probands_get

get_probands = partial(get_probands_api_v2_probands_get.sync, client=client)

probands = get_probands() or []
print(f"Total probands: {len(probands)}\n")

# Print first and last proband for sanity check
if probands:
    print("First proband:")
    print(probands[0])
    print("\nLast proband:")
    print(probands[-1])

import json
if probands:
    print("First proband:")
    print(json.dumps(probands[0].to_dict(), indent=2))
    print("\nLast proband:")
    print(json.dumps(probands[-1].to_dict(), indent=2))
