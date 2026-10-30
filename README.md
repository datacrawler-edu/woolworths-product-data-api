# Woolworths product data API: Python, JSON and CSV

Collect Australian grocery prices, nutrition and rating summaries with the hosted [Woolworths Product Scraper](https://apify.com/datascraperes/woolworths-products-scraper?fpr=edudata). Use the web form, or start bounded runs from Python, JavaScript and cURL.

This repository contains integration examples and a real, shortened product snapshot. It is an independent integration guide, not an official Woolworths service. Links to Apify include an affiliate referral parameter.

## What this repository helps you do

- Search Woolworths products and retain prices, unit prices and product identities.
- Build a grocery dataset with ingredients, nutrition and allergen fields where published.
- Run several small searches with an explicit per-run spending cap.
- Export an existing Dataset to CSV without starting another collection.

## Example result

This is a projection of a real product observed on 30 October 2026. Prices and availability change; it is not a current offer. The [JSON sample](data/sample-output.json) contains more fields; the [CSV sample](data/sample-output.csv) is a flattened subset.

```json
{
  "stockcode": "6073909",
  "name": "Full+ On The Go Meal Replacement Chocolate",
  "price": 5.95,
  "cupString": "$12.40 / 1L",
  "isAvailable": true,
  "productURL": "https://www.woolworths.com.au/shop/productdetails/6073909/full-on-the-go-meal-replacement-chocolate"
}
```

## Run without code

1. Open the [hosted Actor](https://apify.com/datascraperes/woolworths-products-scraper?fpr=edudata).
2. Enter `milk` under **Search terms** and set **Maximum products** to `5`.
3. Keep product details enabled; optionally enable ratings.
4. Click **Start**, review progress and open the **Dataset**.
5. Export JSON or CSV. Read warnings and `SUMMARY` before treating a result as complete.

See the [no-code walkthrough](docs/no-code-guide.md).

## Try it with Apify's free plan

Apify's Free plan currently includes $5 of monthly prepaid usage, with no credit card required to start. Available credits can cover a small test; they do not mean unlimited free runs. Unused credits expire at the end of the billing cycle. See [current Apify pricing](https://apify.com/pricing?fpr=edudata).

## Quick start for developers

Python examples use the standard library, with Python 3.10 or later. No package installation is needed. Set your own token locally:

```bash
export APIFY_API_TOKEN="your-token"
python examples/python/search_products.py
```

In Windows PowerShell:

```powershell
$env:APIFY_API_TOKEN = "your-token"
python examples/python/search_products.py
```

This starts a real, chargeable run: five products, a 240-second run timeout and a $0.01 PPE spending cap. The cap is a billing limit, not a completeness guarantee. No automatic retry starts another run. Keep tokens out of Git and shared logs.

## Input example

```json
{
  "source": "online",
  "searchTerms": [
    "milk"
  ],
  "maxProducts": 5,
  "includeProductDetails": true,
  "includeRatings": true
}
```

See [all input fields](docs/input-reference.md). Use readable full state names for weekly mode; online search needs no state codes.

## Request examples

- [Python single search](examples/python/search_products.py)
- [Python batch workflow](examples/python/batch_searches.py): two independent small runs, up to $0.01 PPE each.
- [Python CSV export](examples/python/export_products.py): reads an existing Dataset; no new Actor run.
- [JavaScript with Node.js 20+](examples/javascript/request.mjs)
- [cURL request](examples/curl-request.md)

Python and JavaScript inspect the run status and `SUMMARY`. They warn on partial/invalid input even when Apify reports SUCCEEDED. Treat each batch run separately; cross-run duplicates are possible.

## Output fields

| Field | Meaning |
| --- | --- |
| `stockcode`, `barcode`, `productURL` | Product identity and public link |
| `price`, `wasPrice`, `cupString` | Observed price, previous price and unit-price label |
| `priceContext`, `storeNo` | Price context; the default anonymous context is not a store guarantee |
| `ingredients`, `nutrition`, `allergens`, `dietary` | Published detail data; fields can be empty or null |
| `departmentNames`, `categoryNames`, `classification` | Product taxonomy where available |
| `rating`, `ratingRetrieved` | Rating summary and retrieval flag, not individual reviews |
| `fetchedAt` | Observation timestamp |

See the [complete field reference](docs/output-reference.md). Keep null prices distinct from zero. With `includeStoreDirectory`, Dataset rows can also have `type: store`; examples export only products.

## Common use cases

See [workflow inputs](docs/use-cases.md) for product searches, half-price offers and category collection. Prices are snapshots; repeated runs create a history only if you save them.

## Export Woolworths prices to CSV with Python

After a run, copy its Dataset ID and use:

```bash
python examples/python/export_products.py DATASET_ID products.csv
```

This reads every Dataset page and writes one row per product. Nested nutrition/rating data stays available in JSON rather than being flattened into ambiguous cells.

## Collect nutrition and allergens for grocery products

Keep `includeProductDetails` enabled. Inspect `productDetailsRetrieved` and the actual fields before using them. A product may have no ingredients, nutrition or rating data. Nutrition and allergen labels are source information, not medical advice or a substitute for checking the product label.

## FAQ

The [FAQ](docs/faq.md) covers missing data, store context, partial results, invalid input and spending caps.

## Limits and pricing

The Actor uses pay-per-event billing for each product successfully saved to the Dataset. Product details are included; there is no separate event for the additional columns. Store-directory and diagnostic records are not product events.

Verified on 30 October 2026: Free $1.00, Bronze $0.90, Silver $0.80, and Gold/Platinum/Diamond $0.75 per 1,000 product events. Check the [current Actor pricing](https://apify.com/datascraperes/woolworths-products-scraper?fpr=edudata) before running larger workloads.

`maxProducts` accepts 1–1,000 and applies **per source**, not across the entire input. Two terms with a limit of 5 may deliver up to 10 products before deduplication. Direct product links return one product. Source blocks, missing data, spending limits and unavailable products may reduce results. A SUCCEEDED status alone does not prove completeness.

## Hosted version

Use the [hosted Actor](https://apify.com/datascraperes/woolworths-products-scraper?fpr=edudata) for web runs, API access, scheduling and Dataset storage. This repository does not run the collector locally.

## Responsible use

Use public product information lawfully and respect applicable terms. Do not access private account data. Woolworths is a trademark of its respective owner; this project is not affiliated with Woolworths.

## Support

For an example problem, [open a GitHub issue](https://github.com/datacrawler-edu/woolworths-product-data-api/issues) with sanitized input and the error. For collection issues, use the [Actor support tab](https://apify.com/datascraperes/woolworths-products-scraper?fpr=edudata) and provide the run ID. Never post a token.

## License

The integration examples are MIT licensed. Sample source data remains subject to its owners' rights.
