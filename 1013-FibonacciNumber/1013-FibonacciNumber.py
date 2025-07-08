# Last updated: 7/9/2025, 1:41:37 AM
class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        x=[0,1]
        for i in range(2,n+1):
            temp=x[0]+x[1]
            x[0],x[1]=x[1],temp
        return x[-1]
        