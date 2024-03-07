from dataclasses import dataclass

@dataclass
class Command:
    address: str
    value: str
    is_new_module: bool