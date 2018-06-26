from heapq import heappop, heappush

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        trav = dummy = ListNode(-1)
        heap = []
        for ll in lists:
            if ll:
                self.heappushNode(heap, ll)
                
        while heap:
            node = heappop(heap)[1]
            trav.next = node
            trav = trav.next
            #print(trav.val)
            if trav.next:
                self.heappushNode(heap, trav.next)
                
                    
        return dummy.next
            
    def heappushNode(self, heap, node):
        heappush(heap, (node.val, node))
