# FAQ

## Does this repository scrape Woolworths locally?

No. It calls the hosted Apify Actor. You need your own Apify account and token; no Woolworths account is needed.

## Is every field present?

No. Product details and ratings depend on published source data and selected options. Null means unavailable, not zero. ratingRetrieved can be true while no rating exists.

## Can I select a store without knowing a code?

Use storeQuery with a full store name, suburb or postcode. Ambiguous matches need refinement. postcode alone selects nearby-stock context, not a pricing store.

## Is maxProducts a total input cap?

No. It applies per search/category/specials source. Use one target first, and a PPE spending cap for a bounded integration.

## Can a successful run be partial?

Yes. Inspect SUMMARY and warnings. Correct invalid targets before rerunning; retain already delivered useful rows. The examples display non-Completed summaries instead of treating SUCCEEDED as full coverage.

## Will the examples retry a failed run automatically?

No. Starting another Actor run can add charges. The Python helper polls the same run and requests abort if its local wait deadline expires. A network failure can leave an existing run active: inspect its ID in Console before retrying.

## Does export start another run?

No. export_products.py reads an existing Dataset and writes selected flat product fields. Keep JSON for nested nutrition, taxonomy and rating structures.

## Are the sample prices current?

They are historical observations from 30 October 2026. Run the Actor for a fresh snapshot; prices and availability depend on context and can change.
