# Output reference

The JSON sample is a selected-field projection of one real product, not a promise that all products contain every field. Dataset rows can be products or stores. Optional fields can be null or empty. Numeric prices are Australian dollars where supplied. Keep price context and observation time when comparing prices.

| Field | Meaning |
| --- | --- |
| `type` | Record type |
| `source` | Source |
| `sourceKind` | Source kind |
| `query` | Search term |
| `categoryPath` | Category path |
| `categoryId` | Category ID |
| `position` | Position |
| `storeNo` | Store number |
| `storeName` | Store |
| `priceContext` | Price context |
| `state` | State |
| `location` | Catalogue location |
| `catalogueStoreId` | Catalogue store ID |
| `catalogueStoreName` | Catalogue store |
| `saleId` | Sale ID |
| `saleName` | Catalogue |
| `publishDate` | Published |
| `startDate` | Offer starts |
| `endDate` | Offer ends |
| `validityText` | Validity |
| `cataloguePdfUrl` | Catalogue PDF |
| `cataloguePageCount` | Pages |
| `pageNo` | Page |
| `pageUrl` | Page image |
| `thumbnailUrl` | Page thumbnail |
| `pageWidth` | Page width |
| `pageHeight` | Page height |
| `catalogueItemId` | Catalogue item ID |
| `stockcode` | Stockcode |
| `barcode` | Barcode |
| `name` | Product |
| `displayName` | Display name |
| `description` | Description |
| `richDescription` | Rich description |
| `brand` | Brand |
| `packageSize` | Package size |
| `unit` | Unit |
| `imageUrl` | Product image |
| `imageUrls` | Product images |
| `productURL` | Product URL |
| `itemCoordinates` | Page coordinates |
| `boundingBox` | Page position |
| `price` | Price |
| `wasPrice` | Was price |
| `lowestPrice` | Lowest price |
| `highestPrice` | Highest price |
| `savingsAmount` | Savings |
| `cupPrice` | Unit price |
| `cupString` | Unit price text |
| `comparativeText` | Unit price text (catalogue) |
| `pricingUnit` | Pricing unit |
| `offerTerms` | Offer terms |
| `isOnSpecial` | On special |
| `isHalfPrice` | Half price |
| `isAvailable` | Available |
| `isInStock` | In stock |
| `isPurchasable` | Purchasable |
| `instorePrice` | In-store price |
| `instoreWasPrice` | In-store was price |
| `instoreCupString` | In-store unit price |
| `instoreIsAvailable` | In-store available |
| `instoreIsPurchasable` | In-store purchasable |
| `isOnlineOnly` | Online only |
| `isForCollection` | Collection |
| `isForDelivery` | Delivery |
| `isForExpress` | Express |
| `isMarketProduct` | Marketplace product |
| `vendor` | Marketplace vendor |
| `supplyLimit` | Supply limit |
| `nextAvailabilityDate` | Next availability |
| `offerId` | Offer ID |
| `priceOptions` | Catalogue price options |
| `additionalSkus` | Related stockcodes |
| `ingredients` | Ingredients |
| `allergenStatement` | Allergen statement |
| `lifestyleStatement` | Dietary statement |
| `healthStarRating` | Health star rating |
| `nutrition` | Nutrition |
| `storageInstructions` | Storage |
| `productWarnings` | Warnings |
| `directions` | Directions |
| `suitableFor` | Suitable for |
| `countryOfOrigin` | Country of origin |
| `ingredientPercentage` | Australian ingredient percentage |
| `countryOfOriginText` | Country of origin text |
| `primaryCategory` | Primary category |
| `rating` | Rating |
| `ratingAverage` | Average rating |
| `ratingCount` | Rating count |
| `reviewCount` | Review count |
| `fiveStarCount` | Five-star count |
| `nearbyStores` | Nearby stores |
| `detailsRetrieved` | Details retrieved |
| `productDetailsRetrieved` | Product details retrieved |
| `ratingRetrieved` | Rating retrieved |
| `maxProductsReached` | Maximum products reached |
| `regionLimitReached` | Region limit reached |
| `fetchedAt` | Fetched at |
| `storeNumber` | Store number (directory) |
| `addressLine1` | Address |
| `addressLine2` | Address line 2 |
| `suburb` | Suburb |
| `postcode` | Postcode |
| `country` | Country |
| `division` | Division |
| `latitude` | Latitude |
| `longitude` | Longitude |
| `phone` | Phone |
| `email` | Email |
| `facilities` | Facilities |
| `tradingHours` | Trading hours |
| `timeZone` | Time zone |
| `geoLevel` | Geographic level |
| `images` | Store images |
| `allergens` | allergens |
| `mayContain` | mayContain |
| `freeFrom` | freeFrom |
| `dietary` | dietary |
| `promotionLabels` | promotionLabels |
| `sponsored` | sponsored |
| `isRewardsSpecial` | isRewardsSpecial |
| `multiBuy` | multiBuy |
| `departments` | Departments |
| `departmentNames` | Department names |
| `categoryNames` | Category names |
| `subcategoryNames` | Subcategory names |
| `classification` | Product classification |
| `purchaseLimit` | Configured product purchase cap |
| `minimumQuantity` | Minimum purchase quantity |
| `supplyLimitSource` | Reason for supply limit |
| `isNew` | New product |
| `savingsPercent` | Savings percent |
| `promotionType` | Promotion type |
| `seller` | Marketplace seller |
| `delivery` | Marketplace delivery |
| `servingSize` | Serving size |
| `servingsPerPack` | Servings per pack |

`SUMMARY` in the default key-value store reports collection status. Inspect it alongside Dataset rows: `Completed`, `Partial` and `invalid_input` communicate different outcomes even when the run exits normally. Rating summaries are not individual customer reviews.
