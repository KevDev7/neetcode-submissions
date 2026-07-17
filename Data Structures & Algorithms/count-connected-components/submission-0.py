from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build an adjacency list for every node
        graph = {}

        for node in range(n):
            graph[node] = []

        # Because the graph is undirected, store each edge both ways
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()
        component_count = 0

        def dfs(start_node):
            # Stack holds discovered nodes whose neighbors
            # still need to be checked
            stack = [start_node]
            visited.add(start_node)

            while stack:
                current_node = stack.pop()

                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

        # Each unvisited node starts a new connected component
        for node in range(n):
            if node not in visited:
                component_count += 1
                dfs(node)

        return component_count
        