from dataclasses import dataclass, field
from typing import List, Optional

from avenieca.config.broker import Broker
from avenieca.config.db import DB
from avenieca.config.log import Log
from avenieca.config.ras import RAS
from avenieca.config.vse import VSE
from avenieca.data import Base


@dataclass
class Twin(Base):
    # database configuration
    db_config: DB
    # vector similarity search engine configuration
    vse_config: VSE
    # logger configuration for the twin instance
    log_config: Log
    # sensor or actuator
    physical_twin_type: str
    # length of state vector
    shape: int = 0
    # the display name of the twin
    display_name: str = ""
    # Unique id
    module_id: str = ""
    # a time threshold for which an aggregated but out of sync ess is re-aggregated
    # in subsequent aggregates.
    duration_threshold: str = "1s"
    # the rate at which to query db for new states
    sync_rate: str = "1s"
    # if true, the twin will run the sync/aggregate loop once and exit
    sync_once: bool = False
    # broker config for streams
    broker_config: Optional[Broker] = None
    # ras config for setting valence
    ras_config: Optional[RAS] = None
    # Incoming twin configurations for Aggregate
    in_twins: List['Twin'] = field(default_factory=list)
    # Outgoing twin configurations that the twin is aggregated to
    out_twins: List['Twin'] = field(default_factory=list)


@dataclass
class TwinConfig(Base):
    twin: Twin
