from dataclasses import dataclass
from typing import List

from avenieca.config.twin import Twin
from avenieca.config.db import DB
from avenieca.config.log import Log
from avenieca.data import Base


@dataclass
class Cortex(Base):
    # the twin that the predictive processing algorithm should act on
    pag: str
    # the rate at which to query db for new states
    sync_rate: str
    # a time threshold for which an ess is valid
    duration_threshold: str
    # PAG configurations
    twin_configs: List[Twin]
    # database config for the response table
    db_config: DB
    # logger configuration for core
    log_config: Log
    # Name for the core
    name: str = "core"
    # configure how far back in time the predictive processing algorithm
    # looks when recalling previous instances of a sequence
    recall: int = 2
    # configure how far back in time the predictive processing
    # algorithm looks when considering previous state in a sequence.
    range: int = 2
    # if true, the core will run the sync loop once and exit, useful for tests
    sync_once: bool = False


@dataclass
class CortexConfig(Base):
    cortex: Cortex
