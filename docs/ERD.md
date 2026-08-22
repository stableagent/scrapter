# Entity Relationship Design

```text
Product 1 ---- N ProductVariant
Product N ---- N Category
Product 1 ---- N ProductImage
Product 1 ---- N TechnicalSpecification
Product 1 ---- 1 SEO
ProductVariant N ---- N AttributeValue
Attribute 1 ---- N AttributeValue
```

The final schema will also retain source URLs, source identifiers, content hashes, crawl status and raw snapshots.
