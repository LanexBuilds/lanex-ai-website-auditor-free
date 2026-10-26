# Sheets Daily Summary Template

This template runs once a day, reads data from a Google Sheet, and sends a summary email.

## Requirements

* **Google Sheets Credentials:** You need to authenticate with a Google account that has access to the spreadsheet you want to read.
* **SMTP Credentials:** You need SMTP server details to send the summary email.

## How to Import

1. Copy the contents of `workflow.json`.
2. Open your n8n workspace.
3. Click "Add Workflow".
4. Click the gear icon in the top right, then select "Import from Clipboard" (or press Cmd/Ctrl + V on the workflow canvas).
