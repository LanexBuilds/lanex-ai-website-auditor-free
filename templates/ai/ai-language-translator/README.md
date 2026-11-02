# AI Language Translator

This simple n8n micro-template translates input text to Spanish using OpenAI.

## How it works
1. A Webhook receives a GET request with a `text` query parameter.
2. The OpenAI node translates the provided text into Spanish.

## Credentials Required
- **OpenAI API Key**: Required to use the OpenAI chat completion endpoint.

## How to Import
1. Download the `workflow.json` file.
2. Open your n8n workspace.
3. In a new workflow, click the options menu (three dots) in the top right.
4. Select "Import from File" and choose the downloaded file.
