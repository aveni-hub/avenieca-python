from dataclasses import dataclass
from typing import Optional

from avenieca.config.document import Document
from avenieca.data import Base


@dataclass
class OAIConfig(Base):
    api_url: str
    api_key: str
    model: str
    max_tokens: Optional[int] = 1000
    temperature: Optional[int] = 0
    top_p: Optional[float] = 0
    n: Optional[int] = 2


@dataclass
class Retrieval(Base):
    # one of the supported APIs [openai, basic]
    api: str
    document_config: Document
    oai_config: Optional[OAIConfig] = None
