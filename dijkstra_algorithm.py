# https://informatics.msk.ru/mod/statements/view.php?chapterid=3494#1
# O(V log V + E log V), where V is the number of vertices and E is the number of edges in the graph.

import heapq

def dijkstra(graph: list, start: int) -> list:
    n = len(graph)
    distance = [float('inf')] * n  # Initialize all distances to infinity.
    distance[start] = 0  # The distance to the starting vertex is 0.
    visited = [False] * n  # Keep track of visited vertices.
    priority_queue = [(0, start)]  # Initialize the priority queue with the starting vertex and its distance.

    while priority_queue:
        u = heapq.heappop(priority_queue)[1]  # Get the vertex with the smallest distance from the priority queue.

        if visited[u]:
            continue  # Skip this vertex if it has already been visited.

        visited[u] = True  # Mark the current vertex as visited.

        for v, weight in graph[u]:
            # Relaxation step: Check if the path to 'v' through 'u' is shorter than the current known distance to 'v'.
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight  # Update the distance to 'v'.
                heapq.heappush(priority_queue, (distance[v], v))  # Add 'v' to the priority queue with the updated distance.

    return distance

num_tests = int(input())  # Read the number of test cases.

for _ in range(num_tests):
    n, m = map(int, input().split())  # Read the number of vertices and edges for the current graph.
    graph = [[] for _ in range(n)]  # Initialize an adjacency list for the graph.

    for _ in range(m):
        a, b, c = map(int, input().split())  # Read the vertices and edge weights.
        graph[a].append((b, c))  # Add the edge (a, b) to the graph.
        graph[b].append((a, c))  # Since it's an undirected graph, add (b, a) as well.

    start_vertex = int(input())  # Read the starting vertex for this test case.

    distances = dijkstra(graph, start_vertex)  # Apply Dijkstra's algorithm to find distances from the starting vertex.

    print(" ".join(map(str, distances)))  # Print the distances for all vertices.
