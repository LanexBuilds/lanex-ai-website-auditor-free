# Webhook to Google Sheet

This simple n8n micro-template adds a new row to a Google Sheet whenever a webhook is triggered.

## How it works
1. A Webhook receives a POST request with payload data.
2. The Google Sheets node appends the payload data to a specified Google Sheet.

## Credentials Required
- **Google Sheets OAuth2/Service Account**: Required to authenticate with Google Sheets and write data.

## How to Import
1. Download the `workflow.json` file.
2. Open your n8n workspace.
3. In a new workflow, click the options menu (three dots) in the top right.
4. Select "Import from File" and choose the downloaded file.
