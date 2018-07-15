class Solution:
    """
    @param str: A string
    @return: An integer
    """
    def atoi(self, str):
        # write your code here
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if not str:
            return 0
        str = str.strip()
        if str[0] == "-":
            start = 1
            sign = -1
        elif str[0] == "+":
            start = 1
            sign = 1
        else:
            start = 0
            sign = 1
        
        ans = 0
        
        for i in xrange(start, len(str)):
            if not str[i].isdigit():
                return sign * ans
            else:
                ans = ans * 10 + ord(str[i]) - ord('0')
                if sign > 0 and ans >= MAX_INT:
                    return MAX_INT
                elif sign < 0 and sign * ans <= MIN_INT:
                    return MIN_INT
        
        return sign * ans
        
