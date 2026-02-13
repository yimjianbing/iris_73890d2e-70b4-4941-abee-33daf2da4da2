"""
# `copilot_diagnose`

Generate a diagnosis report for user issues by analyzing trajectory and generating insights using LLM.
This tool is more efficient and should be prioritized over reading workspace files.
diagnosis includes: Diagnosis Summary; Root Cause Analysis; Failure Classification

---

**Parameters Schema:**

{"type":"object","properties":{"query":{"type":"string","description":"your issue to diagnose, should be concise and direct - just write the problem statement directly","properties":{}}},"required":["query"]}

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
            toolset="copilot_diagnose",
            tool_name="copilot_diagnose",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
