"""Two independent runs, each capped at $0.01 PPE and five products."""
import json
from apify_api import collect, items

def main():
    for term in ("milk", "bread"):
        run, summary = collect({"source": "online", "searchTerms": [term],
                                "maxProducts": 5, "includeProductDetails": True})
        for product in items(run["defaultDatasetId"]):
            print(json.dumps({"requestedTerm": term, "runId": run["id"], "product": product}))

if __name__ == "__main__":
    main()
