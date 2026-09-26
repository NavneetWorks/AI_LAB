"""
Simple Cleaning Robot Simulation - 2x2 Grid of Rooms

Rooms are laid out like this (row, col):
    (0,0) | (0,1)
    ------+------
    (1,0) | (1,1)

Each room is either 'Dirty' or 'Clean'.
The robot visits every room one by one, cleans it if dirty,
and prints the grid after every step so you can see progress live.
"""

import random
import time

DIRTY = "Dirty"
CLEAN = "Clean"

ROWS, COLS = 2, 2


def create_grid(random_dirt=True):
    """Creates the 2x2 grid. If random_dirt=True, randomly marks rooms dirty/clean."""
    grid = {}
    for r in range(ROWS):
        for c in range(COLS):
            grid[(r, c)] = random.choice([DIRTY, CLEAN]) if random_dirt else DIRTY
    return grid


def print_grid(grid, robot_pos):
    """Prints the 2x2 grid visually, marking the robot's current room with [R]."""
    print()
    for r in range(ROWS):
        row_strs = []
        for c in range(COLS):
            status = grid[(r, c)]
            marker = "R" if (r, c) == robot_pos else " "
            cell = f"[{marker}] {status:^5}"
            row_strs.append(cell)
        print("   ".join(row_strs))
        if r < ROWS - 1:
            print("-" * 30)
    print()


def clean_room(grid, pos):
    """Cleans the room at pos if it's dirty. Returns True if cleaning happened."""
    if grid[pos] == DIRTY:
        grid[pos] = CLEAN
        return True
    return False


def get_room_order():
    """Defines the order in which the robot visits rooms (simple sweep pattern)."""
    return [(0, 0), (0, 1), (1, 1), (1, 0)]  # clockwise sweep


def all_clean(grid):
    return all(status == CLEAN for status in grid.values())


def run_cleaning_simulation(delay=1.0):
    grid = create_grid(random_dirt=True)
    order = get_room_order()

    print("Initial state of rooms:")
    print_grid(grid, robot_pos=None)

    for step, pos in enumerate(order, start=1):
        print(f"Step {step}: Robot moves to room {pos}")
        time.sleep(delay)
        print_grid(grid, robot_pos=pos)

        if grid[pos] == DIRTY:
            print(f"  Room {pos} is DIRTY -> cleaning now...")
            clean_room(grid, pos)
        else:
            print(f"  Room {pos} is already CLEAN -> skipping.")

        time.sleep(delay)
        print_grid(grid, robot_pos=pos)

    print("Final state of all rooms:")
    print_grid(grid, robot_pos=None)

    if all_clean(grid):
        print("All rooms are clean! Robot's job is done. ✅")
    else:
        print("Some rooms are still dirty. ⚠️")


if __name__ == "__main__":
    run_cleaning_simulation(delay=0.5)
