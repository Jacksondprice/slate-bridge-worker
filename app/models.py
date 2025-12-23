from dataclasses import dataclass
from datetime import date


@dataclass
class Device:
    id: int
    name: str
    created: date
    active: bool = True
