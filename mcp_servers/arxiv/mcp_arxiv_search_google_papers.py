"""
# `mcp:arxiv_search_google_papers`

Search for papers on google scholar with basic filtering

---

**Parameters Schema:**

{"type":"object","properties":{"max_results":{"type":"integer","properties":{},"maximum":50},"query":{"type":"string","properties":{}},"sort_by":{"type":"string","enum":["relevance","date"],"properties":{},"default":"relevance"},"year_high":{"type":"string","description":"must not be *","properties":{},"format":"YYYY"},"year_low":{"type":"string","properties":{},"format":"YYYY"}},"required":["query"]}

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
            toolset="arxiv",
            tool_name="mcp:arxiv_search_google_papers",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
