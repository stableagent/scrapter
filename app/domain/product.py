from dataclasses import dataclass, field


@dataclass(slots=True)
class Product:
    source_id: str | None
    name: str
    slug: str | None
    source_url: str
    product_type: str
    attributes: dict[str, str] = field(default_factory=dict)
