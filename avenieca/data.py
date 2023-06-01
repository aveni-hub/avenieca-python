from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional, List
from json import dumps
from dataclass_wizard import JSONWizard


@dataclass
class Base(JSONWizard):
    @property
    def __dict__(self):
        return asdict(self)

    @property
    def json(self):
        return dumps(self.__dict__, indent=4)

    def to_json_file(self, file):
        with open(file, "w") as outfile:
            outfile.write(self.json)


@dataclass
class Signal(Base):
    state: List[float]
    valence: Optional[float] = None
    score: Optional[int] = None
    emb_inp: Optional[int] = None
