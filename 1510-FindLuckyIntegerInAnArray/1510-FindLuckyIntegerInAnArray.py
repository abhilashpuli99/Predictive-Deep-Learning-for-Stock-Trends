# Last updated: 7/9/2025, 1:41:22 AM
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=dict()
        for i in range(len(arr)):
            freq[arr[i]]=freq.get(arr[i],0)+1
        for key,val in sorted(freq.items(),key=lambda x: -x[0]):
            if key==val:
                return key
        return -1