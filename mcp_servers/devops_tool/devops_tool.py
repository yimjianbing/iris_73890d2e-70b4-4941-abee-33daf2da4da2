"""
# `devops_tool`

Intelligent DevOps Agent Tool with automatic operation routing based on project type and user intent.

### Task Type

**ALWAYS use task="verify"** - the system automatically determines the appropriate operation.

### Required Parameters

**Basic:**
- task: "verify" (always)
- codebase_repo: Repository in format {namespace}/{repo} (e.g., "cld/my-project")

**User Intent (MUST analyze user query and set these flags):**
- mentions_build: true if user mentions build/编译/构建
- mentions_deploy: true if user mentions deploy/部署
- mentions_tce: true if user mentions TCE/后端部署
- mentions_bits: true if user mentions Bits client build/客户端构建
- mentions_codebase_ci: true if user mentions Codebase CI/流水线

**Optional (system can infer from deployment history):**
- branch: Git branch name
- env: Environment lane (e.g., "ppe_staging", "boe_test")
- psm: Backend service PSM identifier

**Task-Specific (when needed):**
- bits_template_id: Required when mentions_bits=true
- bits_params: Build parameters (empty {} if not specified)
- yaml_filename: Required when mentions_codebase_ci=true
- yaml_inputs: Input parameters (empty {} if not specified)

### Usage Examples

**1. Simple Build:**
```json
{
  "task": "verify",
  "codebase_repo": "myteam/myproject",
  "mentions_build": true
}
```

**2. Backend Deploy (system infers PSM and env from history):**
```json
{
  "task": "verify",
  "codebase_repo": "backend/api-service",
  "mentions_deploy": true,
  "mentions_tce": true
}
```

**3. Build and Deploy Together:**
```json
{
  "task": "verify",
  "codebase_repo": "backend/api",
  "branch": "main",
  "mentions_build": true,
  "mentions_deploy": true,
  "mentions_tce": true
}
```

**4. Bits Client Build:**
```json
{
  "task": "verify",
  "codebase_repo": "mobile/android-app",
  "branch": "develop",
  "mentions_bits": true,
  "bits_template_id": 12345,
  "bits_params": {}
}
```

**5. Codebase CI:**
```json
{
  "task": "verify",
  "codebase_repo": "backend/service",
  "branch": "main",
  "mentions_codebase_ci": true,
  "yaml_filename": ".ci/pipeline.yaml",
  "yaml_inputs": {}
}
```

The tool automatically detects project type, infers missing parameters from deployment history, and routes to the optimal operation.

---

**Parameters Schema:**

{"type":"object","properties":{"api_targets":{"type":"array","description":"List of API targets to test. Leave empty to test all APIs in the PSM","properties":{},"items":{"type":"object","properties":{"func_name":{"type":"string","description":"Function name for testing","properties":{}},"http_method":{"type":"string","description":"HTTP method for testing","properties":{}},"http_path":{"type":"string","description":"HTTP path for testing","properties":{}}}}},"bits_params":{"type":"object","description":"Additional parameters for BITS client build (optional)","properties":{}},"bits_template_id":{"type":"integer","description":"BITS template ID (required for bits_client_build task)","properties":{}},"branch":{"type":"string","description":"The branch to build from (default: master)","properties":{}},"codebase_ci_job_name":{"type":"string","description":"Optional job name filter for Codebase CI; when set, only monitor this job after triggering the pipeline","properties":{}},"codebase_commit_sha":{"type":"string","description":"Commit SHA for reusing existing Codebase CI pipeline runs by commit","properties":{}},"codebase_repo":{"type":"string","description":"The codebase repository in format {namespace}/{repo}, e.g., cld/bits-ai-showcase","properties":{}},"env":{"type":"string","description":"Environment/lane for both TCE deployment and API testing. Optional for TCE deploy (generates random ppe_/boe_ if empty). Required for standalone API testing","properties":{}},"env_type":{"type":"string","description":"Environment type for TCE deployment when env is not provided. 'ppe' generates ppe_xxx, 'boe' generates boe_xxx. Ignored if env is provided","properties":{}},"env_url":{"type":"string","description":"Env URL directly from user query. Format: https://bits.bytedance.net/env/life/{env_type}/{region_name}/detail/{env_name}/service","properties":{}},"goofy_app_id":{"type":"string","description":"Goofy App ID for frontend composite","properties":{}},"goofy_channel_id":{"type":"integer","description":"Goofy Channel ID for direct deployment (skips channel creation)","properties":{}},"is_online":{"type":"boolean","description":"Whether to use online environment. Used for API testing and to determine env_type when both env and env_type are not provided. true=ppe, false=boe. Default is false","properties":{}},"mentions_bits":{"type":"boolean","description":"User mentions Bits/客户端构建 (for verify task)","properties":{}},"mentions_build":{"type":"boolean","description":"User mentions build/编译/构建 (for verify task)","properties":{}},"mentions_codebase_ci":{"type":"boolean","description":"User mentions Codebase CI/流水线 (for verify task)","properties":{}},"mentions_deploy":{"type":"boolean","description":"User mentions deploy/部署 (for verify task)","properties":{}},"mentions_goofy":{"type":"boolean","description":"User mentions Goofy/前端部署 (for verify task)","properties":{}},"mentions_tce":{"type":"boolean","description":"User mentions TCE/后端部署 (for verify task)","properties":{}},"psm":{"type":"string","description":"The PSM (Platform Service Management) identifier for both TCE deployment and API testing","properties":{}},"scm_repo":{"type":"string","description":"The SCM repository in format {a}/{b}/{c} or {a}/{b}/{c}/{d} (at least 3 parts), e.g., bits/ai/showcase or web/frontend/app/12345","properties":{}},"scm_version":{"type":"string","description":"The SCM version for deployment (only required when using deploy alone)","properties":{}},"task":{"type":"string","description":"The development task to perform: build, deploy, build_and_deploy, api_test, full_workflow, or pipeline","properties":{}},"yaml_filename":{"type":"string","description":"YAML config file path for Codebase CI (required for codebase_ci task)","properties":{}},"yaml_inputs":{"type":"object","description":"Input parameters for Codebase CI (optional)","properties":{}}},"required":["task","codebase_repo","scm_repo","branch","psm","scm_version","env","env_type","api_targets"]}

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
            toolset="devops_tool",
            tool_name="devops_tool",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
