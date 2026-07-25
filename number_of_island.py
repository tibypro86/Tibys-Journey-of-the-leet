from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        island_count = 0

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            while q:
                curr_r, curr_c = q.popleft()

                for dr, dc in directions:
                    nei_r, nei_c = curr_r + dr, curr_c + dc

                    if (0 <= nei_r < rows and 
                        0 <= nei_c < cols and 
                        grid[nei_r][nei_c] == "1" and 
                        (nei_r, nei_c) not in visit):
                        
                        visit.add((nei_r, nei_c))
                        q.append((nei_r, nei_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    island_count += 1

        return island_count