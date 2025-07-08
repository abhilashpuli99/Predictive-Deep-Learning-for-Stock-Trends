# Last updated: 7/9/2025, 1:40:50 AM
class Solution:
    def findCoins(self, dp: List[int]) -> List[int]:
        n = len(dp)
        dp = [1] + dp
        res = []
        for a in range(1, n + 1):
            if dp[a] > 1: return []
            if dp[a] == 0: continue
            res.append(a)
            for v in range(n, a - 1, -1):
                dp[v] -= dp[v - a]
                if dp[v] < 0:
                    return []
        return res      