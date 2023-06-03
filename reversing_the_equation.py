# Given a mathematical equation that contains only numbers and +, -, *, /. Print the equation in reverse, 
# such that the equation is reversed, but the numbers remain the same.
# It is guaranteed that the given equation is valid, and there are no leading zeros.

import re
class Solution:
    def reverseEqn(self, s):
        # code here
        chh={'+','-','*','/'}
        # we wre splitting the string at arithmatic operators through this functions
        pattern = '|'.join(map(re.escape, chh)) 
        result = re.split(pattern, s)

        # arithmetic operators list
        ch=[]
        
        for ele in s:
            if ele in chh:
                ch.append(ele)
        ans=""
        l=len(ch)
        
        # creating reverse string
        for i in range(l):
            ans=ans+result[l-i]+ch[l-i-1]
        ans=ans+result[0]
        return ans