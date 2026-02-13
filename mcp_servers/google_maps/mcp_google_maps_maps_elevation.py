"""
# `mcp:google_maps_maps_elevation`

Get elevation data for locations on the earth

---

**Parameters Schema:**

{"type":"object","properties":{"locations":{"type":"array","description":"Array of locations to get elevation for","properties":{},"items":{"type":"object","properties":{"latitude":{"type":"number","properties":{}},"longitude":{"type":"number","properties":{}}},"required":["latitude","longitude"]}}},"required":["locations"]}

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
            tool_name="mcp:google_maps_maps_elevation",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
