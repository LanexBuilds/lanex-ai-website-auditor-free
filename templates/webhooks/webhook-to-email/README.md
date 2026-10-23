# Webhook to Email

This n8n micro-template triggers when a webhook is received and sends an email containing the webhook payload.

## Credentials Needed
- **SMTP credentials**: Requires SMTP credentials configured in n8n to send the email.

## How to Import
1. Copy the contents of `workflow.json`.
2. In your n8n workspace, create a new workflow.
3. Paste the contents directly into the workflow editor.
4. Set up your SMTP credentials in the "Send Email" node.
5. Update the "From" and "To" email addresses.
6. Save and activate the workflow to generate the webhook URL.
