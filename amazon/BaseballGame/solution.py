class Solution:
    """
    @param ops: the list of operations
    @return:  the sum of the points you could get in all the rounds
    """
    def calPoints(self, ops):
        # Write your code here
        stack = []
        
        for op in ops:
            if op[-1].isdigit():
                stack.append(int(op))
            elif op == "C":
                stack.pop()
            elif op == "+":
                if len(stack) > 1:
                    stack.append(stack[-1] + stack[-2])
                else:
                    stack.append(stack[-1])
            elif op == "D":
                stack.append(stack[-1] + stack[-1])
            #print stack
        
        return sum(stack)
                
            
