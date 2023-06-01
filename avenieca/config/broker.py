from dataclasses import dataclass

from avenieca.data import Base


@dataclass
class Broker(Base):
    url: str
    sub_topic: str
    pub_topic: str
    group: str
    auto_offset_reset: str = "latest"

