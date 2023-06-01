from dataclasses import dataclass
from typing import List

from avenieca.data import Base


@dataclass
class RAS(Base):
    upsert_from: str
    # full file path to config file where emotified state instances are defined
    file_path: str


@dataclass
class ESI(Base):
    id: int
    state_vec: List[float]
    valence: float


@dataclass
class EmotifiedInstances(Base):
    esi_vec: List[ESI]


@dataclass
class EmotifiedInstancesConfig(Base):
    emotified_instances: EmotifiedInstances
