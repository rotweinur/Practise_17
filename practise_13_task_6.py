import sys
import heapq
from collections import defaultdict

def find_shortest_path(graph: dict[str, list[tuple[str, int]]], start: str, end: str) -> int:
    """
    Finds the shortest distance between two points using Dijkstra's algorithm.
    Args:
        graph (dict[str, list[tuple[str, int]]]): Adjacency list (neighbor, distance).
        start (str): Starting city.
        end (str): Destination city.
    Returns:
        int: Shortest distance or -1 if unreachable.
    """
    queue = [(0, start)]
    visited = set()
    min_distances = {start: 0}

    while queue:
        current_dist, current_city = heapq.heappop(queue)
        if current_city == end:
            return current_dist
        if current_city in visited:
            continue
        visited.add(current_city)
        if current_city in graph:
            for neighbor, weight in graph[current_city]:
                distance = current_dist + weight
                if distance < min_distances.get(neighbor, float('inf')):
                    min_distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
    return -1

def solve_task_6() -> None:
    """
    Reads input and prints the result for Task 6.
    """
    try:
        line_n = sys.stdin.readline()
        if not line_n:
            return
        n = int(line_n.strip())
        line_m = sys.stdin.readline()
        m = int(line_m.strip())
        graph = defaultdict(list)
        for _ in range(m):
            line = sys.stdin.readline().strip()
            if line:
                parts = line.split()
                city1 = parts[0]
                city2 = parts[1]
                distance = int(parts[2])
                graph[city1].append((city2, distance))
                graph[city2].append((city1, distance))
        route_line = sys.stdin.readline().strip()
        start_city, end_city = route_line.split()
        print(find_shortest_path(graph, start_city, end_city))
    except ValueError:
        pass

if __name__ == "__main__":
    solve_task_6()