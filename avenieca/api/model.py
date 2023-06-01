from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List

from avenieca.data import Base


@dataclass
class Config:
    api_token: Optional[str] = ""
    username: Optional[str] = ""
    password: Optional[str] = ""
    uri: Optional[str] = ""


@dataclass
class AuthLogin(Base):
    username: str
    password: str


@dataclass
class AuthResponse(Base):
    role: str
    session_id: str
    user_id: str
    username: str


@dataclass
class ESSInsert(Base):
    state: List[float]
    module_id: str
    valence: float
    avg_ess_valence: float = 0.0
    total_ess_score: int = 0
    avg_ess_score: int = 0
    score: int = 0
    embedding_input: Optional[int] = None
    aggregate_id: List[int] = field(default_factory=list)
    aggregate_valence: List[float] = field(default_factory=list)
    aggregate_score: List[int] = field(default_factory=list)
    aggregate_module_id: List[str] = field(default_factory=list)
    aggregate_shape: List[int] = field(default_factory=list)
    aggregate_context: list = field(default_factory=list)
    aggregate_emb_inp: list = field(default_factory=list)
    context: Optional[str] = None


@dataclass
class ESSResponse(Base):
    id: int
    state: List[float]
    module_id: str
    valence: float
    created_at: str = None
    updated_at: str = None
    avg_ess_valence: float = 0.0
    total_ess_score: int = 0
    avg_ess_score: int = 0
    score: int = 0
    embedding_input: Optional[int] = None
    aggregate_id: List[int] = field(default_factory=list)
    aggregate_valence: List[float] = field(default_factory=list)
    aggregate_score: List[int] = field(default_factory=list)
    aggregate_module_id: List[str] = field(default_factory=list)
    aggregate_shape: List[int] = field(default_factory=list)
    aggregate_context: list = field(default_factory=list)
    aggregate_emb_inp: list = field(default_factory=list)
    context: Optional[str] = None


@dataclass
class AggregateError(Base):
    ess_from_aggregate: str = "",
    field_length_errors: list = field(default_factory=list)
    module_id_position: list = field(default_factory=list)
    verifying_ess_exists: list = field(default_factory=list)
    ess_mismatch: list = field(default_factory=list)
    invalid_ess_db_ids: list = field(default_factory=list)
    invalid_module_ids: list = field(default_factory=list)
    incorrect_avg_ess_score: str = ""
    incorrect_avg_ess_valence: str = ""
    incorrect_valence: str = ""
    incorrect_total_ess_sore: str = ""


@dataclass
class PrettyESS(Base):
    id: int
    state: List[str]
    aggregate_id: List[int]
    aggregate_valence: List[float]
    aggregate_score: List[int]
    aggregate_module_id: List[str]
    aggregate_shape: List[int]
    module_id: str
    valence: float
    id: int
    avg_ess_valence: float
    total_ess_score: int
    avg_ess_score: int
    created_at: str
    updated_at: str
    score: int = 0
    embedding_input: Optional[int] = None
    aggregate_context: list = field(default_factory=list)
    aggregate_emb_inp: list = field(default_factory=list)
    context: Optional[str] = None
    state_float: Optional[float] = None
    state_str: Optional[str] = None


@dataclass
class SequenceInsert(Base):
    module_id: str
    instance_id: int
    status: str = "n"
    context: Optional[str] = None


@dataclass
class SequenceResponse(Base):
    id: int
    module_id: str
    instance_id: int
    status: str
    created_at: str
    updated_at: str
    context: Optional[str] = None


@dataclass
class NextStateRequest(Base):
    module_id: str
    range: int = 2
    recall: int = 2
    n: int = 1
    status: Optional[str] = None
    current_state: int = None
    previous_state: list = None
    store_response: bool = False
    store_sequence: bool = False


@dataclass
class TwinRaw(Base):
    state: List[float]
    aggregate_id: int
    ess_id: int
    module_id: str


@dataclass
class Twin(Base):
    aggregate_id: int
    ess_id: int
    module_id: str
    state: str


@dataclass
class Twins(Base):
    list: List[Twin]


@dataclass
class TwinsRaw(Base):
    list: List[TwinRaw]


@dataclass
class NextStateResponse(Base):
    current_state: List[Twin]
    next_state: List[Twins]


@dataclass
class NextStateResponseRaw(Base):
    current_state: List[TwinRaw]
    next_state: List[TwinsRaw]


@dataclass
class DocumentInsert(Base):
    doc_id: str
    text: str
    embed: bool = False


@dataclass
class DocumentResponse(Base):
    id: int
    doc_id: str
    text: str
    status: str
    created_at: str
    updated_at: str


@dataclass
class EmbeddingInputInsert(Base):
    module_id: str
    input: str
    hash: str


@dataclass
class EmbeddingInputHash(Base):
    hash: str


@dataclass
class SearchResult(Base):
    score: float
    ess: ESSResponse


@dataclass
class EmbeddingInputResponse(Base):
    id: int
    module_id: str
    input: str
    hash: str
    created_at: str
    updated_at: str


@dataclass
class RetrievalRequest(Base):
    query: str


@dataclass
class RetrievalResponse(Base):
    response: str


@dataclass
class ECAResponse(Base):
    percept_ess_ids: List[int]
    response_ess_ids: List[int]
    percept_names: List[str]
    response_names: List[str]
    name: str
    id: int
    percept: int
    response: int
    twin_module_id: str
    status: str
    created_at: str
    updated_at: str


@dataclass
class Search(Base):
    module_id: str
    state: List[float]
    limit: int = 1


@dataclass
class Error(Base):
    errors: List[str]
