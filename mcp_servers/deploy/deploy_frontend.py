"""
# `deploy_frontend`

Specify a directory to deploy a static site to user. The directory can be a relative path (e.g. '.'). The directory should only contain essential files, verify the files list before deploy them.
For frontend projects based on frameworks like Vue or React, first compile the project into static files, and then use this tool to deploy.
The deployment will use index.html as the main entry point. Only include necessary files for the static site (html, css, js, images, etc.)

---

**Parameters Schema:**

{"type":"object","properties":{"directory":{"type":"string","description":"the directory to deploy, it should contain an index.html as the entry point","properties":{}}},"required":["directory"]}

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
            toolset="deploy",
            tool_name="deploy_frontend",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
