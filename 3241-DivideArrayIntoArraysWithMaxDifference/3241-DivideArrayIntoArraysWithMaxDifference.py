# Last updated: 7/9/2025, 1:41:06 AM
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(0,len(nums),3):
            if nums[i+2]-nums[i]>k:
                return []
            result.append(nums[i:i+3])

        return result 

        