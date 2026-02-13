"""
# `create_merge_request_comment`

create comments in a codebase MR, result will contain message, all comments, published count and ignore counts. You should use user preferred locale to generate the comments.

---

**Parameters Schema:**

{"type":"object","properties":{"comments":{"type":"array","description":"required, comments list to create","properties":{},"items":{"type":"object","properties":{"accuracy":{"type":"integer","description":"accuracy of the comment.","properties":{}},"base_commit_id":{"type":"string","description":"base commit id of the merge request.","properties":{}},"code_line_content":{"type":"string","description":"one of the most related code line content of the comment.","properties":{}},"confidence_score":{"type":"number","description":"Confidence score of the comment (0-1.0).","properties":{}},"end_column":{"type":"integer","description":"File position: end column, starting from 1, inclusive, optional.","properties":{}},"end_line":{"type":"integer","description":"File position: end line, starting from 1, inclusive.","properties":{}},"file_path":{"type":"string","description":"File position: file path.","properties":{}},"improvement_example_code":{"type":"string","description":"The code to fix the issue, must be in the same language as the original. Use standard JSON string escaping. Do NOT double-escape or wrap with extra quotes.","properties":{}},"improvement_example_description":{"type":"string","description":"Description of the improvement example. Use user preferred locale to generate the description.","properties":{}},"issue_description":{"type":"string","description":"Description of the issue. Use user preferred locale to generate the description.","properties":{}},"locale":{"type":"string","description":"Locale of the comment, default is zh-CN.","properties":{}},"priority":{"type":"integer","description":"Priority of the comment","properties":{}},"side":{"type":"string","description":"File position: comment on the old side or new side of the merge request diff, default is new.","properties":{}},"source_commit_id":{"type":"string","description":"source commit id of the merge request.","properties":{}},"start_column":{"type":"integer","description":"File position: start column, starting from 1, optional.","properties":{}},"start_line":{"type":"integer","description":"File position: start line, starting from 1.","properties":{}}},"required":["issue_description","improvement_example_description","improvement_example_code","priority","locale","side","file_path","confidence_score","start_line","end_line","base_commit_id","source_commit_id"]}},"draft":{"type":"boolean","description":"optional, whether to create the comment as a draft (invisible to others), default is false","properties":{}},"number":{"type":"integer","description":"required, the number of the merge request","properties":{}},"repo_name":{"type":"string","description":"required, codebase repo name, eg group/repo","properties":{}}},"required":["repo_name","number","comments"]}

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
            tool_name="create_merge_request_comment",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
