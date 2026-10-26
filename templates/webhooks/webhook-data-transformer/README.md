# Webhook Data Transformer Template

This template receives data via a POST Webhook, transforms the data using a simple Code node, and forwards it to another endpoint using an HTTP Request.

## Requirements

* No special credentials are required for basic usage. You will need to provide the target URL in the HTTP Request node.

## How to Import

1. Copy the contents of `workflow.json`.
2. Open your n8n workspace.
3. Click "Add Workflow".
4. Click the gear icon in the top right, then select "Import from Clipboard" (or press Cmd/Ctrl + V on the workflow canvas).
