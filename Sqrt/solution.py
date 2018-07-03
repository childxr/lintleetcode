class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x == 0:
            return x
        assert x > 0
        
        start, end = 0, x/2 + 1
        while start + 1 < end:
            mid = start + (end - start)/2
            guess = mid * mid
            if guess == x:
                return mid
            elif guess < x:
                start = mid
            else:
                end = mid
        
        if end * end <= x:
            return end
        return start
