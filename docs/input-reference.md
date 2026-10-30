# Input reference

Use the hosted form for friendly labels. API keys below are case-sensitive. Unknown field names produce a correction warning; Apify can reject incompatible types before a run starts.

`maxProducts` is per source. Use a small value first. Full state names are accepted for weekly mode; legacy state abbreviations remain compatible.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `searchTerms` | array | `[]` | Up to 20 terms sent to the Woolworths online search. In weekly mode these are case-insensitive filters over flyer product names and stockcodes instead. |
| `urls` | array | `[]` | Paste product, search, category or specials URLs, or numeric product codes, one per line. Online mode only. Use plain URLs; configure filters below. |
| `maxProducts` | integer | `100` | Maximum unique products returned for each search term, category path or specials group. The limit applies separately to each source. |
| `includeProductDetails` | boolean | `true` | Add ingredients, nutrition, allergens, origin, images and other available details. Automatically enabled for a specific store or postcode. Direct product URLs always include details. |
| `postcode` | string | `""` | Four-digit Australian postcode for nearby store stock. The location is estimated from public stores in that postcode. Enables product details and nearby-stock lookup. Prices remain online prices unless you select a specific store under Advanced location. Leave empty to skip. |
| `brands` | array | `[]` | Optional brand terms. Multiple brands are matched as OR. Use the brand names shown on Woolworths product pages. |
| `allergens` | array | `[]` | Optional allergen terms such as Gluten Free or Dairy Free. Multiple terms are matched as OR. |
| `lifestyle` | array | `[]` | Optional lifestyle or dietary terms such as Vegan, Vegetarian or High Protein. Multiple terms are matched as OR. |
| `healthStar` | array | `[]` | Optional health star values such as 4, 4.5 or 5. Multiple values are matched as OR. |
| `sortBy` | string | `"relevance"` | Product order within each source. |
| `includeUnavailable` | boolean | `false` | Include products that are currently unavailable in the anonymous default context. Leave false to keep only available products. |
| `includeMarketplace` | boolean | `false` | Include Woolworths Everyday Market partner products. Leave false for a supermarket-only dataset; marketplace products can dominate price sorts. |
| `includeRatings` | boolean | `false` | Fetch the public rating summary, review count and star distribution for each product. This adds one request per product. |
| `storeQuery` | string | `""` | Optional store selection for store-specific prices. Enter a full store name, suburb or postcode; if several stores match, use one of the suggested full names and locations. Leave empty for the default online price context. |
| `storeNo` | string | `""` | Optional alternative for integrations that already know a Woolworths store number. For normal use, search by store name, suburb or postcode above. Do not combine with store search. |
| `includeNearbyStores` | boolean | `false` | For each product, add nearby stores with distance and in-store availability. Requires latitude and longitude and adds one request per product. |
| `latitude` | number | `null` | Latitude used for nearby store availability, for example -33.8697 for Sydney. |
| `longitude` | number | `null` | Longitude used for nearby store availability, for example 151.2099 for Sydney. |
| `source` | string | `"online"` | Choose Online products for keywords and product links. Choose Weekly catalogue to collect products from the weekly flyer for the states selected below. |
| `states` | array | `[]` | For Weekly catalogue only. Choose states by their full names. Existing integrations may still send state abbreviations. Leave empty for online searches or the store directory. |
| `maxProductsPerRegion` | integer | `300` | Maximum flyer product records from each selected state catalogue. |
| `includeStoreDirectory` | boolean | `false` | Add the public Woolworths Australia supermarket directory, including addresses, coordinates, facilities and trading hours. |
| `categoryPaths` | array | `[]` | Up to 20 public Woolworths category URLs or /shop/browse/... paths, for example /shop/browse/fruit-veg/fruit. Each path is resolved against the public category index. Existing integrations can keep this field; new users can paste links into Woolworths URLs instead. |
| `specials` | array | `[]` | Choose Half price or Everyday low price. Existing integrations may still use the original group identifiers. |

When valid and invalid targets are mixed, valid results can be retained with a partial summary. When nothing is usable, correct the input before starting a new run. Details and ratings are optional; ratings need details. Marketplace products are excluded by default.

Do not combine postcode with explicit coordinates. Store selection may need a more precise full name if the supplied suburb matches several stores.
