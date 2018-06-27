import copy

class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def __init__(self):
        self.ans = set([])
    
    def removeInvalidParentheses(self, s):
        # Write your code here
        if not s:
            return [""]
        rml, rmr = 0, 0
        for ch in s:
            if ch == "(":
                rml += 1
            elif ch == ")":
                if rml > 0:
                    rml -= 1
                else:
                    rmr += 1
        self.helper(s, rml, rmr, 0, [], 0)
        return list(self.ans)
    
    
    def helper(self, s, rml, rmr, openp, buf, index):
        if not s:
            return
        if index > len(s):
            return
        if rmr < 0 or rml < 0 or openp < 0:
            return
        if index == len(s):
            if rml == 0 and rmr == 0 and openp == 0:
                self.ans.add(''.join(buf))
            return
        
        tmp = copy.deepcopy(buf)
        ch = s[index]
        if ch == "(":
            self.helper(s, rml-1, rmr, openp, tmp, index+1)
            tmp.append("(")
            self.helper(s, rml, rmr, openp+1, tmp, index+1)
        elif ch == ")":
            self.helper(s, rml, rmr-1, openp, tmp, index+1)
            tmp.append(")")
            self.helper(s, rml, rmr, openp-1, tmp, index+1)
        else:
            tmp.append(ch)
            self.helper(s, rml, rmr, openp, tmp, index+1)
            
            
            
            
