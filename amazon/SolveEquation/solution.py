class Solution:
    """
    @param equation: a string
    @return: return a string
    """
    def extend(self, s):
        if s[0] == 'x' or s[0].isdigit():
            s = "+" + s
        return s
    
    def reverseSign(self, s):
        ans = ""
        for a in s:
            if a == "-":
                ans += "+"
            elif a == "+":
                ans += "-"
            else:
                ans += a
        return ans
    
    def solveEquation(self, equation):
        # write your code here
        left, right = equation.split("=")
        left = self.extend(left)
        right = self.reverseSign(self.extend(right))
        expr = left + right
        cntX = 0
        sign = 1
        i = 0
        seq = []
        buf = []
        while i < len(expr):
            if expr[i] == "+":
                if buf:
                    seq.append(int("".join(str(j) for j in buf)) * sign)
                    buf = []
                sign = 1
            elif expr[i] == "-":
                if buf:
                    seq.append(int("".join(str(j) for j in buf)) * sign)
                    buf = []
                sign = -1
            elif expr[i].isdigit():
                buf.append(expr[i])
            elif expr[i] == "x":
                if buf:
                    cntX += int("".join(str(j) for j in buf)) * sign
                    buf = []
                else:
                    cntX += sign
            i += 1
        
        if buf:
            seq.append(int("".join(str(j) for j in buf))*sign)
        
        if cntX == 0 and sum(seq) == 0:
            return "Infinite solutions"
        if cntX == 0 and sum(seq) != 0:
            return "No solution"
        return "x={}".format(-1 * sum(seq) / cntX)

