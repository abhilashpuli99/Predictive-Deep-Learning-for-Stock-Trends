# Last updated: 7/9/2025, 1:41:25 AM
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        for i in range (0,len(grid)):
            for j in range (0,len(grid[i])):
                if(grid[i][j]<0):
                    count=count+1
        return count
            