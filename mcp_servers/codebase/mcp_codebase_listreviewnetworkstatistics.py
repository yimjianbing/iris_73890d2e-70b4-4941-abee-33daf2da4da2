"""
# `mcp:codebase_ListReviewNetworkStatistics`

List review network statistics.
It returns the review network statistics based on the specified criteria.
Use self as author if both author and reviewer are empty.

---

**Parameters Schema:**

{"type":"object","properties":{"AuthorId":{"type":"string","description":"Optional. ID of the author to filter by.","properties":{}},"AuthorUsername":{"type":"string","description":"Optional. Username of the author to filter by.","properties":{}},"ReviewerId":{"type":"string","description":"Optional. ID of the reviewer to filter by.","properties":{}},"ReviewerUsername":{"type":"string","description":"Optional. Username of the reviewer to filter by.","properties":{}},"TopN":{"type":"integer","description":"Optional. Number of top results to return. Default 3.","properties":{}}}}

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
            toolset="codebase",
            tool_name="mcp:codebase_ListReviewNetworkStatistics",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
