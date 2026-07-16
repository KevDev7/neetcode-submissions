class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # No cells means there cannot be any islands.
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        # Stores every land cell that has already been discovered.
        # This prevents the same connected land from being counted again.
        visited = set()

        islands = 0

        # Directions used to explore the complete shape of one island.
        directions = [
            (1, 0),    # down
            (-1, 0),   # up
            (0, 1),    # right
            (0, -1),   # left
        ]

        def bfs(start_r, start_c):
            # The queue stores discovered land cells whose neighbors
            # still need to be explored.
            #
            # It begins with only the island's starting cell, but more
            # connected land cells are added as BFS discovers them.
            queue = deque([(start_r, start_c)])

            # Mark the starting cell immediately so it cannot be added
            # to the queue again by one of its neighbors.
            visited.add((start_r, start_c))

            while queue:
                # Remove one discovered cell whose neighbors have not
                # been fully checked yet.
                row, col = queue.popleft()

                # Explore every direction from the current cell.
                for dr, dc in directions:
                    new_r = row + dr
                    new_c = col + dc

                    if (
                        # The neighboring cell must exist in the grid.
                        0 <= new_r < rows
                        and 0 <= new_c < cols

                        # It must be land.
                        and grid[new_r][new_c] == "1"

                        # It must not have already been discovered.
                        and (new_r, new_c) not in visited
                    ):
                        # "visited" means we now know this cell belongs
                        # to the current island.
                        visited.add((new_r, new_c))

                        # Adding it to the queue means we still need to
                        # explore this cell's own neighbors later.
                        queue.append((new_r, new_c))

            # When the queue becomes empty, every connected land cell
            # belonging to this island has been discovered and explored.

        # The outer loop searches for the starting point of each island.
        # It does not explore the island itself; BFS handles that.
        for r in range(rows):
            for c in range(cols):
                # An unvisited land cell means we found a new island.
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1

                    # Explore and mark every cell connected to this island
                    # so the outer loop does not count them again later.
                    bfs(r, c)

        return islands