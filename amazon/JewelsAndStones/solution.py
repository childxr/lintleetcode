class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    def numJewelsInStones(self, J, S):
        # Write your code here
        m = {}
        for s in S:
            v = m.get(s, 0)
            m[s] = v + 1
        
        cnt = 0
        for j in J:
            cnt += m.get(j, 0)
        
        return cnt
