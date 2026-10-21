# Webhook to Google Sheets

A simple workflow that receives incoming data via a webhook and automatically appends it as a new row in a specified Google Sheet. Ideal for logging form submissions, lead generation data, or system alerts.

## Prerequisites

- **Google Sheets Credentials**: You need to authenticate n8n with your Google account via OAuth2 or a Service Account.

## Setup Instructions

1. Import `workflow.json` into your n8n instance.
2. In the **Google Sheets** node, set up your authentication.
3. Update the `documentId` and `sheetName` in the Google Sheets node to point to your specific spreadsheet. Ensure your sheet has headers that match the incoming JSON keys from the Webhook.
4. Activate the workflow and point your data source to the Webhook URL.
