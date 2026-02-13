"""
# `mcp:yfinance_architjn-slash-yahoo-finance`

This tool calls the Actor "architjn/yahoo-finance" and retrieves its output results.
Use this tool instead of the "call-actor" if user requests this specific Actor.
Actor description: Effortlessly fetch comprehensive financial data, historical prices, news, and analytics for any stock ticker from Yahoo Finance. Perfect for investors, analysts, and developers seeking fast, reliable, and detailed market insights in one click!

---

**Parameters Schema:**

{"type":"object","properties":{"end_date":{"type":"string","description":"(Optional) End date for historical data in YYYY-MM-DD format.","properties":{}},"start_date":{"type":"string","description":"(Optional) Start date for historical data in YYYY-MM-DD format.","properties":{}},"tickers":{"type":"array","description":"**REQUIRED** Array of ticker symbols (e.g., [\"AAPL\", \"GOOG\"]).\nExample values: [\"AAPL\",\"GOOG\",\"MSFT\"]","properties":{},"items":{"type":"string","description":"**REQUIRED** Array of ticker symbols (e.g., [\"AAPL\", \"GOOG\"]).","properties":{}}}},"required":["tickers"]}

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
            toolset="yfinance",
            tool_name="mcp:yfinance_architjn-slash-yahoo-finance",
            parameters=json.loads(payload_json),
            response_format="text",
        )
        print(result.result)
    except Exception as e:
        print(e)
        sys.exit(1)
