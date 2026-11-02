# Email to Slack Notification

This simple n8n micro-template sends a Slack message whenever a new email is received.

## How it works
1. The Email Read Imap node checks an inbox for new emails.
2. The Slack node sends a message to a channel with the sender and subject of the email.

## Credentials Required
- **IMAP Account**: Required to read incoming emails.
- **Slack API Key/OAuth Token**: Required to authenticate with Slack and post messages.

## How to Import
1. Download the `workflow.json` file.
2. Open your n8n workspace.
3. In a new workflow, click the options menu (three dots) in the top right.
4. Select "Import from File" and choose the downloaded file.
