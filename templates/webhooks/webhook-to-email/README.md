# Webhook to Email

This simple n8n micro-template sends an email notification whenever a webhook is triggered.

## How it works
1. A Webhook receives a POST request with payload data.
2. The Send Email node dispatches an email containing the webhook payload data.

## Credentials Required
- **SMTP Account**: Required to authenticate and send the email.

## How to Import
1. Download the `workflow.json` file.
2. Open your n8n workspace.
3. In a new workflow, click the options menu (three dots) in the top right.
4. Select "Import from File" and choose the downloaded file.
