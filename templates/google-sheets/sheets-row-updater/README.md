# Sheets Row Updater

This simple n8n micro-template accepts data via a webhook and updates an existing row in a Google Sheet. It assumes the webhook payload contains the row data to update.

## Requirements
*   Google Sheets API credentials configured in n8n.

## How to Import
1. Copy the contents of `workflow.json`.
2. In n8n, go to your workspace.
3. Paste the contents directly into the workflow canvas.
4. Set up your Google Sheets credentials in the Google Sheets node and select the document and sheet you wish to update.
