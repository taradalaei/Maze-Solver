# Maze Solver

This project provides a collection of algorithms to solve mazes using various pathfinding techniques. It includes implementations of Depth-First Search (DFS), Breadth-First Search (BFS), Iterative Deepening Search (IDS), A* Search, and A* Search with a geometric heuristic. The solver visualizes the maze solving process using Pygame.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Algorithms](#algorithms)
  - [Depth-First Search (DFS)](#depth-first-search-dfs)
  - [Breadth-First Search (BFS)](#breadth-first-search-bfs)
  - [Iterative Deepening Search (IDS)](#iterative-deepening-search-ids)
  - [A* Search](#a-star-search)
  - [A* Search with Geometric Heuristic (ASG)](#a-star-search-with-geometric-heuristic-asg)
- [Generating Test Cases](#generating-test-cases)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project, you need Python installed on your system. Additionally, install the required packages using pip:

```bash
pip install -r requirements.txt
```

Ensure you have Pygame installed:

```bash
pip install pygame
```

## Usage

### Install requirements

To install requirements, run:

```bash
pip install -r requirements.txt
```

### Run the code

Running the code needs 4 parameters:

1. `-a`, `--algorithm`
    - This parameter specifies the algorithm which is going to run.
    - `[dfs, bfs, ids, a_star, asg]` are your only options.
2. `-m`, `--map`
    - Map parameter demonstrates the map which the algorithm solves.
    - `[0, 1, 2, 3, 4, 5, 6, 7]` are the options of map.
3. `-s`, `--start`
    - The start position of your agent, such as `1,2`.
4. `-g`, `--goal`
    - The goal position of your agent, for instance `7,9`.

### Example

```shell
python3 main.py -a a_star -m 3 -s '1,2' -g '6,4'
```

## Algorithms

### Depth-First Search (DFS)

DFS explores a path to its fullest before backtracking and trying a new path. It uses a stack to manage the nodes.

### Breadth-First Search (BFS)

BFS explores all neighbors at the present depth level before moving on to nodes at the next depth level. It uses a queue to manage the nodes.

### Iterative Deepening Search (IDS)

IDS combines the depth-first search's space-efficiency and breadth-first search's completeness. It performs a series of depth-limited searches with increasing limits.

### A* Search

A* search uses heuristics to guide its search. It combines the path cost from the start and a heuristic estimate to the goal.

### A* Search with Geometric Heuristic (ASG)

This variation of A* search uses the Euclidean distance as the heuristic, providing a different approach to guide the search.

## Generating Test Cases

You can generate test mazes of custom sizes with random obstacles using the script provided:

```bash
python generate_test_case.py
```

This will generate a `test_case.csv` file with the maze grid.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
