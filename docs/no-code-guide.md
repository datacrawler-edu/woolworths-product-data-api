# Search grocery products without code

Open [Woolworths Product Scraper](https://apify.com/datascraperes/woolworths-products-scraper?fpr=edudata), enter one search term such as milk and select a small maximum product count. Keep Product details enabled for ingredients and nutrition. Enable ratings only when needed. Start the run and inspect its log, SUMMARY and Dataset before exporting JSON or CSV.

For store-specific pricing, enter a full store name in Store search. A postcode adds nearby-stock context; it does not automatically choose the price store. Leave location fields empty for the default online context.

For the weekly flyer choose Weekly catalogue and full state names such as New South Wales. These are flyer entries rather than the complete online catalogue. Use Online catalogue for product search, categories and details.

An invalid field or link should produce a correction message. A partially valid list can keep useful products and report Partial. Correct the indicated input rather than assuming a normal exit means every target was collected.
