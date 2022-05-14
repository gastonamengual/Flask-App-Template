from dataclasses import dataclass


@dataclass()
class User:
    id_: str = ""
    name: str = ""
    email: str = ""

    def __post_init__(self):
        if self.name == "":
            raise ValueError("Name must not be empty")

        if self.email == "":
            raise ValueError("Email must not be empty")
