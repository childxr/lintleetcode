import math

class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    
    def __init__(self):
        self.cnt = 0
        
    def isPrime(self, n):
        if n <= 1:
            return False
        elif n in [2, 3, 5, 7]:
            return True
        else:
            for x in xrange(2, int(math.sqrt(n)) + 1):
                if n % x == 0:
                    return False
            return True
    
    def countPrimes(self, n):
        # write your code here
        
        for i in xrange(0, n):
            if self.isPrime(i):
                self.cnt += 1
        
        return self.cnt
            
