"""
# `analyze_video`

Understand a given video. This tool ONLY accepts video files (mp4/m4v/mpeg/mpg/mov/avi/flv/webm/wmv/3gp/wgpp)

---

**Parameters Schema:**

{"type":"object","properties":{"paths":{"type":"string","description":"the local path of video file","properties":{}},"task":{"type":"string","description":"the message to send to the LLM","properties":{}}},"required":["task","paths"]}

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
            toolset="analyze_media",
            tool_name="analyze_video",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
