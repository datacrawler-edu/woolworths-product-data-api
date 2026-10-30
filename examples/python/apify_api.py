"""Small REST helper for the hosted Actor; Python standard library only."""
import json
import os
import sys
import time
from urllib.error import HTTPError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

BASE = "https://api.apify.com/v2"
ACTOR = "datascraperes~woolworths-products-scraper"

def request(path, method="GET", body=None, params=None):
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise RuntimeError("Set APIFY_API_TOKEN locally before calling Apify.")
    url = BASE + path + ("?" + urlencode(params) if params else "")
    data = json.dumps(body).encode() if body is not None else None
    req = Request(url, data=data, method=method, headers={
        "Authorization": "Bearer " + token, "Content-Type": "application/json"})
    try:
        with urlopen(req, timeout=45) as response:
            return json.load(response)
    except HTTPError as exc:
        raise RuntimeError(f"Apify HTTP {exc.code}. Check your Console before starting another run.") from None

def collect(run_input):
    run = request("/acts/" + ACTOR + "/runs", "POST", run_input,
                  {"timeout": 240, "maxTotalChargeUsd": 0.01})["data"]
    run_id = run["id"]
    print("Run ID:", run_id, file=sys.stderr)
    deadline = time.monotonic() + 300
    while run["status"] in {"READY", "RUNNING", "TIMING-OUT", "ABORTING"}:
        if time.monotonic() >= deadline:
            request("/actor-runs/" + quote(run_id, safe="") + "/abort", "POST", {})
            raise RuntimeError("Wait deadline reached; abort requested for run " + run_id)
        time.sleep(2)
        run = request("/actor-runs/" + quote(run_id, safe=""))["data"]
    if run["status"] != "SUCCEEDED":
        raise RuntimeError("Run " + run_id + " ended " + run["status"])
    summary = request("/key-value-stores/" + quote(run["defaultKeyValueStoreId"], safe="") + "/records/SUMMARY")
    if summary.get("status") != "Completed":
        print("Collection needs attention:", json.dumps(summary), file=sys.stderr)
    return run, summary

def items(dataset_id):
    offset = 0
    while True:
        page = request("/datasets/" + quote(dataset_id, safe="") + "/items",
                       params={"format": "json", "clean": "true", "offset": offset, "limit": 1000})
        if not page:
            return
        yield from page
        offset += len(page)
