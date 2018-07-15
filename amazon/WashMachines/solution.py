class Solution:
    """
    @param machines: an integer array representing the number of dresses in each washing machine from left to right on the line
    @return: the minimum number of moves to make all the washing machines have the same number of dresses
    """
    def findMinMoves(self, machines):
        # Write your code here
        if not machines:
            return 0
        sm = sum(machines)
        if sm % len(machines) != 0:
            return -1
        target = sm / len(machines)
        move = [0 for _ in xrange(len(machines))]
        ans = 0
        for i, machine in enumerate(machines):
            if i == len(machines) - 1:
                break
            if target > machine:
                move[i+1] = target - machine
                machines[i] = target
                machines[i+1] -= target-machine
                ans = max(ans, move[i+1])
            else:
                move[i] += machine - target
                machines[i] = target
                machines[i+1] += machine - target
                ans = max(ans, move[i])
        
        return ans
