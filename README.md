# Premium Handpiece Parts Scraper

A modular Python data-extraction project for reconstructing complete product/catalog data from Premium Handpiece Parts, with parent-product/variation relationships preserved for later POS/ERP import.

## Architecture

`URL discovery -> Downloader -> Raw storage -> Parser -> Extractors -> Normalizers -> Validators -> Database -> Exporters`

Raw source material is retained separately from normalized data so parsers can be corrected and rerun without recrawling the website.

## Local setup

Use Python 3.12+. Create and activate `.venv`, copy `.env.example` to `.env`, install dependencies, and run `python main.py`.

The crawler will be resumable and will track source URLs, source identifiers, hashes, crawl state, and parent/variation relationships. It will use bounded concurrency, caching, retries with backoff, and respect site policies and rate limits rather than attempting to evade access controls.
