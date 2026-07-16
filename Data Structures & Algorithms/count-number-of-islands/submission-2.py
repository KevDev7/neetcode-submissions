class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # empty grid, 0 islands
        if not grid:
            return 0

        visited = set()     # set of tuples
        island_counter = 0

        def bfs(start_r, start_c):
            q = deque([(start_r, start_c)])     # create a queue to hold cells need to traverse around
            visited.add((start_r, start_c))     # store starting point in visited

            # get all directions
            directions = [
                [1, 0],
                [0, 1],
                [-1, 0],
                [0, -1]
            ]

            # while q is not empty
            while q:
                row, col = q.popleft()
                for (dr, dc) in directions:
                    new_r = row + dr
                    new_c = col + dc

                    if (
                        new_r in range(len(grid)) and new_c in range(len(grid[0])) and
                        grid[new_r][new_c] == "1" and
                        (new_r, new_c) not in visited
                    ):
                        visited.add((new_r, new_c))
                        q.append(((new_r, new_c)))


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # found island starting point
                if grid[r][c] == "1" and (r, c) not in visited:
                    island_counter += 1
                    bfs(r, c)   # traverse around island starting point to see how big it is
        
        return island_counter

