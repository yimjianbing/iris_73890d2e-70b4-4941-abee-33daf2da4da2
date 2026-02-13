"""
# `mcp:codebase_ListMergeRequestCheckRuns`

List check runs for a merge request.

---

**Parameters Schema:**

{"type":"object","properties":{"Number":{"type":"integer","description":"The number of the merge request.","properties":{}},"PageNumber":{"type":"integer","description":"Pagination number, starts from 1.","properties":{}},"PageSize":{"type":"integer","description":"Pagination size. Maximum 100, default is 10.","properties":{}},"RepoId":{"type":"string","description":"The ID or path (e.g. path/to/repo) of the repository.","properties":{}},"Unsuccessful":{"type":"boolean","description":"`true` means filter unsuccessful check runs (pending, running, failed, warning, etc.). Default is `false`.","properties":{}}},"required":["RepoId","Number","Unsuccessful","PageNumber","PageSize"]}

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
            tool_name="mcp:codebase_ListMergeRequestCheckRuns",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
