# from typing import Optional

from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    age: int


u = User(id=1, name="Alice", age=30)


print(u.name)
