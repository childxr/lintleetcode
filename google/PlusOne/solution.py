class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        stack = []
        for d in digits:
            stack.append(d)
        
        c = 1
        ans = []
        while len(stack) > 0:
            s = c+stack.pop()
            ans.append(s % 10)
            c = s / 10
        if c > 0:
            ans.append(c)
        ans.reverse()
        return ans

