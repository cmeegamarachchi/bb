from world import World

world = World()

def setup() -> None:
    """
    Set up the world.
    """
    print("World set up with hives and bees.")
    world.add_hive(location=(0, 0), number_of_workers=10, number_of_drones=10)

def main() -> None:
    """
    Main function to run the simulation.
    """
    setup()
    print("Simulation started.")
    # Add more simulation logic here
    # For example, you can call methods on the world or hives to simulate bee behavior
    # world.simulate()
    print("Simulation ended.")

if __name__ == "__main__":
    main()