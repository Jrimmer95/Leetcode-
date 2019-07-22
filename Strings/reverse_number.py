"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
    range: [−2**31,  2**31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed
    integer overflows.

"""

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = str(x)
            y = ''
            y += (x[::-1])
            if int(y) > (2**31)-1:
                return 0
            return int(y)
        elif x < 0:
            x = x * -1
            x = str(x)
            y = ''
            y += (x[::-1])
            if -int(y) < -(2**31):
                return 0
            return -int(y)
