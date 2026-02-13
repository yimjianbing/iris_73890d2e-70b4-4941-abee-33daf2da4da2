"""
# `mcp:codebase_CountUserActivities`

Count user activities by date range.
It returns the count of user activities within the specified date range.

---

**Parameters Schema:**

{"type":"object","properties":{"EndDate":{"type":"string","description":"Optional. End date (YYYY-MM-DD format). If StartDate and EndDate are not both provided, use now.","properties":{}},"StartDate":{"type":"string","description":"Optional. Start date (YYYY-MM-DD format). If StartDate and EndDate are not both provided, use now-365days.","properties":{}},"TenantId":{"type":"string","description":"Optional. Tenant ID. If Username and TenantId are not provided, use self.","properties":{}},"Username":{"type":"string","description":"Optional. Username. If Username and TenantId are not provided, use self.","properties":{}}}}

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
            tool_name="mcp:codebase_CountUserActivities",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
