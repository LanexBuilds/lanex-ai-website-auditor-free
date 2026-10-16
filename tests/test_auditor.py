import pytest
import respx
import httpx
from src.auditor import audit

@pytest.fixture
def good_html():
    with open("tests/fixtures/good.html", "r", encoding="utf-8") as f:
        return f.read()

@pytest.fixture
def bad_html():
    with open("tests/fixtures/bad.html", "r", encoding="utf-8") as f:
        return f.read()

@respx.mock
def test_audit_good_html(good_html):
    url = "https://example.com"
    respx.get(url).mock(return_value=httpx.Response(200, text=good_html, request=httpx.Request("GET", url)))

    result = audit(url)

    assert result["url"] == url
    assert result["ok"] == True

    # Check that all findings passed
    for finding in result["findings"]:
        assert finding["status"] == "pass"

    assert result["scores"]["seo"] == 100
    assert result["scores"]["conversion"] == 100
    assert result["scores"]["trust"] == 100
    assert result["scores"]["overall"] == 100

@respx.mock
def test_audit_bad_html(bad_html):
    url = "http://example.com"
    respx.get(url).mock(return_value=httpx.Response(200, text=bad_html, request=httpx.Request("GET", url)))

    result = audit(url)

    assert result["url"] == url
    assert result["ok"] == False

    # HTTPS should fail, Title should fail, Meta Desc should fail, H1 should fail, Image Alt should fail, Viewport should fail
    for finding in result["findings"]:
        assert finding["status"] == "fail", f"Finding {finding['check']} unexpectedly passed"

    assert result["scores"]["seo"] == 0
    assert result["scores"]["conversion"] == 0
    assert result["scores"]["trust"] == 0
    assert result["scores"]["overall"] == 0

@respx.mock
def test_audit_http_error():
    url = "https://error.com"
    respx.get(url).mock(side_effect=httpx.ConnectError)

    result = audit(url)

    assert result["ok"] == False
    assert "Failed to fetch URL" in result["summary"]

@respx.mock
def test_audit_redirect(good_html):
    # Simulate a redirect from http to https
    url = "http://example.com"
    final_url = "https://example.com"

    respx.get(url).mock(return_value=httpx.Response(301, headers={"Location": final_url}))
    respx.get(final_url).mock(return_value=httpx.Response(200, text=good_html))

    result = audit(url)

    assert result["ok"] == True
    # Trust score should be 100 because final_url is https
    assert result["scores"]["trust"] == 100
    # The HTTPS check should pass
    https_finding = next(f for f in result["findings"] if f["check"] == "HTTPS")
    assert https_finding["status"] == "pass"

@respx.mock
def test_audit_no_images(good_html):
    # Test a scenario with no images to ensure the alt text check still passes
    no_img_html = good_html.replace('<img src="good.jpg" alt="A descriptive alt text for this image">', '').replace('<img src="another.jpg" alt="Another descriptive alt text">', '')
    url = "https://example.com"
    respx.get(url).mock(return_value=httpx.Response(200, text=no_img_html, request=httpx.Request("GET", url)))

    result = audit(url)

    assert result["ok"] == True

    alt_finding = next(f for f in result["findings"] if f["check"] == "Image Alt Text")
    assert alt_finding["status"] == "pass"
