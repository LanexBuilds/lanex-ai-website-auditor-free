# Slack Daily Quote

This simple n8n micro-template sends a random daily quote to a Slack channel.

## How it works
1. A Schedule Trigger fires every day.
2. An HTTP Request fetches a random quote from a public API.
3. The Slack node posts the quote to a designated channel.

## Credentials Required
- **Slack API Key/OAuth Token**: Required to authenticate with Slack and post messages.

## How to Import
1. Download the `workflow.json` file.
2. Open your n8n workspace.
3. In a new workflow, click the options menu (three dots) in the top right.
4. Select "Import from File" and choose the downloaded file.
