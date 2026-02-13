"""
# `mcp:arxiv_read_paper`

Read the full content of a stored arxiv paper in markdown format

---

**Parameters Schema:**

{"type":"object","properties":{"paper_id":{"type":"string","description":"The arXiv ID or google paper filename (for example, test is the name 'https://xxx/test.pdf') of the paper to read","properties":{}}},"required":["paper_id"]}

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
            tool_name="mcp:arxiv_read_paper",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
