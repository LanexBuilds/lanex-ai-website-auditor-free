# Free version of AI Website Auditor.
# Full version with setup support: https://lanexbuilds.com/blueprints/ai-website-auditor

import sys
import json
import httpx
from lxml import html

def audit(url: str) -> dict:
    result = {
        "url": url,
        "ok": False,
        "scores": {"seo": 0, "conversion": 0, "trust": 0, "overall": 0},
        "findings": [],
        "summary": ""
    }

    try:
        response = httpx.get(url, timeout=12.0, follow_redirects=True)
    except httpx.RequestError as e:
        result["summary"] = f"Failed to fetch URL: {e}"
        return result

    final_url = str(response.url)

    # 1. HTTPS Check (Trust/SEO)
    is_https = final_url.startswith("https://")
    if is_https:
        result["findings"].append({"check": "HTTPS", "status": "pass", "issue": "Site uses HTTPS", "fix": ""})
    else:
        result["findings"].append({"check": "HTTPS", "status": "fail", "issue": "Site does not use HTTPS", "fix": "Enable SSL/TLS certificate for the domain"})

    try:
        tree = html.fromstring(response.content)
    except Exception as e:
        result["summary"] = f"Failed to parse HTML: {e}"
        return result

    # 2. Title Tag (SEO/Conversion)
    titles = tree.xpath("//title/text()")
    title_text = titles[0].strip() if titles else ""
    if 25 <= len(title_text) <= 65:
        result["findings"].append({"check": "Title Tag", "status": "pass", "issue": f"Title length is optimal ({len(title_text)} chars)", "fix": ""})
    else:
        result["findings"].append({"check": "Title Tag", "status": "fail", "issue": f"Title length is {len(title_text)} chars (should be 25-65)", "fix": "Adjust title tag length to be between 25 and 65 characters"})

    # 3. Meta Description (SEO/Conversion)
    meta_descs = tree.xpath('//meta[@name="description"]/@content')
    meta_desc_text = meta_descs[0].strip() if meta_descs else ""
    if 70 <= len(meta_desc_text) <= 165:
        result["findings"].append({"check": "Meta Description", "status": "pass", "issue": f"Meta description length is optimal ({len(meta_desc_text)} chars)", "fix": ""})
    else:
        result["findings"].append({"check": "Meta Description", "status": "fail", "issue": f"Meta description length is {len(meta_desc_text)} chars (should be 70-165)", "fix": "Adjust meta description length to be between 70 and 165 characters"})

    # 4. Exactly one H1 (SEO/Conversion)
    h1s = tree.xpath("//h1")
    if len(h1s) == 1:
        result["findings"].append({"check": "H1 Tag", "status": "pass", "issue": "Exactly one H1 tag found", "fix": ""})
    else:
        result["findings"].append({"check": "H1 Tag", "status": "fail", "issue": f"Found {len(h1s)} H1 tags", "fix": "Ensure there is exactly one H1 tag on the page"})

    # 5. Image Alt Text (SEO)
    images = tree.xpath("//img")
    images_without_alt = [img for img in images if not img.get("alt") or not img.get("alt").strip()]
    if not images or len(images_without_alt) == 0:
        result["findings"].append({"check": "Image Alt Text", "status": "pass", "issue": "All images have alt text", "fix": ""})
    else:
        result["findings"].append({"check": "Image Alt Text", "status": "fail", "issue": f"{len(images_without_alt)} images missing alt text", "fix": "Add descriptive alt text to all images"})

    # 6. Viewport Meta Tag (Conversion)
    viewports = tree.xpath('//meta[@name="viewport"]/@content')
    if viewports:
        result["findings"].append({"check": "Viewport Meta Tag", "status": "pass", "issue": "Viewport meta tag present", "fix": ""})
    else:
        result["findings"].append({"check": "Viewport Meta Tag", "status": "fail", "issue": "Viewport meta tag missing", "fix": "Add a viewport meta tag for mobile responsiveness"})

    # Scoring Logic
    # SEO: Title (30), Meta Desc (30), H1 (20), Alt text (20)
    seo_score = 0
    if 25 <= len(title_text) <= 65: seo_score += 30
    if 70 <= len(meta_desc_text) <= 165: seo_score += 30
    if len(h1s) == 1: seo_score += 20
    if not images or len(images_without_alt) == 0: seo_score += 20

    # Conversion: Title (20), Meta Desc (20), H1 (30), Viewport (30)
    conv_score = 0
    if 25 <= len(title_text) <= 65: conv_score += 20
    if 70 <= len(meta_desc_text) <= 165: conv_score += 20
    if len(h1s) == 1: conv_score += 30
    if viewports: conv_score += 30

    # Trust: HTTPS (100)
    trust_score = 100 if is_https else 0

    overall = int((seo_score + conv_score + trust_score) / 3)

    result["scores"]["seo"] = seo_score
    result["scores"]["conversion"] = conv_score
    result["scores"]["trust"] = trust_score
    result["scores"]["overall"] = overall

    result["ok"] = overall >= 80
    result["summary"] = f"Audit complete. Overall score: {overall}/100"

    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/auditor.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    report = audit(url)
    print(json.dumps(report, indent=2))
