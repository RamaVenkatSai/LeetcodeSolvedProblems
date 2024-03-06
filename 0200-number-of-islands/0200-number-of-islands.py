class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid,i,j):
            if  i>len(grid)-1 or j>len(grid[0])-1 or i<0 or j<0 or grid[i][j]!="1" :
                return 
            grid[i][j]="2"
            dfs(grid, i+1,j)
            dfs(grid, i-1,j)
            dfs(grid, i,j+1)
            dfs(grid, i,j-1)
            
            
        no_of_islands=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    
                 
                    dfs(grid, i, j)
                    no_of_islands=no_of_islands+1
        return no_of_islands
            
                
            
        