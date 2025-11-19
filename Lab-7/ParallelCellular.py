import numpy as np
import time


def initialize_grid(size=5, tree_density=0.7):
    """Initialize forest grid with given tree density and one burning tree."""
    grid = np.random.choice([0, 1], size=(size, size), p=[1 - tree_density, tree_density])

    tree_positions = np.argwhere(grid == 1)
    if len(tree_positions) > 0:
        i, j = tree_positions[np.random.randint(len(tree_positions))]
        grid[i, j] = 2
    else:
        i, j = np.random.randint(0, size, size=2)
        grid[i, j] = 2

    return grid

def step_parallel(grid):
    """Perform one parallel update step of the forest fire model (no regrowth or lightning)."""
    size = grid.shape[0]
    new_grid = grid.copy()
    burning = (grid == 2)

    new_grid[burning] = 0

    neighbor_burning = (
        np.roll(burning, 1, axis=0) | np.roll(burning, -1, axis=0) |
        np.roll(burning, 1, axis=1) | np.roll(burning, -1, axis=1)
    )
    catch_fire = (grid == 1) & neighbor_burning
    new_grid[catch_fire] = 2

    return new_grid

def run_until_no_trees(size=5, delay=0.5, max_steps=100):
    grid = initialize_grid(size)
    step = 0

    while step < max_steps:
        num_trees = np.sum(grid == 1)
        num_burning = np.sum(grid == 2)

        print(f"\nStep {step} | Trees: {num_trees} | Burning: {num_burning}")
        print(grid)

        if (num_trees + num_burning) == 0:
            print(f"\n🔥 Simulation ended at step {step}: no trees left to burn.")
            break

        grid = step_parallel(grid)
        step += 1
        time.sleep(delay)
    else:
        print("\n⚠️ Reached maximum steps without burnout.")

if __name__ == "__main__":
    run_until_no_trees(size=5, delay=0.4)
