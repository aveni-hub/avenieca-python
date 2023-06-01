from dataclasses import dataclass

from avenieca.data import Base


@dataclass
class Embedding(Base):
    # one of the supported APIs (defaults to OpenAPI)
    api: str
    api_url: str
    api_key: str
    model: str
    embedding_size: int
