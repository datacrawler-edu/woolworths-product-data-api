import json
from pathlib import Path
from apify_api import collect, items

def main():
    sample = Path(__file__).resolve().parents[2] / "data/sample-input.json"
    run, summary = collect(json.loads(sample.read_text(encoding="utf-8")))
    print(json.dumps(list(items(run["defaultDatasetId"])), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
