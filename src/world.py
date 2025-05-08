from hive import Hive
from typing import List, Tuple

class World:
    """
    A class representing the world.
    """
    hives: List[Hive]

    def __init__(self):
        self.hives = []

    def add_hive(self, location: Tuple[int, int], number_of_workers: int = 10, number_of_drones: int = 10):
        """
        Add a hive to the world.
        """
        hive = Hive()
        hive.create(location=location, number_of_workers=number_of_workers, number_of_drones=number_of_drones)
        self.hives.append(hive)