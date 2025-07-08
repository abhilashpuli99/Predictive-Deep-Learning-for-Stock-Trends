# Last updated: 7/9/2025, 1:40:54 AM
class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        from collections import defaultdict
        best_y=dict()
        for xi,yi in zip(x,y):
            if xi not in best_y or yi>best_y[xi]:
                best_y[xi]=yi
        if len(best_y)<3:
            return -1
        return sum(sorted(best_y.values(),reverse=True)[:3])
        
        