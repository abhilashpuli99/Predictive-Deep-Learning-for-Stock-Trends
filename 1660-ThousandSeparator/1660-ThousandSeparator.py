# Last updated: 7/9/2025, 1:41:19 AM
class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        num=str(n)
        if(len(num)<=3):
            return str(n)
        else:
            num=num[::-1]
            ele=""
            for i in range (len(num)):
                if i%3==0:
                    ele+='.'
                    ele+=num[i]
                else:
                    ele+=num[i]
        
        return ele[::-1].strip('.')




        