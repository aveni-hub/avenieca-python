from dataclasses import dataclass

from avenieca.data import Base


@dataclass
class DB(Base):
    table: str = ""
    uri: str = ""

