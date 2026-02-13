"""
# `mcp:google_maps_maps_search_places`

Search for places using Google Places API

---

**Parameters Schema:**

{"type":"object","properties":{"location":{"type":"object","description":"Optional center point for the search","properties":{"latitude":{"type":"number","properties":{}},"longitude":{"type":"number","properties":{}}}},"query":{"type":"string","description":"Search query","properties":{}},"radius":{"type":"number","description":"Search radius in meters (max 50000)","properties":{}}},"required":["query"]}

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
            tool_name="mcp:google_maps_maps_search_places",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
