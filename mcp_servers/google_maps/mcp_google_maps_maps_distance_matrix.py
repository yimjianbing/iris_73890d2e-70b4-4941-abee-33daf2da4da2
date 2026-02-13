"""
# `mcp:google_maps_maps_distance_matrix`

Calculate travel distance and time for multiple origins and destinations

---

**Parameters Schema:**

{"type":"object","properties":{"destinations":{"type":"array","description":"Array of destination addresses or coordinates","properties":{},"items":{"type":"string","properties":{}}},"mode":{"type":"string","description":"Travel mode (driving, walking, bicycling, transit)","enum":["driving","walking","bicycling","transit"],"properties":{}},"origins":{"type":"array","description":"Array of origin addresses or coordinates","properties":{},"items":{"type":"string","properties":{}}}},"required":["origins","destinations"]}

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
            tool_name="mcp:google_maps_maps_distance_matrix",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
