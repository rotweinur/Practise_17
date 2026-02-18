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
    queue = []
    heapq.heappush(queue, (0, start))
    
    visited = set()
    min_distances = {start: 0}

    while len(queue) > 0:
        current_dist, current_city = heapq.heappop(queue)

        if current_city == end:
            return current_dist

        if current_city in visited:
            continue
        visited.add(current_city)

        if current_city in graph:
            neighbors = graph[current_city]
            for neighbor, weight in neighbors:
                distance = current_dist + weight
                if distance < min_distances.get(neighbor, float('inf')):
                    min_distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
    
    return -1


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    
    city_graph = defaultdict(list)
    
    for _ in range(m):
        line = input()
        parts = line.split()
        city1 = parts[0]
        city2 = parts[1]
        dist = int(parts[2])
        
        city_graph[city1].append((city2, dist))
        city_graph[city2].append((city1, dist))
        
    route_line = input()
    start_point, end_point = route_line.split()
    
    print(find_shortest_path(city_graph, start_point, end_point))
