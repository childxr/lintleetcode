class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1
        return self.innerMyPower(x, n) if n > 0 else 1.0 / self.innerMyPower(x, -n)
        
    def innerMyPower(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        ans = self.innerMyPower(x, n/2)
        return ans * ans if n % 2 == 0 else x * ans * ans