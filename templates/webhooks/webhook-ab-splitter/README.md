# Webhook A/B Splitter

A simple workflow that takes incoming webhook data and randomly routes it to one of two paths (50/50 split). Perfect for A/B testing different backend processes or distributing load.

## Prerequisites

- None. This workflow uses built-in nodes.

## Setup Instructions

1. Import `workflow.json` into n8n.
2. The **If** node evaluates `Math.random() >= 0.5` to split the flow.
3. Replace the "Path A" and "Path B" NoOp nodes with the actual actions you want to perform (e.g., sending to different CRMs, testing two different prompt variations with an AI node).
4. Activate the workflow and send POST requests to the Webhook URL.
