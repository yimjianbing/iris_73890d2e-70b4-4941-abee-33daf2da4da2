"""
# `mcp:yfinance_get-actor-output`

Retrieve the output dataset items of a specific Actor run using its datasetId.
You can select specific fields to return (supports dot notation like "crawl.statusCode") and paginate results with offset and limit.
This tool is a simplified version of the get-dataset-items tool, focused on Actor run outputs.

The results will include the dataset items from the specified dataset. If you provide fields, only those fields will be included (nested fields supported via dot notation).

You can obtain the datasetId from an Actor run (e.g., after calling an Actor with the call-actor tool) or from the Apify Console (Runs → Run details → Dataset ID).

USAGE:
- Use when you need to read Actor output data (full items or selected fields), especially when preview does not include all fields.

USAGE EXAMPLES:
- user_input: Get data of my last Actor run
- user_input: Get number_of_likes from my dataset
- user_input: Return only crawl.statusCode and url from dataset aab123

Note: This tool is automatically included if the Apify MCP Server is configured with any Actor tools (e.g., "apify-slash-rag-web-browser") or tools that can interact with Actors (e.g., "call-actor", "add-actor").

---

**Parameters Schema:**

{"type":"object","properties":{"datasetId":{"type":"string","description":"Actor output dataset ID to retrieve from.","properties":{},"minLength":1},"fields":{"type":"string","description":"Comma-separated list of fields to include (supports dot notation like \"crawl.statusCode\"). For example: \"crawl.statusCode,text,metadata\"","properties":{}},"limit":{"type":"number","description":"Maximum number of items to return (default: 100).","properties":{},"default":100},"offset":{"type":"number","description":"Number of items to skip (default: 0).","properties":{},"default":0}},"required":["datasetId","offset","limit"]}

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
            toolset="yfinance",
            tool_name="mcp:yfinance_get-actor-output",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
