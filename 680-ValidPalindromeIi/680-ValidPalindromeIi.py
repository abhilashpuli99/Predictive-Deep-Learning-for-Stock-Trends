# Last updated: 7/9/2025, 1:41:47 AM
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        left,right=0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return is_palindrome(left+1,right) or is_palindrome(left,right-1)
            left+=1
            right-=1
        return True