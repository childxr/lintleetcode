class Solution:
    """
    @param codeList: The codeList
    @param shoppingCart: The shoppingCart
    @return: The answer
    """
    def buyFruits(self, codeList, shoppingCart):
        # Write your code here
        tags = {}
        cnt = 0
        for code in codeList:
            for item in code:
                if not tags.get(item) and item != "anything":
                    tags[item] = str(cnt)
                    cnt += 1
        
        for item in shoppingCart:
            if not tags.get(item):
                tags[item] = str(cnt)
                cnt += 1
        
        s = "".join([tags[item] for item in shoppingCart])
        p = ""
        for code in codeList:
            for item in code:
                if item == "anything":
                    p += "."
                else:
                    p += tags[item]

        #print s
        #print p
        def matches(a, b):
            return a == b or b == "."
            
        i, j = 0, 0
        while i < len(s) - len(p) + 1:
            if matches(s[i], p[0]):
                k, j = i, 0
                while j < len(p):
                    if not matches(s[k], p[j]):
                        break
                    k += 1
                    j += 1
                if j == len(p):
                    return 1
            i += 1
        
        return 0
                
        
        
