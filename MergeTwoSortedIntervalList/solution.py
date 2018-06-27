"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def is_overlap(self, ainter, binter):
        lower = ainter if ainter.start < binter.start else binter
        higher = ainter if ainter.start >= binter.start else binter
        return lower.end >= higher.start
    
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        if not list1 and not list2:
            return []
        if not list1:
            return list2
        if not list2:
            return list1
        
        ans = []
        
        i, j = 0, 0
        if list1[i].start < list2[j].start:
            ans.append(list1[i])
            i += 1
        else:
            ans.append(list2[j])
            j += 1
        cur = 0
        
        while True:
            if i == len(list1) and j == len(list2):
                break
            if i < len(list1) and j < len(list2):
                if list1[i].start < list2[j].start:
                    if self.is_overlap(ans[cur], list1[i]):
                        ans[cur].start = min(ans[cur].start, list1[i].start)
                        ans[cur].end = max(ans[cur].end, list1[i].end)
                    else:
                        ans.append(list1[i])
                        cur += 1
                    i += 1
                else:
                    if self.is_overlap(ans[cur], list2[j]):
                        ans[cur].start = min(ans[cur].start, list2[j].start)
                        ans[cur].end = max(ans[cur].end, list2[j].end)
                    else:
                        ans.append(list2[j])
                        cur += 1
                    j += 1
            elif i < len(list1):
                if self.is_overlap(ans[cur], list1[i]):
                    ans[cur].start = min(ans[cur].start, list1[i].start)
                    ans[cur].end = max(ans[cur].end, list1[i].end)
                else:
                    ans.append(list1[i])
                    cur += 1
                i += 1
            else:
                if self.is_overlap(ans[cur], list2[j]):
                    ans[cur].start = min(ans[cur].start, list2[j].start)
                    ans[cur].end = max(ans[cur].end, list2[j].end)
                else:
                    ans.append(list2[j])
                    cur += 1
                j += 1
        return ans
        

