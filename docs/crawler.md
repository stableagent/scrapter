# Crawler

The crawler will be resumable. URL state is tracked separately from parsed product state so failed downloads, parse failures and completed records can be distinguished.

The implementation will use bounded concurrency, caching, retries with backoff and explicit crawl budgets. It will respect robots.txt, site terms and rate limits and will not attempt to evade access controls or blocking mechanisms.
