"""
# `go_diagnostics`

Retrieve code diagnostics (errors and warnings) from the language server (LSP) for the current workspace.
	Note: This tool is only available for Go projects.

---

**Parameters Schema:**

{"type":"object","properties":{}}

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
            toolset="lsp",
            tool_name="go_diagnostics",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
