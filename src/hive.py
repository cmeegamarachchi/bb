# import pydantic
from bee import Bee, DroneBee, QueenBee, WorkerBee
from typing import Tuple, List

class Hive:
    """
    A class representing a hive.
    """
    location: Tuple[int, int]
    bees: List[Bee]

    def __init__(self):
        self.bees = []
        self.location = (0, 0)

    def create(self, location: Tuple[int, int] = (0,0), number_of_workers: int = 10, number_of_drones: int = 10):
        """
        Set up the hive.
        """
        self.location = location
        for i in range(number_of_workers):
            self.bees.append(WorkerBee(id=f"worker_{i}"))
        for i in range(number_of_drones):
            self.bees.append(DroneBee(id=f"drone_{i}"))
        self.bees.append(QueenBee(id="queen"))
