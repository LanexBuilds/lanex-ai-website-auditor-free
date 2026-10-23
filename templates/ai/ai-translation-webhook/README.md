# AI Translation Webhook

This n8n micro-template accepts text via a webhook, translates it to Spanish using OpenAI, and returns the translated text.

## Credentials Needed
- **OpenAI API**: Requires an OpenAI API Key.

## How to Import
1. Copy the contents of `workflow.json`.
2. In your n8n workspace, create a new workflow.
3. Paste the contents directly into the workflow editor.
4. Set up your OpenAI API credentials.
5. Save the workflow and activate it to get the test/production webhook URL.
6. Post JSON data to the webhook like `{"text": "Hello world"}`.
