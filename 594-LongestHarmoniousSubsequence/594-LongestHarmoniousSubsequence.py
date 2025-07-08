# Last updated: 7/9/2025, 1:41:51 AM
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq=Counter(nums)
        maxi=0
        for num in nums:
            if num+1 in freq:
                maxi=max(maxi,freq[num]+freq[num+1])
        return maxi