# AI Sentiment Analyzer

A micro-automation that accepts text via a webhook, uses OpenAI to determine the sentiment (Positive, Negative, or Neutral), and outputs the result.

## Prerequisites

- **OpenAI API Key**: You will need an active OpenAI account with API credits to run the sentiment analysis.

## Setup Instructions

1. Create a new workflow in n8n.
2. Click **Import from File** or copy the raw JSON from `workflow.json` and paste it into the editor.
3. Select or create your OpenAI API credentials in the OpenAI node.
4. Activate the workflow or click "Test step" on the Webhook node and send a POST request with `{ "text": "I love this product!" }` to test it.
