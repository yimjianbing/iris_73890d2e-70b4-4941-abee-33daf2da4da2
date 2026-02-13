"""
# `mcp:meego_get_workflow_detail`

Retrieve workflow details for a Meego work item, including nodes and transitions, the fields in nodes are mandatory to transfer next state, if not sure what option or value to fill, check with `get_work_item_metadata` tool for specific filed_key

---

**Parameters Schema:**

{"type":"object","properties":{"flow_type":{"type":"integer","description":"Optional, workflow type (0 for node flow like story, 1 for state flow like issue)","properties":{}},"simple_name":{"type":"string","description":"Required, workspace name","properties":{}},"work_item_id":{"type":"integer","description":"Required, work item ID","properties":{}},"work_item_type_key":{"type":"string","description":"Required, work item type key (e.g., story, issue)","properties":{}}},"required":["simple_name","work_item_type_key","work_item_id","flow_type"]}

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
            toolset="meego",
            tool_name="mcp:meego_get_workflow_detail",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
