class Solution:
    """
    @param cost: an array
    @return: minimum cost to reach the top of the floor
    """
    def minCostClimbingStairs(self, cost):
        # Write your code here
        n = len(cost)
        # f(n) is the min cose when reaches to n
        # f(n) = min(f(n-1) + cost[n-1], f(n-2) + cost[n-2])
        # f(0) = 0
        # f(1) = 0
        return self.helper(n, cost)
        
    
    def helper(self, n, cost):
        if n == 0 or n == 1:
            return 0
        else:
            cost1 = cost[n-1] + self.helper(n-1, cost)
            cost2 = cost[n-2] + self.helper(n-2, cost)
            return min(cost1, cost2)

