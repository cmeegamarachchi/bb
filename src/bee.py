# import pydantic
from typing import Tuple

class Bee:
    """
    A class representing a bee.
    """

    id: str
    is_queen: bool = False
    current_location: Tuple[int, int] = (0, 0)

class QueenBee(Bee):
    """
    A class representing a queen bee.
    """

    def __init__(self, id: str):
        self.id = id
        self.is_queen = True

class DroneBee(Bee):
    """
    A class representing a drone bee.
    """

    def __init__(self, id: str):
        self.id = id
        self.is_queen = False

class WorkerBee(Bee):
    """
    A class representing a worker bee.
    """

    def __init__(self, id: str):
        self.id = id
        self.is_queen = False
