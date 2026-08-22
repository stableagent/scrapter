from dataclasses import dataclass


@dataclass(slots=True)
class ProductVariant:
    source_id: str | None
    parent_product_id: str
    sku: str | None
    source_url: str | None
    price: str | None
    stock: str | None
    attributes: dict[str, str]
