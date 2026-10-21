# Scheduled Slack Message

A micro-automation that sends a predefined message to a specific Slack channel on a regular schedule (e.g., daily standup reminders, weekly updates).

## Prerequisites

- **Slack Credentials**: You will need to authenticate n8n with your Slack workspace (either via OAuth2 or a Bot Token).

## Setup Instructions

1. Import the `workflow.json` into n8n.
2. In the **Schedule Trigger** node, configure how often you want the message to be sent (e.g., Every Day at 9:00 AM).
3. In the **Slack** node, set up your credentials.
4. Update the `channel` parameter to the name of your target channel (e.g., `general` or `#team-updates`).
5. Update the `text` parameter with your desired message.
6. Activate the workflow.
