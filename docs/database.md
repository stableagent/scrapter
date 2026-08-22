# Database design

The core model will preserve source identifiers and normalized business data separately. Planned entities include Product, ProductVariant, Category, Attribute, AttributeValue, VariantAttribute, ProductImage, Download, SEO, TechnicalSpecification, Crawl/URL records and raw-source snapshots.

A variation must never become an orphan: `parent_product_id` is mandatory for variation records.

The final schema will be derived from observed site/WooCommerce data before the crawler is implemented.
