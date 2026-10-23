# Email to Slack

This n8n micro-template triggers when a new email is received and sends a notification to a Slack channel with the sender's address and email subject.

## Credentials Needed
- **IMAP credentials**: Requires IMAP credentials configured in n8n to read emails.
- **Slack API**: Requires a Slack account and a Bot Token (or OAuth integration) with permissions to post in the desired channel.

## How to Import
1. Copy the contents of `workflow.json`.
2. In your n8n workspace, create a new workflow.
3. Paste the contents directly into the workflow editor.
4. Set up your IMAP credentials in the "Email Read Imap" node.
5. Set up your Slack credentials in the "Slack" node.
6. Update the Slack channel name if necessary.
