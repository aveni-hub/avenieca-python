from dataclasses import dataclass
from typing import Optional

from avenieca.config.db import DB

from avenieca.config.cortex import Cortex
from avenieca.config.document import Document
from avenieca.config.log import Log
from avenieca.config.retrieval import Retrieval
from avenieca.data import Base


@dataclass
class User(Base):
    username: str
    password: str
    api_key: str
    db_config: DB


@dataclass
class WebAPI(Base):
    user_config: User
    cortex_config: Cortex
    log_config: Log
    host: str = "0.0.0.0"
    port: str = "2580"
    cors_max_age: int = 3600
    document_config: Optional[Document] = None
    retrieval_config: Optional[Retrieval] = None


@dataclass
class ServerConfig(Base):
    server: WebAPI
