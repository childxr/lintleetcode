class Solution:
    """
    @param: x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        left = 0  
        right = x * 1.0
        if x < 1.0:
            right = 1.0
        while right - left > 10e-12:
            mid = left + (right-left)/2.0
            if mid * mid < x:
                left = mid
            else:
                right = mid
        return right
