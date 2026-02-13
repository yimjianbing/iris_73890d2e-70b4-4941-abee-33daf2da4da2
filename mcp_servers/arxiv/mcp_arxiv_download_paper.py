"""
# `mcp:arxiv_download_paper`

Download an arxiv paper(pdf) and create a converted markdown for it, support multiple inputs

---

**Parameters Schema:**

{"type":"object","properties":{"check_status":{"type":"boolean","description":"If true, only check conversion status without downloading","properties":{},"default":false},"paper_ids":{"type":"array","description":"The arXiv ID list of the paper to download","properties":{},"items":{"type":"string","properties":{}}},"pdf_urls":{"type":"array","description":"The URL of the paper's PDF to download","properties":{},"items":{"type":"string","properties":{}}}}}

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
            tool_name="mcp:arxiv_download_paper",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
