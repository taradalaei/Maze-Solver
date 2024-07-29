from _helpers import Node, Stack, Queue, PriorityQueue
import math
from queue import PriorityQueue

class Node:
    def __init__(self, pos, parent):
        self.pos = pos
        self.parent = parent

    def position(self):
        return self.pos

    def __lt__(self, other):
        return False

class DFS_Algorithm:
    def __init__(self, start_pos, goal_pos, grid_dim):
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.grid_dim = grid_dim
        self.stack = Stack()
        self.stack.push(Node(pos=start_pos, parent=None))

    def get_successors(self, x, y):
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def is_valid_cell(self, pos):
        return 0 <= pos[0] <= self.grid_dim[0] and 0 <= pos[1] <= self.grid_dim[1]

    def backtrack_solution(self, curr_node):
        return self._backtrack(curr_node)

    def _backtrack(self, curr_node):
        return [] if curr_node.parent is None else self._backtrack(curr_node.parent) + [curr_node.position()]

    def update(self, grid):
        curr_state = self.stack.pop()
        x, y = curr_state.position()
        done = False
        solution_path = []

        for step in self.get_successors(x, y):
            if self.is_valid_cell(step) and grid[step[0], step[1]] in [1, 3]: # 1: empty cell has not explored yet, 3: goal cell
                self.stack.push(Node(pos=step, parent=curr_state))

                if step == self.goal_pos:
                    done = True
                    solution_path = self.backtrack_solution(curr_state)
                    break
            
            grid[x, y] = 4 # visited

        return solution_path, done, grid


class BFS_Algorithm:
    def __init__(self, start_pos, goal_pos, grid_dim):
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.grid_dim = grid_dim
        self.queue = Queue()
        self.queue.push(Node(pos=start_pos, parent=None))

    def get_successors(self, x, y):
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def is_valid_cell(self, pos):
        return 0 <= pos[0] < self.grid_dim[0] and 0 <= pos[1] < self.grid_dim[1]

    def backtrack_solution(self, curr_node):
        return self._backtrack(curr_node)

    def _backtrack(self, curr_node):
        return [] if curr_node.parent is None else self._backtrack(curr_node.parent) + [curr_node.position()]

    def update(self, grid):
        while not self.queue.isEmpty():
            curr_state = self.queue.pop()
            x, y = curr_state.position()

            if (x, y) == self.goal_pos:
                return self.backtrack_solution(curr_state), True, grid

            for step in self.get_successors(x, y):
                if self.is_valid_cell(step) and grid[step[0]][ step[1]] in [1,3]:
                    self.queue.push(Node(pos=step, parent=curr_state))
                    grid[step[0]][step[1]] = 4  # Mark cell as visited

        return [], False, grid


class IDS_Algorithm:
    def init(self, start_pos, goal_pos, grid_dim):
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.grid_dim = grid_dim
        self.max_depth = 0
    
    def get_successors(self, x, y):
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    
    def is_valid_cell(self, pos):
        return 0 <= pos[0] < self.grid_dim[0] and 0 <= pos[1] < self.grid_dim[1]
    
    def depth_limited_DFS(self, curr_node, grid, depth):
        if depth == 0:
            return None
        x, y = curr_node.position()
        if (x, y) == self.goal_pos:
            return [curr_node.position()]
        for step in self.get_successors(x, y):
            if self.is_valid_cell(step) and grid[step[0]][step[1]] in [1, 3]:  # Assuming 1 is unvisited, 3 is goal
                grid[step[0]][step[1]] = 4  # Mark as visited
                new_node = Node(pos=step, parent=curr_node)
                result = self.depth_limited_DFS(new_node, grid, depth - 1)
                if result is not None:
                    return [curr_node.position()] + result
        return None
    
    def update(self, grid):
        while True:
            result = self.depth_limited_DFS(Node(pos=self.start_pos, parent=None), grid, self.max_depth)
            if result is not None:
                return result, True, grid
            self.max_depth += 1
            # Reset grid for next depth-limited search
            for i in range(self.grid_dim[0]):
                for j in range(self.grid_dim[1]):
                    if grid[i][j] == 4:  # Reset visited cells for next iteration
                        grid[i][j] = 1  # Reset to unvisited
        return [], False, grid  # If goal not found within grid dimensions

class A_Star_Algorithm:
    def __init__(self, start_pos, goal_pos, grid_dim):
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.grid_dim = grid_dim
        self.open_list = PriorityQueue()
        self.open_list.put((0, Node(pos=start_pos, parent=None)))  # Using put instead of push

    def heuristic(self, pos):
        return abs(pos[0] - self.goal_pos[0]) + abs(pos[1] - self.goal_pos[1])

    def get_successors(self, x, y):
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def is_valid_cell(self, pos):
        return 0 <= pos[0] < self.grid_dim[0] and 0 <= pos[1] < self.grid_dim[1]

    def backtrack_solution(self, curr_node):
        # Assuming _backtrack is a method of the class A_Star_Algorithm
        return self._backtrack(curr_node)

    def _backtrack(self, curr_node):
        # Backtrack method implementation
        return [] if curr_node.parent is None else self._backtrack(curr_node.parent) + [curr_node.position()]

    def update(self, grid):
        while not self.open_list.empty():
            _, curr_state = self.open_list.get()
            x, y = curr_state.position()

            if (x, y) == self.goal_pos:
                return self.backtrack_solution(curr_state), True, grid

            for step in self.get_successors(x, y):
                if self.is_valid_cell(step) and grid[step[0]][step[1]] in [1, 3]:
                    new_node = Node(pos=step, parent=curr_state)
                    cost = 1 + self.heuristic(step)
                    self.open_list.put((cost, new_node))
                    grid[step[0]][step[1]] = 4  # Mark cell as visited

        return [], False, grid


class A_Star_Geometric_Algorithm:
    def __init__(self, start_pos, goal_pos, grid_dim):
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.grid_dim = grid_dim

    def euclidean_distance(self, pos1, pos2):
        # Calculate Euclidean distance between two positions
        return math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2)

    def get_successors(self, pos):
        # Get neighboring positions
        x, y = pos
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def is_valid_cell(self, pos):
        # Check if the position is within the grid boundaries
        return 0 <= pos[0] < self.grid_dim[0] and 0 <= pos[1] < self.grid_dim[1]

    def update(self, grid):
        # A* search algorithm with Euclidean heuristic
        open_list = PriorityQueue()
        open_list.put((0, self.start_pos))  # Initial node with priority 0
        came_from = {}  # Dictionary to store parent of each node
        cost_so_far = {}  # Dictionary to store cost to reach each node
        came_from[self.start_pos] = None
        cost_so_far[self.start_pos] = 0

        while not open_list.empty():
            current_cost, current_pos = open_list.get()

            if current_pos == self.goal_pos:
                # Reconstruct path if goal reached
                solution_path = self.reconstruct_path(came_from, current_pos)
                return solution_path, True, grid

            for next_pos in self.get_successors(current_pos):
                if self.is_valid_cell(next_pos) and grid[next_pos[0]][next_pos[1]] in [1, 3]:
                    new_cost = cost_so_far[current_pos] + 1  # Assuming unit cost for each move

                    if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                        cost_so_far[next_pos] = new_cost
                        priority = new_cost + self.euclidean_distance(next_pos, self.goal_pos)
                        open_list.put((priority, next_pos))
                        came_from[next_pos] = current_pos

            grid[current_pos[0]][current_pos[1]] = 4  # Mark current cell as visited

        # If goal not reached
        return [], False, grid

    def reconstruct_path(self, came_from, current_pos):
        # Reconstruct path from start to goal
        path = []
        while current_pos is not None:
            path.append(current_pos)  # Use append instead of push
            current_pos = came_from[current_pos]
        return path[::-1]  # Reverse the path to start from the beginning

