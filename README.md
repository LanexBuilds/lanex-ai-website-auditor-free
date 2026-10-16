# AI Website Auditor — Free Version

> **Want the full version with setup support?** → [Get the blueprint](https://lanexbuilds.com/blueprints/ai-website-auditor?utm_source=github&utm_medium=repo&utm_campaign=ai-website-auditor-free)

## What it does
Point it at any URL. Get a scored report: SEO, conversion, trust.

## Architecture
URL → httpx fetch → lxml parse → run checks → score → JSON output

## Installation
git clone this repo
pip install -r requirements.txt

## Usage
python src/auditor.py https://example.com

## What it checks
- HTTPS and redirect
- Title tag length
- Meta description length
- Exactly one H1
- Image alt text
- Viewport meta tag

## Limitations
This is the free version. It checks 7 things. The paid version checks 40+, includes AI-written fixes, and generates a PDF report.

## Need help setting this up?

The free version works on its own. If you want it running against your own site with a full report — I do setup sessions.

→ [Book a 15-min audit](https://lanexbuilds.com/book-audit?utm_source=github&utm_medium=repo&utm_campaign=ai-website-auditor-free)

→ [See all blueprints](https://lanexbuilds.com/blueprints?utm_source=github&utm_medium=repo&utm_campaign=ai-website-auditor-free)

## License
MIT