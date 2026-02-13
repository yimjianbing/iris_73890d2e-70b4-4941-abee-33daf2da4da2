"""
# `mcp:SlardarApp_get_event_log`

获取issue下某个event上报时的原始日志

---

**Parameters Schema:**

{"type":"object","properties":{"crash_time":{"type":"string","properties":{}},"device_id":{"type":"string","properties":{}},"event_id":{"type":"string","properties":{}},"slardar_link":{"type":"string","properties":{},"format":"uri"}},"required":["slardar_link","event_id","device_id","crash_time"]}

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
            toolset="SlardarApp",
            tool_name="mcp:SlardarApp_get_event_log",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
