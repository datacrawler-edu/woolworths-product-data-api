"""Read an existing Dataset; does not start an Actor run."""
import argparse
import csv
from apify_api import items

FIELDS = ["stockcode", "name", "brand", "packageSize", "price", "wasPrice",
          "cupString", "isAvailable", "priceContext", "productURL", "fetchedAt"]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset_id")
    parser.add_argument("output", nargs="?", default="products.csv")
    args = parser.parse_args()
    with open(args.output, "w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        for item in items(args.dataset_id):
            if item.get("type") == "product":
                writer.writerow({key: item.get(key) for key in FIELDS})

if __name__ == "__main__":
    main()
