import heapq
import math


class Node:
    """Egy rácscellát reprezentáló csomópont az A* kereséshez."""

    def __init__(self, x: int, y: int, g: float = 0.0, h: float = 0.0, parent=None):
        self.x = x
        self.y = y
        self.g = g  # Kezdőponttól megtett költség
        self.h = h  # Célpontig becsült heurisztikus költség
        self.f = g + h  # Teljes becsült költség
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f


class AStarSolver:
    """2D-s A* útvonaltervező osztály bináris rácstérképhez."""

    def __init__(self, allow_diagonal: bool = True):
        self.allow_diagonal = allow_diagonal

    def heuristic(self, a: tuple[int, int], b: tuple[int, int]) -> float:
        if self.allow_diagonal:
            return math.hypot(a[0] - b[0], a[1] - b[1])
        return float(abs(a[0] - b[0]) + abs(a[1] - b[1]))

    def solve(
        self,
        grid: list[list[int]],
        start: tuple[int, int],
        goal: tuple[int, int],
    ) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        """
        Megkeresi a legrövidebb ütközésmentes utat a rácson.

        Args:
            grid: 2D lista (0 = szabad mező, 1 = akadály)
            start: (x, y) kezdőkoordináta
            goal: (x, y) célkoordináta

        Returns:
            (path, visited_order): az optimális útvonal pontjai és a bejárt cellák sorrendje
        """
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        if not (0 <= start[0] < cols and 0 <= start[1] < rows):
            return [], []
        if not (0 <= goal[0] < cols and 0 <= goal[1] < rows):
            return [], []
        if grid[start[1]][start[0]] == 1 or grid[goal[1]][goal[0]] == 1:
            return [], []

        start_node = Node(start[0], start[1], 0.0, self.heuristic(start, goal))
        open_set = []
        heapq.heappush(open_set, start_node)

        open_dict = {start: start_node}
        closed_set = set()
        visited_order = []

        if self.allow_diagonal:
            neighbors = [
                (0, 1, 1.0), (1, 0, 1.0), (0, -1, 1.0), (-1, 0, 1.0),
                (1, 1, math.sqrt(2)), (1, -1, math.sqrt(2)),
                (-1, 1, math.sqrt(2)), (-1, -1, math.sqrt(2)),
            ]
        else:
            neighbors = [(0, 1, 1.0), (1, 0, 1.0), (0, -1, 1.0), (-1, 0, 1.0)]

        while open_set:
            current = heapq.heappop(open_set)
            curr_pos = (current.x, current.y)

            if curr_pos in closed_set:
                continue

            closed_set.add(curr_pos)
            visited_order.append(curr_pos)

            if curr_pos == goal:
                path = []
                curr = current
                while curr is not None:
                    path.append((curr.x, curr.y))
                    curr = curr.parent
                return path[::-1], visited_order

            for dx, dy, step_cost in neighbors:
                nx, ny = current.x + dx, current.y + dy

                if not (0 <= nx < cols and 0 <= ny < rows):
                    continue
                if grid[ny][nx] == 1 or (nx, ny) in closed_set:
                    continue

                new_g = current.g + step_cost
                neighbor_pos = (nx, ny)

                if neighbor_pos not in open_dict or new_g < open_dict[neighbor_pos].g:
                    h_val = self.heuristic(neighbor_pos, goal)
                    neighbor_node = Node(nx, ny, new_g, h_val, current)
                    open_dict[neighbor_pos] = neighbor_node
                    heapq.heappush(open_set, neighbor_node)

        return [], visited_order
