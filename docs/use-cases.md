# Grocery data workflows

## Small product search

Use the sample input to collect up to five milk products with details and ratings. Run search_products.py for one request, or batch_searches.py for two separate small searches. Each run is independently billed and capped.

## Half-price products

```json
{"source":"online","specials":["Half price"],"maxProducts":5,"includeProductDetails":true}
```

## Category products

```json
{"source":"online","categoryPaths":["/shop/browse/fruit-veg"],"maxProducts":5,"includeProductDetails":true}
```

Category paths must exist in the current storefront. An unavailable or ambiguous category requires correction; do not assume an old path remains valid.

## Price history

Export each completed Dataset, retain fetchedAt and priceContext, and compare matching stockcodes. A repeated search may change ordering and coverage; matching keyword positions is not a reliable product join.
