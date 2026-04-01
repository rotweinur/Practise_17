def get_shortest_path(graph, start_city, end_city):
    """
    Calculates the shortest distance between two nodes in a graph using Dijkstra's algorithm.

    Args:
        graph (dict): Adjacency dictionary where keys are city names and 
            values are dictionaries of neighbors with distances.
        start_city (str): The name of the starting node.
        end_city (str): The name of the target node.

    Returns:
        int or float: The minimum distance to the target city. 
            Returns float('inf') if the path does not exist.
    """
    distances = {}
    for city in graph:
        distances[city] = float('inf')
        
    if start_city in distances:
        distances[start_city] = 0
        
    unvisited = list(graph.keys())

    while unvisited:
        current_city = None
        for city in unvisited:
            if current_city is None or distances[city] < distances[current_city]:
                current_city = city
                
        if distances[current_city] == float('inf') or current_city == end_city:
            break
            
        unvisited.remove(current_city)
        
        for neighbor, weight in graph[current_city].items():
            if neighbor in unvisited:
                new_distance = distances[current_city] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances.get(end_city, float('inf'))


if __name__ == "__main__":
    n_input = input()
    if n_input:
        n = int(n_input)
    
    m_input = input()
    if m_input:
        m = int(m_input)
    
    cities_graph = {}
    
    for _ in range(m):
        row = input().split()
        if len(row) == 3:
            city1, city2, dist = row[0], row[1], int(row[2])
            
            if city1 not in cities_graph:
                cities_graph[city1] = {}
            if city2 not in cities_graph:
                cities_graph[city2] = {}
                
            cities_graph[city1][city2] = dist
            cities_graph[city2][city1] = dist

    endpoints = input().split()
    if len(endpoints) == 2:
        start, end = endpoints
        result = get_shortest_path(cities_graph, start, end)
        print(result)
