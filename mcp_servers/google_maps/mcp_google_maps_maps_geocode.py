"""
# `mcp:google_maps_maps_geocode`

Convert an address into geographic coordinates

---

**Parameters Schema:**

{"type":"object","properties":{"address":{"type":"string","description":"The address to geocode","properties":{}}},"required":["address"]}

"""
import os
import sys
import site
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    payload_json = " ".join(sys.argv[1:])
    try:
        result = call_aime_tool(
            toolset="google_maps",
            tool_name="mcp:google_maps_maps_geocode",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
