from dataclasses import dataclass


@dataclass()
class User:
    id_: str = None
    name: str = None
    email: str = None
    password: str = None
