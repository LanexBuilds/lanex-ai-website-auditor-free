# Schedule to Sheets

This n8n micro-template triggers on a schedule and appends a row (e.g., a timestamp) to a Google Sheet.

## Credentials Needed
- **Google Sheets API**: Requires Google OAuth2 credentials or a Service Account configured in n8n.

## How to Import
1. Copy the contents of `workflow.json`.
2. In your n8n workspace, create a new workflow.
3. Paste the contents directly into the workflow editor.
4. Set up your Google Sheets credentials.
5. Select the Document (Spreadsheet) and Sheet you want to append data to in the "Google Sheets" node.
