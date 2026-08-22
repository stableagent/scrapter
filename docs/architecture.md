# Architecture

```text
URL discovery -> Downloader -> Raw storage -> Parser -> Extractors -> Normalizers -> Validators -> Database -> Exporters
```

Raw source material is kept separate from normalized data. Parser changes can therefore be applied to stored source snapshots without requesting the website again.

Every variation keeps an explicit parent product reference and its own source identifier, URL when available, SKU, price, stock, image and selected attributes.
