from pydantic import BaseModel, Field


class SourceRef(BaseModel):
    source_url: str
    source_id: str | None = None
    source_type: str = "web"


class ProductRecord(SourceRef):
    name: str
    slug: str | None = None
    sku: str | None = None
    product_type: str
    parent_product_id: str | None = None
    description: str | None = None
    short_description: str | None = None
    raw_attributes: dict[str, object] = Field(default_factory=dict)
