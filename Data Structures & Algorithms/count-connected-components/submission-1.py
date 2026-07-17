class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # make an adjacency list using a dict holding list values
        adj_list = {}

        # fill in empty list for adjacency list values
        for node in range(n):
            adj_list[node] = []

        # fill in neighbors for each node
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        # set to hold all nodes already visited
        visited = set()

        component_counter = 0

        def dfs(start_node):
            # make stack to hold nodes that neighbors need to checked out, 1st node to check out it's neighbors will be start_node
            stack = [start_node]

            # add start_node to visited
            visited.add(start_node)

            # map out the node's neighbors, while stack not empty
            while stack:
                curr_node = stack.pop()     # use pop to check on latest added node
                for neighbor in adj_list[curr_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)   # add neighbor to visited
                        stack.append(neighbor)  # add neighbor to stack to then check neighbor's neighbors

        # go through each node
        for node in range(n):
            if node not in visited:
                component_counter += 1   # increment component counter
                dfs(node)                # map out big component is so connected nodes aren't counted as new components

        return component_counter