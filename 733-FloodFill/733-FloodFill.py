# Last updated: 7/9/2025, 1:41:46 AM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        current_color=image[sr][sc]
        rows,cols=len(image),len(image[0])
        queue=deque([(sr,sc)])
        image[sr][sc]=color
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while queue:
            r,c=queue.popleft()
            for row,col in directions:
                row,col=row+r,col+c
                if 0<=row<rows and 0<=col<cols and image[row][col]==current_color and image[row][col]!=color:
                    image[row][col]=color
                    queue.append((row,col))
        return image
