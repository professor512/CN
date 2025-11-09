# Distance Vector Routing using Bellman-Ford Algorithm

def distance_vector_routing(graph, source):
    # Initialize distances from source to all nodes as infinity
    distance = {node: float('inf') for node in graph}
    distance[source] = 0

    # Number of nodes
    num_nodes = len(graph)

    # Relax edges repeatedly (Bellman-Ford core step)
    for _ in range(num_nodes - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    # Print the final distance vector from the source
    print(f"Distance vector from node '{source}':")
    for node in graph:
        print(f"To {node} : {distance[node]}")

# Example network topology as an adjacency list with costs
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 7},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 7, 'C': 3}
}

# Call the function with source node 'A'
distance_vector_routing(graph, 'C')
