# Webhook Data Formatter

This simple n8n micro-template receives data via a webhook, modifies and formats the data using a JavaScript Code node, and then sends the formatted data to a target URL via an HTTP POST request.

## Requirements
*   No specific external credentials are required, but you need to know the target URL for the HTTP request.

## How to Import
1. Copy the contents of `workflow.json`.
2. In n8n, go to your workspace.
3. Paste the contents directly into the workflow canvas.
4. Modify the Code node logic to fit your data formatting needs.
5. Update the HTTP Request node with your target URL.
