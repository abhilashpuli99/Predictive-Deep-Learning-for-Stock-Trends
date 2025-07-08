# Last updated: 7/9/2025, 1:40:59 AM
class Solution:
    def maxDifference(self, s: str) -> int:
        bucket=Counter(s)
        even=float('inf')
        odd=0
        for i in bucket:
            if bucket[i]%2!=0:
                odd=max(bucket[i],odd)
            if bucket[i]%2==0 :
                even=min(even,bucket[i])
        return odd-even
        
        