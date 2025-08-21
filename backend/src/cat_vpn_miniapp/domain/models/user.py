from dataclasses import dataclass


@dataclass
class User:
    tid: int
    first_name: str
    last_name: str | None
    username: str | None
