import sys
class Solution:
    """
    @param tagList: The tag list.
    @param allTags: All the tags.
    @return: Return the answer
    """
    def getMinimumStringArray(self, tagList, allTags):
        # Write your code here
        e = {}
        ec = 0
        # build expected map
        need = set(tagList)
        e = {tag: 0 for tag in need}
        for tag in tagList:
            e[tag] += 1
            ec += 1
        
        left, right = -1, 0
        m = {tag: 0 for tag in need}
        
        ans = sys.maxint
        rc = 0
        while right < len(allTags):
            tag = allTags[right]
            if tag in need:
                m[tag] += 1
                if m[tag] <= e[tag]:
                    rc += 1
                while rc == ec:
                    l = right - left
                    ans = min(ans, l)
                    left += 1
                    rw = allTags[left]
                    if rw in need:
                        m[rw] -= 1
                        if m[rw] < e[rw]:
                            rc -= 1
            right += 1
            
        return -1 if ans == sys.maxint else ans
            
