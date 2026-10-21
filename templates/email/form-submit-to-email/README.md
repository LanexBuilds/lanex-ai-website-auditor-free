# Form Submit to Email

A simple workflow that receives data from a contact form submission (via Webhook) and sends an email notification with the submission details.

## Prerequisites

- **SMTP Credentials**: You need an active email account (like Gmail, Sendgrid, etc.) that can send emails via SMTP to configure the Email node.

## Setup Instructions

1. Import the `workflow.json` into n8n.
2. In the **Send Email** node, set up your SMTP credentials.
3. Update the `fromEmail` and `toEmail` fields in the Send Email node to match your addresses.
4. Update your frontend form to send POST requests to the generated Webhook URL with JSON payload containing `name`, `email`, and `message`.
5. Activate the workflow.
