# Small synchronous request

Set APIFY_API_TOKEN in your shell. Run from this repository's root in a POSIX shell:

```bash
curl --fail-with-body --max-time 300 \
  -X POST 'https://api.apify.com/v2/acts/datascraperes~woolworths-products-scraper/run-sync-get-dataset-items?timeout=240&maxTotalChargeUsd=0.01&format=json' \
  -H "Authorization: Bearer $APIFY_API_TOKEN" \
  -H 'Content-Type: application/json' \
  --data-binary @data/sample-input.json
```

This starts a real run with a $0.01 PPE cap. Do not add automatic POST retries. A client/network timeout does not prove the run stopped: inspect Console before repeating it. Synchronous Dataset output alone does not expose completeness; inspect the run's SUMMARY in Console. Use the Python or JavaScript workflow for run IDs, status and summary handling. For larger jobs, use asynchronous runs rather than extending this synchronous example.
