from dataclasses import dataclass

from avenieca.data import Base


@dataclass
class Log(Base):
    level: str = ""
    log_file: str = ""
