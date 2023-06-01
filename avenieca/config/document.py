from dataclasses import dataclass
from typing import Optional

from avenieca.config.twin import Twin
from avenieca.config.db import DB
from avenieca.config.embedding import Embedding
from avenieca.config.log import Log
from avenieca.config.vse import VSE
from avenieca.data import Base


@dataclass
class Document(Base):
    name: str
    # sync rate to create documents from twin
    sync_rate: str
    # if true, newly created documents will be embedded after creation
    create_n_embed: bool
    # Twin config
    twin_config: Twin
    # database configuration
    db_config: DB
    # vector similarity search engine configuration
    vse_config: VSE
    # logger configuration for the module
    log_config: Log
    # Embedding config for creating document embeddings
    embedding_config: Optional[Embedding]
    # if true, run the sync loop once and exit, useful for tests
    sync_once: bool = False


@dataclass
class DocumentConfig(Base):
    document: Document
